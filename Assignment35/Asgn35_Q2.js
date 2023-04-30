// In the webTechs array check if Sass exists in the array and if it exists print 'Sass is a
// CSS preprocess'. If it does not exist add Sass to the array and print the array.


const CSS_preprocess =["SaaS", "IaaS", "PaaS"]

b = CSS_preprocess.includes("SaaS")


if (b==true){
    console.log("Sass is a CSS preprocess")
}
else{
    CSS_preprocess.push("SaaS")
    console.log(CSS_preprocess)
}


