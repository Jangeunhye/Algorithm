function solution(s) {
    let answer = [...s];
    answer = answer.sort().reverse().join("")
    return answer;
}