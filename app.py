import pyautogui
from time import sleep

#registrar usuário
pyautogui.click(949,544,duration=2)
pyautogui.write('matheus')

pyautogui.click(953,584,duration=2)
pyautogui.write('123456')

pyautogui.click(836,626,duration=2)

#acessar usuário
pyautogui.click(976,544,duration=2)
pyautogui.write('matheus')

pyautogui.click(972,581,duration=2)
pyautogui.write('123456')

pyautogui.click(826,626,duration=2)

#abrir e salvar dados do txt
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        #clicar e digitar o produto
        pyautogui.click(548,520,duration=2)
        pyautogui.write(produto)
        #clicar e digitar a quantidade
        pyautogui.click(556,564,duration=2)
        pyautogui.write(quantidade)
        #clicar de digitar o preço
        pyautogui.click(552,598,duration=2)
        pyautogui.write(preco)
        #registrar
        pyautogui.click(413,835,duration=2)
        sleep(1)