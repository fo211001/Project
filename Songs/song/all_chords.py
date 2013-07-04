from itertools import product

all_chord_types = ["", "m", "7", "m7", "mmaj7", "m+7", "maj7", "+7", "m7b5",
              "dim7", "0", "sus2", "7sus2", "sus4", "7sus4", "sus", "5",
              "#5", "+5", "aug", "m#5", "m+5", "maug", "b5", "-5", "dim",
              "mb5", "m-5", "mdim", "6", "m6", "6/9", "m6/9", "9", "11",
              "13", "add9", "madd9"]

all_chord_tones = ["A", "B", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

tones_indexed = { x: i for i, x in enumerate(all_chord_tones)}

all_chords = set(["{}{}".format(x, y) for x, y in product(all_chord_tones, all_chord_types)])


def get_all_chord_tones():
    return all_chord_tones


def get_tone(chord):
    if u"#" in chord:
        return chord[0, 1]
    else:
        return chord[0]


def get_modif(chord):
    if "#" in chord:
        return chord[2, -1]
    else:
        return chord[1, -1]



