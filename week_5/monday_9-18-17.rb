sentences = ["hello", "old friend", "today", "mac and cheese"]
new_sentences_array = []

new_array = sentences.map { |e| e.include?(" ") ? e.capitalize : e  }

p new_array
