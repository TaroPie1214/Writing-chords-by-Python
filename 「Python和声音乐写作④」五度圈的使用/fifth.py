from Chord import *
from mido import Message, MidiFile, MidiTrack

def circle_of_fifth(chord_list, name_list, chord_loc):
    root_note = chord_list[chord_loc]
    last_fifth = {
        'B':'F',
        'E':'B',
        'A':'E',
        'D':'A',
        'G':'D',
        'C':'G',
        'F':'C'
        }
    third_chord = {
        'C':'maj3',
        'D':'min3',
        'E':'min3',
        'F':'maj3',
        'G':'maj3',
        'A':'min3',
        'B':'dim3'
        }
    new_chord = last_fifth[root_note]
    chord_list.insert(chord_loc,new_chord)
    name_list.insert(chord_loc,third_chord[new_chord])
