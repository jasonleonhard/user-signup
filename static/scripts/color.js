// waiting for page load
    // non-jquery version
        // document.addEventListener("DOMContentLoaded", function(event) {
    // jquery version
        // $(function() {


function updateR(R) {
    document.querySelector('#R_number').value = R;
    document.querySelector('#R_range').value = R;
}
function updateG(G) {
    document.querySelector('#G_number').value = G;
    document.querySelector('#G_range').value = G;
}
function updateB(B) {
    document.querySelector('#B_number').value = B;
    document.querySelector('#B_range').value = B;
}
function updateA(A) {
    document.querySelector('#A_number').value = A;
    document.querySelector('#A_range').value = A;
}

function changeColor() {
    var R = document.querySelector('#R_number').value;
    var G = document.querySelector('#G_number').value;
    var B = document.querySelector('#B_number').value;
    var A = document.querySelector('#A_number').value;

    var current_color = "rgba(" + R + ", " + G + ", " + B +  ", " + A + ")";
    console.log(current_color);

    $('body').css('background', current_color)
    document.getElementById("rgba").innerHTML = current_color;

    // if (R == 0 && G == 255 && B == 255 && A == 1) {
    //     var color_name = document.querySelector('#color_name');
    //     color_name.innerHTML = 'aqua';
    //     document.getElementById("rgba").innerHTML = current_color;
    // } else {
    //     // color_name.innerHTML = current_color;
    //     // $("#rgb").text(current_color);
    //     // document.getElementById("rgba").innerHTML = '';
    //     document.getElementById("rgba").innerHTML = '';
    // }
}
