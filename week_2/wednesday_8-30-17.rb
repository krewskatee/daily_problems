def palindrome?(string)
  if string == string.reverse
    true
  else
    false
  end
end

p palindrome?("racecar")
p palindrome?("wazzzzup")
