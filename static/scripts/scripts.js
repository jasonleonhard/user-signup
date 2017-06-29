// using external javascript
function changeContents() {
    document.getElementById("hi").innerHTML = 'you!!!?'
}

function sayHello() {
    alert("Hello")
}

function logit() {
    console.log("works");
}

// If not using inline javascript you can use on window load
// without jQuery wait for window to load to run
    // window.onload = function () {
        // example
        // document.getElementById("hi").innerHTML = 'there'
    // }

// jQuery version
    // $(document).ready(function() {
    //     // jQuery code goes here
    // });

// without waiting caching will lock this file and changes will not work
    // document.getElementById("hi").innerHTML = 'there'
