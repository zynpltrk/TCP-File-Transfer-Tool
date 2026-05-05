"""
creates a socket
binds to localhost and a port (like 12345)
listens
accepts one connection
prints “client connected”

"""

import socket

def start_server(host='127.0.0.1', port=12345):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            server_socket.bind((host,port))
            print(f"Server started on {host}:{port}")

            server_socket.listen()
            print("Waiting for a connection...")

            while True:
                conn, addr = server_socket.accept()
                with conn:
                    # print(f"Connected by {addr}")
                    # while True:
                    #     data= conn.recv(1024)
                    #     if not data:
                    #         break
                    #     print(f"Received: {data.decode()}")
                    #     conn.sendall(b"Message received")
                    with open("recSendMessage.txt", "wb") as file:
                        while True:
                            data=conn.recv(1024)
                            if not data:
                                break

                            file.write(data)
    except Exception as e:
        print(f"Server error: {e}")
if __name__=="__main__":
    start_server()
