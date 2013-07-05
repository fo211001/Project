from distance import shift_tone
from all_chords import all_chord_tones, get_modif, get_tone

modifications = {
    "": (0, 4, 7),
    "7sus2": (0, 2, 7),
    "m": (0, 3, 7),
    "7": (0, 4, 8, 11),
    "m7": (0, 3, 7, 10),
    "maj7": (0, 4, 7, 11),
    "m+7": (0, 3, 7, 11),
    "m7b5": (0, 3, 6, 10),
    "dim7": (0, 3, 6, 9),
    "sus2": (0, 2, 7),
    "sus4": (0, 5, 7),
    "7sus4": (0, 5, 7, 10),
    "sus": (0, 5, 7),
    "5": (0, 5),
    "dim": (0, 3, 6),
    "6": (0, 4, 7, 16),
    "m6": (0, 3, 7, 16),
    "9": (0, 4, 7, 10),
    "11": (0, 4, 7, 10, 14, 17),
    "13": (0, 4, 7, 10, 14, 19),
    "add9": (0, 4, 7, 21),
    "madd9": (0, 4, 7, 21)
}


def mus(chord):

    tone = get_tone(chord)
    mod = get_modif(chord)
    print [shift_tone(tone, x)
            for x in modifications[mod]]
mus("Asus2")

    #     tone = chord[0]
    #     mod = chord.modification
    #     elif mod == "6/9":
    #         tone1 = 4
    #         tone2 = 3
    #         tone3 = 4
    #         tone4 = 5
    #         mus(tone, tone1, tone2, tone3, tone4)
    #     elif mod == "m6/9":
    #         tone1 = 3
    #         tone2 = 4
    #         tone3 = 9
    #         tone4 = 14
    #         mus(tone, tone1, tone2, tone3, tone4)