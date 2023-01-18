'use strict'
// Data type or type of variable

// Looks for HTML elements by ID
const textbox = document.querySelector("#textbox")
const button = document.querySelector("#button")
const header = document.querySelector("#function_text")
const dataDiv = document.querySelector("#data_div")
const dataButton = document.querySelector("#data_button")
console.log(dataDiv)


const getData = () => {
    fetch("https://uselessfacts.jsph.pl/random.json")
    .then((response) => response.json())
    .then((data) => {
        createFact(data.text)
    });
}

const createFact = (fact) => {
    const newFact = document.createElement("h4");
    newFact.innerText = fact
    dataDiv.appendChild(newFact)
}

const buttonClick = () => {
    // Setting the text in the header to be the value of the textbox
    header.textContent = textbox.value
}

button.addEventListener("click", buttonClick) 
dataButton.addEventListener("click", getData)