'''
Created on 10 de jun de 2016

@author: Antonio
'''
from arvoreNova import ArvoreBinaria, NoArvore

class noAvl(NoArvore):
    def __init__(self, valor):
        super(noAvl, self).__init__(valor)
        self._altura = -1

class ArvoreAvl(ArvoreBinaria):
    def inserirAvl(self, valor):
        no, pai = super(ArvoreAvl, self).inserir(valor)
        while pai != None:
            if self.balancear(pai.getValor()) == True:
                break
            else:
                pai = pai.getNoPai()
                    
    def removerAvl(self, valor):
        no, pai = super(ArvoreAvl, self).remover(valor)
        self.balancear(pai.getValor())
        
    def balancear(self, no):
        x = self.fatorBalanceamento(self.pesquisar(no))
        if x >= -1 and x <= 1:
            return False
        if x > 1:
            if self.fatorBalanceamento(self.pesquisar(no).getNoDireito()) < 0:
                self.giroDireito(self.pesquisar(no).getNoDireito())
                self.giroEsquerdo(self.pesquisar(no))
            else:
                self.giroEsquerdo(self.pesquisar(no))
            return True
        else:
            if self.fatorBalanceamento(self.pesquisar(no).getNoEsquerdo()) > 0:
                self.giroEsquerdo(self.pesquisar(no).getNoEsquerdo())
                self.giroDireito(self.pesquisar(no))
            else:
                self.giroDireito(self.pesquisar(no))
            return True

    def fatorBalanceamento(self, no):
        alturaEsquerda = self.alturaNo(no.getNoEsquerdo())
        alturaDireita = self.alturaNo(no.getNoDireito())
        return alturaDireita - alturaEsquerda

    def giroEsquerdo(self, x):
        y = x.getNoDireito()
        x.setNoDireito(y.getNoEsquerdo())
        if y.getNoEsquerdo() != None:
            y.getNoEsquerdo().setNoPai(x)
        y.setNoPai(x.getNoPai())
        if x.getNoPai() == None:
            self.setRaiz(y)
        elif x == x.getNoPai().getNoEsquerdo():
            x.getNoPai().setNoEsquerdo(y)
        else:
            x.getNoPai().setNoDireito(y)
        y.setNoEsquerdo(x)
        x.setNoPai(y)

    def giroDireito(self, x):
        y = x.getNoEsquerdo()
        x.setNoEsquerdo(y.getNoDireito())
        if y.getNoDireito() != None:
            y.getNoDireito().setNoPai(x)
        y.setNoPai(x.getNoPai())
        if x.getNoPai() == None:
            self.setRaiz(y)
        elif x == x.getNoPai().getNoDireito():
            x.getNoPai().setNoDireito(y)
        else:
            x.getNoPai().setNoEsquerdo(y)
        y.setNoDireito(x)
        x.setNoPai(y)

    def giroDuploEsquerdo(self, no):
        self.giroDireito(no)
        self.giroEsquerdo(no)

    def giroDuploDireito(self, no):
        self.giroEsquerdo(no)
        self.giroDireito(no)
        
    def alturaNo(self, no):
        if no == None:
            return -1
        h1 = self.alturaNo(no.getNoEsquerdo())
        h2 = self.alturaNo(no.getNoDireito())
        return 1 + max(h1, h2)
                                  
avl = ArvoreAvl()
avl.inserirAvl(50)
avl.inserirAvl(30)
avl.inserirAvl(70)
avl.inserirAvl(10)
avl.inserirAvl(40)
avl.removerAvl(50)
avl.removerAvl(10)
avl.inserirAvl(80)
avl.inserirAvl(65)
avl.inserirAvl(9)
avl.inserirAvl(13)
avl.inserirAvl(20)
avl.inserirAvl(14)
avl.removerAvl(13)

lista = []
avl.percorrerPreOrdem(avl.getRaiz(), lista)
print(lista)
