var meals = [["breakfast", "pancakes with maple syrup"], ["lunch", "BLT"], ["dinner", "salmon with lemon rice"]];
var dict = {}

for (i = 0; i < meals.length; i++) {
  dict[meals[i][0]] = meals[i][1] 
}

console.log(dict)
