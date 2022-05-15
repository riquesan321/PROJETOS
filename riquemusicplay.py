import pygame

pygame.init()

print('⇨⇨⇨⇨⇨⇨⇨')
print('⇧ ℝ𝕀ℚ𝕌𝔼 ⇩')
print('⇧ ℙ𝕃𝔸𝕐  ⇩')
print('⇧ 𝕄𝕌𝕊𝕀ℂ ⇩')
print('⇧ 𝕍𝟙     ⇩')
print('⇦⇦⇦⇦⇦⇦⇦')
pygame.time.delay(500)
print('ESCOLHA O NUMERO DE UMA MUSICA: ')
pygame.time.delay(500)
o1 = int(input('\n[1]E OS MENINO DO URSO\n[2]ESCRAVOS DO PO\n[3]NA SELVA DA PENHA\n[4]VAI POLLY\n'))

if o1 == 1:
    pygame.mixer.music.load('e_os_menino_do_urso.mp3')
    pygame.mixer.music.play()
    x = input('DIGITE ALGO PARA PARAR...')
elif o1 == 2:
    pygame.mixer.music.load('escravos_do_po.mp3')
    pygame.mixer.music.play()
    x = input('DIGITE ALGO PARA PARAR...')
elif o1 == 3:
    pygame.mixer.music.load('na_selva_da_penha.mp3')
    pygame.mixer.music.play()
    x = input('DIGITE ALGO PARA PARAR...')
elif o1 == 4:
    pygame.mixer.music.load('vai_polly.mp3')
    pygame.mixer.music.play()
    x = input('DIGITE ALGO PARA PARAR...: ')


