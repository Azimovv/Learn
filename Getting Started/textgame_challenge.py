word = input("This is a palindrome checker, enter a word: ")
backwards = list()

for letter in range(len(word)-1, 0, -1):
    backwards += word[letter]
backwards+=word[0]

if word == "".join(backwards):
    print("The word {} is indeed a palindrome".format(word))
else:
    print("The word {} is not a palindrome".format(word))

