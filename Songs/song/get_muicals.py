from all_chords import all_chord_tones


def get_musicals(chord):
    """


    """
    tone = chord[0]
    mod = chord.modification
    if mod == "":
        tone1 = 4
        tone2 = 3
        mus(tone, tone1, tone2)
    elif mod == "m":
        tone1 = 3
        tone2 = 4
        tone3 = 0
        mus(tone, tone1, tone2, tone3)
    elif mod == "7":
        tone1 = 4
        tone2 = 4
        tone3 = 3
        mus(tone, tone1, tone2, tone3)
    elif mod == "m7":
        tone1 = 3
        tone2 = 4
        tone3 = 3
        mus(tone, tone1, tone2, tone3)
    elif mod == "maj7":
        tone1 = 4
        tone2 = 3
        tone3 = 4
        mus(tone, tone1, tone2, tone3)
    elif mod == "m+7":
        tone1 = 3
        tone2 = 4
        tone3 = 4
        mus(tone, tone1, tone2, tone3)
    elif mod == "+7":
        tone1 = 3
        tone2 = 4
        tone3 = 4
        mus(tone, tone1, tone2, tone3)
    elif mod == "m7b5":
        tone1 = 3
        tone2 = 3
        tone3 = 4
        mus(tone, tone1, tone2, tone3)
    elif mod == "dim7":
        tone1 = 3
        tone2 = 3
        tone3 = 3
        mus(tone, tone1, tone2, tone3)
    elif mod == "sus2":
        tone1 = 2
        tone2 = 5
        mus(tone, tone1, tone2)
    elif mod == "7sus2":
        tone1 = 2
        tone2 = 3
        mus(tone, tone1, tone2)
    elif mod == "sus4":
        tone1 = 5
        tone2 = 2
        mus(tone, tone1, tone2)
    elif mod == "7sus4":
        tone1 = 5
        tone2 = 2
        tone3 = 3
        mus(tone, tone1, tone2, tone3)
    elif mod == "sus":
        tone1 = 5
        tone2 = 2
        mus(tone, tone1, tone2)
    elif mod == "5":
        tone1 = 5
        mus(tone, tone1)
    elif mod == "dim":
        tone1 = 3
        tone2 = 3
        mus(tone, tone1, tone2)
    elif mod == "6":
        tone1 = 4
        tone2 = 3
        tone3 = 9
        mus(tone, tone1, tone2, tone3)
    elif mod == "m6":
        tone1 = 3
        tone2 = 4
        tone3 = 9
    elif mod == "6/9":
        tone1 = 4
        tone2 = 3
        tone3 = 4
        tone4 = 5
        mus(tone, tone1, tone2, tone3, tone4)
    elif mod == "m6/9":
        tone1 = 3
        tone2 = 4
        tone3 = 9
        tone4 = 14
        mus(tone, tone1, tone2, tone3, tone4)
    elif mod == "9":
        tone1 = 4
        tone2 = 3
        tone3 = 3
        tone4 = 4
        mus(tone, tone1, tone2, tone3, tone4)
    elif mod == "11":
        tone1 = 4
        tone2 = 3
        tone3 = 3
        tone4 = 4
        tone5 = 3
        mus(tone, tone1, tone2, tone3, tone4, tone5)
    elif mod == "13":
        tone1 = 4
        tone2 = 3
        tone3 = 3
        tone4 = 4
        tone5 = 5
        mus(tone, tone1, tone2, tone3, tone4, tone5)
    elif mod == "add9":
        tone1 = 4
        tone2 = 3
        tone3 = 14
        mus(tone, tone1, tone2, tone3)
    elif mod == "madd9":
        tone1 = 4
        tone2 = 3
        tone3 = 14
        mus(tone, tone1, tone2, tone3)



def prov(tone, t1, t2, t3=None, t4=None, t5=None):
    if t1 > 12:
        t1 = t1 - 12
    if t2 > 12:
        t2 = t2 -12
    if t3 > 12:
        t3 = t3 - 12
    if t4 > 12:
        t4 = t4 -12
    if t5 > 12:
        t5 = t5 -12

def mus(tone, tone1, tone2=None, tone3=None, tone4=None, tone5=None):
    t1 = tone + tone1
    t2 = t1 + tone2
    t3 = t2 + tone3
    t4 = t3 + tone4
    t5 = t4 + tone5
    prov(tone, t1, t2, t3, t4, t5)
    if tone2 == None:
        musicals = list[tone, all_chord_tones[t1]]
    elif tone3 == None:
        musicals = list[tone, all_chord_tones[t1], all_chord_tones[t2]]
    elif tone4 == None:
        musicals = list[tone, all_chord_tones[t1], all_chord_tones[t2], all_chord_tones[t3]]
    elif tone5 == None:
        musicals = list[tone, all_chord_tones[t1], all_chord_tones[t2], all_chord_tones[t3], all_chord_tones[t4]]
    else:
        musicals = list[tone, all_chord_tones[t1], all_chord_tones[t2], all_chord_tones[t3], all_chord_tones[t4], all_chord_tones[t5]]
    print musicals