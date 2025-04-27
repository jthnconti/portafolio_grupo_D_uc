class Post:
    def __init__(self, title, content, author, tags=None):
        if len(title.strip()) < 5:
            raise ValueError("Título muy corto.")
        self.title = title
        self.content = content
        self.author = author
        self.tags = tags or []

    def resumen(self):
        return self.content[:100] + "..."

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "tags": self.tags,
            "resumen": self.resumen()
        }