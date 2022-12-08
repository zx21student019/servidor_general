function subirLibro() {
    var newImage = document.createElement('img');
    newImage.src = item_image;
    $("#fileNewIssue").src = newImage.src;
}