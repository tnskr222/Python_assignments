// 8. Write a function called modifyArray takes array as parameter and modifies the fifth
// item of the array and return the array. If the array length is less than five it return 'item
// not found'.

let items_Array=[89, "ineuron",5,9,8,898,995,58]
let items=[]

function modifyArray(x){
    if (x.length>=5){
        x.splice(5,1,"Modified")
        y=x
    }
    else{
        y ="item not found"
    }
    return y
}

console.log(modifyArray(items_Array))