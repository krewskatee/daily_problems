fruits = [
  {"name" => "apple", "color" => "red"},
  {"name" => "banana", "color" => "yellow"},
  {"name" => "grape", "color" => "purple"}
]
fruits_hash = {}

#fruits_hash = fruits.map{ |i| i.values }.to_h - "long version"
fruits_hash = fruits.map(&:values).to_h
p fruits_hash
