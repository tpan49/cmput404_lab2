import socket

BYTES_TO_READ =  4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connect by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)
    return

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)
    return


start_server()