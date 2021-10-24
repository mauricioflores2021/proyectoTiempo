function fechahoraReal() {
    document.getElementById("output").innerHTML = new Date();
}
setInterval(updateTime, 1000);