function changeText(id) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student13.cse.nd.edu:51000/movies/32", true);
	xhr.onload = function(e) {
		id.setText(xhr.responseText);
	}
	xhr.send(null);
}

function vote() {
	var selectedValue = dropdown.getSelected();
	var xhr = new XMLHttpRequest();
	xhr.open("PUT", "http://student13.cse.nd.edu:51000/recommendations/247", true);
	xhr.onload = function(e) {
		alert(xhr.responseText)
	}
	xhr.send(JSON.stringify({ "movie_id": "32", "rating": selectedValue }));
}

Label.prototype = new Item();
label= new Label();
label.createLabel("Which movie?", "theLabel");
label.addToDocument();

Button.prototype = new Item();
button = new Button();
button.createButton("Click Here", "theButton");
button.addClickEventHandler(changeText, label);
button.addToDocument();

var break_element1 = document.createElement("br");
var break_element2 = document.createElement("br");
document.body.appendChild(break_element1);
document.body.appendChild(break_element2);

Dropdown.prototype = new Item();
dropdown = new Dropdown();
const ratings = {
    1: "Just Plain Bad",
    2: "Not So Good",
    3: "OK I Guess",
    4: "Pretty Good",
    5: "Awesome!"
};
dropdown.createDropdown(ratings, "voting", 5);
dropdown.addSubmitEventHandler(vote);
dropdown.addToDocument();
