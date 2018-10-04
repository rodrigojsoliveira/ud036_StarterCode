"""
Media Module

This module contains entertainment medias. Examples of media that could
be modelled are TV Shows, Music Concerts, Sports Broadcast, and so on.
"""


class Movie():
    """
    Class Movie

    A movie object will contain basic information of a movie, like its title,
    poster image url, and trailer url. Other properties can be created
    depending on the information you wish to display to the end user.
    """

    # Class constructor.
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
