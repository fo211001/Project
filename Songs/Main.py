#-*- coding: utf-8 -*-
from song.song import Song
from song.chord import Chord
from song.couplet import Couplet
from song.song_part import SongPart

def help():
    return "read - прочитать песню из файла\n" \
           + "input - ввести песню самостоятельно\n" \
           + "addk - добавить куплет\n" \
           + "exit - выйти из программы\n"

if __name__ == "__main__":
    print ">>"
    song = Song ("A", [
        Couplet(
            SongPart("qwe", Chord(1, "7"))
        )
    ])
    
#    print help()
#    while True:
#        command = raw_input("»")
#        if command == "read":
#            file_name = raw_input("Введите имя файла:")
#            file = open (file_name)
#            text = file.read()
#            song = Song(text)
#            print song.get_base_chord()
#            for i in song.get_couplets():
#                print "---------------------------"
#                print i
#        elif command == "input":
#            text = raw_input("Введите песню\n")
#            song = Song(text)
#        elif command == "addk":
#            couplet = raw_input("Введите куплет\n")
#        elif command == "help":
#            print help()
#        elif command == "exit":
#            print("До свидания")
#            exit()
#        else:
#            print("Такой команды нет!")