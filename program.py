from exceptions import PermissionDenied
from forum import Forum
from thread import Thread, ThreadPostLink
from post import Post, PostUpvotes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User
from base import Base


# You can put any testing code (that won't be run by the marker)
# in the block below.


if __name__ == '__main__':
  # Test your code here. This will not be checked by the marker.
  # Here is the example from the question.
  engine = create_engine("sqlite:///forum.db")
  Session = sessionmaker(bind=engine)
  session = Session()
  Base.metadata.create_all(engine)
  forum = Forum()
  first_post = Post('Veni, vidi, vici!', 'Caesar')
  session.add(first_post)
  session.flush()

  thread = forum.publish('Battle of Zela', first_post, 'Caesar')
  session.add(thread)
  session.flush()
  thread.set_tags(['battle', 'brag'], 'Caesar')

  thread.publish_post(first_post, session)

  posts = [
    Post('That was quick!', 'Amantius'),
    Post('Hardly broke a sweat.', 'Caesar'),
    Post('Any good loot?', 'Amantius')
  ]
  for post in posts:
    session.add(post)
    session.flush()  
    thread.publish_post(post, session)

  session.commit()  

  print("The contents of Caesar's posts:")
  caesar_posts = forum.search_by_author('Caesar')
  print(sorted([p.get_content() for p in caesar_posts]))
  print()

  existing = thread.get_posts(session)[0]
  existing.set_content('I came, I saw, I conquered!', 'Caesar')

  existing.upvote('Cleopatra')
  existing.upvote('Brutus')
  existing.upvote('Amantius')
  existing.upvote('Cleopatra')



  print("[{}](+{}) -- {}\n".format(
    existing.get_author(),
    existing.get_upvotes(),
    existing.get_content()
  ))

  # And some access control:
  try:
    thread.set_title('Hijacked!', 'Cleopatra')
  except PermissionDenied:
    print('Cleopatra was not allowed to hijack the thread.')