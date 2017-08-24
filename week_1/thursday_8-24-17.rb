def find_longest_word(string)
  string.split(/[^\w]+/).max_by(&:length) #regular expression to split spaces and all non-word characters
end

p find_longest_word("Are you lame or supercalifragilisticexpialidocious?")
