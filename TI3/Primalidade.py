from GeradorPseudoAleatorio import GeradorPseudoAleatório
import math

class TestePrimalidade():
    def __init__(self, tamanho, algoritmo ="Miller"):
        self.tamanho = tamanho
        self.algoritmo = algoritmo
        self.gerador = GeradorPseudoAleatório(tamanho)

    def set_algoritmo(self, algoritmo):
        self.algoritmo = algoritmo
    
    def gerar_numero_primo(self):
        while True:
            candidato_primo = self.gerador.gerar_numero()
        #print(self.test_primalidade(5850725702766829291491370712136286009948642125131436113342815786444567))
            if(candidato_primo %2 != 0):
                if(self.test_primalidade(candidato_primo)):
                    print(candidato_primo)
                    return candidato_primo
            
    def test_primalidade(self, candidato_primo):
        if(self.algoritmo == "Miller"):
            for i in range(4):
                if(not(self.miller_habin(candidato_primo))):
                    return False
            return True
        
        elif(self.algoritmo == "Fermat"):
            for i in range(4):
                if(not(self.fermat(candidato_primo))):
                    return False
            return True
        else:
            print("Algoritmo não conhecido")
    
    def fermat(self,candidato):
        # Geração de um a aleatório não divisivel pelo candidato n
        #entre 2 e n-1 para facilitar a geração.
        a = self.gerador.gerar_numero() % (candidato)
        while(a <= 2):
            a = self.gerador.gerar_numero() % (candidato)
        
        # Retorna se a^n-1 é congruente a 1 mod n
        return pow(a, candidato-1, candidato)==1
    
    def miller_habin(self, candidato):
        n_1 = candidato - 1
        k = 1
        # Achando a parte impar de n - 1
        m = n_1 // 2
        while (m % 2 == 0):
            m = m//2
            k += 1

        # geração de um número aleatório entre 2 e n-2
        a = self.gerador.gerar_numero() % (candidato)
        while(a <= 2):
            a = self.gerador.gerar_numero() % (candidato)
        # b = (a^m) mod n se = 1 então retorna primo
        # uma vez que 1² mod n sempre = 1 mod n
        b = pow(a,m,candidato)
        if (b == 1):
            return True
        
        # teste para a^(2^i * m) se algum é congruente a -1 mod m
        for i in range(k):

            if (b == n_1):
                return True
            b = pow(b,2, candidato)
        return False
    
primalidade = TestePrimalidade(1024)
tamanhos = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
primalidade.gerar_numero_primo()