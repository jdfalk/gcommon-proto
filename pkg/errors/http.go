// file: pkg/errors/http.go
// version: 1.0.0
// guid: 21b70e69-5e9d-4e40-b9d1-8f89980bba34

package errors

import (
	"encoding/json"
	"net/http"
)

// ToHTTPStatus maps an Error to an HTTP status code.
func ToHTTPStatus(err Error) int {
	if err == nil {
		return http.StatusOK
	}
	switch err.Code() {
	case ErrCodeInvalidInput:
		return http.StatusBadRequest
	case ErrCodeNotFound:
		return http.StatusNotFound
	case ErrCodeAlreadyExists:
		return http.StatusConflict
	case ErrCodeTimeout:
		return http.StatusGatewayTimeout
	case ErrCodeUnauthorized:
		return http.StatusUnauthorized
	case ErrCodeForbidden:
		return http.StatusForbidden
	case ErrCodeUnavailable:
		return http.StatusServiceUnavailable
	default:
		return http.StatusInternalServerError
	}
}

// HTTPErrorResponse is the serialized HTTP error payload.
type HTTPErrorResponse struct {
	Code    int                    `json:"code"`
	Message string                 `json:"message"`
	Details map[string]interface{} `json:"details,omitempty"`
}

// WriteHTTPError writes an Error to an http.ResponseWriter as JSON.
func WriteHTTPError(w http.ResponseWriter, err Error) {
	status := ToHTTPStatus(err)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	payload := HTTPErrorResponse{Code: int(err.Code()), Message: err.Error(), Details: err.Details()}
	_ = json.NewEncoder(w).Encode(payload)
}
