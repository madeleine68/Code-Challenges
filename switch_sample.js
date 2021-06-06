// Create a script that takes a string variable "hello world"
// and translate it to at least 3 different languages base on 
// a "language" variable.
// make an defualt language English if a match isn't found.
var language = "Spanish";
var script ="Hello World";
var message = "";

switch (language) {
   case "Arabic":
      message = "Salam";
      break;
   case "Spanish":
      message = "holla hoo";
      break;
   case "French":
      message = "Bonjoo";
      break;
   default:
      message = "Hello World";
} 

gs.info(script+ " in " + language+ " is "+ message)