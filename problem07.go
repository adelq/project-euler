package main

import (
	"fmt"
	"math"
)

func main() {
	n := 0
	i := 0
	for n < 10001 {
		i++
		if prime(i) {
			n++
		}
	}
	fmt.Println(i)
}

func prime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i < int(math.Sqrt(float64(n))+1); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
