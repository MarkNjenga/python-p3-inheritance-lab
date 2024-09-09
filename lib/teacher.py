#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, *args, knowledge=None):
        super().__init__(*args)
        if knowledge is None:
            self.knowledge = self.__class__.knowledge
        else:
            self.knowledge = knowledge

    def teach(self):
        min_index = 0
        max_index = len(self.knowledge) - 1
        random_index = random.randint(min_index, max_index)
        return self.knowledge[random_index]