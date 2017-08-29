import media
import fresh_tomatoes

the_intership = media.Movie("The Internship",
                            "https://upload.wikimedia.org/wikipedia/en/e/ed/"
                            "The-internship-poster.jpg",
                            "https://www.youtube.com/watch?v=cdnoqCViqUo")

batman = media.Movie("Batman: The Dark Knight",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_K"
                     "night.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

spiderman = media.Movie("Spider-Man: Homecoming",
                        "https://upload.wikimedia.org/wikipedia/en/f/"
                        "f9/Spider-Man_Homecoming_poster.jpg",
                        "https://www.youtube.com/watch?v=U0D3AOldjMU")

guardians_galaxy = media.Movie("Guardians of the Galaxy Vol. 2",
                               "https://upload.wikimedia.org/wikip"
                               "edia/en/9/95/GotG_Vol2_poster.jpg",
                               "https://www.youtube.com/watch?v=2cv2ueYnKjg")

gone_girl = media.Movie("Gone Girl",
                        "https://upload.wikimedia.org/wikipedia/en/0/05/Go"
                        "ne_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")

nightcrawler = media.Movie("Nightcrawler",
                           "https://upload.wikimedia.org/wikipedia/en/d/d4/Ni"
                           "ghtcrawlerfilm.jpg",
                           "https://www.youtube.com/watch?v=u1uP_8VJkDQ")

movies = [the_intership, batman, spiderman,
          guardians_galaxy, gone_girl, nightcrawler]

fresh_tomatoes.open_movies_page(movies)
