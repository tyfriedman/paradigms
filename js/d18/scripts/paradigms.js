function Item() {
	this.addToDocument = function() {
		document.body.appendChild(this.item);
	}
}

function Label() {
	this.createLabel = function(text, id) {
		this.item = document.createElement("p");
		this.item.setAttribute("id", id);
		this.item.innerHTML = text;
	},
	this.setText = function(text) {
		this.item.innerHTML = text;
	}
}

function Button() {
	this.createButton = function(text, id) {
		this.item = document.createElement("button");
		this.item.setAttribute("id", id);
		this.item.innerHTML = text;
	},
	this.addClickEventHandler = function(handler, arg) {
		this.item.onmouseup = function() {
			handler(arg);
		}
	}
}

