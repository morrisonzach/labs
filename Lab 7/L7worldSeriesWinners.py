#
#   purpose: find the number of times a team has won a world series
#   author: zachary morrison
#   date written: 11/18/2020
#   Version: 1.0.0
#

#   making object to hold each baseball team
class BaseballTeam:
    def __init__(self, name):
        self.name = name
        self.wins = 1

    def get_name(self):
        return self.name

    def get_wins(self):
        return self.wins

    def add_win(self):
        self.wins += 1

    def __str__(self):
        return format((self.name + " " + str(self.wins)), "20")


#   array of baseball teams
teams = []

#   checks if a team already exists within the team array


def team_exists(check="", teams=[BaseballTeam]):
    for team in range(len(teams)):
        if teams[team].name.lower() == check.lower():
            return team
    return -1

#   read file containing baseball team records and puts teams into an array


def read_records(file):
    try:
        f = open(file, "rt")
        lines = f.readlines()
        f.close()
        for line in lines:
            if len(teams) == 0:
                teams.append(BaseballTeam(line.rstrip()))
            elif team_exists(line.rstrip(), teams) != -1:
                teams[team_exists(line.rstrip(), teams)].add_win()
            else:
                teams.append(BaseballTeam(line.rstrip()))
    except IOError:
        print("something in the file has not been properly read!")
    except IndexError:
        print("~~this is not the team you are looking for~~")

#   this function finds the number of wins for a particular team that is input by the user


def find_wins():
    going = True
    while (going):
        team_name = str(
            input("enter the name of the team whose record you'd like to see: "))
        if team_exists(team_name, teams) != -1:
            print(teams[team_exists(team_name, teams)])
        else:
            print("it doesn't look like that team exists :(")

        if str(input("\nwould you like to try again? [y, n] ")).lower() != 'y':
            going = False


print("this program contains the World Series records from the year 1903 to 2009. it will return the record for any team who's name is accurately typed into the input. \n======================================================\n")
read_records("WorldSeriesWinners.txt")
find_wins()
