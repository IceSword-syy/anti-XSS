#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class Scripts(object):
    '''
    Scripts class useed as a global var.
    '''

    content = []

    def __init__(self):
        pass

    def addText(self, text):
        self.text.append(text)

    def setContent(self, text):
        self.content = content

    def getContent(self):
        return self.content
