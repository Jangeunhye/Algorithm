function solution(s){
    let pCount = 0;
    let yCount = 0;
    for (let w of s){
        if(w==='P'||w==='p'){
            pCount+=1
        }
        else if(w==='Y'||w==='y'){
            yCount+=1
        }
    }
     return  (!pCount&& !yCount)?true:pCount ===yCount;
}