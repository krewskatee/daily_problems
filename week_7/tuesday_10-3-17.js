function find_longest_word(string){
  var strSplit = string.split(' ');
  var maxCount = 0;
  var longestWord = "";
  for(var i = 0; i < strSplit.length; i++){
    if(strSplit[i].length > maxCount){
      maxCount = strSplit[i].length;
      longestWord = strSplit[i]
    }
  }
  return longestWord
}

console.log(find_longest_word("What is the longest word in this phrase?")); // "longest"
