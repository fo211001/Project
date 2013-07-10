#-*- coding: utf-8 -*-
from distance import semitone_distance
from itertools import product

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





