import datetime

class CricketPLayer:
    team_size = 11
    def __init__(self, fname, lname, birth_year, team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}, the cricket player from {self.team}"

    def __lt__(self, other):
        self_avg_score = self.get_average_score()
        other_avg_score = other.get_average_score()
        return self_avg_score < other_avg_score

    def __eq__(self, other):
        self_age = self.get_age()
        other_age = other.get_age()
        return self_age == other_age

virat = CricketPLayer('virat', 'kohli', 1988, 'India')
virat.add_score(37)
virat.add_score(100)
virat.add_score(23)

print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
print(virat.scores)
print(virat.get_average_score())
print(f"Age of {virat.first_name.capitalize()} is:{virat.get_age()}")
print(virat)

david = CricketPLayer('david', 'warner', 1986, 'Australia')
print(david.first_name)
print(david.last_name)
print(david.birth_year)

david.add_score(45)
david.add_score(120)
david.add_score(12)

print(virat.get_average_score())
print(david.get_average_score())

#print(david.get_average_score()<virat.get_average_score())
print(virat == david)