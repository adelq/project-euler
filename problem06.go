package main

import "fmt"

func main() {
	n := 100
	fmt.Println(sqsum(n) - sumsq(n))
}

func sqsum(n int) int {
	s := 0
	for i := 0; i <= n; i++ {
		s += i
	}
	return s * s
}

func sumsq(n int) int {
	s := 0
	for i := 0; i <= n; i++ {
		s += i * i
	}
	return s
}
