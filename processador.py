from funcUtils import adiciona_zero_esquerda
from processo import Processo
import json
import time
class Processador ():   
    def __init__(self):
        self.listaProcessos = [];
        self.listaProcessosEmEspera = [];
        self.listaProcessosFinalizados = [];
        self.tempoAtual = 0
        self.processoEmExecusao = None    

    
    def carregarProcessos(self, caminhoListaProcessos):
        with open(caminhoListaProcessos, 'r', encoding='utf-8') as lista:
            lista_processos = json.load(lista)
            if len(lista_processos) > 0:
                lista_processos.sort(key=lambda p: p['at'])
                for processo in lista_processos:
                    novo_processo = Processo(nome=processo['nome'],at=processo['at'],pt=processo['pt'],pr=processo['pr'])
                    self.listaProcessos.append(novo_processo)
    
    def executarProcessos(self,contarTempo,prioridade=False):
        while len(self.listaProcessos) > len(self.listaProcessosFinalizados):                
            for i in range(0, len(self.listaProcessos)):                
                if (self.listaProcessos[i].at == self.tempoAtual):                            
                    self.listaProcessosEmEspera.append(self.listaProcessos[i])
            if prioridade:
                    self.listaProcessosEmEspera.sort(key=lambda p: p.pr,reverse=True)
            if len(self.listaProcessosEmEspera) > 0 and self.processoEmExecusao == None:               
                self.processoEmExecusao = self.listaProcessosEmEspera[0]
                self.listaProcessosEmEspera.pop(0)
                print("")
                print("")
                print("**********************************************************************")               
                print(f"**               Iniciando processo: {self.processoEmExecusao.nome} com {adiciona_zero_esquerda(self.processoEmExecusao.pt)} partes               **")
                print("**********************************************************************")                       
            
            if self.processoEmExecusao != None:  
                ptNumberExecution = (self.processoEmExecusao.pt - self.processoEmExecusao.rt) + 1              
                print(f"Tempo {adiciona_zero_esquerda(self.tempoAtual)}: Executando processo {self.processoEmExecusao.nome} || {adiciona_zero_esquerda(ptNumberExecution)} de {adiciona_zero_esquerda(self.processoEmExecusao.pt)} partes do processo ||  processos na fila: {['nome: ' + p.nome + ( f" pr: {p.pr}" if prioridade else '') for p in self.listaProcessosEmEspera]}")
                self.processoEmExecusao.rt -= 1                    
                if self.processoEmExecusao.rt == 0:
                    print("**********************************************************************")
                    print("**                       ATENÇÃO!!!                                 **")
                    print(f"**                  Processo finalizado {self.processoEmExecusao.nome}                          **")
                    print("**********************************************************************")
                    self.processoEmExecusao.tt = self.tempoAtual + 1 - self.processoEmExecusao.at
                    self.processoEmExecusao.wt = self.processoEmExecusao.tt - self.processoEmExecusao.pt 
                    self.listaProcessosFinalizados.append(self.processoEmExecusao)                
                    self.processoEmExecusao = None
            else:
                print(f"Tempo {adiciona_zero_esquerda(self.tempoAtual)}: CPU ociosa")
            if contarTempo:
                time.sleep(1)
            self.tempoAtual += 1
        print("")
        print("**********************************************************************")
        for i in range(len(self.listaProcessosFinalizados)):            
            print(f"**  Processo {self.listaProcessos[i].nome} || AT: {adiciona_zero_esquerda(self.listaProcessos[i].at)} || PT: {adiciona_zero_esquerda(self.listaProcessos[i].pt)} || PR: {adiciona_zero_esquerda(self.listaProcessos[i].pr)} || TT: {adiciona_zero_esquerda(self.listaProcessos[i].tt)} ||  WT: {adiciona_zero_esquerda(self.listaProcessos[i].wt)}  **")            
        
        print("**                                                                  **")
        print("**  Media tempo de espera: ", sum(p.wt for p in self.listaProcessosFinalizados) / len(self.listaProcessosFinalizados) ,"                                   **")
        print("**                                                                  **")
        print("**********************************************************************")        
    
    
