people = [
  {"name" => "Saron", "age" => 34},
  {"name" => "Majora", "age" => 28},
  {"name" => "Danilo", "age" => 45}
]
p people.sort{ |v| v["age"] }
