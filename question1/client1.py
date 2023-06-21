import socket

server_ip = '127.0.0.1'
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

client_name = input('Enter your name: ')
client_socket.send(client_name.encode())

welcome_message = client_socket.recv(1024).decode()
print(welcome_message)

# receive the quiz questions from the server and send answers
for i in range(3):
    question = client_socket.recv(1024).decode()
    print(question)
    client_answer = input('Enter your answer: ')
    client_socket.send(client_answer.encode())

    response = client_socket.recv(1024).decode()
    print(response)

score_message = client_socket.recv(1024).decode()
print(score_message)

client_socket.close()
