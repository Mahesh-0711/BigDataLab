import csv

def map_reducer(tags):
    result = {}
    for row in tags:
        movie_id , tag = row['movieId'],row['tag']
        result.setdefault(movie_id,set()).add(tag)
    return result

with open('tags.csv') as f:
    tags = list(csv.DictReader(f))

with open('movies.csv') as f:
    movies = {r['movieId']: r['title'] for r in csv.DictReader(f)}

result = map_reducer(tags)
for movie_id,tag in result.items():
    print(f"Movie : {movies[movie_id]},Tags {', '.join(tag)}")