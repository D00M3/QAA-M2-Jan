'use strict'

// Looks for HTML elements by ID
const textbox = document.querySelector("#textbox")
const button = document.querySelector("#button")
const header = document.querySelector("#function_text")
console.log(textbox)
console.log(button)
console.log(header)

const buttonClick = () => {
    // Setting the text in the header to be the value of the textbox
    header.textContent = textbox.value
}

button.addEventListener("click", buttonClick) 