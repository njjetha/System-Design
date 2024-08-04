from BuilderComputer import BuilderComputer
from GamingComputer import GamingComputer
from Director import Director

if __name__ == "__main__":
    gaming = GamingComputer()
    director = Director(gaming)
    director.construct(24,2,2,8)