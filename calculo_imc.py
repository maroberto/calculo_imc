from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from time import sleep


# recupara dados da textbox
def listar_dados():
    altura = imc.lineEdit.text()
    peso = imc.lineEdit_2.text()
    print(altura, peso)
    calculo_imc = float(peso) / (float(altura) * float(altura))
    print('{:.2f}'.format(calculo_imc))
    if (calculo_imc < 16.9):
        # verifica o peso ideal
        peso_atual = []
        ideal = 24.9
        while float(peso) / (float(altura) * float(altura)) < ideal:
            (peso) = float(peso) + 1
            peso_atual.append(peso)
        print('Seu peso ideal é {:.0f}'.format(peso_atual[-2]))
        reposta = ('O seu IMC é {:.2f} você está muito abaixo do\npeso ideal!\nSeu peso ideal é {:.0f}'.format(calculo_imc, peso_atual[-2]))
        print('O seu IMC é {:.2f}, você está muito abaixo do peso ideal!'.format(calculo_imc))
        zerar_barra2()
    elif (calculo_imc < 18.4):
        # verifica o peso ideal
        peso_atual = []
        ideal = 24.9
        while float(peso) / (float(altura) * float(altura)) < ideal:
            (peso) = float(peso) + 1
            peso_atual.append(peso)
        print('Seu peso ideal é {:.0f}'.format(peso_atual[-2]))
        reposta = ('O seu IMC é {:.2f} você está abaixo do peso ideal!\nSeu peso ideal é {:.0f}'.format(calculo_imc, peso_atual[-2]))
        print('O seu IMC é {:.2f}, você está abaixo do peso ideal!'.format(calculo_imc))
        zerar_barra2()
    elif (calculo_imc < 24.9):
        reposta = ('O seu IMC é {:.2f} você está no peso normal!'.format(calculo_imc))
        print('O seu IMC é {:.2f}, você está no peso normal!'.format(calculo_imc))
        zerar_barra2()
    elif (calculo_imc < 29.9):
        # verifica o peso ideal
        peso_atual = []
        ideal = 24.9
        while float(peso) / (float(altura) * float(altura)) > ideal:
            (peso) = float(peso) - 1
            peso_atual.append(peso)
        print('Seu peso ideal é {:.0f}'.format(peso_atual[-1]))
        reposta = ('O seu imc é {:.2f} você está acima do peso!\nSeu peso ideal é {:.0f}'.format(calculo_imc, peso_atual[-1]))
        print('O seu imc é {:.2f}, você está acima do peso!'.format(calculo_imc))
        zerar_barra2()
    elif (calculo_imc < 34.9):
        # verifica o peso ideal
        peso_atual = []
        ideal = 24.9
        while float(peso) / (float(altura) * float(altura)) > ideal:
            (peso) = float(peso) - 1
            peso_atual.append(peso)
        print('Seu peso ideal é {:.0f}'.format(peso_atual[-1]))
        reposta = ('O seu IMC é {:.2f} Você tem obesidade grau I !\nSeu peso ideal é {:.0f}'.format(calculo_imc, peso_atual[-1]))
        print('O seu IMC é {:.2f}, Você tem obesidade grau I !'.format(calculo_imc))
        zerar_barra2()
    elif (calculo_imc < 40):
        # verifica o peso ideal
        peso_atual = []
        ideal = 24.9
        while float(peso) / (float(altura) * float(altura)) > ideal:
            (peso) = float(peso) - 1
            peso_atual.append(peso)
        print('Seu peso ideal é {:.0f}'.format(peso_atual[-1]))
        reposta = ('O seu IMC é {:.2f} você tem obesidade grau II !\nSeu peso ideal é {:.0f}'.format(calculo_imc, peso_atual[-1]))
        print('O seu IMC é {:.2f}, você tem obesidade grau II !'.format(calculo_imc))
        zerar_barra2()
    else:
        # verifica o peso ideal
        peso_atual = []
        ideal = 24.9
        while float(peso) / (float(altura) * float(altura)) > ideal:
            (peso) = float(peso) - 1
            peso_atual.append(peso)
        print('Seu peso ideal é {:.0f}'.format(peso_atual[-1]))
        reposta = ('O seu IMC é {:.2f} você tem obesidade grau III !\nSeu peso ideal é {:.0f} '.format(calculo_imc, peso_atual[-1]))
        print('O seu IMC é {:.2f} você tem obesidade grau III ! '.format(calculo_imc))
        zerar_barra2()
    imc.label_5.setText(reposta)


valor = 0


# Barra de progresso
def incrementa_barra():
    global valor
    while (valor < 120):
        imc.progressBar.setValue(valor)
        valor = valor + 4
        sleep(0.1)


# Limpar dados
def zerar_barra():
    global valor
    valor = 0
    QMessageBox.about(imc, 'Alerta', 'Tem certeza que deseja apagar?')
    imc.progressBar.setValue(valor)
    imc.lineEdit.setText('')
    imc.lineEdit_2.setText('')


# Limpa segundo click
def zerar_barra2():
    global valor
    valor = 0
    imc.progressBar.setValue(valor)


app = QtWidgets.QApplication([])
imc = uic.loadUi('ui/tela_imc.ui')  # chama o arquivo ui
imc.pushButton.clicked.connect(incrementa_barra)
imc.pushButton.clicked.connect(listar_dados)
imc.pushButton_2.clicked.connect(zerar_barra)


imc.show()
app.exec()
