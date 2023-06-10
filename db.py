import sqlite3
import random
import time

#last_id = 40960

# Connect to sqlite db
db = sqlite3.connect("anime.db")
_cur = db.cursor()

class Anime():
    
    id = "?"
    title = "?"
    synopsis = "?"
    genres = []
    aired_season = "?"
    episodes = "?"
    popularity = "?" # MAL rank
    ranked = "?" # score rank?
    score = "?"
    img_url = "?"
    link = "?"
    studios = []
    # TODO: source type

    def get_anime(id):
        global _cur
        _cur.execute("SELECT * FROM anime WHERE anime_id = ?", [id])
        anime = _cur.fetchone()
        result = Anime()

        result.id = anime[0]
        result.link = anime[1]
        result.title = anime[2]
        result.synopsis = anime[3]
        result.img_url = anime[4]
        try:
            result.episodes = float(anime[7])
        except ValueError:
            result.episodes = "?"
        result.aired_season = anime[11]
        
        result.studios = anime[12].split('|')
        result.genres = anime[13].split('|')
        try:
            result.score = float(anime[14])
        except ValueError:
            result.score = "?"
        result.ranked = anime[16]
        result.popularity = anime[17]

        return result
    
    def get_random_by_popularity(popularity): # maybe use score rank?
        random.seed(time.process_time())
        rand_int = random.randint(0, popularity)
        _cur.execute("SELECT anime_id FROM anime WHERE popularity_rank = ?", [rand_int])
        id = _cur.fetchone()[0]

        return Anime.get_anime(id)

    # get total count of anime in db
    def get_total():
        _cur.execute("SELECT COUNT(*) FROM anime")
        count = _cur.fetchone()[0]
        return count
    
    def get_by_title(title):
        _cur.execute("SELECT anime_id FROM anime WHERE title = ?", [title])
        id = _cur.fetchone()[0]
        print(title)
        print(id)

        return Anime.get_anime(id)
        

    # TODO: hints for popularity/ranked
    def compare_hints(self, guess):
        result = "Episodes: "

        if self.episodes == "?":
            result += "No info"
        elif guess.episodes == "?":
            result += "[No info for guessed episodes]"
        else:
            if guess.episodes < self.episodes:
                result += (">")
            elif guess.episodes > self.episodes:
                result += ("<")
            elif guess.episodes == self.episodes:
                result += str(self.episodes)
        
        result += "\nAired season: "


        if self.aired_season == "":
            result += "No info"
        elif guess.aired_season == "":
            result += "[No info for guessed season]"
        else:
            s_g = guess.aired_season.split(' ') # TODO: just serialize it when getting from db
            s_s = self.aired_season.split(' ')
            guess_season_year = s_g[1]
            self_season_year = s_s[1]

            guess_season_season = 0 if s_g[0] == 'Winter' else 1 if s_g[0] == 'Spring' else 2 if s_g[0] == 'Summer' else 3 if s_g[0] == 'Fall' else ''
            self_season_season = 0 if s_s[0] == 'Winter' else 1 if s_s[0] == 'Spring' else 2 if s_s[0] == 'Summer' else 3 if s_s[0] == 'Fall' else ''

            if guess.aired_season == self.aired_season:
                result += (self.aired_season)
            elif guess_season_year < self_season_year:
                result += (">")
            elif guess_season_year > self_season_year:
                result += ("<")
            elif guess_season_year == self_season_year:
                if guess_season_season < self_season_season:
                    result += (">")
                elif guess_season_season > self_season_season:
                    result += ("<")


        result += "\nStudios: "
        
        flag = False
        for s in self.studios:
            if s in guess.studios:
                result += (s + ",")
                flag = True
        if not flag:
            result += ("[X]")

        result += "\nGenres: "            
        
        flag = False
        for g in self.genres:
            if g in guess.genres:
                result += (g + ",")
                flag = True
        if not flag:
            result += ("[X]")

        result += "\nScore: "

        if self.score == "?":
            result += "No info"
        elif guess.score == "?":
            result += "[No info for guessed score]"
        else:
            if guess.score < self.score:
                result += (">")
            elif guess.score > self.score:
                result += ("<")
            elif guess.score == self.score:
                result += str(self.score)
        




        #comparison = Anime()

        #correct_genres = []

        #for g in guess.genre:
        #    if g in self.genre:
        #        correct_genres.append(g)
        #print(correct_genres)
        #if len(correct_genres) > 0:
        #    if len(correct_genres) == len(self.genre):
        #        comparison.genre = "[ALL CORRECT] " + str(correct_genres)
        #    comparison.genre = correct_genres

        #else:
        #    comparison.genres = "X"

        #if guess.episodes == self.episodes:
        #    comparison.episodes = self.episodes

        return result


    def __str__(self):

        result = f"""Title: {self.title}
Genres: {self.genres}
Aired season: {self.aired_season}
Episodes: {self.episodes}
Popularity: {self.popularity}
Ranked: {self.ranked}
Score: {self.score}
Studios: {self.studios}"""

        return result
    def __repr__(self):
        result = f"""Title: {self.title}
Genres: {self.genres}
Aired season: {self.aired_season}
Episodes: {self.episodes}
Popularity: {self.popularity}
Ranked: {self.ranked}
Score: {self.score}
Studios: {self.studios}"""

        return result
    
if __name__ == "__main__":
    #print(get_anime)
#    print(Anime.get_by_title("Death Note"))
    popularity = 10
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
    print(Anime.get_random_by_popularity(popularity))
