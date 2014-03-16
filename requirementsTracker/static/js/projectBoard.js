$(document).ready(mustHave);

function mustHave() {
	var elem = document.getElementById("whiteboard");
	elem.style.background = "#DB8484";
	$("#should").hide()
	$("#could").hide()
	$("#would").hide()
	$("#must").show()
}

function shouldHave() {
	var elem = document.getElementById("whiteboard");
	elem.style.background = "#EBC17A";
	$("#must").hide()
	$("#could").hide()
	$("#would").hide()
	$("#should").show()
}

function couldHave() {
	var elem = document.getElementById("whiteboard");
	elem.style.background = "#C0E099";
	$("#must").hide()
	$("#should").hide()
	$("#would").hide()
	$("#could").show()
}

function wouldLike() {
	var elem = document.getElementById("whiteboard");
	elem.style.background = "#AACFE3";
	$("#must").hide()
	$("#should").hide()
	$("#could").hide()
	$("#would").show()
}
