// 10. JavaScript variable name does not support special characters or symbols except $
// or _. Write a function isValidVariable which check if a variable is valid or invalid variable.

function isvalidvariable(x){
    let spec_char = /[!@#%^&*()+\-=\[\]{}:';"\/,.<>?]+/;
    if(spec_char.test(x)){
        return false
    }
    else{
        return true
    }
}

let variable="Ineuron_ "
console.log(isvalidvariable(variable))