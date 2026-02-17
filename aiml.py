sentence=input("Enter the sentence: ")
abrev=["AI","ML"]
result=" "
words=sentence.split()
for w in words:
   if w.upper() in abrev:
    result.add(w.upper())
   else:
    w.capitalize()
    result.add(w.capitalize()) 

print(result)