from functools import lru_cache
from constants import N__GRAM


@lru_cache(maxsize=256)
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return -L[m][n]


@lru_cache(maxsize=256)
def levenshtein(s, t, costs=(2, 1, 2)):
    """
        costs: a tuple or a list with three integers (d, i, s)
            where d defines the costs for a deletion
                  i defines the costs for an insertion and
                  s defines the costs for a substitution
    """
    rows = len(s)+1
    cols = len(t)+1
    deletes, inserts, substitutes = costs

    dist = [[0 for x in range(cols)] for x in range(rows)]
    for row in range(1, rows):
        dist[row][0] = row * deletes

    for col in range(1, cols):
        dist[0][col] = col * inserts

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitutes
            dist[row][col] = min(dist[row-1][col] + deletes,
                                 dist[row][col-1] + inserts,
                                 dist[row-1][col-1] + cost)  # substitution
    return dist[row][col]


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


def generate_ngrams(word, n=N__GRAM, lpad=True, rpad=False):
    word = f"{' '* (n-1) * lpad}{word}{' '* (n-1) * rpad}"
    return [word[x:x + n] for x in range(len(word) - (n-1))]


def ngrams_match(match, word, lpad=True, rpad=False):
    match_grams = generate_ngrams(match, lpad=lpad, rpad=rpad)
    word_grams = generate_ngrams(word, lpad=lpad, rpad=rpad)
    return -len(set(match_grams).intersection(word_grams))
