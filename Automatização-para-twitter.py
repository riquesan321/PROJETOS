import tweepy
import time

# Configurações de autenticação do Twitter
consumer_key = "sua_consumer_key"
consumer_secret = "seu_consumer_secret"
access_token = "seu_access_token"
access_token_secret = "seu_access_token_secret"

# Configurações de automação
mensagens = ["Olá, mundo!", "Estou testando um script de automação para o Twitter!"]
hashtags = ["#python", "#automacao", "#twitter"]
usuarios = ["usuario1", "usuario2", "usuario3"]
palavras_chave = ["automacao", "python"]

# Autenticação no Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Criação de objeto API do Twitter
api = tweepy.API(auth)

# Postar mensagens
for mensagem in mensagens:
    api.update_status(mensagem)
    time.sleep(10)

# Seguir usuários
for usuario in usuarios:
    api.create_friendship(usuario)

# Curtir e comentar postagens
for palavra_chave in palavras_chave:
    resultados = api.search(q=palavra_chave, count=10)
    for resultado in resultados:
        try:
            api.create_favorite(resultado.id)
            api.update_status("Adorei esse post! #twitter")
            time.sleep(5)
        except tweepy.TweepError as error:
            print(f"Erro ao curtir ou comentar: {error}")
