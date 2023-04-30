// Write a program to print unit digit of a given number.
// Input : 6693
// Output : 3

const prompt = require("prompt-sync")({sigint:true})

let a = prompt("Enter a number : ")

console.log('Unit digit of ' +a + ' is :'+ a%10)