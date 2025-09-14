from funcUtils import limpar_terminal
from processador import Processador
def simular():
    print("Iniciando simulação...")
    print("Carregando processos do arquivo JSON...")
    processador_execucao = Processador()
    processador_execucao.carregarProcessos('dadosSimulacao.json')
    print("Processos carregados:")
    print("Pressione Enter para iniciar a simulação em Fifo.")
    input()
    limpar_terminal()
    processador_execucao.executarProcessos()
    input("Simulação finalizada. Pressione Enter para simular utilizando  Prioridade (sem preempção).")
    limpar_terminal()
    print("Simulando utilizando Prioridade (sem preempção).")
    processador_execucao_prioridade = Processador()
    processador_execucao_prioridade.carregarProcessos('dadosSimulacao.json')
    processador_execucao_prioridade.executarProcessos(prioridade=True)
    
if __name__ == "__main__":
    simular()


