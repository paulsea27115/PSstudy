package main

import (
	"bufio"
	"fmt"
	"os"
)

func mod(n int, m int) int{
    big, small := 0, 0
    if n >= m{
        big = n
        small = m
    } else {
        big = m
        small = n
    }
    return big % small
}

func euclidean(n int, m int) int {    
    div_mod := mod(n,m)
    
    if div_mod == 0{
        return m
    }
    return euclidean(m, div_mod)
}

func main(){
    var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	    
	defer writer.Flush()
	
	a,b,c,d := 0, 0, 0, 0
    under, top := 0, 0
	fmt.Fscanln(reader, &a, &b)
	fmt.Fscanln(reader, &c, &d)
	
	under = b*d
    top = a*d + c*b	
	
	res := euclidean(top, under)
	if res == 1{
	    fmt.Fprintln(writer, top, under)
	} else {
	    fmt.Fprintln(writer, top / res, under / res)   
	}
}
