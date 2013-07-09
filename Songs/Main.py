#-*- coding: utf-8 -*-
from song.song import Song
from song.parse import parse_text
from song.to_fingering import to_fingering
from song.filters import DistFilter, JustBarreFilter, WithoutCordsFilter,\
    AllNeedNotesFilter, WithoutBarreFilter, JustAllCordsFilter
from song.print_song import print_song


def help():
    return "read - прочитать песню из файла\n" \
           + "input - ввести песню самостоятельно\n" \
           + "addk - добавить куплет\n" \
           + "exit - выйти из программы\n"\
           + "fingering - аппликатура нот\n"


if __name__ == "__main__":
    print help()
    while True:
        command = raw_input("»")
        if command == "read":
            file = open("2.txt")
            text = file.read().decode('utf-8')
            song = parse_text(text)
            print_song(song, song.base_chord)
        elif command == "fingering":
            print "Введите ноты для получения аппликатур"
            notes = raw_input().split(" ")
            # print "Укажите какие аппликатуры необходимо вывести с учетом следующих параметров."
            # print "Если какой-либо из фильтров вам не нужен, то нажимайте Enter."
            # all_filters = ["Расстояние между струнами (число/Enter):", "Вывести только баррэ (да/Enter)",
            #                "Вывести только без баррэ (да/Enter)", "Обязательно все струны (да/Enter)",
            #                "Без струн (1 2/Enter)"]
            # need_filters = []
            # for string_filter in all_filters:
            #     print string_filter
            #     f = raw_input().split(" ")
            #     if f != None and f != "\n":
            #         need_filters.append(f)
            #     else:
            #         need_filters.append(None)
            # for i, filt in enumerate(need_filters):
            #     if filt != None:
            #         if i == 0:
            default_filt = AllNeedNotesFilter(notes)
            dist_filt = DistFilter(3)
            barre_filt = JustBarreFilter(notes)
            not_barre_filt = WithoutBarreFilter(notes)
            all_cords = JustAllCordsFilter()
            not_cords_filt = WithoutCordsFilter([0])  # указываем на единицу меньше желаемой, сейчас без 1-ой струны
            filters = [default_filt, dist_filt]
            to_fingering(notes, filters)
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