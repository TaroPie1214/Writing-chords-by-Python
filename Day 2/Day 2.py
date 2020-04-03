from mido import Message, MidiFile, MidiTrack
import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))

def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
    bpm = 75
    meta_time = 60 * 60 * 10 / bpm
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    track.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
    track.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

#0.5=八分音符

#random.ranint(1,10)
my_list = [0.5, 1, 1.5]
#print(random.choice(my_list))

for v in range(1,100):
    play_note(random.randint(1,7), random.choice(my_list), track)

mid.save('newSong.mid')