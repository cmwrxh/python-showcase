from pyshowcase.text_tools import slugify, word_count


def test_slugify():
    assert slugify("Hello World") == "hello-world"


def test_word_count():
    assert word_count("Python is clean") == 3
