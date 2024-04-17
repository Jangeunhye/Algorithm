function solution(n) {
    for(let x = 1; x<=Math.sqrt(n);x++){
        if(x**2===n)
            return (x+1)**2;
    }
    
    return -1;
}