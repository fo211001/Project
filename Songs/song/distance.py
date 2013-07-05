#-*- coding: utf-8 -*-
from all_chords import get_tone, get_modif, tones_indexed


def semitone_distance(first_chord, second_chord):
    "Возвращаем число полутонов от первого до 2-го аккорда"
    return (tones_indexed[get_tone(second_chord)] - tones_indexed[get_tone(first_chord)]) % 12


def get_chord(base, chord):
    "Возвращаем название аккорда"
    t = (tones_indexed[get_tone(base)] + chord.distance) % 12
    s = tones_indexed
    for k in s.keys():
        if s[k] == t:
            return k + chord.modification
    return
    #return tones_indexed.keys()[t] + chord.modification






