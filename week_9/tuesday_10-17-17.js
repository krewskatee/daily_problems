people = [
  {name: "Saron", age: 34},
  {name: "Majora", age: 28},
  {name: "Danilo", age: 45}
]

console.log(people.sort(function(a, b) {
    return b.age - a.age;
}));
