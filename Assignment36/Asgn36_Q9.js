// 9. Write a function which checks if all the items of the array are the same data type.

let items = [85,95,984,954,985,"Hello",95,"Name"]

function check_datatype(x){
    for (i=0; i<x.length; i++){

        if (typeof(x[0])==typeof(x[i])){
            y="All items having same datatype"
            continue
        }
        else{
            y = "Datatype of " +(i+1) +" element is " +typeof(x[i])
            break
        }
        
    }
    return y
}

console.log(check_datatype(items))