"""
Client side setup
"""
import socket

def create_tcp_client(server_ip: str, server_port: int):
    #Validate port range
    if not(0 < server_port < 65536):
        raise ValueError("Port number must be between 1 and 65535.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        try:
            print(f"Connecting to {server_ip}:{server_port}...")
            client_socket.connect((server_ip,server_port))
            print("Connected successfully.")

            # message="Hello from client!"
            # client_socket.sendall(message.encode('utf-8'))
            # print(f"Sent: {message}")
            
            file_path="sendMessage.txt"
            with open(file_path, "rb") as file:
                while True:
                    chunk=file.read(1024)

                    if not chunk:
                        break

                    client_socket.sendall(chunk)
            print("File sent successfully.")

            # response=client_socket.recv(1024)
            # if not response:
            #     print("No data received from server.")
            # else:
            #     print(f"Received: {response.decode('utf-8',errors='replace')}")

        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            print("Closing connection.")

if __name__=="__main__":
    SERVER_IP="127.0.0.1" #LOCALHOST
    SERVER_PORT=12345 #NEEDS TO MATCH LISTENING PORT ON SERVER

    try:
        create_tcp_client(SERVER_IP, SERVER_PORT)
    except ValueError as ve:
        print(f"Invalid input: {ve}")