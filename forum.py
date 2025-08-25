class Forum:
  def __init__(self):
    """
    Perform initialisation of a new forum object, as needed.
    """
    pass
  
  def get_threads(self):
    """
    Returns a list of threads in the forum, in the order that they were published.
    """
    pass
  
  def publish(self, title, content, author):
    """
    Creates a new thread with the given title and adds it to the forum.
    The content and author are provided to allow you to create the first post object.
    Forum threads are stored in the order that they are published.
    Returns the new thread.
    """
    pass
  
  def search_by_tag(self, tag):
    """
    Searches all forum threads for any that contain the given tag.
    Returns a list of matching thread objects in the order they were published.
    """
    pass
  
  def search_by_author(self, author):
    """
    Searches all forum threads for posts by the given author.
    Returns a list of matching post objects in any order you like.
    """
    pass
