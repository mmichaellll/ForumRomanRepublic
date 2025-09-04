import unittest
from forum import Forum
from user import User
from thread import Thread
from post import Post

class TestCode(unittest.TestCase):

    def setUp(self):
        self.forum = Forum('Testing land test forum')
        self.user = User('email@gmail.com', 'abc123', 'Bob', 'Smith', 1999, 7, 23)
        self.thread = Thread('New Thread with stuff', Post('hi there!', self.user))

    def testPublishing(self):
        published = self.forum.publish('New Thread with stuff', 'hi there!', self.user)
        self.assertEqual(published, self.thread, 'The forum thread is not correct')

if __name__ == '__main__':
    unittest.main()