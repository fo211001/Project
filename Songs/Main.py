#-*- coding: utf-8 -*-
from song.song import Song
from song.chord import Chord
from song.couplet import Couplet
from song.song_part import SongPart, Space, EndOfLine
from song.distance import semitone_distance, get_chord
from song.parse import parse_text
from song.to_fingering import return_fingerings_from_chords


def help():
    return "read - прочитать песню из файла\n" \
           + "input - ввести песню самостоятельно\n" \
           + "addk - добавить куплет\n" \
           + "exit - выйти из программы\n"


def print_couplet(couplet, main_chord):
    string_chords = []
    string_words = []
    lines = []
    for i, part in enumerate(couplet.song_parts):
        syl = part.syllable
        size = len(syl)
        chord = part.chord
        chord_str = ""
        if chord:
            chord_str = get_chord(main_chord, chord) + " "
        size_chord = len(chord_str)
        if size_chord > size:
            if i+1 < len(couplet.song_parts):
                next_part = couplet.song_parts[i+1]
                sep = "-" if not next_part.is_space else " "
            else:
                sep = " "
            syl += sep * (size_chord - size)
        else:
            chord_str += " " * (size - size_chord)
        string_chords.append(chord_str)
        string_words.append(syl)
        if isinstance(part, EndOfLine):
            string_chords.append("\r\n")
            lines.append("".join(string_chords + string_words))
            string_chords = []
            string_words = []
    string_chords.append("\r\n")
    lines.append("".join(string_chords + string_words))
    return "".join(lines)


def print_song(song, base_chord):
    for i in song.couplets:
        print print_couplet(i, base_chord)


if __name__ == "__main__":
    print help()
    while True:
        command = raw_input("»")
        if command == "read":
            file = open("1.txt")
            text = file.read().decode('utf-8')
            song = parse_text(text)
            print_song(song, song.base_chord)
        elif command == "fingering":
            print "Введите список имен аккордов"
            names_chords = list(raw_input())
            list_fing = return_fingerings_from_chords(names_chords)
            for fing in list_fing:
                if fing:
                    print fing
                    print ""
            #song = Song("A", [Couplet([SongPart(u"как", Chord(3, "sus7"))])])
            #couplets = song.couplets
            #part = couplets[0].song_parts
            #print part[0].chord.fingering
        elif command == "input":
            text = raw_input("Введите песню\n")
            song = Song(text)
        elif command == "addk":
            couplet = raw_input("Введите куплет\n")
        elif command == "help":
            print help()
        elif command == "exit":
            print("До свидания")
            exit()
        else:
            print("Такой команды нет!")


# def trying():
#     song = Song("A", [
#         Couplet([
#             SongPart(u"как", Chord(2, "sus7")),
#             Space(),
#             SongPart(u"кра", Chord(1, "7")),
#             SongPart(u"си", Chord(8, "m")),
#             SongPart(u"во", Chord(5, "9")),
#             SongPart(chord=Chord(2, "+7")),
#             EndOfLine(),
#             SongPart(u"бла", Chord(3, "m+7")),
#             SongPart(u"го", Chord(8, "#5")),
#             SongPart(syllable=u"род"),
#             SongPart(u"но", Chord(4, "7"))
#         ])
#     ])
#     print "Введите аккорд"
#     chord = raw_input()
#     print_song(song, chord)