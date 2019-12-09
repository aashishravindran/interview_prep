function makesound(){
	console.log(this.sound)
}
makesound()

let cat= {
	sound:"Mewoooo!!",
	makesound:makesound

}

let dog={
	sound:"Wooof!!!",
	makesound:makesound // Assignemnet like this should never be done since it return undefinged or a wrong result 
	// for example dog.makesound => "Woof!" because context of this is set only when the funcntion is called :) 
	/// One of the quirks of javascript :)

}
dog.makesound() // Woof => scope of this is referes to the sound propertu of the dog when this function is called 
cat.makesound() // Mewooo! scope of this is referes to the sound propertu of the cat when this function is called



let boundsound=dog.makesound // At the time this function is called, this keyword refers to the global scope,
boundsound()                   /// This is because, javascript assigns context only when a function call is made, unless explicitly specified using call,apply,bind

/// we can also use call, apply to explicity say what the keyword this means. It is similart to assigning context as shown in the example below 

/// to assign context of the "this" keyword we can either use call,apply or bind
//call and apply assign context and execute the function immediately
// bind assigns context and reuturns a fucntion definition, which can be used later
/// exampe 

let callex=makesound //executing callex() will retunr undefined, since context/scope of this is the window object at the time of execution
//callex()
callex.call(cat) /// retuns mewoo!! becasue we have explicitly told the to assign this to the cat object which has a property called sound
callex.apply(dog)

let callexbound=callex.bind(cat) // this return as fucntion definiton and explicitly binds the keyword "this" to the cat object!! calling callexbound returns "Mewooo!"
callexbound() /// bind is extremely useful whenever you want a fucntion to exceute after a certain period and s
