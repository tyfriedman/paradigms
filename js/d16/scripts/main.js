document.getElementById("theButton").onmouseup = changeText;
var label = document.createElement("p");

label.setAttribute("id", "theLabel");

var labelText = document.createTextNode("who");

label.appendChild(labelText);

document.body.appendChild(label);

function changeText() {
	var tl = document.getElementById("theLabel");
	tl.innerHTML = "ty";
}
