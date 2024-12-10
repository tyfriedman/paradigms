// get recommendation
function getRecommendation(title, rating, movieImg) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student13.cse.nd.edu:51020/recommendations/1", true);
	xhr.onload = function(e) {
		var movie = JSON.parse(xhr.responseText);
		getRating(title, rating, movieImg, movie);
		curr_movie_id = movie.movie_id;
	}
	xhr.send(null);
}

// get rating
function getRating(title, rating, movieImg, movie) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student13.cse.nd.edu:51020/ratings/" + movie.movie_id, true);
	xhr.onload = function(e) {
		var movie_rating = JSON.parse(xhr.responseText);
		updatePage(title, rating, movieImg, movie.movie_id, movie_rating.rating);
	}
	xhr.send(null);
}

// update page
function updatePage(title, rating, movieImg, movie_id, movie_rating) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student13.cse.nd.edu:51020/movies/" + movie_id, true);
	xhr.onload = function(e) {
		var movie = JSON.parse(xhr.responseText);
		title.setText(movie.title);
		movieImg.setAttribute("src", "http://www3.nd.edu/~cmc/teaching/cse30332/images" + movie.img);
		rating.setText(movie_rating);
	}
	xhr.send(null);
}

Label.prototype = new Item();
Button.prototype = new Item();

// div
var upperDiv = document.createElement("div");
document.body.appendChild(upperDiv);

// title
var title = new Label();
title.createLabel("Title", "titleLabel");
title.id = "titleLabel";
upperDiv.appendChild(title.item);

// div
var middleDiv = document.createElement("div");
middleDiv.id = "middleDiv";
document.body.appendChild(middleDiv);

// up vote
var upVote = new Button();
upVote.createButton("UP", "upVoteButton");
upVote.id = "button";
middleDiv.appendChild(upVote.item);

// image
var movieImg = document.createElement("img");
movieImg.setAttribute("alt", "movie image");
movieImg.classList.add("movieImg");
middleDiv.appendChild(movieImg);

// down vote
var downVote = new Button();
downVote.createButton("DOWN", "downVoteButton");
downVote.id = "button";
middleDiv.appendChild(downVote.item);

// div
var lowerDiv = document.createElement("div");
document.body.appendChild(lowerDiv);

// rating
var rating = new Label();
rating.createLabel("Rating", "ratingLabel");
rating.id = "ratingLabel";
lowerDiv.appendChild(rating.item);

// add event handlers
upVote.addClickEventHandler(vote, title, rating, movieImg, "5");
downVote.addClickEventHandler(vote, title, rating, movieImg, "1");

// on load function
var curr_movie_id;
window.onload = function() {
	getRecommendation(title, rating, movieImg);
}

// on vote function
function vote(title, rating, movieImg, user_vote) {
	var xhr = new XMLHttpRequest();
	xhr.open("PUT", "http://student13.cse.nd.edu:51020/recommendations/1", true);
	xhr.onload = function(e) {
		getRecommendation(title, rating, movieImg);
	}
	xhr.send(JSON.stringify({ "movie_id": curr_movie_id, "rating": user_vote }));
}
