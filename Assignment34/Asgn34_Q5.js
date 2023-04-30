// Write a code which can give grades to students according to theirs scores:
// a. 80-100, A
// b. 70-89, B
// Untitled 2
// c. 60-69, C
// d. 50-59, D
// e. 0-49, F


const prompt = require("prompt-sync")({sigint:true})

let check_grade=(x)=>{
    if (x>=90 & x<=100){
        console.log('Your got A grade with marks :'+x)
    }
    else if (x>=70 & x<=89){
        console.log('Your got B grade with marks :'+x)
    }
    else if (x>=60 & x<=69){
        console.log('Your got C grade with marks :'+x)
    }
    else if (x>=50 & x<=59){
        console.log('Your got D grade with marks :'+x)
    }
    else if (x>=0 & x<=49){
        console.log('Your got F grade with marks :'+x)
    }
    else {
        console.log(x + ' Marks are not valid')
    }
}



let a = prompt("Please enter Marks ")
check_grade(a)