from exceptions import PermissionDenied

class Thread:
  def __init__(self, title, first_post):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post is also the owner of the thread.
    The owner cannot change once the thread is created.
    """

    self.title = title
    self.first_post = first_post
    self.owner = first_post.get_author() 
    self.tags = {}
    self.posts = [first_post]

  def get_owner(self):
    """
    Returns the owner of the thread.
    """
    return self.first_post.get_author()
  
  def get_title(self):
    """
    Returns the title of the thread.
    """
    return self.title
  
  def get_tags(self):
    """
    Returns a alphabetically sorted list of unique tags.
    """
    return sorted(self.tags)
  
  def get_posts(self):
    """
    Returns a list of posts in this thread, in the order they were published.
    """
    return self.posts
  
  def publish_post(self, post):
    """
    Adds the given post object into the list of posts.
    """
    self.posts.append(post)
  
  def remove_post(self, post, by_user):
    """
    Allows the given user to remove the post from this thread.
    Does nothing if the post is not in this thread.
    * raises PermissionDenied if the given user is not the author of the post.
    """
    if post in self.posts and post.get_author() == by_user:
      self.posts.remove(post)
      return True
    else:
      raise PermissionDenied()        

  def set_title(self, title, by_user):
    """
    Allows the given user to edit the thread title.
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
  
    if self.get_owner() == by_user:
      self.title = title
    else:
      raise PermissionDenied()
  
  def set_tags(self, tag_list, by_user):
    """
    Allows the given user to replace the thread tags (list of strings).
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
    if self.get_owner() == by_user:
      self.tags = tag_list
    else:
      raise PermissionDenied()