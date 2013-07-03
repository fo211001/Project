#-*- coding: utf-8 -*-

from song_part import SongPart, Space, EndOfLine
from chord import Chord
from distance import semitone_distance
from song import Song
from couplet import Couplet
from all_chords import all_chord_types, all_chords, all_chord_tones, tones_indexed, get_modif, get_tone


def parse_text(text):
    list_of_couplets_text = parse_to_couplet_text(text)
    list_of_couplets = []
    for i in list_of_couplets_text():
        list_of_string = parse_to_list_of_string(get_base_chord(text), i)

        list_of_couplets.append(Couplet(list(create_couplet(list_of_string))))
    song = Song(get_base_chord(text), list_of_couplets)
    return song


def get_base_chord(text):
    temp_str = ""
    for i in text:
        if not i == " " or not i == "\n":
            temp_str += i
        elif temp_str in all_chords:
            return get_tone(temp_str)
    return None


def parse_to_syl(word):
    listSyllables = []
    temp_str = ""
    for i in word:
        if i in "аеёиоуыэюя":
            temp_str += i
            listSyllables.append(temp_str)
            tempStr = ""
        else:
            temp_str += i
            if i == word[-1] or i == '-':
                listSyllables[-1] += temp_str
                temp_str = ""
    for j in listSyllables:
        print j
    return listSyllables


def parse_to_couplet_text(song):
    list_couplets = []
    couplet = ""
    i = 0
    while i < len(song):
       if song[i] == "\n" or song[i] == "\r\n":
           couplet += song[i]
           if i+1 < len(song):
               if song[i+1] == "\n" or song[i+1] == "\r\n":
                   if not couplet == "":
                       list_couplets.append(couplet)
                       couplet = ""
       else:
           couplet += song[i]
       i += 1
    if not couplet == "":
        list_couplets.append(couplet)
    return list_couplets


def parse_to_list_of_string(base_chord, string):
    """
    принимаем куплет в виде строки, возвращаем список списков, в которых хранятся или аккорды или слоги
    :param base_chord:
    :param string:
    """
    temp_str=""
    list_of_strings = []
    for i in string.split('\n'):
        word_list = []
        pos = 0
        for j in i:
            if not j == " " or pos == len(i)-1:
                temp_str += j
            else:
                word_list.append((temp_str, len(temp_str) - pos + 1))
            pos += 1
        #проверим - строка с аккордами?
        is_chord = True
        for word in word_list:
            if word[0] not in all_chords:
                is_chord = False
        if is_chord:
            chord_list = []
            for chords in word_list:
                chord = Chord(semitone_distance(base_chord, chords[0]), get_modif(chords[0]))
                chord_list.append((chord, chords[1]))
            list_of_strings.append(chord)
        else:
            syl_list = []
            for words in word_list:
                syl_list += parse_to_syl(words)
                syl_list += Space()
            list_of_strings.append(syl_list)
    return list_of_strings


def create_couplet(list_of_string):
    for i, string in enumerate(list_of_string):
        if chords_only(string) and i+1 < len(list_of_string):
            for part in join_chords(string, list_of_string[i+1]):
                yield part
        else:
            for part in parts_of_string(string):
                yield part


def parts_of_string(string):
    for part, pos in string:
        if isinstance(part, Chord):
            yield SongPart(chord=part)
        else:
            yield SongPart(part)


def chords_only(string):
    for chord in string:
        if not isinstance(chord[0], Chord):
            return False
    return True


def join_chords(chords, words):
    i, j = 0, 0
    while i < len(chords) and j < len(words):
        chord, word = chords[i], words[j]
        cpos, wpos, wlen = chord[1], word[1], len(word[0])
        if cpos >= wpos and cpos < wpos + wlen:
            j += 1
            i += 1
            yield SongPart(word[0], chord[0])

        elif cpos < wpos:
            i += 1
            yield SongPart("", chord[0])
        elif cpos >= wpos+wlen:
            j += 1
            yield SongPart(words[j][0])

    while i < len(chords):
        i += 1
        yield SongPart("", chords[i][0])

    while j < len(words):
        j += 1
        yield SongPart(words[j][0])


