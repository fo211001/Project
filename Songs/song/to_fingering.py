from all_chords import get_all_chord_tones

# all_chord_tones = ["A", "B", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

all_fingering = [[(0, 2, 2, 2, 0 ,0), (1, 1, 2, 3, 3, 1), (3, 4, 3, 1, 0, 0), (0, 2, 1, 3, 4, 0), (0, 3, 3, 3, 1, 0)],
                 [(1, 4, 4, 4, 1, 0), (0, 1, 1, 1, 3, 4), (1, 1, 2, 3, 3, 1), (3, 4, 3, 1, 0, 0), (0, 2, 1, 3, 4, 0)],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()],
                 [(), (), (), (), ()]
                ]


def fingering():
    chords = get_all_chord_tones()
    dict = {}
    i = 0
    while i < min (len(chords), len(all_fingering)):
        dict[chords[i]] = all_fingering[i]
        i += 1
    return dict
