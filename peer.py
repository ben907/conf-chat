

import socket
import threading

class Peer:
    def __init__(self, username, port):
        self.username = username
        self.port = port
        self.running = True
        self.connections = []  # list of connected sockets

    # -------------------------
    # Start listening for peers
    # -------------------------
    def start(self):
        listener = threading.Thread(target=self.listen_for_peers)
        listener.daemon = True
        listener.start()
        print(f"[INFO] Peer '{self.username}' listening on port {self.port}")

    # Listen for incoming connections
    def listen_for_peers(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", self.port))
        server.listen(5)

        while self.running:
            try:
                conn, addr = server.accept()
                print(f"[INFO] Connected by {addr}")
                self.connections.append(conn)
                threading.Thread(target=self.handle_peer, args=(conn,)).start()
            except:
                break

    # Handle messages from connected peers
    def handle_peer(self, conn):
        while self.running:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"\n[MSG] {data.decode()}")
            except:
                break

    # -------------------------
    # Connect to another peer
    # -------------------------
    def connect_to_peer(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            self.connections.append(s)
            print(f"[INFO] Connected to peer at {ip}:{port}")
            threading.Thread(target=self.handle_peer, args=(s,)).start()
        except:
            print("[ERROR] Could not connect")

    # -------------------------
    # Send a message
    # -------------------------
    def send_message(self, message):
        full_message = f"{self.username}: {message}"
        for conn in self.connections:
            try:
                conn.send(full_message.encode())
            except:
                pass

    # -------------------------
    # Stop peer
    # -------------------------
    def stop(self):
        self.running = False
        for c in self.connections:
            try:
                c.close()
            except:
                pass
        print("[INFO] Peer stopped")
