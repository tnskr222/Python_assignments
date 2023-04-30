// Even numbers are divisible by 2 and the remainder is zero. How do you check, if a
// number is even or not using JavaScript?

const prompt = require("prompt-sync")({sigint:true})

let check_even_number=(x)=>{
    if (x%2==0){
        console.log(x +' is even number')
    }
    else {
        console.log(x+ ' is not even number')
    }
}



let a = prompt("Please enter a number ")
check_even_number(a)