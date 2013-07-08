#-*- coding: utf-8 -*-
from all_chords import get_all_chord_tones
from distance import semitone_distance


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
        # if is_barre:
        #     count = 0
        #     for i in fingering:
        #         if i != min(*fingering) and i != 'x':
        #             count += 1
        #     if count != len(self.notes):
        #         is_barre = False
        return not is_barre


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

            # j = 0
            # temp_notes = []
            # was_adding = False
            # while j < len(notes):
            #     if notes[j] == note_from_fing:
            #         one_fingering.append(tune)
            #         was_adding = True
            #         n += 1
            #     else:
            #         temp_notes.append(notes[j])
            #     j += 1
            # if not was_adding:
            #     one_fingering.append('x')
            # notes = temp_notes
