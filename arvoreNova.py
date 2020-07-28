'''
Created on 19 de mai de 2016

@author: Antonio
'''
class NoArvore:
    def __init__(self, valor):
        self._valor = valor
        self._noEsquerdo = None
        self._noDireito = None
        self._noPai = None
    
    def getValor(self):
        return self._valor
    def setValor(self, valor):
        self._valor = valor
    def getNoEsquerdo(self):
        return self._noEsquerdo
    def setNoEsquerdo(self, novoNo):
        self._noEsquerdo = novoNo
    def getNoDireito(self):
        return self._noDireito
    def setNoDireito(self, novoNo):
        self._noDireito = novoNo
    def getNoPai(self):
        return self._noPai
    def setNoPai(self, novoNo):
        self._noPai = novoNo
        
    def ehEsquerdo(self, node):
        self.setNoPai(node.getNoPai())
        if self.getNoPai() == None:
            return False
        if self.getNoPai().getNoEsquerdo() == node:
            return True
        return False
    
    def ehDireito(self, node):
        self.setNoPai(node.getNoPai())
        if self.getNoPai() == None:
            return False
        if self.getNoPai().getNoDireito() == node:
            return True
        return False
    
    def noIrmao(self, node):
        if node.getNoPai() == None:
            return False
        if self.ehEsquerdo(node):
            return node.getNoPai().getNoDireito()
        return node.getNoPai().getNoEsquerdo()  
        
class ArvoreBinaria:
    def __init__(self):
        self._raiz = None
        
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, novoNo):
        self._raiz = novoNo
    
    def percorrerEmOrdem(self, raiz):
        if raiz != None:
            self.percorrerEmOrdem(raiz.getNoEsquerdo())
            print(raiz.getValor())
            self.percorrerEmOrdem(raiz.getNoDireito())
            
    def percorrerPreOrdem(self, raiz, lista):
        if raiz != None:
            lista.append(raiz.getValor())
            self.percorrerPreOrdem(raiz.getNoEsquerdo(), lista)
            self.percorrerPreOrdem(raiz.getNoDireito(), lista)
            
    def percorrerPosOrdem(self, raiz):
        if raiz != None:
            self.percorrerPosOrdem(raiz.getNoEsquerdo())
            self.percorrerPosOrdem(raiz.getNoDireito())
            print(raiz.getValor())
                        
    '''        
    def pesquisar(self, raiz, valor):#Recursivo
        if (raiz == None) or (valor == raiz.getValor()):
            return raiz
        if valor < raiz.getValor():
            return self.pesquisar(raiz.getNoEsquerdo(), valor)
        else:
            return self.pesquisar(raiz.getNoEsquerdo(), valor)
    '''
    
    def pesquisar(self, valor): #Interativo
        raiz = self._raiz
        while raiz != None and valor != raiz.getValor():
            if valor < raiz.getValor():
                raiz = raiz.getNoEsquerdo()
            else:
                raiz = raiz.getNoDireito()
        return raiz
    
    def minimo(self, raiz):
        while raiz.getNoEsquerdo() != None:
            raiz = raiz.getNoEsquerdo()
        return raiz
    
    def maximo(self, raiz):
        while raiz.getNoDireito() != None:
            raiz = raiz.getNoDireito()
        return raiz

    def sucessor(self, node):
        if node.getNoDireito() != None:
            return self.minimo(node.getNoDireito())
        y = node.getNoPai()
        while y != None and node == y.getNoDireito():
            node = y 
            y = y.getNoPai()
        return y
    
    def antecessor(self, node):
        if node.getNoEsquerdo() != None:
            return self.maximo(node.getNoEsquerdo())
        y = node.getNoPai()
        while y != None and node == y.getNoEsquerdo():
            node = y 
            y = y.getNoPai()
        return y
    
    def inserir(self, valor):
        node = NoArvore(valor)
        y = None
        raiz = self.getRaiz()
        while raiz != None:
            y = raiz
            if node.getValor() < raiz.getValor():
                raiz = raiz.getNoEsquerdo()
            else:
                raiz = raiz.getNoDireito()
        node.setNoPai(y)
        if y == None:
            self.setRaiz(node)
        elif node.getValor() < y.getValor():
            y.setNoEsquerdo(node)
        else:
            y.setNoDireito(node)
        return node, y
                
    def remover(self, valor):
        node = self.pesquisar(valor)
        if node.getNoEsquerdo() == None or node.getNoDireito() == None:
            y = node
        else:
            y = self.sucessor(node)
        if y.getNoEsquerdo() != None:
            x = y.getNoEsquerdo()
        else:
            x = y.getNoDireito()
        if x != None:
            x.setNoPai(y.getNoPai())
        if y.getNoPai() == None:
            self.setRaiz(x)
        else:
            if y == y.getNoPai().getNoEsquerdo():
                y.getNoPai().setNoEsquerdo(x)
            else:
                y.getNoPai().setNoDireito(x)
        if y != node:
            node.setValor(y.getValor())
        return y.getValor(), y.getNoPai()
            
arvore = ArvoreBinaria()
arvore.inserir(15)
arvore.inserir(9)
arvore.inserir(7)
arvore.inserir(19)
arvore.inserir(16)
arvore.inserir(25)
arvore.inserir(10)

lista = []
arvore.percorrerEmOrdem(arvore.getRaiz())
print("---")
arvore.percorrerPreOrdem(arvore.getRaiz(), lista)
print(lista)
print("---")
arvore.percorrerPosOrdem(arvore.getRaiz())
         