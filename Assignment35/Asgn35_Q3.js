// The following is an array of 10 students ages:
//  const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
// Sort the array and find the min and max age
// Find the median age(one middle item or two middle items divided by two)
// Find the average age(all items divided by number of items)
// Find the range of the ages(max minus min)
// Compare the value of (min - average) and (max - average), use abs()
// method

const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_sort = ages.sort()
console.log(ages_sort)

function ages_calc(x){
    y=x.sort()
    min_age=y[0]
    max_age=y[y.length-1]
    console.log(max_age)
    if (y.length%2==0){
        console.log("even")
        median_age = y[y.length/2]
        console.log("Median age is "+ median_age)
    }
    else{
        median_age= (y[(y.length+1)/2]+y[(y.length-1)/2])/2
        console.log("Median age is "+  median_age)
    }
    sum=0
    for (let i=0; i<y.length; i++){
        sum=sum+y[i]
    }
    console.log("sum of ages is "+sum)
    average=sum/y.length
    console.log("Average of ages is "+average)
    console.log("range of ages is "+ (max_age-min_age))
    console.log("Min age is "+ min_age)
    console.log("Max age is "+ max_age)
    c=Math.abs(min_age-average)-Math.abs(max_age-average)
    console.log("Compare with abs() of ages is "+ c)
}
ages_calc(ages)