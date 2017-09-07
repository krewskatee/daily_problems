def sum_of_range(starting, ending)
  starting, ending = ending, starting if ending < starting
  sum = 0
  (starting..ending).each do |n|
    sum += n
  end
  sum
end

p sum_of_range(1, 4)
