import pyautogui
from pynput.keyboard import Key, Controller
import keyboard
import xerox
import time
from copypaste import copy

lista = [{"Nome do Professor": "Biografia dele"}]


def paste():
    keyboard.press('ctrl')
    keyboard.press('v')
    keyboard.release('ctrl')

def DocentesPermanentes():
    return DocentesPermanentes

def escrever(abc):
    for char in abc:
        print(char)
        teclar(char, 0.13)
        
def teclar(caractere, tempo):
      keyboard.press(caractere)
      keyboard.release(caractere)
      time.sleep(tempo)

def clicar(coordenadas):   
    pyautogui.click(coordenadas[0], coordenadas[1])

def detectorDeCoordenadas():
    while True:
        # Mostra a cordenada atual do mouse
        currentMouseX, currentMouseY = pyautogui.position()
        print(currentMouseX, currentMouseY)

        # Aguarda um botão ser apertado para mostrar novamente
        #Enccerra o loop
        if keyboard.read_key() == "esc":
            print("Progam finish")
            break

def main(lista):

    for professor in lista:

        #Clicar em Adicionar Nova
        time.sleep(3)
        botao_adicionarNova = [-1209, -72] 
        clicar(botao_adicionarNova)
        print("cliquei no botao \"Adicionar Nova")
        
        #carregamento
        time.sleep(4)

        #Escrever o titulo
        for key in professor.keys():
            xerox.copy(key)
            print(f'copiei o item: {key}')
            paste()
        print("escrevi o título")
        time.sleep(1)

        #Entrar no botao (+)
        teclar('tab', 0.13)
        teclar('enter', 0.13)

        for i in range(4):          
            teclar('tab', 0.13)
            print(f"APERTEI TAB pela {i}° vez")
        teclar('enter', 0.13)
        print("Entrei em botaoMais\n ")

        #Slecionar bloco reutilizavel
        for i in range(17):
            teclar('tab', 0.15)
        
        teclar('enter', 0.13)
        teclar('tab', 0.13)
        teclar('enter', 0.13)
        print("Entrei no bloco reutilizável")

         #Transformar em bloco normal 
        for j in range(3):
            teclar('tab', 0.13)
        teclar('enter', 0.5)

        for i in range(4):
            teclar('tab', 0.13)
        teclar('enter', 0.13)
        print("_" * 10, "Bloco convertido para normal")
        
        #Entrando no <p> de biografia
        for i in range(3):  
          keyboard.press("shift")
          teclar('tab', 0)
          keyboard.release('shift')
        for i in range(63):
            teclar('right', 0.005)
        print("_" * 10, "Editando a Biografia...")

        #Acrescentar conteudo da biografia
        for value in professor.values():
            xerox.copy(value)
            print(f'copiei o item: {value}')
            paste()

        #Salvando como rascunho 
        for i in range(38):  
            keyboard.press("shift")
            teclar('tab', 0.05)
            keyboard.release('shift')
        teclar('enter', 0.2)

        #Retornando as Páginas 
        for i in range(89):  
            keyboard.press("shift")
            teclar('tab', 0.05)
            keyboard.release('shift')
        teclar('enter', 0.10)

# detectorDeCoordenadas()
main(lista)
