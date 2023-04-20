import pygame.mixer
import pygame.time
import pygame.event
import pygame.locals
import pygame
pygame.init()

pygame.mixer.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)
playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song = 0
pygame.mixer.music.load(playlist[current_song])
while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            # check if music is playing
            if pygame.mixer.music.get_busy() == 0:
                # load and play next song in playlist
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.locals.K_SPACE:
                if pygame.mixer.music.get_busy() == 0:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.pause()
            elif event.key == pygame.locals.K_n:
                # load and play next song in playlist
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.locals.K_p:
                # load and play previous song in playlist
                current_song = (current_song - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.locals.K_s:
                pygame.mixer.music.stop()
