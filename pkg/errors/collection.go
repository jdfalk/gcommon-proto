// file: pkg/errors/collection.go
// version: 1.0.0
// guid: c4f5aa8b-90d4-4b16-8c5c-f1990e8abcde

package errors

import "strings"

// Collection aggregates multiple Errors.
type Collection struct {
	errs []Error
}

// Add appends an Error to the collection.
func (c *Collection) Add(err Error) {
	if err == nil {
		return
	}
	c.errs = append(c.errs, err)
}

// Error implements the error interface returning a concatenated message.
func (c *Collection) Error() string {
	msgs := make([]string, 0, len(c.errs))
	for _, e := range c.errs {
		msgs = append(msgs, e.Error())
	}
	return strings.Join(msgs, "; ")
}

// Errors returns the underlying slice of Errors.
func (c *Collection) Errors() []Error {
	return c.errs
}

// Len returns the number of errors in the collection.
func (c *Collection) Len() int {
	return len(c.errs)
}
