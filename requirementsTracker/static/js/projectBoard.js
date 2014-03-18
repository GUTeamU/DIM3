function show_all() {
	$("#whiteboard").css( "border-color", "#FFFFFF");

	$("#must").show();
	$("#should").show();
	$("#could").show();
	$("#would").show();
	
};

function mustHave() {
	$("#whiteboard").css( "border-color", "#FF0000")

	$("#should").hide()
	$("#could").hide()
	$("#would").hide()
	$("#must").show()

};

function shouldHave() {
	$("#whiteboard").css( "border-color", "#FF8330")
	
	$("#must").hide()
	$("#could").hide()
	$("#would").hide()
	$("#should").show()


};

function couldHave() {
	$("#whiteboard").css( "border-color", "#19A319")	

	$("#must").hide()
	$("#should").hide()
	$("#would").hide()
	$("#could").show()

};

function wouldLike() {
	$("#whiteboard").css( "border-color", "#1693BC")	

	$("#must").hide()
	$("#should").hide()
	$("#could").hide()
	$("#would").show()

};

