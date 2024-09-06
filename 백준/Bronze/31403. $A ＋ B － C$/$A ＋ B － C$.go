package main
import (
    "fmt"
)

func main() {
    var a,b,c int
    var num = 0
    fmt.Scan(&a)
    fmt.Scan(&b)
    fmt.Scan(&c)
    
    for i := 1 ; i <= b; i *= 10 {
        num = i
    }
    
    fmt.Println(a + b - c);
    
    fmt.Println(a * (num * 10) + b - c)
}