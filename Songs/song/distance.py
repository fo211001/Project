from all_chords import get_tone, get_modif, tones_indexed


def semitone_distance(first_chord, second_chord):
    "Возвращаем число полутонов от первого до 2-го аккорда"
    return (tones_indexed[get_tone(second_chord)] - tones_indexed[get_tone(first_chord)]) % 12


def get_chord(base, dist):
    t = (tones_indexed[get_tone(base)] + dist) % 12
    return tones_indexed.keys()[t]






