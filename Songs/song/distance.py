#-*- coding: utf-8 -*-
from all_chords import get_tone, get_modif, tones_indexed, all_chord_tones


def semitone_distance(first_chord, second_chord):
    "Возвращаем число полутонов от первого до 2-го аккорда"
    return (tones_indexed[get_tone(second_chord)] - tones_indexed[get_tone(first_chord)]) % 12

def shift_tone(base_tone, distance):
    t = (tones_indexed[base_tone] + distance) % 12
    return all_chord_tones[t];

def get_chord(base, chord):
    "Возвращаем название аккорда"
    return shift_tone(get_tone(base), chord.distance) +  chord.modification






