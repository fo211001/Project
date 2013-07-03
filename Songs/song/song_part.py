#-*- coding: utf-8 -*-

class SongPart(object):
    
    def __init__(self,  syllable="", chord=None):
        self._chord = chord
        self._syllable = syllable
        
    @property
    def chord (self):
        return self._chord
    
    @property
    def syllable (self):
        return self._syllable
    
class Space (SongPart):
    def __init__(self):
        super(Space, self).__init__(" ")
        
class EndOfLine (SongPart):
    def __init__(self):
        super(EndOfLine, self).__init__("\n")