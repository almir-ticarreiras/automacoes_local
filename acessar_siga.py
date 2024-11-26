import pyautogui
import time

pyautogui.PAUSE = 0.5
tempo_de_espera = 1
tempo_transicao = 1
data_inicio = "01102024"
data_fim = "31102024"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(tempo_de_espera)

pyautogui.write("https://siga.congregacao.org.br/")
pyautogui.press("enter")

#Clica no Não sou um robô
time.sleep(tempo_de_espera)
pyautogui.moveTo(x=558, y=486, duration=tempo_transicao)
pyautogui.click()

#Clica no Entrar
time.sleep(tempo_de_espera)
pyautogui.moveTo(x=654, y=568, duration=tempo_transicao)
pyautogui.click()

#Clica no menu Contabilidade
time.sleep(tempo_de_espera)
pyautogui.moveTo(x=193, y=563, duration=tempo_transicao)
pyautogui.click()

#Clica no menu Relatórios
pyautogui.moveTo(x=190, y=679, duration=tempo_transicao)
pyautogui.click()

#Rola tela pra baixo
pyautogui.scroll(-100)

#Clica no menu Razão
pyautogui.moveTo(x=87, y=633, duration=tempo_transicao)
pyautogui.click()

#Clica na opção de selecionar Localizada
pyautogui.moveTo(x=548, y=328, duration=tempo_transicao)
pyautogui.click();

#Seleciona a Opção "ADM - ITUPEVA - SP"
pyautogui.moveTo(x=335, y=420, duration=tempo_de_espera)
pyautogui.click()

#Clica na opção de selecionar Centro de Custo
pyautogui.moveTo(x=323, y=393, duration=tempo_de_espera)
pyautogui.click()

#Seleciona o Opção "ADM - ITUPEVA - SP"
pyautogui.moveTo(x=350, y=492, duration=tempo_de_espera)
pyautogui.click()

#Clica na opção para selecionar o Tipo de saída
pyautogui.moveTo(x=300, y=593, duration=tempo_de_espera)
pyautogui.click()

#Seleciona a opção "Excel"
pyautogui.moveTo(x=250, y=529, duration=tempo_de_espera)
pyautogui.click()

#Clica no campo de data inicio
pyautogui.moveTo(x=588, y=260, duration=tempo_de_espera)
pyautogui.click()

#Limpa a data início pré selecionada e informa uma nova
pyautogui.press("backspace", presses=8)
pyautogui.write(data_inicio)

#Clica no campo de data fim
pyautogui.moveTo(x=734, y=261, duration=tempo_de_espera)
pyautogui.click()

#Limpa a data fim pré selecionada e informa uma nova
pyautogui.press("backspace", presses=8)
pyautogui.write(data_fim)

#Clica em gerar relatório
pyautogui.moveTo(x=282, y=674, duration=tempo_de_espera)
pyautogui.click()

# Atalho para abrir o Explorador de Arquivos (Windows + E)
pyautogui.hotkey('win', 'e')
time.sleep(1)

# Digita o caminho da pasta Downloads
pyautogui.typewrite('C:\\Users\\Usuario\\Downloads')  # Altere "SeuUsuario" pelo nome do usuário do seu sistema
pyautogui.press('enter')