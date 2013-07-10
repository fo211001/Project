#-*- coding: utf-8 -*-
from song.parse import parse_text
from song.fingering import iterate_fingerings
from Songs.song.fingering.filters import DistFilter, JustBarreFilter, WithoutCordsFilter,\
    AllNeedNotesFilter, WithoutBarreFilter, JustAllCordsFilter
from song.print_song import print_song
from song.muisicals import mus


def help():
    return "read - прочитать песню из файла\n" \
           + "input - ввести песню самостоятельно\n" \
           + "addk - добавить куплет\n" \
           + "exit - выйти из программы\n"\
           + "chord - аппликатуры аккорда"


if __name__ == "__main__":
    print help()
    while True:
        command = raw_input("»")
        if command == "read":
            file = open("1.txt")
            text = file.read().decode('utf-8')
            song = parse_text(text)
            print print_song(song, song.base_chord)
        elif command == "chord":
            print "Введите аккорд"
            akkord = raw_input()
            notes = mus(akkord)
            default_filt = AllNeedNotesFilter(notes)
            dist_filt = DistFilter(3)
            barre_filt = JustBarreFilter(notes)
            not_barre_filt = WithoutBarreFilter(notes)
            all_cords = JustAllCordsFilter()
            not_cords_filt = WithoutCordsFilter([0])  # указываем на единицу меньше желаемой, сейчас без 1-ой струны
            filters = [default_filt, dist_filt, barre_filt]
            fingerings = iterate_fingerings(notes, filters)
            for fingering in fingerings:
                print fingering
                print ""
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