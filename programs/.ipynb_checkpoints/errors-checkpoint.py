class Not_Avalible_Site(Exception):
    """
    Exception raised when a function is not defied for a website.
    
    Attributes:
        - website
        - message
    """

    def __init__(self,website):
        self.website=website
        self.message = "The site '{}' is not in the sites list 'tweet_links.websites'".format(website)
        super().__init__(self.message)
        