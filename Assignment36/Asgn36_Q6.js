//  Declare a function name capitalizeArray. It takes array as a parameter and it returns
// the - capitalizedarray.

const fruits = ['banana', 'orange', 'mango', 'lemon']
let c=String

function capitalized_fruitsarray(x){
    for (i=0, b=[]; i<fruits.length; i++){
        c=fruits[i].toUpperCase()
        b.push(c)
    }
    return b
}

console.log(capitalized_fruitsarray(fruits))