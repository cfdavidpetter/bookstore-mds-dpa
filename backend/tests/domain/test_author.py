from src.domain.author import Author


def test_should_create_author():
  author: Author = Author(id=1, title="Murilo F. Silva", biography="Murilo is a writer books")

  assert author.id == 1
  assert author.title == "Murilo F. Silva"
  assert author.slug == "murilo-f-silva"

  author: Author = Author(title="Murilo", biography="Murilo is a writer books", slug="mrl")

  assert author.id is None
  assert author.slug == "mrl"