class Processo ():
    nome = ''
    at = 0  #Tempo de chegada
    pt = 0  #Tempo de processamento
    pr = 0  #prioridade
    rt = 0  #Tempo restante
    wt = 0  #Tempo de espera
    tt = 0  #Tempo total 
    
    def __init__(self, nome, at, pt, pr):
        self.nome = nome  
        self.at = at     
        self.pt = pt      
        self.pr = pr     
        self.rt = pt      
        self.wt = 0       
        self.tt = 0       
