# biblioteca para trabalhar com threads
import threading
# biblioteca para simular tempo.
import time

# Função de cada thread
def imprimir_sequencia(inicio, fim, atraso):
    # pega o nome da thread automaticamente
    nome = threading.current_thread().name  

    # mensagem de início
    print(f"{nome} começou")

    # loop que vai do número inicial até o final
    for numero in range(inicio, fim + 1):
        print(f"{nome}: {numero}")  # mostra o número no console
        time.sleep(atraso)  # pausa um pouco antes de mostrar o próximo número

    # mensagem de fim
    print(f"{nome} terminou")


def main():
    # Criando duas threads:
    # - a primeira vai rodar de 1 a 10
    # - a segunda vai rodar de 50 a 60
    t1 = threading.Thread(target=imprimir_sequencia, name="Thread-1", args=(1, 10, 0.5))
    t2 = threading.Thread(target=imprimir_sequencia, name="Thread-2", args=(50, 60, 0.5))

    # Iniciando as threads, elas rodam ao mesmo tempo.
    t1.start()
    t2.start()

    # faz o programa principal esperar até as threads terminarem
    t1.join()
    t2.join()

    # mensagem de finalização 
    print("Programa finalizado!")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
