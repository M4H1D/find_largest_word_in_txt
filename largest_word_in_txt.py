# Longest word

# Reading sentence from user

sentence = input()

# Finding longest word
longest = max(sentence.split(), key=len)

# Displaying longest word
print(longest)