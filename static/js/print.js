function printReport() {
    var printButton = document.getElementById("printreport");
    printButton.style.visibility = 'hidden';
    window.print()
    printButton.style.visibility = 'visible';
}