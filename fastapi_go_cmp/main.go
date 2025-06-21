package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"

	"github.com/siuyin/dflt"
)

func main() {
	http.HandleFunc("/", root)
	http.HandleFunc("GET /items/{id}", items)
	port := dflt.EnvString("PORT", "8080")
	log.Fatal(http.ListenAndServe(":"+port, nil))
}

func root(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, `{"Hello":"World"}`)
}

type item struct {
	ID json.Number `json:"id"`
	Q  string      `json:"q"`
}

func items(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	b, err := parseItem(r)
	if err != nil {
		log.Println(err)
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.Write(b)
}

func parseItem(r *http.Request) ([]byte, error) {
	i := item{ID: json.Number(r.PathValue("id")), Q: r.FormValue("q")}
	b, err := json.Marshal(&i)
	if err != nil {
		return nil, err
	}
	return b, nil
}
