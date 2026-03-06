def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
string = input("Enter a string: ")
result = count_vowels(string)
print("Number of vowels:", result)