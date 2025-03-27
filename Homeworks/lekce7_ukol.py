def is_adult(age):
    return age >= 18


def is_name_valid(name):
        return len(name) >= 4


def create_user(name, age):
    if not is_name_valid(name):
        return {
            "success": False,
            "error": "Jméno musí mít nejméně 4 znaky."
        }
    if not is_adult(age):
        return {
            "success": False,
            "error": "Uživatel musí být dosplělý"
        }
    return {
        "success": True,
        "user": {
            "name": name,
            "age": age
        }
    }

def print_user_info(result):
    if result["success"]:
        user = result["user"]
        print(f"\nUživatel byl úspěšně vytvořen:")
        print(f"Jméno: {user['name']}, Věk: {user['age']}")
    else:
        print(f"\nChyba: {result["error"]}")

users = [
    create_user("Zdeněk", 35),
    create_user("Štěpán", 4),
    create_user("Alt", 19),
    create_user("Honza", 33)
]
for u in users:
    print_user_info(u)