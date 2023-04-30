// Write a program which tells the number of days in a month.

const prompt = require("prompt-sync")({sigint:true})

let check_days=(x)=>{
    if (x==1){
        console.log('January Month has 31 days')
    }
    else if (x==2){
        console.log('Febrauary month has 28 days in normal year and 29 days in leap year')
    }
    else if (x==3){
        console.log('March month has 31 days')
    }
    else if (x==4){
        console.log('April month has 30 days')
    }
    else if (x==5){
        console.log('May month has 31 days')
    }
    else if (x==6){
        console.log('June month has 30 days')
    }
    else if (x==7){
        console.log('July month has 31 days')
    }
    else if (x==8){
        console.log('August month has 31 days')
    }
    else if (x==9){
        console.log('September month has 30 days')
    }
    else if (x==10){
        console.log('October month has 31 days')
    }
    else if (x==11){
        console.log('November month has 30 days')
    }
    else if (x==12){
        console.log('December month has 31 days')
    }
    else {
        console.log('Given month number is not valid')
    }
}



let a = prompt("Please enter month number : ")
check_days(a)