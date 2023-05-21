/* Lesson 5 */

const currentDate = new Date()
const currentDayOfWeek = currentDate.getDay()
let welcomeMessage = ""
let secondMessage = ""
const weekdays = ['Monday, Tuesday, Wednesday, Thursday, Friday']
let templesList = []

function GetCurrentDay(currentDayOfWeek){
    
    switch (currentDayOfWeek){
        case 1:
            secondMessage = 'Monday';
            break
        case 2:
            secondMessage = 'Tuesday';
            break
        case 3:
            secondMessage = 'Wednesday';
            break
        case 4:
            secondMessage = 'Thursday';
            break
        case 5:
            secondMessage = 'Friday';
            break
        case 6:
            secondMessage = 'Saturday';
            break
        case 7:
            secondMessage = 'Sunday';
            break
        default:
            console.log('Day of the week could not be retrieved. value was ${currentDayOfWeek}')
            console.log(currentDayOfWeek)
    }
    return secondMessage
}

function output(templesList) {
    templesList.forEach(element => {
        document.createElement("article")
        document.createElement("h3", {templeName: element.templeName})
        document.createElement("h4", {location: element.location})
        document.createElement("h4", {dedicated: element.dedicated})
        document.createElement("img", {src : element.imageUrl},)

        
    });
}

if (currentDayOfWeek in weekdays){
    welcomeMessage = "hang in there!"
}
else {
    welcomeMessage = "Woohoo! It's the weekend!"
}

document.querySelector('#message2').textContent = GetCurrentDay(currentDayOfWeek)
document.querySelector('#message1').textContent = welcomeMessage
output(templesList)

/* FETCH */

// Step 2: Declare a function named output that accepts a list of temples as an array argument and does the following for each temple:
// - Creates an HTML <article> element
// - Creates an HTML <h3> element and add the temple's templeName property to it
// - Creates an HTML <h4> element and add the temple's location property to it
// - Creates an HTML <h4> element and add the temple's dedicated property to it
// - Creates an HTML <img> element and add the temple's imageUrl property to the src attribute and the temple's templeName property to the alt attribute
// - Appends the <h3> element, the two <h4> elements, and the <img> element to the <article> element as children
// - Appends the <article> element to the HTML element with an ID of temples

// Step 3: Create another function called getTemples. Make it an async function.
// Step 4: In the function, using the built-in fetch method, call this absolute URL: 'https://byui-cse.github.io/cse121b-course/week05/temples.json'. Create a variable to hold the response from your fetch. You should have the program wait on this line until it finishes.
// Step 5: Convert your fetch response into a Javascript object ( hint: .json() ). Store this in the templeList variable you declared earlier (Step 1). Make sure the the execution of the code waits here as well until it finishes.
// Step 6: Finally, call the output function and pass it the list of temples. Execute your getTemples function to make sure it works correctly.

// Step 7: Declare a function named reset that clears all of the <article> elements from the HTML element with an ID of temples

// Step 8: Declare a function named sortBy that does the following:
// - Calls the reset function
// - Sorts the global temple list by the currently selected value of the HTML element with an ID of sortBy
// - Calls the output function passing in the sorted list of temples

// Step 9: Add a change event listener to the HTML element with an ID of sortBy that calls the sortBy function

/* STRETCH */

// Consider adding a "Filter by" feature that allows users to filter the list of temples
// This will require changes to both the HTML and the JavaScript files
