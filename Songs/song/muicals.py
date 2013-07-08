#-*- coding: utf-8 -*-
from distance import shift_tone, semitone_distance
from all_chords import get_modif, get_tone, get_add_note

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
    """

    :param chord:
    """
    mod = get_modif(chord)                                  # достаем модификацию
    tone = get_tone(chord)                                  # достаем тон аккорда
    note = semitone_distance(tone, get_add_note(chord))     # достаем расстояние от основного аккорда до доп.ноты
    modifications[mod] = list(modifications[mod])           #
    modifications[mod].append(note)                         # добавляем ноту к модификации
    tuple(modifications[mod])
    return [shift_tone(tone, x) for x in modifications[mod]]


# mus("F/D")
