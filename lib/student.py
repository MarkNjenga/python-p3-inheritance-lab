#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    def __init__(self, *args, knowledge=None):
        super().__init__(*args)
        if knowledge is None:
            self.knowledge = self.__class__.knowledge
        else:
            self.knowledge = knowledge

    def learn(self, string):
      self.knowledge.append(string)