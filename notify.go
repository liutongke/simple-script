package main

import (
	"github.com/fsnotify/fsnotify"
	"log"
)

func main() {
	// 创建文件/目录监听器
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		log.Fatal(err)
	}
	defer watcher.Close()
	done := make(chan bool)
	go func() {
		for {
			select {
			case event, ok := <-watcher.Events:
				if !ok {
					return
				}
				// 打印监听事件
				log.Println("event:", event)
			case _, ok := <-watcher.Errors:
				if !ok {
					return
				}
			}
		}
	}()
	// 监听当前目录
	err = watcher.Add("./")
	if err != nil {
		log.Fatal(err)
	}
	<-done
}
