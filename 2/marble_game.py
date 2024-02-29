import regex
import numpy

class Game:
    def __init__(self, input:str) -> None:
        self.game_number = 0
        self.hands =[]
        self.__analyse_input(input)
        self.sum_min_set = self.__find_minimum_set()

    def __analyse_input(self, input:str):
        game_split = input.split(sep=':')
        self.game_number = regex.findall('\d+', game_split[0])[0]
        hands = game_split[1].split(sep=';')
        for hand in hands:
            self.__observe_hand(hand)
    
    def __observe_hand(self, hand:str):
        observed_hand = {"red":0, "blue":0, "green":0}
        colors_in_hand = hand.split(sep=',')
        for color in colors_in_hand:
            color_split = color.split()
            observed_hand[color_split[1]] = int(color_split[0])
        self.hands.append(observed_hand)

    def __find_minimum_set(self) -> int:
        min_hand = {}
        for hand in self.hands:
            if not min_hand:
                min_hand = hand
            else:
                for key in hand:
                    if key in min_hand:
                        if min_hand[key] < hand[key]:
                            min_hand[key] = hand[key]
                    else:
                        min_hand[key] = hand[key]
        product_of_minset = 1
        for val in min_hand.values():
            product_of_minset = product_of_minset * val
        return product_of_minset


    def obeys_constraints(self, constraints:dict) -> bool:
        for hand in self.hands:
            for key in constraints:
                if hand[key] > constraints[key]:
                    return False
        return True


### analyses part
# sample_line = "Game 36: 4 blue, 4 red, 4 green; 8 red, 8 blue, 4 green; 3 green, 9 red, 5 blue; 1 red, 4 green, 13 blue; 7 blue, 9 green, 9 red; 13 blue, 8 red"

# test = Game(sample_line)
# print(test.sum_min_set)

game_constraints = {"red":12, "blue":14, "green":13}

filepath = '/home/rj/codeing/Advent_of_code/2/games'

games = []
minhand_sums = []

game_file = open(filepath, "r")

lines = game_file.readlines()

for line in lines:
    game = Game(line)
    if game.obeys_constraints(game_constraints):
        games.append(int(game.game_number))
    minhand_sums.append(game.sum_min_set)

print(games)
print("sum of games adhering to constraints = "+ str(sum(games)))
print("sum of minhands: " + str(sum(minhand_sums)))