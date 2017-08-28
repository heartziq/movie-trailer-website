import webbrowser

class Movie():
    """ This class is all about your favourite movies description """
    VALID_RATINGS = ["PG", "R", "M"]

    def __init__(self, title, storyline, poster_img, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

