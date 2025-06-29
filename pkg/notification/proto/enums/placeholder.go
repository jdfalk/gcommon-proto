// file: pkg/notification/proto/enums/placeholder.go
// Placeholder file to satisfy import requirements until protobuf generation is complete

package enums

// TODO: This file will be replaced by generated protobuf files
// Placeholder types to satisfy import requirements

// DeliveryStatus represents the status of notification delivery
type DeliveryStatus int32

const (
	DeliveryStatus_DELIVERY_STATUS_UNSPECIFIED DeliveryStatus = 0
	DeliveryStatus_PENDING                     DeliveryStatus = 1
	DeliveryStatus_SENT                        DeliveryStatus = 2
	DeliveryStatus_DELIVERED                   DeliveryStatus = 3
	DeliveryStatus_FAILED                      DeliveryStatus = 4
)
