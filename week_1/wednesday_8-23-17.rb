def reverse_a_string(string)
  convert_string = string.to_s #if integer is put in
  split_string = convert_string.chars
  reverse_array = []
  for i in 0..split_string.size-1
    reverse_array << split_string.pop
  end
  return reverse_array.join
end

p reverse_a_string("pirate")
