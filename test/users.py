import json

# Ruta del archivo JSON
JSON_PATH = "data/users.json"  # cambia la ruta si es necesario

def cargar_usuarios():
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Archivo JSON no encontrado.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el JSON.")
        return []

def validar_usuario(usuario, clave):
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u["usuario"] == usuario and u["clave"] == clave:
            return True
    return False

if __name__ == "__main__":
    print("=== Prueba de Login ===")
    user = input("Usuario: ")
    pwd = input("Contraseña: ")

    if validar_usuario(user, pwd):
        print("✅ Inicio de sesión exitoso.")
    else:
        print("❌ Usuario o contraseña incorrectos.")
