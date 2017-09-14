def find_missing_letter(string)
  split_string = string.split("")
  limit = split_string.length-1
  missing_letters_array = []
  (split_string[0]..split_string[limit]).each do |e|
    unless split_string.include?(e)
      missing_letters_array << e
    end
  end
  unless missing_letters_array.length == 0
    return missing_letters_array.join("")
  else
    return nil
  end
end

p find_missing_letter("opqrsuv")
p find_missing_letter("xyz")
p find_missing_letter("ace")
