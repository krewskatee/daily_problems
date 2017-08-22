items = [
  {id: 1, body: 'foo'},
  {id: 2, body: 'bar'},
  {id: 3, body: 'foobar'}
]
items_array = []
items_array += items.map{ |k| k[:id]}
p items_array
