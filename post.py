class Post:
  def __init__(self, content, author):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post at the time of thread creation is the owner of the thread.
    The owner cannot change once the thread is created.
    """
    pass
  
  def get_author(self):
    """
    Returns the author of the post.
    """
    pass
  
  def get_content(self):
    """
    Returns the content of the post.
    """
    pass
  
  def get_upvotes(self):
    """
    Returns a single integer representing the total number of upvotes.
    """
    pass
  
  def set_content(self, content, by_user):
    """
    Called when the given user wants to update the content.
    * raises PermissionDenied if the given user is not the author.
    """
    pass
  
  def upvote(self, by_user):
    """
    Called when the given user wants to upvote this post.
    A user can only perform an up vote *once*.
    """
    pass