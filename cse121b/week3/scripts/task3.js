/* Lesson 3 */

/* FUNCTIONS */

// Step 1: Using function declaration, define a function named add that takes two arguments, number1 and number2

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

let buttonAdd = document.getElementById("addNumbers");
let sum = buttonAdd.addEventListener("click", function() {addNumbers();});
let buttonSub = document.getElementById("subtractNumbers");
let diff = buttonAdd.addEventListener("click", function() {subtractNumbers();});
let buttonmult = document.getElementById("multiplyNumbers");
let product = buttonAdd.addEventListener("click", function() {multiplyNumbers();});
let buttondiv = document.getElementById("divideNumbers");
let quotient = buttonAdd.addEventListener("click", function() {divideNumbers();});

/* BUILT-IN METHODS */

// Step 1: Declare and instantiate a variable of type Date to hold the current date

// Step 2: Declare a variable to hold the current year

// Step 3: Using the variable declared in Step 1, call the built-in getFullYear() method/function and assign it to the variable declared in Step 2

// Step 4: Assign the current year variable to an HTML form element with an ID of year


/* ARRAY METHODS */

// Step 1: Declare and instantiate an array variable to hold the numbers 1 through 25

// Step 2: Assign the value of the array variable to the HTML element with an ID of "array"

// Step 3: Use the filter array method to find all of the odd numbers of the array variable and assign the reult to the HTML element with an ID of "odds" ( hint: % (modulus operartor) )

// Step 4: Use the filter array method to find all of the even numbers of the array variable and assign the result to the HTML element with an ID of "evens"

// Step 5: Use the reduce array method to sum the array variable elements and assign the result to the HTML element with an ID of "sumOfArray"

// Step 6: Use the map array method to multiple each element in the array variable by 2 and assign the result to the HTML element with an ID of "multiplied"

// Step 7: Use the map and reduce array methods to sum the array elements after multiplying each element by two.  Assign the result to the HTML element with an ID of "sumOfMultiplied"
