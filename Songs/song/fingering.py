
class Fingering(object):
    def __init__(self, chords, fingering):
        for i, chord in enumerate(chords):
            self.chord_str[i] = chord
        for j, finger in enumerate(fingering):
            self.fingering[j] = finger

    def set_from_chord_to_finger(self, chord, finger):
        self.chord_str = chord
