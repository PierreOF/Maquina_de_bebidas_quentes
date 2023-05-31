import os
import time
#from main import *

# saldo inicial
credito_atual = float(0)
#reservatorios 
volume_copo = float(100) # escolha o valor em ml para o seu copo
cafe = float(1000)
leite = float(1000)
agua = float(1000)
chocolate = float(1000)
copo = 50
reservatorios = [cafe,leite,agua,chocolate,copo]

# bebidas e seus respectivos precos
bebidas = ["Expresso","Longo","Pingado","Capuccino","Cap-Choc","Cafe com Chocolate","Chocolate","Chocolate com Leite"]
valores = [0.5 , 0.75 ,1 , 1.25 ,1.5 ,1.75 ,2 ,2.25]

def tela(display):
        print("="*46)
        print(f"|{display.center(44)}|")
        print("="*46)
        print("| 1 - Café Expresso  5 - Cap-Choc            |")
        print("| 2 - Café Longo     6 - Café com Chocolate  |")
        print("| 3 - Café Pingado   7 - Chocolate           |")
        print("| 4 - Capuccino      8 - Chocolate com leite |")
        print("="*46)

def sensor_expresso():
        global cafe , agua , credito_atual , valores,copo
        if cafe >= ((9/10) * volume_copo) and agua >= ((1/10) * volume_copo) and copo > 0:
            copo -= 1
            cafe -= ((9/10) * volume_copo)
            agua -= ((1/10) * volume_copo)
            credito_atual = float(credito_atual) - valores[0]
            return True
        else:
            return False
        
def sensor_longo():
        global cafe , agua , credito_atual , valores , volume_copo , copo
        if cafe >= ((3/10) * volume_copo) and agua >= ((7/10) * volume_copo) and copo > 0:
            copo -= 1
            cafe -= ((3/10) * volume_copo)
            agua -= ((7/10) * volume_copo)
            credito_atual = float(credito_atual) - valores[1]
            return True
        else:
            return False

def sensor_pingado():
        global cafe , agua , credito_atual , valores , volume_copo , leite , copo
        if cafe >= ((1/100) * volume_copo) and agua >= ((9/100) * volume_copo): 
            if leite >= ((9/10) * volume_copo) and copo > 0:
                copo -= 1
                cafe -= ((1/100) * volume_copo)
                agua -= ((9/100) * volume_copo)
                leite -= ((9/10) * volume_copo)
                credito_atual = float(credito_atual) - valores[2]
                return True
            else:
                 return False
        else:
            return False

def sensor_capuccino():
        global cafe , agua , credito_atual , valores , volume_copo , leite , copo
        if cafe >= ((3/100) * volume_copo) and leite >= ((3/4) * volume_copo):
            if agua >= ((22/100)) and copo > 0:
                copo -= 1
                cafe -= ((3/100) * volume_copo)
                agua -= ((22/100) * volume_copo)
                leite -= ((3/4) * volume_copo)
                credito_atual = float(credito_atual) - valores[3]
                return True
            else:
                 return False
        else:
            return False

def sensor_cap_choc():
        global cafe , agua , credito_atual , valores , volume_copo , leite, chocolate , copo
        if cafe >= ((3/100) * volume_copo) and leite >= ((2/4) * volume_copo) and copo > 0:
            if agua >= ((22/100) * volume_copo) and chocolate >= ((1/4) * volume_copo) :
                copo -= 1
                cafe -= ((3/100) * volume_copo)
                agua -= ((22/100) * volume_copo)
                leite -= ((2/4) * volume_copo)
                chocolate -= ((1/4) * volume_copo)
                credito_atual = float(credito_atual) - valores[4]
                return True
            else:
                return False
        else:
            return False

def sensor_cafe_com_chocolate():
        global cafe , agua , credito_atual , valores , volume_copo , leite, chocolate , copo
        if cafe >= ((5/100) * volume_copo) and chocolate >= ((1/2) * volume_copo) :
            if agua >= ((45/100) * volume_copo) and copo > 0:
                copo -= 1
                cafe -= ((5/100) * volume_copo)
                agua -= ((45/100) * volume_copo)
                chocolate -= ((1/2) * volume_copo)
                credito_atual = float(credito_atual) - valores[5]
                return True
            else:
                return False
        else:
            return False

def sensor_chocolate():
    global chocolate , agua , credito_atual , copo , valores
    if chocolate >= (volume_copo) and copo > 0:
        copo -= 1
        chocolate -= (volume_copo)
        credito_atual = (float(credito_atual) - valores[6])
        return True
    else:
        return False

def sensor_chocolate_com_leite():
    global chocolate , leite , credito_atual , valores , copo
    if chocolate >= ((1/2) * volume_copo) and leite >= ((1/2) * volume_copo) and copo > 0:
        copo -= 1
        chocolate -= ((1/2) * volume_copo)
        leite -= ((1/2) * volume_copo)
        credito_atual = float(credito_atual) - valores[7]
        return True
    else:
        return False

def sensor_ingredientes(x):
    global cafe , leite , chocolate , agua , copo , valores , credito_atual
    if x == 0 :
        print(f"cafe = {cafe} g")
        print(f"leite = {leite} ml")
        print(f"chocolate = {chocolate} g")
        print(f"agua = {agua} ml")
    if x == 1 :
        sensor_bebida = sensor_expresso()
        return sensor_bebida
    if x == 2 :
        sensor_bebida = sensor_longo()
        return sensor_bebida
    if x == 3 :
        sensor_bebida = sensor_pingado()
        return sensor_bebida
    if x == 4:
        sensor_bebida = sensor_capuccino()
        return sensor_bebida
    if x == 5:
        sensor_bebida = sensor_cap_choc()
        return sensor_bebida
    if x == 6:
        sensor_bebida = sensor_cafe_com_chocolate()
        return sensor_bebida
    if x == 7:
        sensor_bebida = sensor_chocolate()
        return sensor_bebida
    if x == 8:
        sensor_bebida = sensor_chocolate_com_leite()
        return sensor_bebida
    
def limpa_tela():
    time.sleep(3)
    os.system("cls")


while True:
    tela(f"SALDO ATUAL : {credito_atual}")

    credito_atual = input("Insira o valor de crédito : ")
    
    if credito_atual.isdigit():
        None
    else:
        limpa_tela()
        tela("Digite apenas números")
        limpa_tela()
        credito_atual = 0
        continue

    bebida_selecionada=int(input("Qual é a bebida desejada ? : "))
    if bebida_selecionada == 9:
        break
    if bebida_selecionada > 9 or bebida_selecionada < 0:
        print("escolha apenas um número de 1 até 8")
    else:
        os.system("cls")


    # iniciando preparação da bebida
    if bebida_selecionada == 0:
        sensor_ingredientes(0)
        print(f"TROCO DE {credito_atual} DEVOLVIDO")
        credito_atual = 0
    else:
        if (float(credito_atual) >= (valores[bebida_selecionada-1])):

            if sensor_ingredientes(bebida_selecionada):
                tela("ótima escolha !")
                limpa_tela()
                tela("Preparando sua bebida...")
                limpa_tela()
                tela("Esquentando ingredientes...")
                limpa_tela()
                tela("Servindo Bebida...")
                limpa_tela()
                tela("Pedido Concluido !")
                limpa_tela()
                tela(f"Troco de R${credito_atual} Devolvido !")
                limpa_tela()
                credito_atual = 0
                continue
            else:
                tela("Ingredientes insuficientes :/ ")
                limpa_tela()
                tela(f"TROCO DE {credito_atual} DEVOLVIDO")
                limpa_tela()
                credito_atual = 0
                continue
        else:
            tela(f"SALDO ATUAL INSUFICIENTE")
            limpa_tela()
            tela(f"TROCO DE R${int(credito_atual):.2f} DEVOLVIDO")
            limpa_tela()
            credito_atual = 0
            continue
















