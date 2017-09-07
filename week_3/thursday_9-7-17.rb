def sum_of_range(arr)
  arr[0], arr[1] = arr[1], arr[0] if arr[1] < arr[0]
  sum = 0
  (arr[0]..arr[1]).each do |n|
    sum += n
  end
  sum
end

p sum_of_range([1, 4])
p sum_of_range([4, 1])
