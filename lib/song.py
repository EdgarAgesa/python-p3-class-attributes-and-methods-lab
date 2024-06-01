class Song:

    count = 0
    genres= []
    artists= []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name= name
        self.artist= artist
        self.genre= genre
        Song.add_song_to_count()
        Song.genres.append(self.genre)
        Song.artists.append(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)



    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1      

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# ninety=Song("Edgar", "My world", "Rock" )

# print(ninety.name)
# ninety.add_to_genres("Roc")
# print(ninety.genres)
# song1 = Song("Lose Yourself", "Eminem", "Rap")
# song2 = Song("Bohemian Rhapsody", "Queen", "Rock")
# song3 = Song("Before He Cheats", "Carrie Underwood", "Country")
# song4 = Song("Stan", "Eminem", "Rap")
# song5 = Song("Cry Me a River", "Justin Timberlake", "Pop")
# song6 = Song("Friends in Low Places", "Garth Brooks", "Country")

# print(Song.artist_count)
# print(Song.genre_count)
# print(Song.artists)