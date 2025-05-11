from users import validar_usuario

def test_usuario_correcto():
    """Debe autenticar correctamente usuario existente."""
    assert validar_usuario("jonathan", "jon@web.com") == True

def test_usuario_incorrecto():
    """Debe fallar si la contraseña es incorrecta."""
    assert validar_usuario("jonathan", "clave_mal") == False

def test_usuario_no_existe():
    """Debe fallar si el usuario no existe."""
    assert validar_usuario("usuario_inexistente", "1234") == False
