#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

__author__ = 'Ruslan Talipov'


from translate import translate
from youtube import youtube_search

def main(russian_question):
    for item in translate(russian_question):
        yield from youtube_search(search_query=item)

if __name__ == '__main__':
    f = open('out.json', 'w')
    json.dump([result for result in main('Как сделать красиво?')], f)
    f.close()
