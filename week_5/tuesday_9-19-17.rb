arr = [1, 23, 54, 63, -1, 8, 90, 5]

p arr.reduce {|min, curr| min < curr ? min : curr }
