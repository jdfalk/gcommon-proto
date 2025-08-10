// file: pkg/errors/wrapping.go
// version: 1.1.0
// guid: ebb740ca-1926-4333-94a6-785dbcd3423b

package errors

// Wrap attaches component and operation context to an existing error.
func Wrap(err error, component, operation string) Error {
	return WrapWithCode(err, ErrCodeUnknown, component, operation)
}

// WrapWithCode attaches a code along with component and operation context.
func WrapWithCode(err error, code ErrorCode, component, operation string) Error {
	if err == nil {
		return nil
	}
	if e, ok := err.(Error); ok {
		if component != "" {
			if be, ok := e.(*BaseError); ok {
				be.component = component
			}
		}
		if operation != "" {
			if be, ok := e.(*BaseError); ok {
				be.operation = operation
			}
		}
		return e
	}
	be := newBaseError(code, component, operation, err.Error())
	be.cause = err
	return be
}

// WrapWithDetails attaches additional details to an error.
func WrapWithDetails(err error, details map[string]interface{}) Error {
	if err == nil {
		return nil
	}
	if e, ok := err.(Error); ok {
		be, ok := e.(*BaseError)
		if ok {
			if be.details == nil {
				be.details = map[string]interface{}{}
			}
			for k, v := range details {
				be.details[k] = v
			}
		}
		return e
	}
	be := newBaseError(ErrCodeUnknown, "", "", err.Error())
	be.cause = err
	be.details = details
	return be
}
