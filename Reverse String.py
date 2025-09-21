input_str = input("ENTER A STRING: ")
words = input_str.split(' ')
for word in words:
  reversed_words = word[::-1]
  print(reversed_words, end = ' ')
