# Lê arquivos de gcodes e gera saída xyz
# Elmar Uhl

file = open("DrillBox2.gcode",'rt') # Abre o arquivo para leitura

texto = file.readlines() # Leitura das linhas do arquivo

texto = list(map(lambda x: x.replace(';\n', ' '), texto)) # Remove os caracteres de nova linha \n adicionais

value = [' 0.000000', ' 0.000000', ' 0.000000']
oldValue = [' 0.000000', ' 0.000000', ' 0.000000']

def obtemValores():
  inicioX = linha.find('X')
  fimX = linha.find(' ', linha.find('X'))
                     
  inicioY = linha.find('Y')
  fimY = linha.find(' ', linha.find('Y'))
                     
  inicioZ = linha.find('Z')
  fimZ = linha.find(' ', linha.find('Z'))

  changed = 0

  if (inicioX != -1):
    changed = 1
    global oldValue
    value[0] = linha[inicioX+1:fimX] # valor de x inicial, (inicio+1 para retirar o caratere x)
    oldValue[0] = value[0]
  if (inicioY != -1):
    changed = 1
    value[1] = linha[inicioY+1:fimY] # valor de Y inicial, (inicio+1 para retirar o caratere Y)
    oldValue[1] = value[1]
  if inicioZ != -1:
    changed = 1
    value[2] = linha[inicioZ+1:fimZ]
    oldValue[2] = value[2]
  if changed == 1:
    print(oldValue[0],oldValue[1],oldValue[2])

for linha in texto:
   obtemValores()
      
file.close()
