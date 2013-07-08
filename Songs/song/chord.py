from to_fingering import dict_with_fingering
from distance import get_chord
from all_chords import get_tone


class Chord(object):
    def __init__(self, dist, modif="", add_note=None):
        self._distance = dist
        self._modification = modif
        self._add_note = add_note
  #      self._fingering = self.set_fingering(base_chord)

    def __repr__(self):
        return u"{}.{}".format(self.distance, self.modification)
        
    @property
    def distance(self):
        return self._distance
    
    @property
    def modification(self):
        return self._modification

    # def set_fingering(self, base_chord):
    #     d = dict_with_fingering()
    #     name_chord = get_tone(get_chord(base_chord, self))
    #     return d.get(name_chord)

    # @property
    # def fingering(self):
    #     return self._fingering

