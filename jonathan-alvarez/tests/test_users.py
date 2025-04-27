from models.user import User

def test_usuario_valido():
    user = User("jalvarez", "jalvarezc@tecsup.edu.pe")
    assert user.to_dict()["email"] == "jalvarezc@tecsup.edu.pe"

def test_email_invalido():
    try:
        User("usuario", "correo_invalido.com")
        assert False
    except ValueError:
        assert True