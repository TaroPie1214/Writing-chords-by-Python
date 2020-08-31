from Chord import *
from mido import Message, MidiFile, MidiTrack

def dominant(chord_list, name_list, chord_loc):
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
        'C':'Mm7',
        'D':'Mm7',
        'E':'Mm7',
        'F':'Mm7',
        'G':'Mm7',
        'A':'Mm7',
        'B':'Mm7'
        }
    new_chord = last_fifth[root_note]
    chord_list.insert(chord_loc,new_chord)
    name_list.insert(chord_loc,third_chord[new_chord])