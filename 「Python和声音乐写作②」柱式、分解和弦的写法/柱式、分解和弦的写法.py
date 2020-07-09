from mido import Message, MidiFile, MidiTrack
import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))

def get_chord_arrangement(name):
    chord_dict = {
        'maj3': [0, 4, 7, 12],  # 大三和弦 根音-大三度-纯五度
        'min3': [0, 3, 7, 12],  # 小三和弦 根音-小三度-纯五度
        'aug3': [0, 4, 8, 12],  # 增三和弦 根音-大三度-增五度
        'dim3': [0, 3, 6, 12],  # 减三和弦 根音-小三度-减五度

        'M7': [0, 4, 7, 11],  # 大七和弦 根音-大三度-纯五度-大七度
        'Mm7': [0, 4, 7, 10],  # 属七和弦 根音-大三度-纯五度-小七度
        'm7': [0, 3, 7, 10],  # 小七和弦 根音-小三度-纯五度-小七度
        'mM7': [0, 3, 7, 11],  # 小大七和弦 根音-小三度-纯五度-大七度
        'aug7': [0, 4, 8, 10],  # 增七和弦 根音-大三度-增五度-小七度
        'm7b5': [0, 3, 6, 10],  # 半减七和弦 根音- 增七和弦 根音-大三度-增五度-小七度
        'augM7': [0, 4, 8, 11],  # 增大七和弦 根音-小三度-减五度-减七度
        'dim7': [0, 3, 6, 9]  # 减减七和弦 根音-小三度-减五度-减七度
    }

    chord = chord_dict[name]

    return chord # 返回值是一个长度为4的一维数组，每一个值表示这个音符与根音相差的半音数

def add_broken_chord(root, name, format, length, track, root_base=0, channel=0):
    root_to_number={
        'C':60,
        'D':62,
        'E':64,
        'F':65,
        'G':67,
        'A':69,
        'B':71
        }
    root_note = root_to_number[root] + root_base*12
    chord = get_chord_arrangement(name)
    time = (length * 480) / len(format)
    for dis in format:
        note = root_note + chord[dis]
        track.append(Message('note_on', note=note, velocity=56, time=0, channel=channel))
        track.append(Message('note_off', note=note, velocity=56, time=round(time), channel=channel))

def add_column_chord(root, name, format, length, track, root_base=0, channel=0):
    root_to_number={
        'C':60,
        'D':62,
        'E':64,
        'F':65,
        'G':67,
        'A':69,
        'B':71
        }
    root_note = root_to_number[root] + root_base*12
    chord = get_chord_arrangement(name)
    time = length * 480
    for dis in format:
        note = root_note + chord[dis]
        track.append(Message('note_on', note=note, velocity=56, time=0, channel=channel))
    for dis in format:
        note = root_note + chord[dis]
        if dis == format[0]:
            track.append(Message('note_off', note=note, velocity=56, time=round(time), channel=channel))
        else:
            track.append(Message('note_off', note=note, velocity=56, time=0, channel=channel))
        

def chord(track):
    format = [0, 2, 3, 2]
    add_broken_chord('C', 'maj3', format, 4, track)
    add_column_chord('C', 'maj3', format, 4, track)

def chord1(track):
    format = [1,2,3]
    add_column_chord('C','maj3',format,2,track)
    add_column_chord('C','maj3',format,2,track)
    add_column_chord('A','min3',format,2,track,-1)
    add_column_chord('A','min3',format,2,track,-1)
    add_column_chord('F','maj3',format,2,track,-1)
    add_column_chord('F','maj3',format,2,track,-1)
    add_column_chord('G','maj3',format,2,track,-1)
    add_column_chord('G','maj3',format,2,track,-1)

def chord2(track):
    format=[0, 2, 3, 2]
    add_broken_chord('C','maj3',format,4,track)
    add_broken_chord('A','min3',format,4,track,-1)
    add_broken_chord('F','maj3',format,4,track,-1)
    add_broken_chord('G','maj3',format,4,track,-1)

#chord(track)
chord1(track)
#chord2(track)

mid.save('newSong.mid')
