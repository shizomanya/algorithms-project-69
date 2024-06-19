import re
import math
from collections import defaultdict, Counter


def preprocess_text(text):
    # Преобразование текста в нижний регистр и удаление знаков препинания
    return re.findall(r'\w+', text.lower())


def build_inverted_index(docs):
    inverted_index = defaultdict(list)
    doc_term_counts = []
    for doc in docs:
        doc_id = doc['id']
        doc_text = doc['text']
        terms = preprocess_text(doc_text)
        term_count = Counter(terms)
        doc_term_counts.append((doc_id, term_count))
        for term in term_count:
            inverted_index[term].append(doc_id)
    return inverted_index, doc_term_counts


def compute_idf(inverted_index, total_docs):
    idf = {}
    # +1 для избегания деления на ноль
    for term, doc_list in inverted_index.items():
        idf[term] = math.log(total_docs / len(doc_list)) + 1
    return idf


def compute_tf_idf(doc_term_count, idf):
    tf_idf = {}
    total_terms = sum(doc_term_count.values())
    for term, count in doc_term_count.items():
        tf = count / total_terms
        tf_idf[term] = tf * idf.get(term, 0)
    return tf_idf


def search(docs, query):
    if not docs:
        return []

    inverted_index, doc_term_counts = build_inverted_index(docs)
    total_docs = len(docs)
    idf = compute_idf(inverted_index, total_docs)
    query_terms = preprocess_text(query)

    if not query_terms:
        return []

    doc_scores = defaultdict(float)

    for term in query_terms:
        if term in inverted_index:
            for doc_id in inverted_index[term]:
                doc_index = None
                for i, doc in enumerate(docs):
                    if doc['id'] == doc_id:
                        doc_index = i
                        break
                doc_tf_idf = compute_tf_idf(doc_term_counts[doc_index][1], idf)
                doc_scores[doc_id] += doc_tf_idf.get(term, 0)

    sorted_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)

    return [doc_id for doc_id, _ in sorted_docs]


def main():
    # Пример использования
    doc1 = {
        'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"
    }
    doc2 = {'id': 'doc2', 'text': "Don't shoot shoot shoot that thing at me."}
    doc3 = {'id': 'doc3', 'text': "I'm your shooter."}
    docs = [doc1, doc2, doc3]

    print(search(docs, 'shoot at me'))  # ['doc2', 'doc1']
    print(search(docs, 'pint!'))        # ['doc1']
    print(search([], 'shoot'))          # []


if __name__ == '__main__':
    main()
