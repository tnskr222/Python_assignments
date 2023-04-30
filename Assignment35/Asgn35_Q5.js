// 
let it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM","Oracle", "Amazon"]

function it(it_companies){
    let y=String
    for (let i=0; i<it_companies.length; i++){
        if (i==0){
            y=it_companies[i]
        }
        else{
            y=y+", "+it_companies[i]
        }
        y =y.toUpperCase()
    }
    console.log(y + " are big IT Companies")
}

it(it_companies)