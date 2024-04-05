function solution(x, n) {
    var answer = [];
    answer.push(x)
    for (let i= 1; i<n;i++){
        answer.push(answer.at(-1)+x)
    }   
    
    
    
    return answer;
}