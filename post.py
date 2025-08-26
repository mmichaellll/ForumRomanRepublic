class Post:
  def __init__(self, content, author):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post at the time of thread creation is the owner of the thread.
    The owner cannot change once the thread is created.
    """
    self.content = content
    self.author = author
    self.upvotes = set()
  
  def get_author(self):
    """
    Returns the author of the post.
    """
    return self.author
  
  def get_content(self):
    """
    Returns the content of the post.
    """
    return self.content
  
  def get_upvotes(self):
    """
    Returns a single integer representing the total number of upvotes.
    """
    return len(list(self.upvotes()))
  
  def set_content(self, content, by_user):
    """
    Called when the given user wants to update the content.
    * raises PermissionDenied if the given user is not the author.
    """
    if by_user == self.author:
      self.content = content
    else:
      raise(PermissionDenied)
  
  def upvote(self, by_user):
    """
    Called when the given user wants to upvote this post.
    A user can only perform an up vote *once*.
    """
    self.upvotes.add(by_user)