movies = [
  {id: 1, title: "Die Hard", rating: 4.0},
  {id: 2, title: "Bad Boys", rating: 5.0},
  {id: 3, title: "The Chamber", rating: 3.0},
  {id: 4, title: "Fracture", rating: 2.0}
]

filtered_movies = []

filtered_movies = movies.select{ |movie| movie[:title].include?("b") || movie[:title].include?("B") }.map { |movie| movie[:id] }

p filtered_movies
