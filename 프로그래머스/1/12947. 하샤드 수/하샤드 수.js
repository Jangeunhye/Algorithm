function solution(x) {
    let sum= 0;
    let tempX = x;
    while(tempX>0){
        sum += tempX%10;
        tempX = Math.floor(tempX/10);
    }
    return x%sum===0;
}