def sumOfArrays(array1, array2)
  new_array = []
  array1.each do |num|
    array2.each do |nums|
      new_array << num+nums
    end
  end
  new_array
end

array1 = [1, 5, 10]
array2 = [100, 500, 1000]

p sumOfArrays(array1, array2)
