from models.post import Post

def test_post_valido():
    post = Post("TDD en Python", "Ejemplo de test con ORM", "jalvarez")
    assert post.to_dict()["author"] == "jalvarez"

def test_titulo_corto_invalido():
    try:
        Post("Hi", "Contenido breve", "jalvarez")
        assert False
    except ValueError:
        assert True