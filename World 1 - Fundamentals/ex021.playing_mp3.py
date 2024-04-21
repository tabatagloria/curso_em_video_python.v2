# Write a Python program that opens and plays audio from an MP3 file:

import pygame #It need to install the library

pygame.init() #start the function
pygame.mixer.music.load("c:/Users/Admin/OneDrive/Área de Trabalho/python - curso em vídeo/Mundo 1 - Fundamentos/prologue.mp3") 
pygame.mixer.music.play() #start the audio
pygame.event.wait()

