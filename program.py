from exceptions import PermissionDenied
from forum import Forum
from thread import Thread, ThreadPostLink
from post import Post, PostUpvotes
from user import User
from forum import Forum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
  caesar = User('caesar@rome.com', 'venividivici7', 'Julius', 'Caesar', 1, 7, 12) #technically born 100 BC but that doesn't work
  cleopatra = User('cleopatra@pharaoh.com', 'nile379%', 'Cleopatra', 'Philopator', 32, 1, 1) #added 101 to age to keep relative ages
  brutus = User('brutus@rome.com', 'etmoibrute11', 'Marcus', 'Brutus', 16, 1, 1) #added 101 to age to keep relative ages
  session.add_all([caesar, cleopatra, brutus])
  session.add(forum)
  session.flush()

  #re-make users to get ids and stuff
  caesar = session.query(User).filter_by(lname="Caesar").first()
  cleopatra = session.query(User).filter_by(fname='Cleopatra').first()
  brutus = session.query(User).filter_by(lname='Brutus').first()
  first_post = Post('Veni, vidi, vici!', caesar)
  session.add(first_post)
  session.flush()
  session.commit()
  print(first_post.get_content(), first_post.get_author(), first_post.get_id())

  #re-open first_post
  first_post_temp = session.query(Post).filter_by(id=first_post.get_id()).first()
  print(first_post_temp.get_id())
  thread = forum.publish('Battle of Zela', first_post, caesar)
  session.add(thread)
  print(thread.get_posts(session))
  session.flush()
  thread.set_tags(['battle', 'brag'], caesar)

  thread.publish_post(first_post, session)

  posts = [
    Post('Hardly broke a sweat.', caesar),
    Post('I\'m Cleopatra', cleopatra)
  ]
  for post in posts:
    session.add(post)
    session.flush()  
    thread.publish_post(post, session)

  session.commit()  

  print("The contents of Caesar's posts:")
  caesar_posts = forum.search_by_author('Caesar', session)
  print(sorted([p.get_content() for p in caesar_posts]))
  print()

  existing = thread.get_posts(session)[0]
  existing.set_content('I came, I saw, I conquered!', caesar)

  existing.upvote(cleopatra)
  existing.upvote(brutus)
  existing.upvote(cleopatra)



  print("[{}](+{}) -- {}\n".format(
    existing.get_author(),
    existing.get_upvotes(),
    existing.get_content()
  ))

  # And some access control:
  try:
    thread.set_title('Hijacked!', cleopatra)
  except PermissionDenied:
    print('Cleopatra was not allowed to hijack the thread.')