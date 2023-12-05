import socket # Importa o módulo de socket para comunicação em rede
import os #Importa o modulo 'os' que fornece uma interface para interagir com o sistema operacional subjacente

host = '127.0.0.1'  
port = 12344

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP/IP
server.bind((host, port))  # Liga o servidor ao host e à porta especificada
server.listen(1)  # Escuta por conexões, aceitando até 1 conexão pendente

print(f"Servidor ativo em {host}:{port}")

while True:  # Loop infinito para aceitar conexões repetidamente
    client, addr = server.accept()  # Aceita a conexão do cliente
    print(f"Aceita a conexão de {addr}")

    data = client.recv(1024).decode('utf-8')  # Recebe os dados do cliente

    if data == 'list':  # Se o cliente solicitar a lista de arquivos
        file_list = os.listdir('.')  # Obtém a lista de arquivos no diretório atual
        client.send(str(file_list).encode('utf-8'))  # Envia a lista de arquivos de volta ao cliente
    elif data.startswith('upload'):  # Se o cliente solicitar upload de arquivo
        filename = data.split(' ')[1]  # Extrai o nome do arquivo do comando 'upload'
        data = client.recv(1024)  # Recebe os dados do arquivo
        with open(filename, 'wb') as file:  # Abre o arquivo para escrita binária
            file.write(data)  # Escreve os dados recebidos no arquivo
        client.send('Arquivo recebido com sucesso'.encode('utf-8'))  # Confirmação ao cliente
    elif data.startswith('rename'):  # Se o cliente solicitar renomear um arquivo
        old_name, new_name = data.split(' ')[1], data.split(' ')[2]  # Extrai os nomes do comando 'rename'
        os.rename(old_name, new_name)  # Renomeia o arquivo
        client.send('Arquivo renomeado com sucesso'.encode('utf-8'))  # Confirmação ao cliente
    elif data.startswith('delete'):  # Se o cliente solicitar deletar um arquivo
        filename = data.split(' ')[1]  # Extrai o nome do arquivo do comando 'delete'
        os.remove(filename)  # Remove o arquivo
        client.send('Arquivo deletado com sucesso'.encode('utf-8'))  # Confirmação ao cliente

    client.close()  # Fecha a conexão com o cliente
