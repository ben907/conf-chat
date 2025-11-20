
# README.md

**Conf-Chat** is a small peer-to-peer (P2P) chat program written in Python.
Every instance acts as a **peer**, so there’s no central server—peers talk directly to each other.


---

# peer.py

This file does the networking stuff:

* Starts a listening socket
* Accepts connections from other peers
* Lets you connect to other peers
* Sends and receives messages
* Runs receiving messages in a separate thread so it doesn’t block

---

# chat.py

This file handles the user interface:

* Shows a login prompt
* Lets you type commands
* Lets you connect to other peers
* Lets you send messages

---

# Networking

* Uses Python’s `socket` library
* Each peer listens on a port you choose
* You connect to others using their IP + port
* No server—everyone is equal

---

# Requirements

* Python 3.7 or higher
* No extra libraries
* Works in VS Code, PyCharm, or any terminal

---

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



---

# Summary

This is a simple Python P2P chat that works, is easy to run, and can be extended with more features. Perfect for learning how peer-to-peer messaging works.

