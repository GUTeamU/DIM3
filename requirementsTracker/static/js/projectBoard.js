function mustHave() {
	document.getElementById("whiteboard").style.borderColor = "#FF0000";
	document.getElementById("boxes").style.backgroundColor = "#FF0000";

	$("#should").hide()
	$("#could").hide()
	$("#would").hide()
	$("#must").show()

};

function shouldHave() {
	document.getElementById("whiteboard").style.borderColor = "#FF8330";
	document.getElementById("boxes").style.backgroundColor = "#FF8330";
	
	$("#must").hide()
	$("#could").hide()
	$("#would").hide()
	$("#should").show()


};

function couldHave() {
	document.getElementById("whiteboard").style.borderColor = "#19A319";
	document.getElementById("boxes").style.backgroundColor = "#19A319";

	$("#must").hide()
	$("#should").hide()
	$("#would").hide()
	$("#could").show()

};

function wouldLike() {
	document.getElementById("whiteboard").style.borderColor = "#1693BC";
	document.getElementById("boxes").style.backgroundColor = "#1693BC";

	$("#must").hide()
	$("#should").hide()
	$("#could").hide()
	$("#would").show()

};

