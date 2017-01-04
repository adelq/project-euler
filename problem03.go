package main

import "fmt"

func main() {
	fmt.Println(maxPrimeFactor(13195))
	fmt.Println(maxPrimeFactor(600851475143))
}

func maxPrimeFactor(n int) int {
	var maxFactor int
	d := 2
	for n > 1 {
		for n%d == 0 {
			if d > maxFactor {
				maxFactor = d
			}
			n /= d
		}
		d++
	}
	return maxFactor
}
