#-*- coding: utf-8 -*-
from all_chords import get_tone, shift_tone


def get_chord(base, chord):
    "Возвращаем название аккорда"
    try:
        tone = shift_tone(get_tone(base), chord.distance)
        if chord.add_tone:
            return tone + chord.modification + "/" + shift_tone(tone, chord.add_tone)
        else:
            return tone + chord.modification
    except AttributeError as error:
        print "Broken on {}\n{}".format(chord, base)






