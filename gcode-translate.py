# Pograma para deslocar valores x, y, z em arquivos gcodes.
# Elmar Uhl - 2024

import sys

for parameter in sys.argv:
  if (parameter.endswith(".ngc")):
    file = parameter
  
# Modifique aqui os valores de translação nos eixos x, y, z
translate = [0.000000, 0.000000, 0.000000]
# -------------------------------------------------------------------------------------------------------------

fInput = open(file,"rt") # Abertura do arquivo de entrada passado como parametro

texto = fInput.readlines() # Le todo o arquivo e armazena na variavel (lista de linhas)

len_texto = len(texto) # Numero de linhas no texto

texto = list(map(lambda x: x.replace('\n', ''), texto)) # Remove os caracteres de nova linha \n adicionais

# Execução linha a linha
for linha in texto:
  if linha.startswith("g0") or linha.startswith("g1") : # Opera nas linhas gcode de movimento
    # Executa a procura pelos valores de x
    inicio = linha.find('x') # Verifica a ocorencia de x e obtem sua posicao
    fim = linha.find(' ', linha.find('x')) # Posicao do final da sequencia do valor x
    if (inicio != -1):
      value = linha[inicio+1:fim] # valor de x inicial, (inicio+1 para retirar o caratere x)
      nValue = "{:.6f}".format(float(value) + translate[0]) # novo valor de x formatado em 6 casa decimais
      linha = linha.replace(value,nValue) # substitui o valor antigo pelo novo na string
    # Executa a procura pelos valores de y
    inicio = linha.find('y') # Verifica a ocorencia de y e obtem sua posicao
    fim = linha.find(' ', linha.find('y')) # Posicao do final da sequencia do valor y
    if (inicio != -1):
      value = linha[inicio+1:fim] # valor de y inicial (inicio+1 para retirar o primeiro caracter y)
      nValue = "{:.6f}".format(float(value) + translate[1]) # novo valor de y formatado em 6 casa decimais
      linha = linha.replace(value,nValue) # substitui o valor antigo pelo novo na string
    # Executa a procura pelos valores em z
    inicio = linha.find('z') # Verifica a ocorencia de z e obtem sua posicao
    fim = linha.find(' ', linha.find('z')) # Posicao do final da sequencia do valor z
    if (inicio != -1):
      value = linha[inicio+1:fim] # valor de z inicial (inicio+1 para retirar o primeiro caracter z)
      nValue = "{:.6f}".format(float(value) + translate[2]) # novo valor de z formatado em 6 casa decimais
      linha = linha.replace(value,nValue) # substitui o valor antigo pelo novo na string
    
    print(linha)
  else:
    print(linha)

fInput.close() # Fecha o arquivo de entrada
