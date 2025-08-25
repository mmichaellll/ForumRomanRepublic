class Thread:
  def __init__(self, title, first_post):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post is also the owner of the thread.
    The owner cannot change once the thread is created.
    """
    pass

  def get_owner(self):
    """
    Returns the owner of the thread.
    """
    pass
  
  def get_title(self):
    """
    Returns the title of the thread.
    """
    pass
  
  def get_tags(self):
    """
    Returns a sorted list of unique tags.
    """
    pass
  
  def get_posts(self):
    """
    Returns a list of posts in this thread, in the order they were published.
    """
    pass
  
  def publish_post(self, post):
    """
    Adds the given post object into the list of posts.
    """
    pass
  
  def remove_post(self, post, by_user):
    """
    Allows the given user to remove the post from this thread.
    Does nothing if the post is not in this thread.
    * raises PermissionDenied if the given user is not the author of the post.
    """
    pass
  
  def set_title(self, title, by_user):
    """
    Allows the given user to edit the thread title.
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
    pass
  
  def set_tags(self, tag_list, by_user):
    """
    Allows the given user to replace the thread tags (list of strings).
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
    pass