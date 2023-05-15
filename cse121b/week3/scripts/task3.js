function add(number1, number2) {
    sum = number1 + number2;
    return sum;
}

function addNumbers(){
    var addend1 = parseInt(document.querySelector("#addend1").value);
    var addend2 = parseInt(document.querySelector("#addend2").value);


    sum = add(addend1, addend2);
    document.querySelector("#sum").value = sum;
    return sum;
}

function subtract(number1, number2){
    difference = number1 - number2
    return difference
}

function subtractNumbers(){
    var minuend = parseInt(document.querySelector("#minuend").value);
    var subtrahend = parseInt(document.querySelector("#subtrahend").value);

    difference = subtract(minuend, subtrahend)
    document.querySelector('#difference').value = difference

}

function divideNumbers(){
    var dividend = parseInt(document.querySelector("#dividend").value);
    var divisor = parseInt(document.querySelector("#divisor").value);
    
    quotient = subtract(dividend, divisor)
    document.querySelector('#quotient').value = quotient
}

function division(number1, number2){
    quotient = number1 - number2
    return quotient
}

function multiply(number1, number2){
    product = number1 * number2
    return product
}

function multiplyNumbers(){
    var factor1 = parseInt(document.querySelector("#factor1").value);
    var factor2 = parseInt(document.querySelector("#factor2").value);

    product = multiply(factor1, factor2)
    document.querySelector('#product').value = product
}

function getOddsArray(value){
    return value % 2 !== 0
}

function getEvensArray(value){
    return value % 2 === 0;
}

function reduceArray(accumulator, value){
    return accumulator + value;
}

function arrayMappedDoubled(value){
    return value * 2;
}

function sumDoubbled(){

}

let currentDate = new Date();
let year  = currentDate.getFullYear();
document.getElementById('year').innerHTML = year;
let buttonAdd = document.getElementById("addNumbers");
let sum = buttonAdd.addEventListener("click", function() {addNumbers();});
let buttonSub = document.getElementById("subtractNumbers");
let diff = buttonAdd.addEventListener("click", function() {subtractNumbers();});
let buttonmult = document.getElementById("multiplyNumbers");
let product = buttonAdd.addEventListener("click", function() {multiplyNumbers();});
let buttondiv = document.getElementById("divideNumbers");
let quotient = buttonAdd.addEventListener("click", function() {divideNumbers();});

let myArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25];
document.getElementById('array').innerHTML = myArray;
let odds = myArray.filter(getOddsArray);
document.getElementById('odds').innerHTML = odds;
let evens = myArray.filter(getEvensArray);
document.getElementById('evens').innerHTML = evens;
let arraySum = myArray.reduce(reduceArray);
document.getElementById('sumOfArray').innerHTML = arraySum;
let arrayMapped = myArray.map(arrayMappedDoubled);
document.getElementById('multiplied').innerHTML = arrayMapped;
let doubbledArraysum = arrayMapped.reduce(reduceArray)
document.getElementById('sumOfMultiplied').innerHTML = doubbledArraysum