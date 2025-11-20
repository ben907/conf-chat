
# README.md

Conf-Chat is a small peer-to-peer (P2P) chat program written in Python.
Every instance acts as a peer



# peer.py

This file does the networking portion:

* Begins listening instance
* Accepts connection from peers
* allows users to connect to each other
* sending and receiving capabilities
* receiving messages are seperate, so each user has their own bank of messages to receive

---------------------------------------------------------------------------------

# chat.py

This file handles the user interface:

* prompt user login
* user can type three commands
* connection to other peers
* sending and receiving messages per user






# How to Run

1. Clone or download the repo
2. Make sure Python 3 is installed
3. Open the project in VS Code (or terminal)
4. Run `chat.py` in different terminals to simulate multiple peers



# How it Works

 -  enter username to "log in"
 -  connect to other peers by using "connect" command
 -  can send messages using the "send" command
 - can connect multiple users to a single port


# Example Commands
connect <ip> <port> - connect to port along with other users
send <message> - command to send message to all connected users
exit - exit chat room and stop receiving



