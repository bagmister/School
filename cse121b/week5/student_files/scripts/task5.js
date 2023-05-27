/* Lesson 5 */

const currentDate = new Date()
const currentDayOfWeek = currentDate.getDay()
let welcomeMessage = ""
let secondMessage = ""
const weekdays = [1, 2, 3, 4, 5]
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

function output(templeList) {
    let temples = document.querySelector('#temples')
    templeList.forEach(temple => {
        const templeName = document.createElement("h3")
        templeName.innerHTML = temple.templeName
        temples.append(templeName)
        const templelocation = document.createElement("h4")
        templelocation.innerHTML = temple.location
        temples.append(templelocation)
        const templeDedication = document.createElement("h4")
        templeDedication.innerHTML = temple.dedicated
        temples.append(templeDedication)
        const templeImage = document.createElement("img")
        templeImage.setAttribute("src", temple.imageUrl)
        templeImage.innerHTML = temple.imageUrl
        temples.append(templeImage)
    }
    );
}

async function getTemples(){
    url = 'https://byui-cse.github.io/cse121b-course/week05/temples.json'
    const response = await fetch(url);
    if (response.ok) {
        templesList = await response.json();
      output(templesList);
    }
}

function resetWorld() {
  document.querySelector('#temples').textContent = ''
}

function sortBy(){
    resetWorld()
    if (templesList[0].templeName == "Bountiful Utah Temple"){
        const sortedTemples = templesList.sort(compareDescend)
        output(sortedTemples)

    }
    else{
        const sortedTemples = templesList.sort(compareAscend)
        output(sortedTemples)
    }
}

function compareDescend(temple1, temple2){
    const compareValue = temple1.templeName.localeCompare(temple2.templeName)
    if(compareValue < 0){

        return 1;
    }
    else if (compareValue > 0) {
        return -1;
    }
    else{ 
        return 0;
    }
}

function compareAscend(temple1, temple2){
    const compareValue = temple1.templeName.localeCompare(temple2.templeName)
    if(compareValue > 0){

        return 1;
    }
    else if (compareValue < 0) {
        return -1;
    }
    else{ 
        return 0;
    }
}

let temples = getTemples()

document.querySelector("#sortBy").addEventListener("change", sortBy)

if (currentDayOfWeek in weekdays){
    welcomeMessage = "hang in there!"
}
else {
    welcomeMessage = "Woohoo! It's the weekend!"
}

document.querySelector('#message2').textContent = GetCurrentDay(currentDayOfWeek)
document.querySelector('#message1').textContent = welcomeMessage
document.querySelector('#year').textContent = currentDate.getFullYear();

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
