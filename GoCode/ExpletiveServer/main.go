// ExpletiveServer project main.go
package main

import (
	"log"
	"github.com/googollee/go-socket.io"
	//"fmt"
	"net/http"
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
	server, err := socketio.NewServer(nil)
    if err != nil {
        log.Fatal(err)
    }
    server.On("connection", func(so socketio.Socket) {
        log.Println("on connection")
        so.Join("chat")
        so.On("chat message", func(msg string) {
            log.Println("emit:", so.Emit("chat message", msg))
            so.BroadcastTo("chat", "chat message", msg)
        })
        so.On("disconnection", func() {
            log.Println("on disconnect")
        })
    })
    server.On("error", func(so socketio.Socket, err error) {
        log.Println("error:", err)
    })

    http.Handle("/socket.io/", server)
    http.Handle("/", http.FileServer(http.Dir("./asset")))
    log.Println("Serving at localhost:5000...")
    log.Fatal(http.ListenAndServe(":5000", nil))
}


