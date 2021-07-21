package main

import (
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"time"
)

func main() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/add", insert)
	port := "12223"
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatal(err)
	}
}

type User struct {
	User string `gorm:"column:user" json:"content"` //请求人的userid
	ID   int    `gorm:"column:id" json:"id"`        //请求人的userid
}

func handler(w http.ResponseWriter, r *http.Request) {
	var user User
	GetMysqlClient().Table("account").First(&user)
	fmt.Println(user)
	fmt.Fprintf(w, "Hello World!\n-------------->"+user.User)
}

func insert(w http.ResponseWriter, r *http.Request) {
	rand.Seed(time.Now().UnixNano())

	user := User{User: time.Now().String(), ID: rand.Intn(100000)}

	GetMysqlClient().Table("account").Create(&user) // 通过数据的指针来创建
	fmt.Fprintf(w, "add \n-------------->"+strconv.Itoa(user.ID))
	// 返回插入数据的主键
}
