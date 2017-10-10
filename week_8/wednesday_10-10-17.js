var numbers = [1, 2, 4, 2];

var even = function (num) {
return num % 2 === 0;
};

var evenNumbers = numbers.filter(even);
console.log(evenNumbers);
