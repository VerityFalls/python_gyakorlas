def feldolgozas(kerdes):
    print("feldolgozas alatt: " + kerdes)

    szamjegyek = dict()
    for betu in kerdes:
        print(betu)
        if betu in ("0" "1" "2" "3" "4" "5" "6" "7" "8" "9"):
            if betu in szamjegyek:
             szamjegyek[betu] += 1




   # return kerdes[::-1]

while True:
    kerdes = input("kerdes: ")
    if kerdes == "exit":
        print("bye")
        break
    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)

    print("Valasz: " + str(valasz))

print ("VEGE.")


