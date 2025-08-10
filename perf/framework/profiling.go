// file: perf/framework/profiling.go
// version: 1.0.0
// guid: ab4d72d9-fc62-4f07-8051-55df394207c0

package framework

import (
	"os"
	"runtime"
	"runtime/pprof"
)

// StartCPUProfile begins CPU profiling and writes to the given path.
func StartCPUProfile(path string) (*os.File, error) {
	f, err := os.Create(path)
	if err != nil {
		return nil, err
	}
	if err := pprof.StartCPUProfile(f); err != nil {
		_ = f.Close()
		return nil, err
	}
	return f, nil
}

// StopCPUProfile stops the CPU profile and closes the file.
func StopCPUProfile(f *os.File) {
	pprof.StopCPUProfile()
	_ = f.Close()
}

// WriteMemProfile writes a heap profile to the specified path.
func WriteMemProfile(path string) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	runtime.GC()
	return pprof.WriteHeapProfile(f)
}
