// file: pkg/notification/grpc/admin_service.go
// version: 1.0.0
// guid: 0b6f7d8e-3c2d-4e5f-8a9b-1c2d3e4f5a6b

package grpcsvc

import (
	"context"
	"errors"

	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// List returns all notifications known to the service.
func (s *Service) List(ctx context.Context, req *pb.ListNotificationsRequest) (*pb.ListNotificationsResponse, error) {
	s.mu.RLock()
	defer s.mu.RUnlock()
	notifs := make([]*pb.NotificationMessage, 0, len(s.notifications))
	for _, n := range s.notifications {
		notifs = append(notifs, n)
	}
	resp := &pb.ListNotificationsResponse{}
	resp.SetNotifications(notifs)
	return resp, nil
}

// UpdatePreferences stores subscription preferences for a user.
func (s *Service) UpdatePreferences(ctx context.Context, req *pb.UpdatePreferencesRequest) (*pb.UpdatePreferencesResponse, error) {
	prefs := req.GetPreferences()
	if prefs == nil {
		return nil, errors.New("preferences required")
	}
	channels := make([]string, len(prefs.GetChannels()))
	for i, ch := range prefs.GetChannels() {
		dc := &pb.DeliveryChannel{}
		dc.SetType(ch)
		name, err := channelToName(dc)
		if err != nil {
			return nil, err
		}
		channels[i] = name
	}
	s.prefs.Set(prefs.GetUserId(), channels)
	resp := &pb.UpdatePreferencesResponse{}
	resp.SetSuccess(true)
	return resp, nil
}

// GetTemplate retrieves a template by ID.
func (s *Service) GetTemplate(ctx context.Context, req *pb.GetTemplateRequest) (*pb.GetTemplateResponse, error) {
	s.mu.RLock()
	tmpl, ok := s.templates[req.GetId()]
	s.mu.RUnlock()
	if !ok {
		return nil, errors.New("template not found")
	}
	resp := &pb.GetTemplateResponse{}
	resp.SetTemplate(tmpl)
	return resp, nil
}

// MarkAsRead marks a notification as acknowledged.
func (s *Service) MarkAsRead(ctx context.Context, req *pb.MarkAsReadRequest) (*pb.MarkAsReadResponse, error) {
	id := req.GetNotificationId()
	if id == "" {
		return nil, errors.New("notification id required")
	}
	if err := s.tracker.UpdateDeliveryStatus(ctx, id, pb.DeliveryStatus_DELIVERY_STATUS_ACKNOWLEDGED); err != nil {
		return nil, err
	}
	resp := &pb.MarkAsReadResponse{}
	resp.SetSuccess(true)
	return resp, nil
}

// Delete removes a notification from the service.
func (s *Service) Delete(ctx context.Context, req *pb.DeleteNotificationRequest) (*pb.DeleteNotificationResponse, error) {
	id := req.GetNotificationId()
	s.mu.Lock()
	_, ok := s.notifications[id]
	if ok {
		delete(s.notifications, id)
	}
	s.mu.Unlock()
	if !ok {
		return nil, errors.New("notification not found")
	}
	resp := &pb.DeleteNotificationResponse{}
	resp.SetSuccess(true)
	return resp, nil
}
