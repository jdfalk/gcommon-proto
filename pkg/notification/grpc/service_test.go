// file: pkg/notification/grpc/service_test.go
// version: 1.0.0
// guid: 4c7d8e9f-1234-5678-9abc-def012345678

package grpcsvc

import (
	"context"
	"testing"

	"github.com/jdfalk/gcommon/pkg/notification/delivery"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
	_ "github.com/jdfalk/gcommon/pkg/notification/providers"
)

func TestServiceSendAndList(t *testing.T) {
	svc := NewService(delivery.NewInMemoryTracker())
	msg := &pb.NotificationMessage{}
	msg.SetId("n1")
	ch := &pb.DeliveryChannel{}
	ch.SetType(pb.DeliveryChannelType_DELIVERY_CHANNEL_TYPE_EMAIL)
	msg.SetChannels([]*pb.DeliveryChannel{ch})
	req := &pb.SendNotificationRequest{}
	req.SetNotification(msg)
	if _, err := svc.Send(context.Background(), req); err != nil {
		t.Fatalf("Send: %v", err)
	}
	listReq := &pb.ListNotificationsRequest{}
	resp, err := svc.List(context.Background(), listReq)
	if err != nil {
		t.Fatalf("List: %v", err)
	}
	if len(resp.GetNotifications()) != 1 {
		t.Fatalf("expected 1 notification, got %d", len(resp.GetNotifications()))
	}
}

func TestServicePreferencesAndTemplate(t *testing.T) {
	svc := NewService(delivery.NewInMemoryTracker())
	tmpl := &pb.Template{}
	tmpl.SetId("t1")
	tmpl.SetBody("hi")
	svc.AddTemplate(tmpl)
	prefs := &pb.SubscriptionPreferences{}
	prefs.SetUserId("u1")
	prefs.SetChannels([]pb.DeliveryChannelType{pb.DeliveryChannelType_DELIVERY_CHANNEL_TYPE_EMAIL})
	upd := &pb.UpdatePreferencesRequest{}
	upd.SetPreferences(prefs)
	if resp, err := svc.UpdatePreferences(context.Background(), upd); err != nil || !resp.GetSuccess() {
		t.Fatalf("UpdatePreferences: %v", err)
	}
	getReq := &pb.GetTemplateRequest{}
	getReq.SetId("t1")
	got, err := svc.GetTemplate(context.Background(), getReq)
	if err != nil || got.GetTemplate().GetId() != "t1" {
		t.Fatalf("GetTemplate: %v", err)
	}
}

func TestServiceMarkAndDelete(t *testing.T) {
	svc := NewService(delivery.NewInMemoryTracker())
	msg := &pb.NotificationMessage{}
	msg.SetId("n2")
	ch := &pb.DeliveryChannel{}
	ch.SetType(pb.DeliveryChannelType_DELIVERY_CHANNEL_TYPE_EMAIL)
	msg.SetChannels([]*pb.DeliveryChannel{ch})
	sendReq := &pb.SendNotificationRequest{}
	sendReq.SetNotification(msg)
	if _, err := svc.Send(context.Background(), sendReq); err != nil {
		t.Fatalf("Send: %v", err)
	}
	markReq := &pb.MarkAsReadRequest{}
	markReq.SetNotificationId("n2")
	if resp, err := svc.MarkAsRead(context.Background(), markReq); err != nil || !resp.GetSuccess() {
		t.Fatalf("MarkAsRead: %v", err)
	}
	delReq := &pb.DeleteNotificationRequest{}
	delReq.SetNotificationId("n2")
	if resp, err := svc.Delete(context.Background(), delReq); err != nil || !resp.GetSuccess() {
		t.Fatalf("Delete: %v", err)
	}
	listReq := &pb.ListNotificationsRequest{}
	list, _ := svc.List(context.Background(), listReq)
	if len(list.GetNotifications()) != 0 {
		t.Fatalf("expected 0 notifications, got %d", len(list.GetNotifications()))
	}
}
