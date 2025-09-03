from post import Post
import random
from random import choice

class ReplyBot():

    f'''
    So, to use the bot you need to initialise it with a name and a keyword. Name dictates what text file is used
    to generate text via markov chains. a bot called 'senator' will use senator.txt, etc. Keyword iw what the bot
    will check for in posts to see if it should respond. just run bot.do_stuff(thread object, post object) to auto
    do stuff everything including checking a post, generating content for the post, and posting the response in
    the thread.
    '''
    
    def __init__(self, name, keyword):
        self.name=name
        self.keyword=keyword.lower()
        self.path = f'markov/{name}.txt'
        self.markov_dict = self.make_dictionary()

    def get_name(self):
        return self.name

    def get_keyword(self):
        return self.keyword

    def get_path(self):
        return self.path

    def get_markov_dict(self):
        return self.markov_dict

    def set_name(self, name):
        self.name = name

    def set_keyword(self, keyword):
        self.keyword = keyword.lower()

    def check_post(self, post):
        if self.get_keyword() in post.get_content().lower():
            return True
        return False

    def pub_to_thread(self, content, thread):
        thread.publish_post(Post(content, self.get_name()))

    def make_dictionary(self):
        good_words = []
        with open(self.get_path(), 'r') as f:
            words = f.readlines()
            words = [i.strip('\n').split(' ') for i in words]
            for line in words:
                for word in line:
                    if word:
                        if '.' in word:
                            good_words.append(word.lower().strip('''.!?,_;:-"'''))
                            good_words.append('.')
                        else:
                            good_words.append(word.lower().strip('''!?,_:;-"'''))
        dictionary = {}
        for i, word in enumerate(good_words):
            if word not in dictionary:
                dictionary[word] = []
            if i+1 < len(good_words):
                dictionary[word].append(good_words[i+1])
        return dictionary

    def make_content(self, post):
        possible_words = set()
        for word in post.get_content():
            if word in self.get_markov_dict():
                possible_words.add(word)
        if possible_words:
            possible_words = list(possible_words)
        else:
            possible_words = list(self.get_markov_dict().keys())
        x = choice(possible_words)
        string = ''
        start = False
        cap = True
        for i in range(random.randint(3, 10)):
            while x != '.':
                if not start:
                    if cap:
                        x = x.capitalize()
                        cap = False
                    string = string + (f" {x}")
                x = x.lower()

                x = choice(self.get_markov_dict()[x])
                if start == True:
                    while x == '.':
                        x = choice(self.get_markov_dict()[x])
                    start = False
                    cap = True
            string += '.'
            x = string.split(' ')[-1].strip('.')
            start = True
        return string

    def make_reply(self, post, thread):
        content = self.make_content(post)
        self.pub_to_thread(content, thread)

    def do_stuff(self, post, thread):
        if self.check_post(poast):
            self.make_reply(self, post, thread)

