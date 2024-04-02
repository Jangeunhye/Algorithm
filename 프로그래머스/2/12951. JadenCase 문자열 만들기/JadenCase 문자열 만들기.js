function solution(s) {
    let temp = s.split(" ")
    let answer =[]
    for (i in temp){
        if(isNaN(temp[i].charAt(0))){
        //숫자가 아닐 경우
        let word = temp[i].charAt(0).toUpperCase()+temp[i].substr(1).toLowerCase()
        answer.push(word)
    }
        else{
            answer.push(temp[i].toLowerCase())
        }


    }
    


    return answer.join(" ");
}