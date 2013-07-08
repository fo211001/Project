from distance import shift_tone, semitone_distance
from all_chords import get_modif, get_tone

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
    "6/9": (0, 4, 7, 11, 16),
    "m6/9": (0, 3, 7, 16, 30),
    "9": (0, 4, 7, 10),
    "11": (0, 4, 7, 10, 14, 17),
    "13": (0, 4, 7, 10, 14, 19),
    "add9": (0, 4, 7, 21),
    "madd9": (0, 4, 7, 21)
}


def mus(chord):
    mod = get_modif(chord)
    tone = get_tone(chord)
    return [shift_tone(tone, x)for x in modifications[mod]]


# def parse_modifications(chord):
#     mod = get_modif(chord)
#     tone = get_tone(chord)
#     print tone
#     temp_str = ""
#     mod_list = []
#     for i in mod:
#         if i == "/":
#             mod_list.append(temp_str)
#             temp_str = ""
#         else:
#             temp_str += i
#             if i == mod[-1]:
#                 mod_list.append(temp_str)
#     add_mod = get_tone(mod_list.pop())
#     print semitone_distance(tone, add_mod)
#     print  mod_list
