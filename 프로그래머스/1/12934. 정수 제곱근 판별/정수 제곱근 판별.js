function solution(n) {
    if(n===1)
        return (n+1)**2;
    
    for(let x = 2; x<Math.floor(n/2);x++){
        if(x**2===n)
            return (x+1)**2;
    }
    
    return -1;
}