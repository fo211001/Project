#-*- coding: utf-8 -*-
from song_part import EndOfLine
from distance import get_chord


def print_couplet(couplet, main_chord):
    string_chords = []
    string_words = []
    lines = []
    for i, part in enumerate(couplet.song_parts):
        syl = part.syllable
        chord = part.chord
        chord_str = ""
        if chord:
            next_part = couplet.song_parts[i+1]
            if next_part.chord:
                chord_str = get_chord(main_chord, chord) + " "
            else:
                chord_str = get_chord(main_chord, chord)
        if len(chord_str) > len(syl):
            if i+1 < len(couplet.song_parts):
                if syl == '':
                    sep = " "
                else:
                    next_part = couplet.song_parts[i+1]
                    sep = "-" if not next_part.is_space else " "
            else:
                sep = ""
            syl += sep * (len(chord_str) - len(syl))
        else:
            chord_str += " " * (len(syl) - len(chord_str))
        string_chords.append(chord_str)
        string_words.append(syl)
        if isinstance(part, EndOfLine):
            usl = False
            for c in string_chords:
                if c != '' and c != ' ' and c != '  ' and c != '   ' and c != '    ' and c != '     ' and c != '      ':
                    usl = True
            # [' '], [' ', '\r\n'], ['   ', '    ', ' ', '\r\n'], [' ', ' ', '   ', ' ', '  ', ' ', '  ', '     ', ' ', '\r\n'], [' ', '\r\n'], ['  ', '  ', '   ', ' ', '  ', ' ', '  ', '  ', ' ', '\r\n']
            if usl:
                string_chords.append("\r\n")
            else:
                string_chords = ["\r"]
            lines.append("".join(string_chords + string_words))
            string_chords = []
            string_words = []
    return "".join(lines)


def print_song(song, base_chord):
    for i in song.couplets:
        p = print_couplet(i, base_chord)
        print p,