var array = [["a", "b", "z"], ["c", "d"], ["e", "f"], ["g", "h", "i", "j"]];
var new_array = [];

for (i = 0; i < array.length; i++) {
  for (j = 0; j < array[i].length; j++) {
    new_array.push(array[i][j])
  }
}

console.log(new_array)
