#-*- coding: utf-8 -*-
from song.parse import parse_text
from song.fingering.filters import (
    DistFilter, OnlyBarreFilter, WithCordsFilter,
    AllNotesNeededFilter, WithoutBarreFilter, TunesFilter
)
from song.fingering import iterate_fingerings
from song.text import couplet_text
from song.chord import musicals

def help():
    return """
    read - прочитать песню из файла
    input - ввести песню самостоятельно
    exit - выйти из программы
    chord - аппликатуры аккорда
    """


if __name__ == "__main__":
    print help()
    while True:
        command = raw_input("»")
        if command == "read":
            f = open("1.txt")
            text = f.read().decode('utf-8')
            song = parse_text(text)
            print couplet_text(song, song.base_chord)
        elif command == "chord":
            print "Введите аккорд"
            chord = raw_input()
            notes = musicals(chord)
            default_filt = AllNotesNeededFilter(notes)
            dist_filt = DistFilter(3)
            barre_filt = OnlyBarreFilter(notes)
            not_barre_filt = WithoutBarreFilter(notes)
            cords_filt = WithCordsFilter([0, 1, 2, 3, 4, 5])  # указываем на единицу меньше желаемых
            tunes_filt = TunesFilter(2, 9)
            filters = [default_filt, dist_filt, tunes_filt]
            print "\r\n".join((",".join((unicode(z) for z in x)) for x in iterate_fingerings(notes, filters)))
        elif command == "input":
            text = raw_input("Введите песню\n")
            song = parse_text(text)
            couplet_text(song, song.base_chord)
        elif command == "help":
            print help()
        elif command == "exit":
            print("До свидания")
            exit()
        else:
            print("Такой команды нет!")