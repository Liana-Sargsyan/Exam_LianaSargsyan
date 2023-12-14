word = input("Please inpute a word: ")
symbol = input("Please input a symbol: ")
if len(word) > 20:
    print("ERROR: max lenght is 20")
else:
    if symbol in word:
        print(word[word.index(symbol):])
    else:
        print("Inputted word does not contain such symbol")
