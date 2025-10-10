// create some var for elems like input field, add button, ul list
const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

// create a function for add button
const addTask = () => {
    if (inputBox.value === "") {
        alert("You must write something!");
        // if input field is empty, alert message will be shown
    } else {
        let li = document.createElement("li");
        // create a li element
        li.innerHTML = inputBox.value;
        // add input field value to li
        listContainer.appendChild(li);
        // append li to ul list


        let span = document.createElement("span");
        // create a span element
        span.innerHTML = "\u00d7";
        // add cross mark to span
        li.appendChild(span);
        // append span to li
    }  
    inputBox.value = "";
    // after adding task, input field will be empty  
    saveData();
    // call the func to store data in local storage
    // the func is writte at the end of addTask func

}

// JS FOR THE CLICK FUNC
// whenever we click on container, this function will be called
// if the clicked target is li, toggle the checked class
// if clicked on span (cross mark), remove the li
listContainer.addEventListener("click", function(e) {
    if (e.target.tagName === "LI") {
        e.target.classList.toggle("checked");

        saveData();
        // call the func to store data in local storage
    }

    else if (e.target.tagName === "SPAN") {
        e.target.parentElement.remove();

        saveData();
        // call the func to store data in local storage
    }
},false);




// fun to store tasks in browser local storage
function saveData() {
    localStorage.setItem("data", listContainer.innerHTML);
}


// display the stored data when the page is loaded
function showTask() {
    listContainer.innerHTML = localStorage.getItem("data");
}
showTask();
// call the func to display the stored data when the page is loaded
