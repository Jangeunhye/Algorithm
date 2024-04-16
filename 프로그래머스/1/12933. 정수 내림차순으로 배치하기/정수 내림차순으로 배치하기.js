function solution(n) {
    let answer = [];
    return +(((n+"").split("").map((item)=> parseInt(item))).sort().reverse().join(""));
}