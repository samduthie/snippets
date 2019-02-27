// concurrency in go
// Sam Duthie 2019

package main

import  (
    "fmt"
    "time"
)

func main() {
    go count("core 1")
    go count("core 2")

    fmt.Scalln()
}

func count(thing string) {
    for i := 1; true; i++ {
        fmt.Println(i, thing)
	time.Sleep(time.Millisecond * 500)
    }
}
