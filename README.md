# Objetivo:
1) Criar um algoritmo genético de forma manual, ou seja, sem auxílio de bibliotecas como DEAP.
2) Aplicar o algoritmo em um problema de otimização.

# O Problema de Otimização:
Supondo que um caminhão baú deverá realizar o frete de alguns itens onde será transportado no máximo um item de cada tipo.
Qual a combinação de itens ótima que maximiza o valor da carga e ocupa um espaço físico factível dentro do caminhão?

# Dados para resolução do problema:
- Item, volume (m3), preço (R$)
1) Iphone 6, 0.0000899, 2911.12
2) TV 55', 0.400, 4346.99
3) TV 50', 0.290, 3999.90
4) TV 42', 0.200, 2999.00
5) Notebook Dell", 0.00350, 2499.90
6) Ventilador Panasonic, 0.496, 199.90
7) Microondas Electrolux, 0.0424, 308.66
8) Microondas LG, 0.0544, 429.90
9) Microondas Panasonic, 0.0319, 299.29
10) Geladeira Brastemp, 0.635, 849.00
11) Geladeira Consul, 0.870, 1199.89
12) Notebook Lenovo, 0.498, 1999.90)
13) Notebook Asus, 0.527, 3999.00
14) Geladeira Dako, 0.751, 999.90

- Restrições:
  - Capacidade máxima do caminhão = 3 m3
  - Somatório do volume de todos os itens = 4,8 m3

# Resolução:
- Parâmetros utilizados:
  1) Número de indivíduos na população = 20
  2) Taxa de mutação = 1%
  3) Numero de gerações = 100
  
# Resultado:
O melhor resultado obtido, executando o algoritmo diversas vezes foi:
- Volume Utilizado = 2.9172899 m3
- Valor da Carga Transportada = R$ 24993.55
1) Iphone 6.
2) TV 55'.
3) TV 50'.
4) TV 42'.
5) Notebook Dell.
6) Microondas Electrolux. 
7) Microondas LG. 
8) Microondas Panasonic. 
9) Geladeira Consul.
10) Notebook Lenovo.
11) Notebook Asus.

    
    

