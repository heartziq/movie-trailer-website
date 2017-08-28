import media, fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story about a boy named Alan who is obssessed with his new toy",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")


avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("The School Of Rock",
                             "An aspired rockstar poses as a school teacher",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?gl=SG&hl=en-GB&v=XCwy6lW5Ixc")

silence_of_the_lambs = media.Movie("Silence Of The Lambs", "A story about a boy named Alan who is obssessed with his new toy",
                        "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",
                        "https://www.youtube.com/watch?v=RuX2MQeb8UM")

gone_girl = media.Movie("Gone Girl", "A story about a boy named Alan who is obssessed with his new toy",
                        "https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")

nightcrawler = media.Movie("Nightcrawler", "A story about a boy named Alan who is obssessed with his new toy",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Nightcrawlerfilm.jpg",
                        "https://www.youtube.com/watch?v=u1uP_8VJkDQ")



movies = [toy_story, avatar, school_of_rock, silence_of_the_lambs, gone_girl, nightcrawler]
fresh_tomatoes.open_movies_page(movies)
