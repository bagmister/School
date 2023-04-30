/* Lesson 2 */

/* VARIABLES */

// Step 1: declare and instantiate a variable to hold your name
const myName = document.querySelector("#name");
myName.textContent = "Kevin Bagley";
// Step 2: place the value of the name variable into the HTML file (hint: document.querySelector())


// Step 3: declare and instantiate a variable to hold the current year


// Step 4: place the value of the current year variable into the HTML file
const currentYear = document.querySelector("#year");
currentYear.textContent = "2023";
// Step 5: declare and instantiate a variable to hold the name of your picture


// Step 6: copy your image into the "images" folder

// Step 7: place the value of the picture variable into the HTML file (hint: document.querySelector().setAttribute())

const myPicture = document.querySelector("#mainPhoto").src ='images/myPhoto.jpg';


/* ARRAYS */

// Step 1: declare and instantiate an array variable to hold your favorite foods
const favoriteFoods = document.querySelector("#food")
favoriteFood1 = "Sea food"
favoriteFood2 = "Hawaiian"
favoriteFood3 = "BBQ"
favoriteFood4 = "Palusami"
favoriteFood5 = "Saimin"
favoriteFoodsArray = [favoriteFood1, favoriteFood2, favoriteFood3, favoriteFood4, favoriteFood5];
favoriteFoodsArray.splice(1,1)
favoriteFoodsArray.splice(3,1)

favoriteFoods.textContent = favoriteFoodsArray

// Step 2: place the values of the favorite foods variable into the HTML file


// Step 3: declare and instantiate a variable to hold another favorite food


// Step 4: add the variable holding another favorite food to the favorite food array


// Step 5: repeat Step 2


// Step 6: remove the first element in the favorite foods array


// Step 7: repeat Step 2


// Step 8: remove the last element in the favorite foods array


// Step 7: repeat Step 2



