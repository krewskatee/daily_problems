def mutation?(string_1, string_2)
  string_arr = string_2.split("")
  string_arr.each do |x|
    return false unless string_1.include?(x)
  end
  true
end

p mutation?('burly', "ruby")
p mutation?('burly', "python")
