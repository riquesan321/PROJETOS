from PIL import Image, ImageEnhance, ImageFilter

# abrir a imagem
imagem = Image.open('minha_imagem.jpg')

# redimensionar a imagem
nova_imagem = imagem.resize((800, 600))

# cortar a imagem
area = (100, 100, 500, 400)
corte = nova_imagem.crop(area)

# girar a imagem
nova_imagem = corte.rotate(45)

# aumentar o contraste
contraste = ImageEnhance.Contrast(nova_imagem)
nova_imagem = contraste.enhance(2.0)

# aumentar o brilho
brilho = ImageEnhance.Brightness(nova_imagem)
nova_imagem = brilho.enhance(1.5)

# aplicar um filtro na imagem
nova_imagem = nova_imagem.filter(ImageFilter.GaussianBlur(radius=10))

# aumentar o zoom
zoom = 2
largura, altura = nova_imagem.size
nova_largura = largura * zoom
nova_altura = altura * zoom
nova_imagem = nova_imagem.resize((nova_largura, nova_altura))

# salvar a nova imagem
nova_imagem.save('minha_imagem_processada.jpg')
