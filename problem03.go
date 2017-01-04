package main

import "fmt"

func main() {
	fmt.Println(max_prime_factor(13195))
	fmt.Println(max_prime_factor(600851475143))
}

func max_prime_factor(n int) int {
	var max_factor int
	d := 2
	for n > 1 {
		for n%d == 0 {
			if d > max_factor {
				max_factor = d
			}
			n /= d
		}
		d++
	}
	return max_factor
}
