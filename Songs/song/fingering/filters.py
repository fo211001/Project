#-*- coding: utf-8 -*-
from Songs.song.all_chords import get_all_chord_tones


class AppFilter(object):

    def filter(self, fingering):
        pass


class DistFilter(AppFilter):
    max_dist = None

    def __init__(self, dist):
        self.max_dist = dist

    def filter(self, fingering):
        is_good = True
        for i, c in enumerate(fingering):
            for j in xrange(i+1, len(fingering)):
                if not (c == 'x' or fingering[j] == 'x'):
                    if abs(int(c) - int(fingering[j])) > self.max_dist:
                        is_good = False
        return is_good


class JustBarreFilter(AppFilter):
    notes = []

    def __init__(self, notes):
        self.notes = notes

    def filter(self, fingering):
        is_barre = False
        probably_indexes_barre = []
        for i, c in enumerate(fingering):
            for j in xrange(i+1, len(fingering)):
                if c == fingering[j]:
                    probably_indexes_barre.append(c)
        for index_barre in probably_indexes_barre:
            if index_barre == min(*fingering):
                is_barre = True
        if is_barre:
            count = 0
            for i in fingering:
                if i != min(*fingering) and i != 'x':
                    count += 1
            if count != len(self.notes):
                is_barre = False
        return is_barre


class WithoutBarreFilter(AppFilter):
    notes = []

    def __init__(self, notes):
        self.notes = notes

    def filter(self, fingering):
        is_barre = False
        probably_indexes_barre = []
        for i, c in enumerate(fingering):
            for j in xrange(i+1, len(fingering)):
                if c == fingering[j]:
                    probably_indexes_barre.append(c)
        for index_barre in probably_indexes_barre:
            if index_barre == min(*fingering):
                is_barre = True
        if is_barre:
            count = 0
            for i in fingering:
                if i != min(*fingering) and i != 'x':
                    count += 1
            if count != len(self.notes):
                is_barre = False
        if not is_barre:
            b = self.counter_of_fingers(fingering)
            return b
        else:
            return False

    def counter_of_fingers(self, fingering):
        count = 0
        for chord in fingering:
            if chord != 'x':
                count += 1
        if count < 5:
            return True
        else:
            return False


class JustAllCordsFilter(AppFilter):

    def filter(self, fingering):
        for chord in fingering:
            if chord == 'x':
                return False
        return True


class WithoutCordsFilter(AppFilter):
    without_cords = []

    def __init__(self, cords):
        self.without_cords = cords

    def filter(self, fingering):
        is_good = True
        for i, chord in enumerate(fingering):
            if i in self.without_cords:
                if not chord == 'x':
                    is_good = False
        return is_good


class AllNeedNotesFilter(AppFilter):
    line_up = ["E", "H", "G", "D", "A", "E"]
    notes = None

    def __init__(self, notes):
        self.notes = notes

    def filter(self, fingering):
        notes_from_fing = []
        chords = get_all_chord_tones()
        for i, tune in enumerate(fingering):
            cord = self.line_up[i]  # i=0 --> cord="E"
            pos_cord = chords.index(cord)  # получили 7
            if tune != 'x':
                d = pos_cord + int(tune)
                if d >= 12:
                    d -= 12
                notes_from_fing.append(chords[d])
            else:
                notes_from_fing.append(tune)
        for note in self.notes:
            if notes_from_fing.count(note) == 0:
                return False
        return True
