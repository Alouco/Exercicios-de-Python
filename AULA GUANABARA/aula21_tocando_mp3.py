import pygame
pygame.init()
arquivo = 'aula21_que-isso-moreno.mp3'
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
  pygame.time.Clock()
