// Create a countries array, check if there is a country or countries containing the word
// 'and'. If there are countries containing 'and', print it as array. If there is no country
// containing the word 'and', print 'All these countries are without and'

const countries=["India", "US", "England", "Russia", "Canada", "Iran", "Iraq", "Sweden", "Newzeland", "South Africa", "Australia"]

let and_countries=[]
let not_and_countries=[]

for (i=0; i<countries.length; i++){
    if (countries[i].includes("and")){
        and_countries.push(countries[i])
    }
    else{
        not_and_countries.push(countries[i])
    }
}

console.log("Countries with and is "+ and_countries)
console.log("Countries without and is "+ not_and_countries)