// Develop a small script which generate any number of characters random id

const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

function generaterandomid(length){
    let result = '';
    const characterslength = characters.length
    for (let i=0; i ,length; i++){
    result += characters.charAt(Math.floor(Math.random()*characterslength))
}
return result
}

console.log(generaterandomid(8))