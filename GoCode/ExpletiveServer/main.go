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

//Users are accounts representing people. Philosophically, it should be one user per person,
// but it should also be acknowledged that this isn't always the case.
type User struct {
	id, email, username, passhash string
}

type Node struct {
	id, User_ID string
}

func main() {
	fmt.Println("Hello World!")

}
