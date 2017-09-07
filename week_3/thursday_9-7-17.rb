def sum_of_range(array)
  array[0], array[1] = array[1], array[0] if array[1] < array[0]
  sum = 0
  (array[0]..array[1]).each do |n|
    sum += n
  end
  sum
end

p sum_of_range([1, 4])
p sum_of_range([4, 1])
