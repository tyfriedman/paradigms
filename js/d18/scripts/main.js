function changeText(id) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student13.cse.nd.edu:51000/movies/32", true);
	xhr.onload = function(e) {
		id.setText(xhr.responseText);
	}
	xhr.send(null);
}

Label.prototype = new Item();
label= new Label();
label.createLabel("Movie 32?", "theLabel");
label.addToDocument();

Button.prototype = new Item();
button = new Button();
button.createButton("CLICK HERE!", "theButton");
button.addClickEventHandler(changeText, label);
button.addToDocument();