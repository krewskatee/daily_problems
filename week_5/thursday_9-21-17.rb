def find_the_most_letter_a(array)
  max_a_count = 0
  letter_a_count_word = ""
  array.each do |word|
    letter_a_count = 0
    arr = word.split("")
    arr.each do |letter|
      if letter == "a"
        letter_a_count += 1
      end
      if letter_a_count > max_a_count
        max_a_count = letter_a_count
        letter_a_count_word = word
      end
    end
  end
  letter_a_count_word
end

p find_the_most_letter_a(["alphabet", "aardvark", "anarchy"])  #=> "aardvark"
