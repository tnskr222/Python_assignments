// In the following shopping cart add, remove, edit itemsconst shoppingCart = ['Milk',
// 'Coffee', 'Tea', 'Honey']
// a. add 'Meat' in the beginning of your shopping cart if it has not been already
// added
// b. add Sugar at the end of you shopping cart if it has not been already added
// c. remove 'Honey' if you are allergic to honey
// d. modify Tea to 'Green Tea'

const prompt = require("prompt-sync")({sigint:true})

const shoppingCart = ['Milk','Coffee', 'Tea', 'Honey']

shoppingCart.splice(0,0,"Meat")

shoppingCart.splice(6,0,"Sugar")

console.log(shoppingCart)
let a = prompt("Enter item i.e., allergic to you : ")
b=shoppingCart.indexOf(a)
shoppingCart.splice(b,1)
console.log(shoppingCart)
d=b=shoppingCart.indexOf("Tea")
shoppingCart.splice(d,1,"Green Tea")
console.log(shoppingCart)