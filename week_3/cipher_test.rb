def decoded_cipher(coded_message)
  input = coded_message.downcase.split("") # Check out this method in IRB to see how it works! Also refer to the Ruby docs.
  decoded_sentence = []
  input.each do |x|
    if (x == "@" || x == "#" || x == "$" || x == "%"|| x == "^" || x == "&"|| x =="*")
      decoded_sentence << " "
    elsif x.ord >= 97 && !(x.ord > 122)
      decoded_sentence << (x.ord - 4).chr
    else
      decoded_sentence << x
    end
  end
  return decoded_sentence # What is this returning?
end


p decoded_cipher("asa,&csy^qywx#lezi^er@eajyp^psx$sj%jvii#xmqi&sr#csyv*lerhw!")


def play_pass(str, n)
  letters = ('a'..'z').to_a
  str.chars.map {|x| letters.include?(x.downcase) ? letters[letters.find_index(x.down_case) + n - letters.size] : x}
end
