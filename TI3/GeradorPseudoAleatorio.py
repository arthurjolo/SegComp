import time
import math

class GeradorPseudoAleatório():
    def __init__(self, tamanho, algoritimo = "LCG") -> None:
        # Definição dos parametros para o LCG
        self.lcg_m = 19993
        self.lcg_a = 15005
        self.lcg_b = 8371
        self.lcg_seed = 135
        ################
        # Definição dos parametros para o LFG
        self.lfg_l = 17
        self.lfg_k = 5
        self.lfg_m = 2**31
        self.lfg_seed = self.lfg_l #start poin, muda para não gerar o mesmo número
        self.lagged_fib_values = [0, 1]
        self.init_lagged_fib()
        ################
        self.tamanho = tamanho
        self.algoritimo = algoritimo
    
    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    def get_tamanho(self):
        return self.tamanho
    
    def set_algoritimo(self, algoritimo):
        self.algoritimo = algoritimo

    def get_algoritimo(self):
        return self.algoritimo
    
    def gerar_numero(self):
        if(self.algoritimo == "LCG"):
            return int(self.lcg(),2)
        elif(self.algoritimo == "LFG"):
            return int(self.lfg(),2)
    
    def fibonacci(self, count):
        for i in range(2,count):
            new_fib = self.lagged_fib_values[i - 1] + self.lagged_fib_values[i - 2] % self.lfg_m
            self.lagged_fib_values.append(new_fib)
        return new_fib
    
    #inicia os l valores inciais do algoritmo
    def init_lagged_fib(self):
        self.lagged_fib_values = [0,1]
        self.fibonacci(self.lfg_l)

    def lfg(self):
        binary = ""
        # Para o tamanho de bis especificado gera os bits
        for i in range(self.tamanho):
            # Gera o i número aleatório confer os 
            si = (self.lagged_fib_values[self.lfg_seed + i - self.lfg_l] +
                  self.lagged_fib_values[self.lfg_seed + i - self.lfg_k]) % self.lfg_m
            zi = si % 2
            # Concatena o bit gerado ao binário aleatório a ser retornado
            binary += str(zi)
            self.lagged_fib_values.append(si)
        self.lfg_seed += 1
        return binary
    # Algoritimo LCG
    def lcg(self):
        binary = ""
        # s0 = semente
        s = self.lcg_seed
        # Loop de geração dos cada bit para uma cadeia com o tamanho escolhido
        for i in range(self.tamanho):
            # LCG para gerar um número pseudo aleatório
            #conforme o número gerado anteriormente
            si = (self.lcg_a * s + self.lcg_b) % self.lcg_m
            # Número gerado é transformado em um 0 ou 1
            zi = si % 2
            # Concatena o bit gerado ao binário aleatório a ser retornado
            binary += str(zi)
            s = si
        # Atualiza a semente para que na próxima chamada do algoritimo
        #seja gerado um número diferente
        self.lcg_seed += 1
        return binary

'''tamanhos = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
gerador = GeradorPseudoAleatório(4096)'''
'''elapsed_times_lcg = []
for tamanho in tamanhos:
    start_time = time.time()
    gerador.set_tamanho(tamanho)
    for i in range(100):
        gerador.gerar_numero()
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_times_lcg.append(elapsed_time)
print(elapsed_times_lcg)
elapsed_times_lfg = []
gerador.set_algoritimo("LFG")
for tamanho in tamanhos:
    start_time = time.time()
    gerador.set_tamanho(tamanho)
    for i in range(100):
        gerador.gerar_numero()
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_times_lfg.append(elapsed_time)

print(elapsed_times_lfg)'''