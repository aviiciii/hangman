import random
import re

films = [
    'The Lord of the Rings: The Fellowship of the Ring (2001)',
    'The Godfather (1972)',
    'The Shawshank Redemption (1994)',
    'The Godfather, Part II (1974)',
    'The Dark Knight (2009)',
    '12 Angry Men (1957)',
    'Schindler\'s List (1993)',
    'The Lord of the Rings: The Return of the King (2003)',
    'Pulp Fiction (1994)',
    'The Good, the Bad, and the Ugly (1966)',
    'The Lord of the Rings: The Fellowship of the Ring (2001)',
    'Fight Club (1999)',
    'Forrest Gump (1994)',
    'Inception (2010)',
    'The Lord of the Rings: The Two Towers (2002)',
    'Star Wars: Episode V: The Empire Strikes Back (1980)',
    'The Matrix (1999)',
    'GoodFellas (1990)',
    'One Flew Over The Cuckoo\'s Nest (1975)',
    'The Seven Samurai (1954)',
    'Se7en (1995)',
    'Life is Beautiful (1997)',
    'City of God (2002)',
    'The Silence of the Lambs (1991)',
    'It\'s A Wonderful Life (1946)',
    'Star Wars (1977)',
    'Saving Private Ryan (1998)',
    'Spirited Away (2001)',
    'The Green Mile (1999)',
    'Interstellar (2014)',
    'Parasite (2019)',
    'Leon, aka The Professional (1994)',
    'The Usual Suspects (1995)',
    'Harakiri (1962)',
    'The Lion King (1994)',
    'Back to the Future (1985)',
    'The Pianist (2002)',
    'Terminator 2: Judgment Day (1991)',
    'American History X (1998)',
    'Modern Times (1936)',
    'Psycho (1960)',
    'Gladiator (2000)',
    'City Lights (1931)',
    'The Departed (2006)',
    'The Intouchables (2011)',
    'Whiplash (2014)',
    'The Prestige (2006)',
    'Grave of the Fireflies (1988)',
    'Hamilton (2020)',
    'Once Upon a Time in the West (1969)',
    'Casablanca (1942)',
]


def main():
    movie, year = select_movie()


def select_movie():
    movie = random.choices(films)
    print(movie)

    if search := re.search(r'^([A-Za-z0-9_.:,\' ]*) \((\d{4})\)$', movie[0]):
        return search.groups()


def function_n():
    ...


if __name__ == "__main__":
    main()