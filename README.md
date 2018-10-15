# fuzzyMatch

## Problem Statement

***Write an HTTP service that provides an endpoint for fuzzy search/autocomplete of English words.***


### Deploying

```
git clone https://github.com/techoni3/fuzzymatch.git

cd fuzzymatch

docker-compose up --build
```
Or
```
gunicorn -b 0.0.0.0:8107 app:app --reload --access-logfile -
```
