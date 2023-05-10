import os
import shutil
import glob
import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Configurações de backup
diretorio_origem = '/home/usuario/pasta_origem'
diretorio_destino = '/home/usuario/pasta_destino'
extensoes_arquivos = ['*.txt', '*.jpg']

# Fazer backup de arquivos
for extensao in extensoes_arquivos:
    for arquivo in glob.glob(os.path.join(diretorio_origem, extensao)):
        shutil.copy2(arquivo, diretorio_destino)

# Limpar pasta de arquivos temporários
pasta_temporaria = '/home/usuario/pasta_temporaria'
for arquivo in os.listdir(pasta_temporaria):
    caminho_arquivo = os.path.join(pasta_temporaria, arquivo)
    if os.path.isfile(caminho_arquivo):
        os.unlink(caminho_arquivo)

# Atualizar planilhas
planilha = openpyxl.load_workbook('minha_planilha.xlsx')
planilha_ativa = planilha.active
planilha_ativa['A1'] = 'Novo valor'
planilha.save('minha_planilha.xlsx')

# Enviar email automático
de_email = 'meu_email@gmail.com'
senha_email = 'minha_senha'
para_email = 'destinatario@email.com'
mensagem = MIMEMultipart()
mensagem['From'] = de_email
mensagem['To'] = para_email
mensagem['Subject'] = 'Assunto do email'
mensagem_texto = 'Olá, isso é um email automático!'
mensagem.attach(MIMEText(mensagem_texto, 'plain'))
with open('minha_planilha.xlsx', 'rb') as arquivo_anexo:
    anexo = MIMEApplication(arquivo_anexo.read(), _subtype='xlsx')
    anexo.add_header('content-disposition', 'attachment', filename='minha_planilha.xlsx')
    mensagem.attach(anexo)
servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
servidor_smtp.starttls()
servidor_smtp.login(de_email, senha_email)
texto_email = mensagem.as_string()
servidor_smtp.sendmail(de_email, para_email, texto_email)
servidor_smtp.quit()
