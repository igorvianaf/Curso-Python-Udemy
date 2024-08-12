"""
CONSTANTE = "variáveis" que não mudam
Muitas condições no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_do_carro = 100 #posição do carro na estrada

RADAR_1 = 60 # Velocidade maxima do radar
LOCAL_1 = 100 # Local onde o radar está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_do_carro >= (LOCAL_1 - RADAR_RANGE) and local_do_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('O carro passou no radar 1')

if carro_multado_radar_1 :
    print('O carro foi multado em radar 1')