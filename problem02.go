package main

import "fmt"

func main() {
	sum := 0
	for i, j := 1, 1; j < 4e6; i, j = i+j, i {
		if j%2 == 0 {
			sum += j
		}
	}
	fmt.Println(sum)
}
