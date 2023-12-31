#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = float('-inf')
    m_key = None

    if a_dictionary is None or a_dictionary == {}:
        return None
    for key, value in a_dictionary.items():
        if value > max_val:
            max_val = value
            m_key = key

    return m_key
