//  Create a human readable time format using the Date time object
// a. YYYY-MM-DD HH:mm
// b. DD-MM-YYYY HH:mm
// c. DD/MM/YYYY HH:mm


const moment = require('moment')
moment().format()

const now = new Date()
const a = moment(now).format('YYYY-MM-DD HH:mm')
const b = moment(now).format('DD-MM-YYYY HH:mm')
const c = moment(now).format('DD/MM/YYYY HH:mm')
console.log(a)
console.log(b)
console.log(c)