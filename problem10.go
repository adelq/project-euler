package main

import (
	"fmt"
	"math"
)

func main() {
	sum := 0
	for i := 0; i < 2e6; i++ {
		if prime(i) {
			sum += i
		}
	}
	fmt.Println(sum)
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
