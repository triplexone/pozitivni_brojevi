print("Unesite dva broja između 1 i 9: ")

prvi_broj = int(input("\t- 1. broj: "))
while prvi_broj < 1 or prvi_broj > 9:
    prvi_broj = int(input("Pogršan unos. Unesi 1. broj: "))

drugi_broj = int(input("\t- 2. broj: "))
while drugi_broj < 1 or drugi_broj > 10:
    drugi_broj = int(input("Pogršan unos. Unesi 2. broj: "))

parni = []

prvi = int(str(prvi_broj) + str(drugi_broj))
parni.append(prvi)

drugi = int(str(drugi_broj) + str(prvi_broj))
parni.append(drugi)

brojevi = [x for x in parni if x % 2 == 0]

if brojevi == []:
    brojevi.append("nema parnih brojeva")

print("Parni brojevi stvoreni od brojeva " + str(prvi_broj) + " i " + str(drugi_broj) + " su: " + (" i ".join(str(x) for x in brojevi)))