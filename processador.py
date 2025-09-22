from processo import Processo
import json
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
    
    def executarProcessos(self,prioridade=False):
        while len(self.listaProcessos) > len(self.listaProcessosFinalizados):                
            for i in range(0, len(self.listaProcessos)):                
                if (self.listaProcessos[i].at == self.tempoAtual):                            
                    self.listaProcessosEmEspera.append(self.listaProcessos[i])
            if prioridade:
                    self.listaProcessosEmEspera.sort(key=lambda p: p.pr)
            if len(self.listaProcessosEmEspera) > 0 and self.processoEmExecusao == None:               
                self.processoEmExecusao = self.listaProcessosEmEspera[0]
                self.listaProcessosEmEspera.pop(0)                       
            
            if self.processoEmExecusao != None:  
                ptNumberExecution = self.processoEmExecusao.pt - self.processoEmExecusao.rt + 1              
                print(f"Tempo {self.tempoAtual}: Executando processo {self.processoEmExecusao.nome} {ptNumberExecution}/{self.processoEmExecusao.pt} processos na fila: {['nome: ' + p.nome + ( f" prioridade: {p.pr}" if prioridade else '') for p in self.listaProcessosEmEspera]}")
                self.processoEmExecusao.rt -= 1                    
                if self.processoEmExecusao.rt == 0:
                    print("Finalizado processo ", self.processoEmExecusao.nome)
                    self.processoEmExecusao.tt = self.tempoAtual + 1 - self.processoEmExecusao.at
                    self.processoEmExecusao.wt = self.processoEmExecusao.tt - self.processoEmExecusao.pt 
                    self.listaProcessosFinalizados.append(self.processoEmExecusao)                
                    self.processoEmExecusao = None
            else:
                print(f"Tempo {self.tempoAtual}: CPU ociosa")
            self.tempoAtual += 1
        for i in range(len(self.listaProcessosFinalizados)):
            print(f"Processo {self.listaProcessos[i].nome} AT: {self.listaProcessos[i].at} PT: {self.listaProcessos[i].pt} PR: {self.listaProcessos[i].pr} TT: {self.listaProcessos[i].tt}, WT: {self.listaProcessos[i].wt}")
        print("Media tempo de espera: ", sum(p.wt for p in self.listaProcessosFinalizados) / len(self.listaProcessosFinalizados))        
    
    
