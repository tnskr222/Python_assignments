// Suppose 1 dollar is equal to 82.23 Indian rupee, create a program which converts
// dollars to rupees.

const prompt = require("prompt-sync")({sigint:true})

let a = prompt("Enter number of dollars you have : ")

let dollar = 82.23

console.log(dollar +' dollars is equal to : ' + dollar*a)
