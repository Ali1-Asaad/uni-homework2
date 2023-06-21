import socket
import threading
import random

server_ip = '127.0.0.1'
server_port = 5555

QUIZ_QUESTIONS = [
    {'question': 'What is the capital of France?', 'answer': 'Paris'},
    {'question': 'What is the largest planet in our solar system?', 'answer': 'Jupiter'},
    {'question': 'What is the boiling point of water?', 'answer': '100 degrees Celsius'}
]

client_scores = {}

# handle clients connection
def handle_client(client_socket):

    client_name = client_socket.recv(1024).decode()


    client_socket.send(f'Welcome to the quiz, {client_name}!\n'.encode())

    # send the quiz questions to the client
    k = 0
    for i, question in enumerate(QUIZ_QUESTIONS):
        client_socket.send(f'Question {i+1}: {question["question"]}\n'.encode())

        client_answer = client_socket.recv(1024).decode().strip()

        # check if the client's answer is correct
        if client_answer.lower() == question['answer'].lower():
            client_socket.send('Correct!\n'.encode())

            client_scores[client_name] = client_scores.get(client_name, 0) + 1
            k = k + 1
        else:
            client_socket.send(f'Incorrect! The correct answer is {question["answer"]}.\n'.encode())
    if k == 0 :
        client_scores[client_name] = client_scores.get(client_name, 0) + 0
    # send the client's score to the client
    client_socket.send(f'Thank you for playing, {client_name}! Your score is {client_scores[client_name]}.\n'.encode())

    client_socket.close()

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))
server_socket.listen()

print(f'Server listening on {server_ip}:{server_port}')

while True:
    client_socket, client_address = server_socket.accept()

    # create a new thread to handle the client connection
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
