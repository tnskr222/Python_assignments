// This is a fruit array , ['banana', 'orange', 'mango', 'lemon'] reverse the order using
// loop without using a reverse method

const fruits = ['banana', 'orange', 'mango', 'lemon']

function fruitsarray(x){
    b = x.length
    for (i=0; i<b-1; i++){
        let c=x[b-1]
        x.pop()
        x.splice(i,0,c)
    }
    return x
}

console.log(fruitsarray(fruits))