#Programa para automatizar entrada e saída de aulas via zoom, adicionar gravação, fechar e salvar a gravação e por fim, desligar o pc
# Abrir o zoom, para poder após ingressar na reunião - No meu caso, estou utilizando Linux Debian Ubuntu; para isso, pressionarei Janela e depois escreverei zoom e Enter

import pyautogui

pyautogui.press('winleft')
pyautogui.write('zoom')
pyautogui.press('enter')
