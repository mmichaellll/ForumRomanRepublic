from post import Post
from thread import Thread

class Forum:
  def __init__(self):
    self.threads = []
  
  def get_threads(self):
    """
    Returns a list of threads in the forum, in the order that they were published.
    """
    return self.threads
  
  def publish(self, title, content, author):
    """
    Creates a new thread with the given title and adds it to the forum.
    The content and author are provided to allow you to create the first post object.
    Forum threads are stored in the order that they are published.
    Returns the new thread.
    """
    first_post = Post(content, author)
    thread = Thread(title, first_post)
    self.threads.append(thread)
    return thread
  
  def search_by_tag(self, tag):
    """
    Searches all forum threads for any that contain the given tag.
    Returns a list of matching thread objects in the order they were published. (currently works oldest -> newest)
    """
    matching_threads = []
    for thread in self.threads:
      tags = thread.get_tags()
      if tag in tags:
        matching_threads.append(thread)
    return matching_threads
  
  def search_by_author(self, author):
    """
    Searches all forum threads for posts by the given author.
    Returns a list of matching post objects in any order you like. (currently works oldest -> newest)
    """
    matching_posts = []
    for thread in self.threads:
      posts = thread.get_posts()
      for post in posts:
        post_author = post.get_author()
        if post_author == author:
          matching_posts.append(post)
    return matching_posts
