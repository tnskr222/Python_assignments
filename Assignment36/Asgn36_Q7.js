// Write a function called sumOfArrayItems, it takes an array parameter and return the
// sum of all the items. Check if all the array items are number types. If not give return
// reasonable feedback


Array_items =[8,952,745,984,"Canada", "6"]
function sumOfArrayItems(x){
    let d=0
    let e=[]
    for (i=0, c=0; i<x.length; i++){
        d=d+x[i]
        if(typeof(x[i]) == "number"){
            c=c+x[i]
        }
        else{
            e.push(x[i])
        }
    }
    let f= ["Sum of items in the Array is "+d," The follwing are not number data types "+e]
    return f
}
console.log(sumOfArrayItems(Array_items))