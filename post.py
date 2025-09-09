from exceptions import PermissionDenied 
from base import Base
from user import User
from sqlalchemy import select, update, ForeignKey, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

class PostUpvotes(Base):
  __tablename__ = 'postupvotes'

  post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)


class Post(Base):
  __tablename__ = 'post'

  id: Mapped[int] = mapped_column(primary_key=True)
  date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
  author: Mapped[int] #user id
  content: Mapped[str]

  def __init__(self, content, author):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post at the time of thread creation is the owner of the thread.
    The owner cannot change once the thread is created.
    """
    self.content = content
    self.author = author.get_id()
  
  def get_author(self):
    """
    Returns the author of the post (user object)
    """
    return select(User).where(User.id == self.author)
  
  def get_content(self):
    """
    Returns the content of the post.
    """
    return self.content
  
  def get_upvotes(self):
    """
    Returns a single integer representing the total number of upvotes.
    """
    # update when upvote linking table is made
    return len(list(self.upvotes()))
  
  def set_content(self, content, by_user):
    """
    Called when the given user wants to update the content.
    * raises PermissionDenied if the given user is not the author.
    """
    if by_user == self.get_author():
      self.content = content
    else:
      raise(PermissionDenied)
  
  def upvote(self, by_user):
    """
    Called when the given user wants to upvote this post.
    A user can only perform an up vote *once*.
    """
    # will need to be updated when post-upvote linking table is made
    self.upvotes.add(by_user)
