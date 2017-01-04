package main

import (
	"fmt"
	"strconv"
)

func main() {
	var max_palindrome int
	for i := 0; i < 1000; i++ {
		for j := i; j < 1000; j++ {
			product := i * j
			if palindrome(product) && product > max_palindrome {
				max_palindrome = product
			}
		}
	}
	fmt.Println(max_palindrome)
}

func palindrome(n int) bool {
	number := strconv.Itoa(n)
	for i, j := 0, len(number)-1; i < j; i, j = i+1, j-1 {
		if number[i] != number[j] {
			return false
		}
	}
	return true
}
