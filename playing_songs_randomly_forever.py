import pygame
import random

pygame.init()

#create my playlist of 3 songs
_songs = ["beep1.ogg","beep2.ogg","beep3.ogg"]
#add a flag indicating the song currently playing
_currently_playing_song = None

SONG_END = pygame.USEREVENT + 1 #higher than any userevent
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load("beep1.ogg")
pygame.mixer.music.play(0)


def play_a_different_song():
    """randomly choose a diff song
    every time SONG_END event is fired"""
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play(0)

def play_next_song():
    """play song in sequential loops"""
    global _songs, _currently_playing_song
    _songs = _songs[1:] + [_songs[0]]#move current song to bacl of list
    _currently_playing_song = _songs[0]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play(0)

while True:
    for event in pygame.event.get():
        if event.type == SONG_END:
            print "playing %s!!" %_currently_playing_song
            play_next_song()