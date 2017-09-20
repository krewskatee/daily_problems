def find_the_most_letter_a(array)
  max = 0
  highest_word = ""
  array.each do |e|
    highest = 0
    arr = e.split("")
    arr.each do |l|
      if l == "a"
        highest += 1
      end
      if highest > max
        max = highest
        highest_word = e
      end
    end
  end
  highest_word
end

p find_the_most_letter_a(["alphabet", "aardvark", "anarchy"])  #=> "aardvark"
