restart = "1"  # první spuštení programu
while restart == "1":
    full_price = 45
    age = input("Zadej svůj věk: \n")
    employee = input("Zadej ano nebo ne, zda jsi zaměstnanec tramvajové služby \n")

    if not age.isnumeric():
        age = input("Zadej svůj věk jako číslo!! \n")

    elif employee != "ano" and employee != "ne":
        employee = input("POZOR! musíš zadat ano nebo ne malými písmeny! \n")

    else:
        age = int(age)
        if age <= 12:
            print("Díky svému věku, nemusíš kupovat jízdenku, máš ji ZDARMA!")
        elif age < 18:
            price = full_price / 2
            print("Cena tvé jízdenky je: ", price, "Kč")
        elif age >= 65:
            price = full_price * 0.70
            print("Cena vaší jízdenky je:", round(price, 2))
        elif employee == "ano" and age >= 55:
            print("Děkujeme vám, že jste naším zaměstnancem, a proto máte jízdenku ZDARMA!")
        elif employee == "ano" and age < 55:
            price = full_price * 0.2
            print("Cena vaší jízdenky je: ", round(price, 2), "Kč")
        else:
            print("Cena vaší jízdenky je: ", full_price, "Kč")
    restart = input("Chceš program spustit znovu? Zadej 1 pro ano, cokoliv jiného pro ukončení: ")

print("Program ukončen")
