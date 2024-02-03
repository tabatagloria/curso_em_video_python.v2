# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3:
import pygame #necessário instalar a biblioteca

pygame.init() #inicia a função
pygame.mixer.music.load("c:/Users/Admin/OneDrive/Área de Trabalho/python - curso em vídeo/Mundo 1 - Fundamentos/prologue.mp3") 
pygame.mixer.music.play() #inicia o audio
pygame.event.wait()

