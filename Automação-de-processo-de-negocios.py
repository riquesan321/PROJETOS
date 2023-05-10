import pyautogui
import time

# Configurações de automação
posicao_botoes = [(100, 200), (300, 200), (500, 200)]
dados_clientes = [('Cliente 1', 'Endereço 1'), ('Cliente 2', 'Endereço 2'), ('Cliente 3', 'Endereço 3')]

# Abrir sistema de processamento de pedidos
pyautogui.press('win')
pyautogui.write('nome_do_programa')
pyautogui.press('enter')

# Processar pedidos de clientes
for posicao_botao, dados_cliente in zip(posicao_botoes, dados_clientes):
    # Clicar no botão para adicionar um novo pedido
    pyautogui.click(posicao_botao)

    # Preencher os dados do cliente
    pyautogui.write(dados_cliente[0])
    pyautogui.press('tab')
    pyautogui.write(dados_cliente[1])

    # Confirmar o pedido
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Aguardar o processamento do pedido
    time.sleep(1)

# Atualizar sistema
pyautogui.press('f5')

# Criar relatório
pyautogui.press('win')
pyautogui.write('nome_do_programa_relatorios')
pyautogui.press('enter')
pyautogui.press('ctrl', 'p')
pyautogui.press('enter')

# Fechar sistema
pyautogui.press('alt', 'f4')
pyautogui.press('enter')
