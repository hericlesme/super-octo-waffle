
let class_names = ["abelha", "livro", "cacto", "cisne", "submarino", "relógio", "tigre", "torradeira", "cueca", "guarda-chuva"];

(() => {
	let canvas = document.querySelector( "#canvas" );
	let context = canvas.getContext( "2d" );
	canvas.width = 280;
	canvas.height = 280;

	let Mouse = { x: 0, y: 0 };
	let lastMouse = { x: 0, y: 0 };
	context.fillStyle="white";
	context.fillRect(0,0,canvas.width,canvas.height);
	context.color = "black";
	context.lineWidth = 15;
    context.lineJoin = context.lineCap = 'round';


	const debug = () => {
		let clearButton = $( "#clearButton" );
		
		clearButton.on( "click", () => {
				context.clearRect( 0, 0, 280, 280 );
				context.fillStyle="white";
				context.fillRect(0,0,canvas.width,canvas.height);
		});


		$( "#colors" ).change(() => {
			let color = $( "#colors" ).val();
			context.color = color;
		});
		
		
		$( "#lineWidth" ).change(() => {
			context.lineWidth = $( this ).val();
		});
	}

	debug();

	canvas.addEventListener( "mousemove", function( e )
	{
		lastMouse.x = Mouse.x;
		lastMouse.y = Mouse.y;

		Mouse.x = e.pageX - this.offsetLeft;
		Mouse.y = e.pageY - this.offsetTop;

	}, false );

	canvas.addEventListener( "mousedown", function( e )
	{
		canvas.addEventListener( "mousemove", onPaint, false );

	}, false );

	canvas.addEventListener( "mouseup", function()
	{
		canvas.removeEventListener( "mousemove", onPaint, false );

	}, false );

	let onPaint = function() {	
		context.lineWidth = context.lineWidth;
		context.lineJoin = "round";
		context.lineCap = "round";
		context.strokeStyle = context.color;
	
		context.beginPath();
		context.moveTo( lastMouse.x, lastMouse.y );
		context.lineTo( Mouse.x, Mouse.y );
		context.closePath();
		context.stroke();
	};
})();


function hideCollage(){
	$('#slider').hide();
}

$(function(){
	hideCollage();
});

var mousePress = false;

canvas.onmousedown = function (e) {
	mousePress = true;
	getPred();
}

canvas.onmouseup = function (e) {
	mousePress = false;
	getPred();
}

function getPred() {
	var label = document.getElementById('label');
	var $SCRIPT_ROOT = "http://localhost:5000";
	var canvasObj = document.getElementById("canvas");
	var img = canvasObj.toDataURL();
	$.ajax({
		type: "POST",
		dataType : 'json',
		contentType: 'application/json',
		url: $SCRIPT_ROOT + "/predict",
		data: JSON.stringify(img),
		success: function (data) {
			label.innerText = class_names[data.index]
		}
	});
}


var counter = 0;

function timer() {
	if (counter < 4) {
		counter = counter + 1;
	}
	else {
		counter = 0
	}
}

setInterval(timer, 100);

document.getElementById("canvas").onmousemove = function (e) {
	if (!mousePress) return;

	while (mousePress) {
		if (counter == 3) {
			getPred();
		}


		return false;
	}

};

	
let categories = document.getElementById('categories');

class_names.map(e => {
	let node = document.createElement("LI");
	let textnode = document.createTextNode(e);
	node.appendChild(textnode); 
	categories.appendChild(node)
});