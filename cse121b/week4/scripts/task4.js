/* Lesson 4 */

/* DATA */
let livedPlace1 = {
    "place" : "centerville",
    "length": "2"
}

let livedPlace2 = {
    "place" : "midvale",
    "length": "3"
}

let livedPlace3 = {
    "place" : "sandy",
    "length": "4"
}

let livedPlace4 = {
    "place" : "magna",
    "length": "5"
}

let livedPlace5 = {
    "place" : "king of prussia",
    "length": "1"
}

let person1 = {
    'name' : 'Kevin',
    'photo': {'photoName': 'me',
    'src':'images/myPhoto.jpg',
    },
    'favoriteFoods': ["Sea food","Hawaiian","BBQ","Palusami","Saimin"],
    'hobbies': ["model railraoding", "3d modeling","auto mechanics","farming"],
    'placesLived': [livedPlace1,livedPlace2,livedPlace3,livedPlace4,livedPlace5]
}


let photo = document.querySelector('img')
document.querySelector('#name').innerHTML = person1['name']
photo.setAttribute("src", person1.photo.src.valueOf());
photo.setAttribute("alt", person1.photo.photoName.valueOf());
let favoriteFoods = document.querySelector("#favorite-foods")
let hobbies = document.querySelector("#hobbies")
let placesLived  = document.querySelector("#places-lived")

for (let i = 0; i < person1.favoriteFoods.length; i++) {
    let favoriteFoodsList = document.createElement('li');
    favoriteFoodsList.textContent = person1.favoriteFoods[i];
    favoriteFoods.append(favoriteFoodsList);
}

for (let i = 0; i < person1.hobbies.length; i++) {
    let hobbiesList = document.createElement('li');
    hobbiesList.textContent = person1.hobbies[i];
    hobbies.append(hobbiesList);
}

for (let i = 0; i < person1.placesLived.length; i++) {
    let placesLivedlistdt = document.createElement('dt');
    let placesLivedlistdd = document.createElement('dd');
    placesLivedlistdt.textContent = person1.placesLived[i].place;
    placesLivedlistdd.textContent = person1.placesLived[i].length;
    placesLived.append(placesLivedlistdt);
    placesLived.append(placesLivedlistdd);
}
