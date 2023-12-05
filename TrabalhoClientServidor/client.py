import socket  # Importa o módulo de socket para comunicação em rede
import sys  # Importa o módulo sys para manipular argumentos da linha de comando
import time  # Importa o módulo time para lidar com temporizações

host = '127.0.0.1'  # Define o endereço IP do servidor (localhost)
port = 12344  # Define o número da porta do servidor

# Cria um socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket ao servidor usando o endereço e a porta especificados
client.connect((host, port))

# Obtém o comando da linha de comando excluindo o nome do script (sys.argv[0])
command = ' '.join(sys.argv[1:])

# Verifica o primeiro argumento da linha de comando
if sys.argv[1] == 'list':  # Se o comando for 'list'
    # Envia o comando codificado para o servidor
    client.send(command.encode('utf-8'))
    # Recebe a lista de arquivos do servidor e converte de bytes para string
    file_list = client.recv(1024).decode('utf-8')
    # Exibe a lista de arquivos do servidor
    print(f"Arquivos no servidor: {file_list}")
elif sys.argv[1] == 'upload':  # Se o comando for 'upload'
    # Envia o comando codificado para o servidor
    client.send(command.encode('utf-8'))
    # Obtém o nome do arquivo do segundo argumento da linha de comando
    filename = sys.argv[2]
    print(filename)  # Exibe o nome do arquivo
    # Abre o arquivo no modo de leitura binária ('rb')
    with open(filename, 'rb') as file:
        # Lê o conteúdo do arquivo
        file_content = file.read()
        # Aguarda por 1 segundo (temporização)
        time.sleep(1)
        # Envia o conteúdo do arquivo para o servidor
        client.send(file_content)
    # Recebe a confirmação do servidor e exibe
    print(client.recv(1024).decode('utf-8'))
elif sys.argv[1] == 'rename':  # Se o comando for 'rename'
    # Envia o comando codificado para o servidor
    client.send(command.encode('utf-8'))
    # Recebe a resposta do servidor e exibe
    print(client.recv(1024).decode('utf-8'))
elif sys.argv[1] == 'delete':  # Se o comando for 'delete'
    # Envia o comando codificado para o servidor
    client.send(command.encode('utf-8'))
    # Recebe a resposta do servidor e exibe
    print(client.recv(1024).decode('utf-8'))
else:  # Se nenhum dos comandos acima corresponder
    print("Comando inválido")  # Exibe "Comando inválido"

# Fecha o socket do cliente
client.close()
