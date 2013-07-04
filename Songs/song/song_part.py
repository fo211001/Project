#-*- coding: utf-8 -*-


class SongPart(object):
    
    def __init__(self,  syllable="", chord=None):
        self._chord = chord
        self._syllable = syllable

    def __repr__(self):
        if not self.chord:
            return self.syllable
        return u"{}:{}".format(self.syllable, self.chord)
        
    @property
    def chord(self):
        return self._chord
    
    @property
    def syllable(self):
        return self._syllable

    @property
    def is_space(self):
        return not len(self.syllable)


class Space (SongPart):
    def __init__(self):
        super(Space, self).__init__(" ")

    @property
    def is_space(self):
        return True


class EndOfLine (SongPart):
    def __init__(self):
        super(EndOfLine, self).__init__("\n")

    @property
    def is_space(self):
        return True