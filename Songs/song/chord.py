class Chord(object):
    """

    """
    
    def __init__(self, dist, modif=""):
        self._distance = dist
        self._modification = modif
        
    @property
    def distance (self):
        return self._distance
    
    @property
    def modification (self):
        return self._modification

    #@classmethod(chrd_str, base)
   # def from_string(cls, str):