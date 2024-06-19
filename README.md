### Hexlet tests and linter status:
[![Actions Status](https://github.com/shizomanya/algorithms-project-69/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shizomanya/algorithms-project-69/actions)

# Search Engine

This project implements a simple search engine that can perform both exact and fuzzy searches on a collection of documents. The search engine supports text preprocessing to handle punctuation and case insensitivity and uses the TF-IDF metric to rank search results by relevance.

## Features

- **Exact Search**: Search for documents containing a specific term.
- **Fuzzy Search**: Search for documents containing any of the terms in the query.
- **Text Preprocessing**: Convert text to lowercase and remove punctuation to ensure accurate search results.
- **Relevance Ranking**: Use TF-IDF (Term Frequency-Inverse Document Frequency) to rank documents by relevance.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` package manager

### Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/algorithms-project-69.git
cd algorithms-project-69
```
2. (Optional) Create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:
```sh
pip install -r requirements.txt
```
### Usage
You can use the search engine by importing the search function and passing a list of documents and a query string. Each document should be a dictionary with id and text keys.

```python
from search_engine import search

# Example documents
doc1 = {'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"}
doc2 = {'id': 'doc2', 'text': "Don't shoot shoot shoot that thing at me."}
doc3 = {'id': 'doc3', 'text': "I'm your shooter."}
docs = [doc1, doc2, doc3]

# Perform search
results = search(docs, 'shoot at me')
print(results)  # Output: ['doc2', 'doc1']
```
## Running Tests
To run the tests, use the following command:

```
pytest
```
The tests are located in the tests directory and include various cases to verify the functionality of the search engine.

## Project Structure
- search_engine.py: Main implementation of the search engine.
- tests/test_search_engine.py: Unit tests for the search engine.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature-branch)
5. Create a new Pull Request

## Acknowledgments
- [TF-IDF](https://en.wikipedia.org/wiki/Tf–idf) - for the relevance ranking metric
- [Python](https://www.python.org) - the programming language used
- pytest - testing framework
