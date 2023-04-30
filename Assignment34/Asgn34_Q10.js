// Write a program to find the area of the circle. Take radius of circle from user as input
// and print the result in below given format

const pi = Math.PI
const prompt = require("prompt-sync")({sigint:true})

let a = prompt("Enter radius of circel : ")
let b = pi*a**2
b = b.toFixed(2)

console.log('Area of circle with radius '+ a + ' is : '+ b)