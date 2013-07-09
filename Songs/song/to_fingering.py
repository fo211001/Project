#-*- coding: utf-8 -*-
from all_chords import get_all_chord_tones
from distance import semitone_distance
from itertools import product

# all_chord_tones = ["A", "B", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

all_fingering = [[(0, 2, 2, 2, 0, 0), (5, 5, 6, 7, 7, 5), (9, 10, 9, 7, 0, 0), (0, 10, 9, 11, 12, 0), (0, 14, 14, 14, 12, 0)],
                 [(1, 3, 3, 0, 0, 0), (0, 3, 3, 3, 1, 0), (6, 6, 7, 8, 8, 6), (10, 11, 10, 8, 0, 0), (0, 11, 10, 12, 13, 0)],
                 [(1, 4, 4, 4, 1, 0), (0, 4, 4, 4, 6, 7), (7, 7, 8, 9, 9, 7), (11, 12, 11, 9, 0, 0), (0, 12, 11, 13, 14, 0)],
                 [(0, 1, 0, 2, 3, 0), (0, 5, 5, 5, 3, 0), (0, 5, 5, 5, 7, 8), (8, 8, 9, 10, 10, 8), (0, 13, 12, 14, 0, 0)],
                 [(1, 2, 1, 3, 4, 0), (0, 6, 6, 6, 4, 0), (0, 6, 6, 6, 8, 9), (9, 9, 10, 11, 11, 9), (13, 14, 13, 11, 0, 0)],
                 [(2, 3, 2, 0, 0, 0), (0, 7, 7, 7, 5, 0), (0, 7, 7, 7, 9, 10), (10, 10, 11, 12, 12, 10), (14, 15, 14, 16, 0, 0)],
                 [(3, 4, 3, 1, 0, 0), (0, 4, 3, 5, 6, 0), (0, 8, 8, 8, 6, 0), (0, 8, 8, 8, 10, 11), (11, 11, 12, 13, 13, 11)],
                 [(0, 0, 1, 2, 2, 0), (4, 5, 4, 6, 0, 0), (0, 9, 9, 9, 7, 0), (0, 9, 9, 9, 11, 12), (12, 12, 13, 14, 14, 12)],
                 [(1, 1, 2, 3, 3, 1), (5, 6, 5, 7, 8, 0), (0, 10, 10, 10, 8, 0), (0, 10, 10, 10, 12, 13), (13, 13, 14, 15, 0, 9)],
                 [(2, 2, 3, 4, 4, 2), (6, 7, 6, 4, 0, 0), (0, 7, 6, 8, 9, 0), (0, 11, 11, 11, 9, 0), (14, 11, 11, 11, 0, 0)],
                 [(3, 3, 0, 0, 2, 3), (3, 3, 4, 5, 5, 3), (7, 8, 7, 5, 0, 0), (0, 8, 7, 9, 10, 0), (0, 12, 12, 12, 10, 0)],
                 [(0, 1, 1, 1, 3, 4), (4, 4, 5, 6, 6, 4), (8, 9, 8, 6, 0, 0), (0, 9, 8, 10, 11, 0), (0, 13, 13, 13, 11, 0)]]


def dict_with_fingering():
    chords = get_all_chord_tones()
    dict = {}
    i = 0
    while i < min(len(chords), len(all_fingering)):
        dict[chords[i]] = all_fingering[i]
        i += 1
    return dict


def return_fingerings_from_chords(names_chords):
    d = dict_with_fingering()
    fingerings = []
    for chord in names_chords:
        fingerings.append(d.get(chord))
    return fingerings

# ["E", "H", "G", "D", "A", "E"]
# all_chord_tones = ["A", "B", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def check_on_dist_between_tones(all_fingerings):
    var_fing = []
    for fing in all_fingerings:
        is_wrong = False
        i = 0
        while i < len(fing):
            j = i + 1
            while j < len(fing):
                if not (fing[i] == 'x' or fing[j] == 'x'):
                    if abs(int(fing[i]) - int(fing[j])) >= 6:
                        is_wrong = True
                j += 1
            i += 1
        if not is_wrong:
            var_fing.append(fing)
    return var_fing


def check_on_identic_fingerings(all_fingerings):
    for i, f in enumerate(all_fingerings):
        j = i + 1
        while j < len(all_fingerings):
            if not f == all_fingerings[j]:
                del all_fingerings[j]
            j += 1
    return all_fingerings


def return_need_fingerings(all_fingerings, all_notes, line_up):
    notes = all_notes
    chords = get_all_chord_tones()
    out_fingerings = []
    for fingering in all_fingerings:
        one_fingering = []
        n = 0
        notes = all_notes
        for i, tune in enumerate(fingering):
            cord = line_up[i]  # i=0 --> cord="E"
            pos_cord = chords.index(cord)  #получили 7
            d = semitone_distance(pos_cord, int(tune))
            #     pos_cord + int(tune)
            # if d >= 12:
            #     d = d - 12
            note_from_fing = chords[d]
            j = 0
            temp_notes = []
            was_adding = False
            while j < len(notes):
                if notes[j] == note_from_fing:
                    one_fingering.append(tune)
                    was_adding = True
                    n += 1
                else:
                    temp_notes.append(notes[j])
                j += 1
            if not was_adding:
                one_fingering.append('x')
            notes = temp_notes
        if not len(one_fingering) == 6:
            print "Ошибка"
        if len(all_notes) <= n:
            out_fingerings.append(one_fingering)
    # print len(out_fingerings)
    f = check_on_identic_fingerings(out_fingerings)
    # print len(f)
    print f
    fing = check_on_dist_between_tones(f)
    return fing


def create_all_notes(line_up, notes, filters):
    """Принимает строй, ноты и список из объектов фильтров"""
    list_fingerings = []
    for cord in line_up:
        fingering = []
        for note in notes:
            fingering.append(semitone_distance(cord, note))
        fingering.append('x')
        list_fingerings.append(fingering)
    for i in product(*list_fingerings):
        okay = True
        for filter in filters:
            if not filter.filter(i):
                okay = False
                break
        if okay:
            yield i


def to_fingering(notes,  filters=[], line_up=["E", "H", "G", "D", "A", "E"]):
    """Принимает ноты.
    Возвращает список из всех возможных аппликатур поданных нот"""
    all_variables_fingering = create_all_notes(line_up, notes, filters)
    for f in all_variables_fingering:
        print f
        print ""
    # print all_variables_fingering



# def finger(line_up):
#     all_fingering = create_all_notes(line_up)
#     i = 0
#     p = (["{} {}".format(x, y).lower() for x, y in product(all_fingering[0], all_fingering[0], all_fingering[0], all_fingering[0], all_fingering[0], all_fingering[0]])
#     for pri in p:
#         print pri
#         print ""

#
    # var_fing = []
    # fing_for_note = []
    # for note in notes:
    #     for note_on_line in line_up:
    #         num = semitone_distance(note_on_line, note)
    #         if num < 0:
    #             num += 12
    #         fing_for_note.append(num)
    #     var_fing.append(fing_for_note)
    #     fing_for_note = []
    #
    # i = 0
    # j = 0
    # n = len(var_fing)
    # #print var_fing
    # list_fing = []
    # fing = []
    # while j <= (len(var_fing[0])/2):
    #     l = 0
    #     for k in range(0, i):
    #             fing.append(0)
    #     while i < n and l < len(var_fing):
    #         var = var_fing[l]
    #         fing.append(var[i])
    #         i += 1
    #         l += 1
    #     for k in range(i, len(var_fing[0])):
    #         fing.append(0)
    #     n += 1
    #     j += 1
    #     i = j
    #     list_fing.append(fing)
    #     fing = []
    # print list_fing
        # while j < len(var):
        #     fing.append(var[j])
        #     j += 1


