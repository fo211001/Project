#-*- coding: utf-8 -*-
from Songs.song.all_chords import semitone_distance
from itertools import product


def iterate_fingerings(notes,  filters=None, line_up=["E", "H", "G", "D", "A", "E"]):
    """Принимает строй, ноты и список из объектов фильтров.
    Возвращает аппликатуру, если она прошла все фильтры"""
    filters = filters or []
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
