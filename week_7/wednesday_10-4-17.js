function mutation(first, second) {
  var testArray = second.split("");
  var contains = false;
  for(var i = 0; i < testArray.length; i++){
    if (!first.includes(testArray[i])) {
      return false;
    }
  }
  return true;
}

console.log(mutation("burly", "ruby"));    // true
console.log(mutation("burly", "python")); // false
