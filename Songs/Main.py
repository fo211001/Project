#-*- coding: utf-8 -*-
from song.song import Song
from song.parse import parse_text
from song.fingering.filters import (
    DistFilter, OnlyBarreFilter, WithoutCordsFilter,
    AllNotesNeededFilter, WithoutBarreFilter, OnlyAllCordsFilter
)
from song.fingering import iterate_fingerings
from song.print_song import print_song
from song.muisicals import mus


def help():
    return """
    read - прочитать песню из файла
    input - ввести песню самостоятельно
    addk - добавить куплет
    exit - выйти из программы
    chord - аппликатуры аккорда
    """


if __name__ == "__main__":
    print help()
    while True:
        command = raw_input("»")
        if command == "read":
            file = open("1.txt")
            text = file.read().decode('utf-8')
            song = parse_text(text)
            print_song(song, song.base_chord)
        elif command == "chord":
            print "Введите аккорд"
            akkord = raw_input()
            notes = mus(akkord)
            default_filt = AllNotesNeededFilter(notes)
            dist_filt = DistFilter(3)
            barre_filt = OnlyBarreFilter(notes)
            not_barre_filt = WithoutBarreFilter(notes)
            all_cords = OnlyAllCordsFilter()
            not_cords_filt = WithoutCordsFilter([0])  # указываем на единицу меньше желаемой, сейчас без 1-ой струны
            filters = [default_filt, dist_filt, not_barre_filt]
            print "\r\n".join((",".join((unicode(z) for z in x)) for x in iterate_fingerings(notes, filters)))
        elif command == "input":
            text = raw_input("Введите песню\n")
            song = parse_text(text)
            print_song(song, song.base_chord)
        elif command == "addk":
            couplet = raw_input("Введите куплет\n")
        elif command == "help":
            print help()
        elif command == "exit":
            print("До свидания")
            exit()
        else:
            print("Такой команды нет!")