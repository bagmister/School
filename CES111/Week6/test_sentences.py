from sentences import get_determiner, get_noun, get_verb, get_conjunction, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners
    plural_determiners = ["some", "many", "the"]
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    quantity = 1
    word = get_noun(quantity)
    assert word is not None
    quantity = 2
    word = get_noun(quantity)
    assert word is not None

def test_get_verb():
    quantity = 1 
    tense = "past"
    word = get_verb(quantity, tense)
    assert word in word
    quantity = 2 
    tense = "present"
    word = get_verb(quantity, tense)
    assert word in word
    quantity = 1 
    tense = "future"
    word = get_verb(quantity, tense)
    assert word is not None

def test_get_conjunction():
    word = get_conjunction()
    assert word is not None

def test_get_preposition():
    word = get_preposition()
    assert word is not None

def test_get_prepositional_phrase():
    past_phrase = get_prepositional_phrase(quantity=1, first_sentance=True, tense="past")
    present_phrase = get_prepositional_phrase(quantity=2, first_sentance=False, tense="present")
    future_phrase = get_prepositional_phrase(quantity=1, first_sentance=True, tense="future")
    print(past_phrase)
    print(present_phrase)
    print(future_phrase)
pytest.main(["-v", "--tb=line", "-rN", __file__])
