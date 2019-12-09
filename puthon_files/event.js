/// Event delegation in JS

//trigger a call back function each time an evet is created 

var state=false;
var time=0;
function call_back(){
	console.log("My Call back Fn")
}

function trigger(state) {
	
	while (state){
		if (!state || time===10){
			time=0
			return 
		}
		else {
			call_back()
			time++
		}
	}
// body...
}

trigger(true)



