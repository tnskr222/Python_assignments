// Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all
// odds. Print sum of evens and sum of odds as array


let a=0
let b=0
let sum = []
for (i=0; i<=100; i++){

    if (i%2==0){
        a=a+i
    }
    else{
        b=b+i
    }
}
console.log(a,b)
sum.push(a,b)
console.log(" Sum of evens and sum of odds as array is "+ sum)