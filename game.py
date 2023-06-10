from db import Anime

class Game():
    game_state = 0
    answer = None
    guess_count = 10

    def start_game(self):
        if self.game_state != 0:
            return "Game is running"
#        rand = random.randint(1,last_uid+1)

#        while not self.answer:
#            try:
#                self.answer = Anime.get_anime(rand)
#            except:
#                rand = random.randint(1,40960+1)

        self.answer = None
        while not self.answer:
            try:
                self.answer = Anime.get_random_by_popularity(100) # TODO: configurable
            except Exception as e:
                return "Failed to start :(\nIt's broken again"
        print(f"[ANSWER] {self.answer.title}")
        self.game_state = 1
        print("Game started")
        return "Game started"
    
    def guess(self, player_guess):
        if self.game_state == 0:
            return "Game not running"

        print(f"Guess: {player_guess}")
        if player_guess == self.answer.title: # TODO: fuzzy
            self.game_state = 0
            self.guess_count = 10
            return f"WINNER WINNER CHICKEN CURRY\nAnswer:\n{str(self.answer)}"
        else:
            try:
                guessed = Anime.get_by_title(player_guess)
            except TypeError:
                return "No anime with this title"
            result = f"Your guess:\n{guessed}\n\nHints:\n"
            result += self.answer.compare_hints(guessed)

            self.guess_count -= 1
            if self.guess_count == 0:
                self.game_state = 0
                self.guess_count = 10
                return f"YOU LOST! Answer:\n{str(self.answer)}"
            
            return result
            


if __name__ == "__main__":
    game = Game()

    game.start_game()

    while game.game_state != 0:
        guess = input()
        print("[Game out] " + game.guess(guess))
