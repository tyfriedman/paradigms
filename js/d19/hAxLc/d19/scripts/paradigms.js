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

function Dropdown() {
    this.getSelected = function() {
        return this.select.value;
    };
	
	this.createDropdown = function(dict, id, selected) {
		
		this.item = document.createElement("form");

		var label = document.createElement("label");
		var txt = document.createTextNode("I thought this movie was...");
		label.appendChild(txt);
		this.item.appendChild(label);
		this.item.appendChild(document.createElement("br"));
		this.item.appendChild(document.createElement("br"));
		this.select = document.createElement("select");
		this.select.setAttribute("id", id);
		this.item.appendChild(this.select);

		for (let key in dict) {
			var tmp = document.createElement("option");
			tmp.setAttribute("value", key);

			if (key == selected) {
                tmp.setAttribute("selected", "selected");
            }

			var txt = document.createTextNode(dict[key]);
			tmp.appendChild(txt);
			this.select.appendChild(tmp);
		}
		var vote = document.createElement("input");
		vote.setAttribute("type", "submit");
		vote.setAttribute("value", "Vote");
		this.item.appendChild(vote);

		this.item.onsubmit = (event) => {
			event.preventDefault();
			if (this.handler) {
				this.handler();
			}
			return false;
		};
	}
	
	this.addSubmitEventHandler = function(handler) {
		this.handler = handler;
	}
	
	this.addToDocument = function() {
		document.body.appendChild(this.item);
	}
}
