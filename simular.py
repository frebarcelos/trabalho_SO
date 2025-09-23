from funcUtils import limpar_terminal
from processador import Processador
def simular():
    print("Iniciando simulação...")
    print("Carregando processos do arquivo JSON...")
    processador_execucao = Processador()
    processador_execucao.carregarProcessos('dadosSimulacao.json')
    print("Processos carregados:")
    tempo = True if input("Deseja Simular o Tempo ? (Y/n): ") == 'Y' else False
    print("Pressione Enter para iniciar a simulação em Fifo.")
    input()
    limpar_terminal()
    print("")
    print("")
    print("**********************************************************************")               
    print(f"**                   Simulação Utilizando Fifo                      **")
    print("**********************************************************************")
    print("")
    processador_execucao.executarProcessos(contarTempo=tempo)
    input("Simulação finalizada. Pressione Enter para simular utilizando  Prioridade (sem preempção).")
    limpar_terminal()
    print("**********************************************************************")               
    print(f"**        Simulação utilizando Prioridade (sem preempção)           **")
    print("**********************************************************************")
    print("")
    processador_execucao_prioridade = Processador()
    processador_execucao_prioridade.carregarProcessos('dadosSimulacao.json')
    processador_execucao_prioridade.executarProcessos(prioridade=True,contarTempo=tempo)
    
if __name__ == "__main__":
    simular()


