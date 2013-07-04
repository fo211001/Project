
#-*- coding: utf-8 -*-

class Song(object):

    def __init__(self, base_chord, couplets=None):
        self._couplets = couplets or []
        self._base_chord = base_chord
     
    @ property   
    def couplets (self):
        "Возвращает список из объектов Couplet"
        return self._couplets 

    @ property
    def base_chord (self):
        "Возвращает объект Chord"
        return self._base_chord
    
    #def create_couplet(self, list_couplets):
        #new_list = []
        #for i in list_couplets:
            #couplet = Couplet(i)
            #new_list.append(couplet)
        #return new_list
    
#    def read_to_couplet(self, song):
#        list_couplets = []
#        couplet = ""
#        i = 0
#        while i < len(song):
#            if song[i] == "\n" or song[i] == "\r\n":
#                couplet += song[i]
#                if i+1 < len(song):
#                    if song[i+1] == "\n" or song[i+1] == "\r\n":
#                        if not couplet == "":
#                            list_couplets.append(couplet)
#                            couplet = ""
#            else:
#                couplet += song[i]
#            i += 1
#        if not couplet == "":
#            list_couplets.append(couplet)
#        return list_couplets
#    
#    def find_base_chord(self, couplet):
#        base_chord = ""
#        first_str = ""
#        is_chords = True
#        for i in couplet:
#            if i == "\n":
#                for j in first_str:
#                    if not j in all_chords:
#                        is_chords = False
#                if is_chords:
#                    k = 0
#                    while k<len(first_str):
#                        if not first_str[k] == ' ':
#                            base_chord = first_str[k]
#                            break
#                        else:
#                            k = k + 1
#                else:
#                    is_chords = True
#                    first_str = ""
#            elif not base_chord == None:
#                break
#            else:
#                first_str += i
#        return base_chord

    
