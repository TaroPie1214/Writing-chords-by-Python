from Chord import *
from chord_inversion import *
from mido import Message, MidiFile, MidiTrack
import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))

# 圈3进行
# C->Am->F->Dm->Bdim->G->Em->C
def Circle3(next_root, name, chord_list, name_list):
    if next_root == 'C':
        last_root = 'E'
        name = 'min3'
    elif next_root == 'E':
        last_root = 'G'
        name = 'maj3'
    elif next_root == 'G':
        last_root = 'B'
        name = 'dim3'
    elif next_root == 'B':
        last_root = 'D'
        name = 'min3'
    elif next_root == 'D':
        last_root = 'F'
        name = 'maj3'
    elif next_root == 'F':
        last_root = 'A'
        name = 'min3'
    elif next_root == 'A':
        last_root = 'C'
        name = 'maj3'

    chord_list.append(last_root)
    name_list.append(name)
    return last_root

# 圈5进行
# C->F->Bdim->Em->Am->Dm->G->C
def Circle5(next_root, name, chord_list, name_list):
    if next_root == 'C':
        last_root = 'G'
        name = 'maj3'
    elif next_root == 'G':
        last_root = 'D'
        name = 'min3'
    elif next_root == 'D':
        last_root = 'A'
        name = 'min3'
    elif next_root == 'A':
        last_root = 'E'
        name = 'min3'
    elif next_root == 'E':
        last_root = 'B'
        name = 'dim3'
    elif next_root == 'B':
        last_root = 'F'
        name = 'maj3'
    elif next_root == 'F':
        last_root = 'C'
        name = 'maj3'

    chord_list.append(last_root)
    name_list.append(name)
    return last_root

# 圈7进行
# C->Dm->Em->F->G->Am->Bdim->C
def Circle7(next_root, name, chord_list, name_list):
    if next_root == 'C':
        last_root = 'B'
        name = 'dim3'
    elif next_root == 'B':
        last_root = 'A'
        name = 'min3'
    elif next_root == 'A':
        last_root = 'G'
        name = 'maj3'
    elif next_root == 'G':
        last_root = 'F'
        name = 'maj3'
    elif next_root == 'F':
        last_root = 'E'
        name = 'min3'
    elif next_root == 'E':
        last_root = 'D'
        name = 'min3'
    elif next_root == 'D':
        last_root = 'C'
        name = 'maj3'

    chord_list.append(last_root)
    name_list.append(name)
    return last_root