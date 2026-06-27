import pytest


def is_anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    return sorted(word1)==sorted(word2)


@pytest.mark.parametrize("phrase1, phrase2", [("listen", "silent"),("Astronomer", "Moon starer"),("A gentleman", "Elegant man"),         
    ("The Morse Code", "Here come dots!")])

def test_is_anagram(phrase1, phrase2):
    assert is_anagram(phrase1, phrase2)


@pytest.mark.parametrize("phrase1, phrase2", [("abc", "def"),("hello", "helloo"),("rat", "car")])
def test_is_anagram_not_anagram(phrase1, phrase2):
    assert not is_anagram(phrase1, phrase2)