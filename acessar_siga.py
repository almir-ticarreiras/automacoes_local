import pyautogui
import time

pyautogui.PAUSE = 0.5
tempo_de_espera = 3
tempo_transicao = 1

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
