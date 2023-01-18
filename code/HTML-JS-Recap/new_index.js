// Tell JS to find my HTML elements
// const - constant variable that is immutable
// let - variable that is mutable
let title = document.querySelector("#main-header")
let inputText = document.querySelector("#input-text")
let buttonText = document.querySelector("#main-button")
let techTitle = document.querySelector("#tech-api")

// Create a function that captures the text value 
// function() {}  ==  () => {}
const getData = () => {
    let inputData = inputText.value
    inputText.value = ""
    console.log(inputData)
    title.innerText = inputData

    fetch("https://techy-api.vercel.app/api/json")
    .then((response) => response.json())
    .then((usable_data) => {
        techTitle.innerText = usable_data.message
        console.log(usable_data)
        console.log(usable_data.message)
    })

    // data = fetch("api url")
}

// Event Listener - Tells an interactive element (button) to do something when a 'click' is registered
buttonText.addEventListener("click", getData)

// https://techy-api.vercel.app/api/json