// file: perf/framework/profiling.go
// version: 1.1.0
// guid: ab4d72d9-fc62-4f07-8051-55df394207c0

package framework

import (
	"fmt"
	"os"
	"runtime"
	"runtime/pprof"
	"time"
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

// CaptureBlockProfile writes a blocking profile to the specified path.
func CaptureBlockProfile(path string, dur time.Duration) error {
	runtime.SetBlockProfileRate(1)
	defer runtime.SetBlockProfileRate(0)
	time.Sleep(dur)
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	if err := pprof.Lookup("block").WriteTo(f, 0); err != nil {
		return err
	}
	return nil
}

// CaptureGoroutineProfile writes goroutine profile to path.
func CaptureGoroutineProfile(path string) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	if err := pprof.Lookup("goroutine").WriteTo(f, 0); err != nil {
		return err
	}
	return nil
}

// RuntimeStats captures current memory and goroutine statistics.
func RuntimeStats() (MemoryMetrics, ResourceMetrics) {
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	mem := MemoryMetrics{AllocatedBytes: m.Alloc, TotalBytes: m.TotalAlloc}
	res := ResourceMetrics{Goroutines: runtime.NumGoroutine()}
	return mem, res
}

// ProfileSection executes fn while collecting CPU profile for duration d.
func ProfileSection(path string, d time.Duration, fn func()) error {
	f, err := StartCPUProfile(path)
	if err != nil {
		return err
	}
	timer := time.AfterFunc(d, func() { StopCPUProfile(f) })
	fn()
	timer.Stop()
	StopCPUProfile(f)
	return nil
}

// LogRuntimeStats prints memory and goroutine usage to stdout.
func LogRuntimeStats() {
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	fmt.Printf("alloc=%d totalAlloc=%d sys=%d numGC=%d goroutines=%d\n",
		m.Alloc, m.TotalAlloc, m.Sys, m.NumGC, runtime.NumGoroutine())
}
