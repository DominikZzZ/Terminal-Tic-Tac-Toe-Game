
import sys


class Game:

    def __init__(self):
        self.a1, self.a2, self.a3 = " ", " ", " "
        self.b1, self.b2, self.b3 = " ", " ", " "
        self.c1, self.c2, self.c3 = " ", " ", " "

        self.info_x_move = "\nX move (etc. A1): "
        self.info_o_move = "\nO move (etc. A1): "
        self.info_wrong_move = "\nWrong move, try again"

        self.x_pos = None
        self.o_pos = None

        self.moves_amount = 9
        self.moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

        self.pattern = ("\n"
                        "    -A- -B- -C-\n"
                       f"-1-  {self.a1} | {self.b1} | {self.c1} \n"
                        "    ---+---+---\n"
                       f"-2-  {self.a2} | {self.b2} | {self.c2} \n"
                        "    ---+---+---\n"
                       f"-3-  {self.a3} | {self.b3} | {self.c3} \n")

    def check_move(self, player, player_move):
        current_player = None
        if player == "X": current_player = "X"
        if player == "O": current_player = "O"

        if player_move == "A1" or player_move == "A2" or player_move == "A3" or\
            player_move == "B1" or player_move == "B2" or player_move == "B3" or\
                player_move == "C1" or player_move == "C2" or player_move == "C3":

            if player_move == "A1" and self.a1 == " ":
                self.a1 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "A1" and self.a1 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()
            if player_move == "A2" and self.a2 == " ":
                self.a2 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "A2" and self.a2 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()
            if player_move == "A3" and self.a3 == " ":
                self.a3 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "A3" and self.a3 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()

            if player_move == "B1" and self.b1 == " ":
                self.b1 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "B1" and self.b1 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()
            if player_move == "B2" and self.b2 == " ":
                self.b2 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "B2" and self.b2 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()
            if player_move == "B3" and self.b3 == " ":
                self.b3 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "B3" and self.b3 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()

            if player_move == "C1" and self.c1 == " ":
                self.c1 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "C1" and self.c1 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()
            if player_move == "C2" and self.c2 == " ":
                self.c2 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "C2" and self.c2 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()
            if player_move == "C3" and self.c3 == " ":
                self.c3 = current_player
                self.moves_amount -= 1
                self.update_pattern()
            elif player_move == "C3" and self.c3 != " ":
                print(self.info_wrong_move)
                if player == "X": self.x_move()
                if player == "O": self.o_move()

        else:
            if player_move == "QUIT": self.exit()

            print(self.info_wrong_move)
            if player == "X": self.x_move()
            if player == "O": self.o_move()

    def check_win(self, player):
        current_player = None
        if player == "X": current_player = "X"
        if player == "O": current_player = "O"

        if self.a1 == current_player and self.a2 == current_player and self.a3 == current_player: self.win(pos1=self.a1, pos2=self.a2, pos3=self.a3, player=current_player)
        if self.b1 == current_player and self.b2 == current_player and self.b3 == current_player: self.win(pos1=self.b1, pos2=self.b2, pos3=self.b3, player=current_player)
        if self.c1 == current_player and self.c2 == current_player and self.c3 == current_player: self.win(pos1=self.c1, pos2=self.c2, pos3=self.c3, player=current_player)
        if self.a1 == current_player and self.b1 == current_player and self.c1 == current_player: self.win(pos1=self.a1, pos2=self.b1, pos3=self.c1, player=current_player)
        if self.a2 == current_player and self.b2 == current_player and self.c2 == current_player: self.win(pos1=self.a2, pos2=self.b2, pos3=self.c2, player=current_player)
        if self.a3 == current_player and self.b3 == current_player and self.c3 == current_player: self.win(pos1=self.a3, pos2=self.b3, pos3=self.c3, player=current_player)
        if self.a1 == current_player and self.b2 == current_player and self.c3 == current_player: self.win(pos1=self.a1, pos2=self.b2, pos3=self.c3, player=current_player)
        if self.a3 == current_player and self.b2 == current_player and self.c1 == current_player: self.win(pos1=self.a3, pos2=self.b2, pos3=self.c1, player=current_player)

    def win(self, pos1, pos2, pos3, player):
        pos1 = "#"; pos2 = "#"; pos3 = "#"
        self.update_pattern()
        print(f"\n{player} won")
        self.exit()

    def check_moves(self):
        if self.moves_amount == 0:
            print("\nNobody won")
            self.exit()
        else:
            pass

    def update_pattern(self):
        self.pattern = ("\n"
                        "    -A- -B- -C-\n"
                       f"-1-  {self.a1} | {self.b1} | {self.c1} \n"
                        "    ---+---+---\n"
                       f"-2-  {self.a2} | {self.b2} | {self.c2} \n"
                        "    ---+---+---\n"
                       f"-3-  {self.a3} | {self.b3} | {self.c3} \n")

        print(self.pattern)

    def x_move(self):
        self.check_moves()

        self.x_pos = input(self.info_x_move)
        self.check_move(player="X", player_move=self.x_pos)
        self.check_win(player="X")

    def o_move(self):
        self.check_moves()

        self.o_pos = input(self.info_o_move)
        self.check_move(player="O", player_move=self.o_pos)
        self.check_win(player="O")

    def exit(self):
        sys.exit()

    def run(self):
        print('\nTo exit enter "QUIT"')
        print(self.pattern)

        while True:
            self.x_move()
            self.o_move()


if __name__ == "__main__":
    game = Game()
    game.run()
