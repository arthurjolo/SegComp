import time

class GeradorPseudoAleatório():
    def __init__(self, tamanho, algoritimo = "LCG") -> None:
        # Definição dos parametros para o LCG
        self.lcg_m = 19993
        self.lcg_a = 15005
        self.lcg_b = 8371
        ################
        self.tamanho = tamanho
        self.algoritimo = algoritimo
        self.seed = 1
    
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
            
            return self.lcg()
    
    # Algoritimo LCG
    def lcg(self):
        binary = ""
        # s0 = semente
        s = self.seed
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
        self.seed += 1
        return binary

tamanhos = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
gerador = GeradorPseudoAleatório(40)
elapsed_times_lcg = []
for tamanho in tamanhos:
    start_time = time.time()
    gerador.set_tamanho(tamanho)
    for i in range(100):
        gerador.gerar_numero()
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_times_lcg.append(elapsed_time)


