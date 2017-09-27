def highest_prime_number_under(num)
  max_array = []
  (1..num).each do |number|
    is_prime = true
    (1..number).each do |current|
      if current > 1 && current < number && number % current == 0
        is_prime = false
        break
      end
    end
    if is_prime == true
      max_array << number
    end
  end
  if max_array[max_array.length-1] == num
   return max_array[max_array.length-2]
  else
    return max_array[max_array.length-1]
  end
end

p highest_prime_number_under(10)  #=> 7
p highest_prime_number_under(11)  #=> 7
p highest_prime_number_under(12)  #=> 11
