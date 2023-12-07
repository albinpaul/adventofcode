package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func isSymbol(i int, j int, matrix [][]string) bool {
	r := len(matrix)
	c := len(matrix[0])
	if !(0 <= i && i < r && 0 <= j && j < c) {
		return false
	}
	e := matrix[i][j]
	if _, err := strconv.Atoi(e); err == nil {
		return false
	}
	return e == "*"
}

func main() {

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var matrix [][]string
	for scanner.Scan() {
		var row []string
		for _, c := range scanner.Text() {
			row = append(row, string(c))
		}
		matrix = append(matrix, row)
	}
	gears := make(map[string][]uint64)
	for i, row := range matrix {
		var num uint64 = 0
		gearList := make(map[string]bool)
		for j, e := range row {
			if d, err := strconv.Atoi(e); err == nil {
				d := uint64(d)
				num = num*10 + d
				for a := -1; a <= 1; a++ {
					for b := -1; b <= 1; b++ {
						if a == 0 && b == 0 {
							continue
						}
						if isSymbol(i+a, j+b, matrix) {
							key := strconv.Itoa(i+a) + "," + strconv.Itoa(j+b)
							gearList[key] = true
						}
					}
				}
				matrix[i][j] = "."
			} else {
				for key, _ := range gearList {
					_, ok := gears[key]
					if !ok {
						gears[key] = []uint64{}
					}
					gears[key] = append(gears[key], num)
				}
				num = 0
				gearList = make(map[string]bool)
			}
		}

		for key, _ := range gearList {
			_, ok := gears[key]
			if !ok {
				gears[key] = []uint64{}
			}
			gears[key] = append(gears[key], num)
		}
		num = 0
		gearList = make(map[string]bool)

	}

	var ans uint64 = 0
	for _, v := range gears {
		if len(v) != 2 {
			continue
		}
		ans += v[0] * v[1]
	}
	fmt.Println(ans)
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
