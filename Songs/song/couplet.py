from itertools import product

class Couplet(object):
    _song_parts = []
    def __init__(self, *args):
        self._song_parts = list(*args)

    @property
    def song_parts(self):
        "SongPart"
        return self._song_parts

    def parse_to_song_parts(self, couplet):
        pass
        #song_part = []
        #part = ""
        #is_chord = True
        #list_words = []
        #list_chord = []
        
        #for i in couplet.split('\n'):
            #for j in i.split():
                #if j not in all_chords:
                    #is_chord = False
            #if is_chord:
                #list_chord += i.split()
            #else:
                #list_words += i.split()
                    
                    
        
        
        #string = ""
        #list_string = []
        #for i in couplet:
            #if i == "\r\n" or i == "\n\r":
                #list_string.append(String(string))
                #string = ""
            #else:
               # string += i
        #return list_string


