// ExpletiveServer project main.go
package main

import (
	"fmt"
)

//Content Pieces, the small packets of data the network transfers.
type Content_Piece struct {
	id string
}

//Content, the specifications for assembling content pieces into items for sale.
type Content struct {
	id string
}

type User struct {
	id string
}

func main() {
	fmt.Println("Hello World!")
}
