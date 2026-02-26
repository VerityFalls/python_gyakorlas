print("hello")
# ez egy komment
x = 10
print(x)
x = 30
print(x)
y = 1.5456
print(y)
nev = "Valaki"
print(nev)

print([1, 2, 3, 4, 5])
print("hello" + " world")
print("hello" + str(12))
print(f"hello {12} {nev}")
print(range(5))
szotar = {"név": "Anna", "kor": 25}
print(szotar)
logikai = False
print(logikai)
ertek = None
print(ertek)

nev = "Jani"
Nev = "Jozsi"
print(nev + Nev + " baratok")

print(1.5 + 2 * 3 - 4 / 2)

x = 5
y = 3
print("x mod y: " + str(x % y))

print("Három az értéke y-nak?" + str(y) == 3)

if y > 5:
    print("y nagyobb mint 5")
    if y % 2 == 0:
        print("y páros és nagyobb, mint 5")
else:
    print("y kisebb vagy egyenlő, mint 5")

for i in range(5):
    print(i)

for nev in ["Anna", "Jani", "Józsi"]:
    print(nev)

while y < 10:
    print("y még kisebb, mint 10")
    y += 1

def fuggveny():
    print("Ez egy függvény")

    return "Alma"

print("kovetkezo sor")

fuggveny()

print("A fuggveny visszaadott erteke: " + fuggveny())