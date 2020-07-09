from Chord import *
from mido import Message, MidiFile, MidiTrack
import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))

root = ''
name = ''
chord_list = []
name_list = []

# 圈3进行
# C->Am->F->Dm->Bdim->G->Em->C
def Circle3(next_root, name):
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

    global root
    global chord_list
    global name_list

    root = last_root
    chord_list.append(root)
    name_list.append(name)

# 圈5进行
# C->F->Bdim->Em->Am->Dm->G->C
def Circle5(next_root, name):
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

    global root
    global chord_list
    global name_list

    root = last_root
    chord_list.append(root)
    name_list.append(name)

# 圈7进行
# C->Dm->Em->F->G->Am->Bdim->C
def Circle7(next_root, name):
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

    global root
    global chord_list
    global name_list

    root = last_root
    chord_list.append(root)
    name_list.append(name)

def chord_inversion(root):
    global root_base
    global format
    if root == 'F' or root == 'G' or root == 'A' or root == 'B':
        format = [1,2,3]
        root_base = -1

root = 'C'
name = 'maj3'

final_chord = ['C']
circle_list = []

for i in range(0,3):
    a = random.choice([3, 5, 7])
    if a == 3:
        Circle3(root, name)
        circle_list.append('圈3')
        final_chord.append(root)
    elif a == 5:
        Circle5(root, name)
        circle_list.append('圈5')
        final_chord.append(root)
    else:
        Circle7(root, name)
        circle_list.append('圈7')
        final_chord.append(root)

chord_list.reverse()
name_list.reverse()

for j in range(0,3):

    root_base = 0
    format = [0,1,2]

    chord_inversion(chord_list[j])

    add_column_chord(chord_list[j], name_list[j], format, 2, track, root_base, channel=0)
    add_column_chord(chord_list[j], name_list[j], format, 2, track, root_base, channel=0)

format = [0,1,2]
add_column_chord('C', 'maj3', format, 2, track, root_base=0, channel=0)
add_column_chord('C', 'maj3', format, 2, track, root_base=0, channel=0)

final_chord.reverse()
print (final_chord) 
circle_list.reverse()
print ("使用的圈式进行是:", circle_list)

mid.save('newSong.mid')