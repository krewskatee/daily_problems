var fruits = [
  {name: "apple", color: "red"},
  {name: "banana", color: "yellow"},
  {name: "grape", color: "purple"}
];

fruit = {}
fruits.reduce(function(prev, elem) {
  fruit[elem.name] = elem.color;
}, 0);

console.log(fruit);
