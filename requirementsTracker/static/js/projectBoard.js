function mustHave() {
	var elem = document.getElementById("whiteboard");
	elem.style.borderColor = "#FF0000";
	$("#should").hide()
	$("#could").hide()
	$("#would").hide()
	$("#must").show()
}

function shouldHave() {
	var elem = document.getElementById("whiteboard");
	elem.style.borderColor = "#FF8330";
	$("#must").hide()
	$("#could").hide()
	$("#would").hide()
	$("#should").show()
}

function couldHave() {
	var elem = document.getElementById("whiteboard");
	elem.style.borderColor = "#19A319";
	$("#must").hide()
	$("#should").hide()
	$("#would").hide()
	$("#could").show()
}

function wouldLike() {
	var elem = document.getElementById("whiteboard");
	elem.style.borderColor = "#1693BC";
	$("#must").hide()
	$("#should").hide()
	$("#could").hide()
	$("#would").show()
}
