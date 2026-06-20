a=input()
b=input()
if len(a)!=len(b):
    print("Not Anagram")
else:
    if sorted(a)==sorted(b):
        print("Anagram")
    else:
        print("Not Anagram")