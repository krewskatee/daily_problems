var newArray = [];
var items = [
  {id: 1, body: 'foo'},
  {id: 2, body: 'bar'},
  {id: 3, body: 'foobar'}
];

newArray = items.map(( (n) => {return n['id']}));

console.log(newArray);
