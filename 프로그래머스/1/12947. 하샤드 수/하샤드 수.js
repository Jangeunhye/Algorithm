function solution(x) {    
    // 1. 자릿수의 합 구하기
    let sum = (x+"").split("").reduce((acc, cur)=> acc+=parseInt(cur),0);
    // 2. 나누어 떨어지는 지 검사하기 
    return x%sum===0
}