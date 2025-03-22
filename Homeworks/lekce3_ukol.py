books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]
# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
books.append({"name": "Železný plamen","price": 715, "author": "Rebecca Yarros", "publication_year": 2025})
books.append({"name": "Psychologie peněz","price": 320, "author": "Morgan Housel", "publication_year": 2022})
print(books)
# 2. Změň cenu jedné libovolné knihy. Vypiš list.
books[1]["price"] = 650
# 3. Odstraň nějakou knihu. Vypiš list.
books.pop(2)
# 4. Vypiš celkový počet knih v listu.
print("V listu mám " + str(len(books)) + " prvky")

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
# Tento kód nepočítá s ošetřením vstupu uživatele a při špatném zadání program spadne
print("Přidej si svou knihu!")

new_book = {
    "name": input("Zadej název knihy: "),
    "price": int(input("Zadej cenu knihy: ")),
    "author": input("Zadej autora: "),
    "publication_year": int(input("Zadej rok vydání: "))
}
books.append(new_book)

print(books)
print("Počet knih ve slovníku: " + str(len(books)))