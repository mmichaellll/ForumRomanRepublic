from post import Post
import random
from random import choice

class ReplyBot():
    def __init__(self, name, keyword):
        self.name=name
        self.keyword=keyword.lower()
        self.path = f'/markov text stuffs <33/{name}'
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
            if word in get_markov_dict():
                possible_words.add(word)
        if possible_words:
            possible_words = list(possible_words)
            #pick a random word to start markov chain
    
