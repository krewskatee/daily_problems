def is_balanced?(array)
  is_balanced = true
  count = 0
  while is_balanced != false
    if array[count] == "["
      if array[(-count)-1] != "]"
        is_balanced = false
      end
    elsif array[count] == "{"
      if array[(-count)-1] != "}"
        is_balanced = false
      end
    elsif array[count] == "("
      if array[(-count)-1] != ")"
        is_balanced = false
      end
    else
      is_balanced = true
      break
    end
    count += 1
  end
  is_balanced
end



p is_balanced?("{[()]}") #=> true
p is_balanced?("{[([)]]}") #=> false
