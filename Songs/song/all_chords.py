#-*- coding: utf-8 -*-

from itertools import product

all_chord_types = ["", "m", "7", "m7", "m+7", "maj7", "+7", "m7b5",
                   "dim7", "sus2", "7sus2", "sus4", "7sus4", "sus",
                   "5", "6", "m6", "6/9", "m6/9", "9", "11", "13",
                   "add9", "madd9"]



all_types_with_add_note = ["{}{}".format(x, y).lower() for x, y in product(all_chord_types, all_chord_types)]

all_chord_tones = ["A", "B", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

all_chords = set([u"{}{}".format(x, y).lower() for x, y in product(all_chord_tones, all_chord_types)])

tones_indexed = {x: i for i, x in enumerate(all_chord_tones)}

sin_tones = {"Ab": 11, "Bb": 0, "Hb": 1, "Cb": 2, "Db": 4, "Eb": 6, "Fb": 7, "Gb": 9,
             "A#": 1, "B#": 2, "H#": 3, "E#": 8}

sin_chord_tones = sin_tones.keys()

all_sin = set(["{}{}".format(x, y).lower() for x, y in product(sin_chord_tones, all_chord_types)])


def is_chord(chord_string):
    chord_and_add_note = chord_string.split("/")
    if len(chord_and_add_note) > 1:
        if len(chord_and_add_note) > 2:
            return False
        add_tone = chord_and_add_note[1]
        if add_tone not in map(lambda x: x.lower(), all_chord_tones) and add_tone not in map(lambda x: x.lower(), all_chord_tones) and add_tone != "9":
            return False
    return chord_and_add_note[0] in all_chords or chord_and_add_note[0] in all_sin


def normal_view(chord_string):
    if chord_string.lower() in all_chords:
        return chord_string
    else:
        converted_tone = all_chord_tones[sin_tones[get_tone(chord_string)]]
        return converted_tone + get_modif(chord_string)

def get_all_chord_tones():
    return all_chord_tones

def get_tone(chord):
    return parse_chord(chord)[0]


def get_modif(chord):
    return parse_chord(chord)[1]

def get_add_note(chord):
    return parse_chord(chord)[2]


def parse_chord(chord):
    """
    :param chord: Принимаем строку, которая является аккордом
    :return: Тьюпл, 1-й элемент - тон аккорда, 2-й - модификация, 3-й - дополнительная нота
    """
    tone, mod, add = None, None, None
    parts = chord.split("/")
    if len(parts) > 1:
        if parts[1] != "9":
            add = parts[1]
            chord = parts[0]

    if len(chord) > 1 and chord[1] in "#b":
        tone = chord[:2]
        mod = chord[2:]
    else:
        tone = chord[:1]
        mod = chord[1:]

    return tone, mod, add
