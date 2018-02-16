books = {"Harry Potter":150,"Da Vi Code":60,"Algorithm":80,"Let Us C":60}
print(books)

var1, var2 = input("Enter both range (with a space in between):").split(' ')

minrange = int(var1)
maxrange = int(var2)

print("You can purchase following books:")

for key, value in books.items():
    if (value >= minrange and value<=maxrange):
        print(key)