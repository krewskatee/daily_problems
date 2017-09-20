def is_prime?(num)
  (1..num).each do |current|
    if current > 1 && current < num && num % current == 0
      return false
    end
  end
  true
end

p is_prime?(10)  #=> false
p is_prime?(11)   #=> true
p is_prime?(12)   #=> false
