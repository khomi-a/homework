class Movie:

    def __init__(self, name, director, year, country, duration, age_rating):
        if isinstance(name, str) and isinstance(director, str)\
            and isinstance(year, int) and isinstance(country, str)\
                and isinstance(duration, int) and isinstance(age_rating, int):
            self.__name = name
            self.__director = director
            self.__year = year
            self.__country = country
            self.__duration = duration
            self.__age_rating = age_rating
        else:
            raise TypeError

    def is_allowed(self, human):
        return 2021 - human.get_year_of_birth() > self.__age_rating


class Cartoon(Movie):

    def __init__(self, technique, name, director, year, country, duration, age_rating):
        super().__init__(name, director, year, country, duration, age_rating)
        if isinstance(technique, str):
            self.__technique = technique
        else:
            raise TypeError


class Anime(Cartoon):

    def __init__(self, technique, name, director, year, country, duration, age_rating):
        super().__init__(technique, name, director, year, country, duration, age_rating)
        if self.__country != 'Japan':
            raise ValueError('Anime must be from Japan')


class Human:

    def __init__(self, name, sex, year_of_birth):
        self.__name = name
        self.__sex = sex
        self.__year_of_birth = year_of_birth

    def get_year_of_birth(self): #getter for year of birth
        return self.__year_of_birth


movie = Movie(
  name="Dune", director="Denis Villeneuve", year=2021,
  country="USA", duration=155, age_rating=13
)

human = Human(name="Neo", sex="M", year_of_birth=1964)

print(movie.is_allowed(human))