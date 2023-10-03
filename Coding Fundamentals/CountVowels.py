word = input("Enter a word: ")
list1 = ["a","e","i","o","u"]
count = 0
for x in word:
    if x in list1:
        count +=1

print(f"There are {count} vowels in {word}")