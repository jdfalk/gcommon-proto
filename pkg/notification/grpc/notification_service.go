// file: pkg/notification/grpc/notification_service.go
// version: 1.1.0
// guid: bbbbbbbb-cccc-dddd-eeee-ffffffffffff

package grpcsvc

import (
	"context"
	"errors"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
	_ "github.com/jdfalk/gcommon/pkg/notification/providers"
)

// Service implements the NotificationService gRPC server.
type Service struct {
	pb.UnimplementedNotificationServiceServer
	tracker notification.DeliveryTracker
}

// NewService creates a new Service.
func NewService(tracker notification.DeliveryTracker) *Service {
	return &Service{tracker: tracker}
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
	name, err := channelToName(chs[0])
	if err != nil {
		return nil, err
	}
	provider, err := notification.NewProvider(name, nil)
	if err != nil {
		return nil, err
	}
	resp, err := provider.Send(ctx, req.GetNotification())
	if err == nil {
		_ = s.tracker.TrackDelivery(ctx, req.GetNotification().GetId(), pb.DeliveryStatus_DELIVERY_STATUS_SENT)
	}
	return resp, err
}
