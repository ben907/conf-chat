
from peer import Peer

def main():
    print("=== Conf-Chat P2P Node ===")

    username = input("Enter username: ")

    port = int(input("Enter your listening port (e.g., 5000): "))
    peer = Peer(username, port)
    peer.start()

    print("\nCommands:")
    print("  connect <ip> <port>    - connect to another peer")
    print("  send <message>         - send message to connected peer")
    print("  exit                   - quit the chat")
    print("-----------------------------")

    while True:
        command = input("> ")

        if command.startswith("connect"):
            try:
                _, ip, port = command.split()
                peer.connect_to_peer(ip, int(port))
            except:
                print("Usage: connect <ip> <port>")

        elif command.startswith("send"):
            msg = command[5:]
            peer.send_message(msg)

        elif command == "exit":
            peer.stop()
            break

        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
