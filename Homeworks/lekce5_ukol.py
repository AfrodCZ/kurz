numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa",
                "3-sOdSxhcds", "3-Kjjjhte"]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.
for n in numbers:
    if n < 0:
        continue
    print(n)
# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči
na = 0
while na < len(names):
    if names[na] == "Alice":
        break
    print(names[na])
    na += 1

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0
new_random_codes = []
for rc in random_codes:
    if "0" in rc:
        new_random_codes.append(rc)
print(new_random_codes)

# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'
new_random_codes1 = []
for code in random_codes:
    part = code.split("-")[1]
    for i in range(len(part) - 2):
        if part[i] == part[i + 1] == part[i + 2]:
            print("Daný řetězec, obsahuje tři znaky: ", code)
            break
