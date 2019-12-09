

var st="catsdogsandshit"
console.log(st.split("dogs").join("cat"))

//Workinf with prototype
//used for inheritance
//Use case - consider a base class which has a couple of methods to do certain tasks
// every other class which inherits from this class would want ot access the properties of this base class
//How can this be accomplished, since javascript dosent have classes ?? 
//Example
//
function mult(){
	return this.a*this.b
}
/*var base_class={
	mult:mult
}*/
/// We have a method which is going to take two params and return the multiplcation of this
/// However notice that the mult fucntion does not take any arguments
// this means that calling this function would retun undefiens
mult() // undefined 

var  base_class={mult:mult}
// calling base class.mult will also return undefined but the scope of the this keyword changes form the global scope(window object )
// to the local socpe of the calss object
// let us now define sub classes c1 and c2 which 
var  mult1={
	a:3,
	b:5
}

Object.setPrototypeOf(mult1,base_class)
console.log(mult1.mult())










/// The new keyword 
function Person(saying) {
	this.saying=saying
}

Person.prototype.talk = function() {
	console.log("I say:",this.saying)
	// body...
};

var crockford = new Person("SDFFFFFF")
crockford.talk()






/// creating a custom new !! 
// New does four things 
/* 1) creates an object 
	2)sets the prototype of the object to the prortotype of the constructor in which it was called 
	3) assigns the arguments passed to the this keyword to the objetcs
	4) returns the object 


*/

function evilSpanNew(constructor){
	var obj={} // creating an object !!
	Object.setPrototypeOf(obj,constructor.prototype) // assigns the arguments passed to the constructor to the this variables 
	// isolate the cinstructor from the arguments 
	var argsArray=Array.prototype.slice.apply(arguments)
	constructor.apply(obj,argsArray.slice(1))
	return obj

}

var evilspawn=evilSpanNew(Person,"Fuck this")
evilspawn.talk()
