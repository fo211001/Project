class Chord(object):
    def __init__(self, dist, modif=""):
        self._distance = dist
        self._modification = modif
        
    @property
    def distance(self):
        return self._distance
    
    @property
    def modification(self):
        return self._modification

    def set_fingering(self, fingering):
        self._fingering = fingering

    @property
    def fingering(self):
        return self._fingering
