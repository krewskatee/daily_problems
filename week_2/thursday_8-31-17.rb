def split_array(array, split_num)
  array.each_slice(split_num).to_a
end

array = [0, 1, 2, 3, 4, 5]

p split_array([0, 1, 2, 3, 4, 5], 3)  #=> [[0, 1, 2], [3, 4, 5]]
