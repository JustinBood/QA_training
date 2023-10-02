word = input("Enter a word: ")
word = word.lower
list1 = ["a","e","i","o","u"," "]
count = 0
for x in word:
    if x not in list1:
        count +=1

print(f"There are {count} vowels in {word}")