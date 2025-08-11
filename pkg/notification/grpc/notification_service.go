// file: pkg/notification/grpc/notification_service.go
// version: 1.2.0
// guid: bbbbbbbb-cccc-dddd-eeee-ffffffffffff

package grpcsvc

import (
	"context"
	"errors"
	"sync"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	"github.com/jdfalk/gcommon/pkg/notification/channels"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
	_ "github.com/jdfalk/gcommon/pkg/notification/providers"
)

// Service implements the NotificationService gRPC server.
type Service struct {
	pb.UnimplementedNotificationServiceServer
	tracker       notification.DeliveryTracker
	prefs         *channels.Preferences
	templates     map[string]*pb.Template
	notifications map[string]*pb.NotificationMessage
	mu            sync.RWMutex
}

// NewService creates a new Service.
func NewService(tracker notification.DeliveryTracker) *Service {
	return &Service{
		tracker:       tracker,
		prefs:         channels.NewPreferences(),
		templates:     make(map[string]*pb.Template),
		notifications: make(map[string]*pb.NotificationMessage),
	}
}

func channelToName(ch *pb.DeliveryChannel) (string, error) {
	switch ch.GetType() {
	case pb.DeliveryChannelType_DELIVERY_CHANNEL_TYPE_EMAIL:
		return "email", nil
	case pb.DeliveryChannelType_DELIVERY_CHANNEL_TYPE_SMS:
		return "sms", nil
	case pb.DeliveryChannelType_DELIVERY_CHANNEL_TYPE_SLACK:
		return "slack", nil
	case pb.DeliveryChannelType_DELIVERY_CHANNEL_TYPE_WEBHOOK:
		return "webhook", nil
	default:
		return "", errors.New("unsupported channel")
	}
}

// Send delivers a notification using registered providers.
func (s *Service) Send(ctx context.Context, req *pb.SendNotificationRequest) (*pb.SendNotificationResponse, error) {
	chs := req.GetNotification().GetChannels()
	if len(chs) == 0 {
		return nil, errors.New("no channels provided")
	}
	var resp *pb.SendNotificationResponse
	for _, ch := range chs {
		name, err := channelToName(ch)
		if err != nil {
			return nil, err
		}
		cfg := map[string]any{}
		switch name {
		case "email":
			cfg["host"] = "localhost"
		case "sms":
			cfg["gateway"] = "gateway"
		case "push":
			cfg["service"] = "service"
		case "webhook":
			cfg["url"] = "http://localhost"
		case "slack":
			cfg["token"] = "token"
			cfg["channel"] = "general"
		}
		provider, err := notification.NewProvider(name, cfg)
		if err != nil {
			return nil, err
		}
		resp, err = provider.Send(ctx, req.GetNotification())
		if err != nil {
			return nil, err
		}
	}
	s.mu.Lock()
	s.notifications[req.GetNotification().GetId()] = req.GetNotification()
	s.mu.Unlock()
	_ = s.tracker.TrackDelivery(ctx, req.GetNotification().GetId(), pb.DeliveryStatus_DELIVERY_STATUS_SENT)
	return resp, nil
}

// AddTemplate registers a template for retrieval.
func (s *Service) AddTemplate(t *pb.Template) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.templates[t.GetId()] = t
}
