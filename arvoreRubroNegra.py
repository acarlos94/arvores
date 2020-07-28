'''
Created on 11 de jun de 2016

@author: Antonio
'''
class NodeRB:
    def __init__(self, valor):
        self._valor = valor 
        self._filhoEsquerdo = None 
        self._filhoDireito = None 
        self._pai = None 
        self._cor = "preto"
    
    def getValor(self):
        return self._valor 
    def setValor(self, valor):
        self._valor = valor
    def getFilhoEsquerdo(self):
        return self._filhoEsquerdo 
    def setFilhoEsquerdo(self, novoNode):
        self._filhoEsquerdo = novoNode
    def getFilhoDireito(self):
        return self._filhoDireito 
    def setFilhoDireito(self, novoNode):
        self._filhoDireito = novoNode
    def getPai(self):
        return self._pai 
    def setPai(self, novoNode):
        self._pai = novoNode
    def getCor(self):
        return self._cor
    def setCor(self, novaCor):
        self._cor = novaCor
        
        
class ArvoreRB:
    def __init__(self):
        self._nodeVazio = NodeRB(None)
        self._raiz = self._nodeVazio
        
    def getVazio(self):
        return self._nodeVazio
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, novoNode):
        self._raiz = novoNode
        
    def inserirRB(self, valor):
        node = NodeRB(valor)
        y = self.getVazio()
        x = self.getRaiz()
        while x != self.getVazio():
            y = x
            if node.getValor() < x.getValor():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        node.setPai(y)
        if y == self.getVazio():
            self.setRaiz(node)
        else:
            if node.getValor() < y.getValor():
                y.setFilhoEsquerdo(node)
            else:
                y.setFilhoDireito(node)
        node.setFilhoEsquerdo(self.getVazio())
        node.setFilhoDireito(self.getVazio())
        node.setCor("vermelho")
        self.inserirFixup(node)
    
    def inserirFixup(self, node):
        while node.getPai().getCor() == "vermelho":
            if node.getPai() == node.getPai().getPai().getFilhoEsquerdo():
                y = node.getPai().getPai().getFilhoDireito()
                if y.getCor() == "vermelho":
                    node.getPai().setCor("preto")
                    y.setCor("preto")
                    node.getPai().getPai().setCor("vermelho")
                    node = node.getPai().getPai()
                else:
                    if node == node.getPai().getFilhoDireito():
                        node = node.getPai()
                        self.giroEsquerdo(node)
                    node.getPai().setCor("preto")
                    node.getPai().getPai().setCor("vermelho")
                    self.giroDireito(node.getPai().getPai())
            else:
                y = node.getPai().getPai().getFilhoEsquerdo()
                if y.getCor() == "vermelho":
                    node.getPai().setCor("preto")
                    y.setCor("preto")
                    node.getPai().getPai().setCor("vermelho")
                    node = node.getPai().getPai()
                else:
                    if node == node.getPai().getFilhoEsquerdo():
                        node = node.getPai()
                        self.giroDireito(node)
                    node.getPai().setCor("preto")
                    node.getPai().getPai().setCor("vermelho")
                    self.giroEsquerdo(node.getPai().getPai())
        self.getRaiz().setCor("preto")
            
    # Esse método está falhando        
    def deletarRB(self, node):
        if node.getFilhoEsquerdo() == self._nodeVazio or node.getFilhoDireito() == self._nodeVazio:
            y = node 
        else:
            y = self.sucessor(node)
        if y.getFilhoEsquerdo() == self._nodeVazio:
            x = y.getFilhoEsquerdo()
        else:
            x = y.getFilhoDireito()
        x.setPai(y.getPai())
        if y.getPai() == self._nodeVazio:
            self.setRaiz(x)
        else:
            if y == y.getPai().getFilhoEsquerdo():
                y.getPai().setFilhoEsquerdo(x)
            else:
                y.getPai().setFilhoDireito(x)
        if y != node:
            node.setValor(y.getValor())
        if y.getCor() == "preto":
            self.deletarFixup(x)
        return y  
    
    def deletarFixup(self, x):
        while x != self.getRaiz() and x.getCor() == "preto":
            if x == x.getPai().getFilhoEsquerdo():
                w = x.getPai().getFilhoDireito()
                if w.getCor() == "vermelho":
                    w.setCor("preto")
                    x.getPai().setCor("vermelho")
                    self.giroEsquerdo(x.getPai())
                    w = x.getPai().getFilhoDireito()
                if w.getFilhoEsquerdo().getCor() == "preto" and w.getFilhoDireito().getCor() == "preto":
                    w.setCor("vermelho")
                    x = x.getPai()
                else:
                    if w.getFilhoDireito().getCor() == "preto":
                        w.getFilhoEsquerdo().setCor("preto")
                        w.setCor("vermelho")
                        self.giroDireito(w)
                        w = x.getPai().getFilhoDireito()
                w.setCor(x.getPai().getCor())
                x.getPai().setCor("preto")
                w.getFilhoDireito().setCor("preto")
                self.giroEsquerdo(x.getPai())
                x = self.getRaiz()
            else:
                w = x.getPai().getFilhoEsquerdo()
                if w.getCor() == "vermelho":
                    w.setCor("preto")
                    x.getPai().setCor("vermelho")
                    self.giroDireito(x.getPai())
                    w = x.getPai().getFilhoEsquerdo()
                if w.getFilhoDireito().getCor() == "preto" and w.getFilhoEsquerdo().getCor() == "preto":
                    w.setCor("vermelho")
                    x = x.getPai()
                else:
                    if w.getFilhoEsquerdo().getCor() == "preto":
                        w.getFilhoDireito().setCor("preto")
                        w.setCor("vermelho")
                        self.giroEsquerdo(w)
                        w = x.getPai().getFilhoEsquerdo()
                w.setCor(x.getPai().getCor())
                x.getPai().setCor("preto")
                w.getFilhoEsquerdo().setCor("preto")
                self.giroDireito(x.getPai())
                x = self.getRaiz()
        x.setCor("preto")
                
    def pesquisar(self, valor):#Interativo
        raiz = self._raiz
        while raiz != self._nodeVazio and valor != raiz.getValor():
            if valor < raiz.getValor():
                raiz = raiz.getNoEsquerdo()
            else:
                raiz = raiz.getNoDireito()
        return raiz
    
    def minimo(self, raiz):
        while raiz.getNoEsquerdo() != self._nodeVazio:
            raiz = raiz.getNoEsquerdo()
        return raiz
    
    def maximo(self, raiz):
        while raiz.getNoDireito() != self._nodeVazio:
            raiz = raiz.getNoDireito()
        return raiz

    def sucessor(self, node):
        if node.getNoDireito() != self._nodeVazio:
            return self.minimo(node.getNoDireito())
        y = node.getNoPai()
        while y != self._nodeVazio and node == y.getNoDireito():
            node = y 
            y = y.getNoPai()
        return y
    
    def antecessor(self, node):
        if node.getNoEsquerdo() != self._nodeVazio:
            return self.maximo(node.getNoEsquerdo())
        y = node.getNoPai()
        while y != self._nodeVazio and node == y.getNoEsquerdo():
            node = y 
            y = y.getNoPai()
        return y 
    
    def giroEsquerdo(self, x):
        y = x.getFilhoDireito()
        x.setFilhoDireito(y.getFilhoEsquerdo())
        if y.getFilhoEsquerdo() != self.getVazio():
            y.getFilhoEsquerdo().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.getVazio():
            self.setRaiz(y)
        elif x == x.getPai().getFilhoEsquerdo():
            x.getPai().setFilhoEsquerdo(y)
        else:
            x.getPai().setFilhoDireito(y)
        y.setFilhoEsquerdo(x)
        x.setPai(y)

    def giroDireito(self, x):
        y = x.getFilhoEsquerdo()
        x.setFilhoEsquerdo(y.getFilhoDireito())
        if y.getFilhoDireito() != self.getVazio():
            y.getFilhoDireito().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.getVazio():
            self.setRaiz(y)
        elif x == x.getPai().getFilhoDireito():
            x.getPai().setFilhoDireito(y)
        else:
            x.getPai().setFilhoEsquerdo(y)
        y.setFilhoDireito(x)
        x.setPai(y)
    
    def percorrerEmOrdem(self, raiz, lista):
        if raiz != self._nodeVazio:
            self.percorrerEmOrdem(raiz.getNoEsquerdo(), lista)
            lista.append(str(raiz.getValor()))
            self.percorrerEmOrdem(raiz.getNoDireito(), lista)
            
    def percorrerPreOrdem(self, raiz, lista):
        if raiz != self._nodeVazio:
            lista.append(str(raiz.getValor()))
            self.percorrerPreOrdem(raiz.getFilhoEsquerdo(), lista)
            self.percorrerPreOrdem(raiz.getFilhoDireito(), lista)
            
    def percorrerPosOrdem(self, raiz, lista):
        if raiz != self._nodeVazio:
            self.percorrerPosOrdem(raiz.getNoEsquerdo(), lista)
            self.percorrerPosOrdem(raiz.getNoDireito(), lista)
            lista.append(str(raiz.getValor()))
        
tree = ArvoreRB()
lista = []
tree.inserirRB(25)
tree.inserirRB(20)
tree.inserirRB(30)
#tree.deletarRB(tree.pesquisar(25))
tree.percorrerPreOrdem(tree.getRaiz(), lista)
print(lista)
  