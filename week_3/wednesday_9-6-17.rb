input = "burly"

def mutation?(string1, string2)
  string_arr = string2.split("")
  string_arr.each do |x|
    unless string1.include?(x)
      return false
    end
  end
  return true
end

p mutation?('burly', "ruby")
p mutation?('burly', "python")
