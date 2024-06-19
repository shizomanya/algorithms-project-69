import pytest
from search_engine.search_engine import search


def test_search_basic():
    doc1 = {'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"}
    doc2 = {'id': 'doc2', 'text': "Don't shoot shoot shoot that thing at me."}
    doc3 = {'id': 'doc3', 'text': "I'm your shooter."}
    docs = [doc1, doc2, doc3]

    assert search(docs, 'shoot at me') == ['doc2', 'doc1']
    assert search(docs, 'pint!') == ['doc1']
    assert search([], 'shoot') == []


def test_search_no_results():
    doc1 = {'id': 'doc1', 'text': "Hello world"}
    docs = [doc1]

    assert search(docs, 'python') == []


def test_search_with_punctuation():
    doc1 = {'id': 'doc1', 'text': "Hello, world!"}
    docs = [doc1]

    assert search(docs, 'world') == ['doc1']
    assert search(docs, 'world!') == ['doc1']


def test_search_relevancy():
    doc1 = {'id': 'doc1', 'text': "Shoot the ball"}
    doc2 = {'id': 'doc2', 'text': "Don't shoot shoot shoot"}
    docs = [doc1, doc2]

    assert search(docs, 'shoot') == ['doc2', 'doc1']


if __name__ == '__main__':
    pytest.main()
