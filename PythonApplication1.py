#21

print("Sisesta kolm erineva pikkusega nime: ")
S=str(input("Esimene nimi: "))
M=str(input("Teine nimi: "))
G=str(input("Kolmas nimi: "))
words = [S, M, G]
print("Suurem s�na: ")
print(max(words, key=len))
print("V�iksem s�na: ")
print(min(words, key=len))

#0

text = 'Hello world'
i = 0
while i < len(text):
    print(text[i])
    i += 1
print("---------------------------------")
for i in text:
    print(i) 
