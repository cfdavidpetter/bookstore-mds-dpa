from src.domain.subject import Subject


def test_should_create_subject():
  subject: Subject = Subject(id=1, title="Romance Books")

  assert subject.id == 1
  assert subject.title == "Romance Books"
  assert subject.slug == "romance-books"

  subject: Subject = Subject(id=1, title="Romance Books", slug="romance")

  assert subject.slug == "romance"