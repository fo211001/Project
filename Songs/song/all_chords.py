#-*- coding: utf-8 -*-
from itertools import product

all_chord_types = ["", "m", "7", "m7", "m+7", "maj7", "+7", "m7b5",
                   "dim7", "sus2", "7sus2", "sus4", "7sus4", "sus",
                   "5", "6", "m6", "6/9", "m6/9", "9", "11", "13",
                   "add9", "madd9"]

all_chord_tones = ["A", "B", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

sin_chord_tones = ["Ab", "Bb", "Hb", "Cb", "Db", "Eb", "Fb", "Gb", "A#", "B#", "H#", "E#"]

all_chords = set(["{}{}".format(x, y).lower() for x, y in product(all_chord_tones, all_chord_types)])

all_sin = set(["{}{}".format(x, y).lower() for x, y in product(sin_chord_tones, all_chord_types)])

tones_indexed = {x: i for i, x in enumerate(all_chord_tones)}

sin_tones = {"Ab": 11, "Bb": 0, "Hb": 1, "Cb": 2, "Db": 4, "Eb": 6, "Fb": 7, "Gb": 9,
             "A#": 1, "B#": 2, "H#": 3, "E#": 8}


def is_chord(chord_string):
    return chord_string in all_chords or chord_string in all_sin


def normal_view(chord_string):
    if chord_string.lower() in all_chords:
        return chord_string
    else:
        converted_tone = all_chord_tones[sin_tones[get_tone(chord_string)]]
        return converted_tone + get_modif(chord_string)

def get_all_chord_tones():
    return all_chord_tones

def get_tone(chord):
    if u"#" in chord or u"b" in chord:
        return chord[: 2]
    else:
        return chord[0]


def get_modif(chord):
    if u"#" in chord or u"b" in chord:
        return chord[2:]
    else:
        return chord[1:]




