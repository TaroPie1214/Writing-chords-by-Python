from Chord import *
from chord_inversion import *
from Circle import *
from fifth import *
from mido import Message, MidiFile, MidiTrack
import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))

next_root = 'C'
name = 'maj3'
chord_list = ['C']
name_list = ['maj3']
circle_list = []

i = 1
while i:
    for i in range(0,3):
        a = random.choice([3, 5, 7])
        if a == 3:
            next_root = Circle3(next_root, name, chord_list, name_list)
            circle_list.append('圈3')
        elif a == 5:
            next_root = Circle5(next_root, name, chord_list, name_list)
            circle_list.append('圈5')
        else:
            next_root = Circle7(next_root, name, chord_list, name_list)
            circle_list.append('圈7')

    chord_list.reverse()
    name_list.reverse()
    circle_list.reverse()
    print ('使用的和弦进行是:\n', chord_list) 
    print ('用到的圈式进行是:\n', circle_list)

    judge = int(input('是否需要重新进行随机？输入1为是，0为否:\n'))
    if judge == 0:
        break
    else:
        next_root = 'C'
        name = 'maj3'
        chord_list = ['C']
        name_list = ['maj3']
        circle_list = []

i=1
j=0
while i:
    judge = int(input('是否需要应用五度圈？输入1为是，0为否:\n'))
    if judge == 0:
        break
    if j == 0:
        corresponding_time = [4,4,4,4]
        j += 1
    chord_loc = int(input('想在哪一个和弦的后面应用五度圈:\n'))
    circle_of_fifth(chord_list, name_list, chord_loc)
    original_time = corresponding_time.pop(chord_loc - 1)
    corresponding_time.insert(chord_loc - 1, 1)
    corresponding_time.insert(chord_loc - 1, original_time - 1)
    print ("新的和弦进行是:\n", chord_list)
    print ("对应的时值是:\n", corresponding_time)

for j in range(0,len(chord_list)):

    root_base = 0
    format = [0,1,2]

    format, root_base = chord_inversion(chord_list[j])

    for k in range(0,corresponding_time[j]):
        add_column_chord(chord_list[j], name_list[j], format, 1, track, root_base, channel=0)

mid.save('newSong.mid')
