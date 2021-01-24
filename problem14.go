package main

import "fmt"

var chainLengths = make(map[int]int)

func main() {
	var maxChainLength int
	var maxStarting int
	for i := 1; i < 1e6; i++ {
		l := ChainLength(i)
		if l > maxChainLength {
			maxChainLength = l
			maxStarting = i
		}
	}
	fmt.Println(maxStarting)
}

func Collatz(n int) int {
	if n%2 == 0 {
		return n / 2
	} else {
		return 3*n + 1
	}
}

func ChainLength(n int) int {
	l := 0
	for n != 1 {
		i, ok := chainLengths[n]
		if ok {
			return l + i
		}
		n = Collatz(n)
		l++
	}
	chainLengths[n] = l
	return l + 1
}
