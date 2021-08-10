from random import random
import numpy as np
import matplotlib.pyplot as plt

#Criação da Classe Produto:
class Produto():

    def __init__(self, nome_produto, volume_produto,  valor_produto):
        self.nome = nome_produto
        self.volume = volume_produto
        self.valor = valor_produto
     
#Criação da Classe Indivíduo:        
class Individuo():
    
    #Construtor:
    def __init__(self, volume_produto, valor_produto, limite_espaco=3, geracao = 0):
        self.volume = volume_produto
        self.valor = valor_produto
        self.limite = limite_espaco
        self.geracao = geracao
        self.cromossomo = []
        self.volume_utilizado = 0
        self.nota_avaliacao = 0
        
        #Inicialização randômica do cromosso:
        for item in range(len(volume_produto)):
            self.cromossomo.append("1" if random() > 0.5 else "0")
    
    #Método: Avaliação:
    def avaliacao(self):
        nota = 0
        somaVolume = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == "1":
                somaVolume += self .volume[i]
                nota += self.valor[i]
        if somaVolume > self.limite:
            nota = 1
        self.volume_utilizado = somaVolume
        self.nota_avaliacao = nota
     
    #Método: Crossover:
    def crossOver(self, outro):
        #Corte randomico:
        corte = round((random() * len(self.cromossomo)))
        filho1 = self.cromossomo[0:corte] + outro.cromossomo[corte::]
        filho2 = outro.cromossomo[0:corte] + self.cromossomo[corte::]
        
        #Tranformando os filhos em indivíduos:
        filhos = [Individuo(self.volume, self.valor, self.limite, self.geracao +1),
                  Individuo(self.volume, self.valor, self.limite, self.geracao +1)]
        
        #Passando os cromossomos dos filhos:
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
     
     #Método: Mutação:
    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                self.cromossomo[i] = "1" if self.cromossomo[i] == "0" else "0"

        return self

# Criação da classe Algortimo Genético:            
class AlgoritmoGenetico():
    
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucao = []
        
    def inicializaPopulacao(self, volume, valor, limite_espaco):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(volume, valor, limite_espaco))
        self.melhor_solucao = self.populacao[0]
        
    def ordenaPopulacao(self):
        self.populacao = sorted(self.populacao, 
                               key = lambda individuo: individuo.nota_avaliacao,
                                reverse = True)
        
    def melhorIndividuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    def soma_avaliacoes(self):
        soma = 0
        for item in self.populacao:
            soma += item.nota_avaliacao
        return soma
    
    def selecaoPai(self):
        pesos = []
        posicao_pais = list(range(0, len(self.populacao)))
        for item in self.populacao:
            pesos.append(item.nota_avaliacao/self.soma_avaliacoes())
        
        pai_id = np.random.choice(a = posicao_pais,
                                  size = 1,
                                  p = pesos)
        return pai_id
    
    def melhorDeCadaGeracao(self):
        melhor = self.populacao[0]
        print(f'G{melhor.geracao} --> R$ {melhor.nota_avaliacao} :{melhor.volume_utilizado} m3')
        print(f'Cromossomo = {melhor.cromossomo}\n')
      
    def visualizaSolucao(self):
        melhor = self.melhor_solucao
        print('----------------------------------------------------------------------------------')
        print(f'Cromossomo = {melhor.cromossomo}')
        print(f'Geracao = {melhor.geracao}')
        print(f'Volume = {melhor.volume_utilizado} m3')
        print(f'Valor= R$ {melhor.nota_avaliacao}\n')
        for i in range(len(melhor.cromossomo)):
            if melhor.cromossomo[i] == "1" :
                print(nome[i], valor[i], volume[i])
                
    def executa(self,volume, valor, limite_espaco, numero_geracoes, taxa_mutacao):
        
        #Inicializa a população
        self.inicializaPopulacao(volume, valor, limite_espaco)
        
        for i in range(numero_geracoes):
        
            #Avaliação:
            for item in self.populacao:
                item.avaliacao()
            
            #Ordenando a População:
            self.ordenaPopulacao()
            
            
            #Visualizar
            self.melhorDeCadaGeracao()
            
            #Melhor Indivíduo:
            self.melhorIndividuo(self.populacao[0])
            
            #Agrupando todas as melhores soluções de cada geração.
            self.lista_solucao.append(self.melhor_solucao.nota_avaliacao)
                
            #Seleçao dos Pais:
            nova_populacao = []
            
            for n_cross in range(0, len(self.populacao), 2):
                Pai1_id = int(self.selecaoPai())
                Pai2_id = int(self.selecaoPai())
               
                #Crossover e Mutação:
                filhos = self.populacao[Pai1_id].crossOver(self.populacao[Pai2_id])
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
        
            #Nova População:
            self.populacao = nova_populacao
        
        #Visualização Resultado:
        self.visualizaSolucao()
        
        
                
# Se este módulo estiver rodando por conta própria sem ser importado:
if __name__ == '__main__':
    
    #Produtos:
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    
    #Dados para criação de indivíduos:
    nome = []
    volume = []
    valor = [] 
    for produto in lista_produtos:
        nome.append(produto.nome)
        volume.append(produto.volume)
        valor.append(produto.valor)
    limite_espaco = 3
    tamanho_populacao = 20
    taxa_mutacao = 0.01
    numero_geracoes = 100
    
    #Criação da Classe Algoritmo Genético:
    ag = AlgoritmoGenetico(tamanho_populacao)
    
    #Execução do algoritmo genético:
    ag.executa(volume, valor, limite_espaco, numero_geracoes, taxa_mutacao)
    
    #Melhores soluções:
    solucoes = ag.lista_solucao
    
    #Gráficos:
    plt.plot(solucoes)
    plt.show()
    
    
    

    
   

    