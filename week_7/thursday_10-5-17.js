array = ["alphabet", "aardvark", "anarchy"];
var find_the_most_letter_a = function(array) {
  max = "";
  maxCount = 0;
  for(var i = 0; i < array.length; i++){
    count = 0;
    for(var j = 0; j < array[i].length; j++) {
      if(array[i][j] == "a") {
        count += 1;
      }
    }
    if(count > maxCount) {
      maxCount = count
      max = array[i];
    }
  }
  return max
}

console.log(find_the_most_letter_a(["alphabet", "aardvark", "anarchy"]));  // "aardvark"
