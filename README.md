# ChatApp — Python

## What this preserves

- One server and one client connection at a time (as in the original Java source)
- Two-way console chat
- TCP socket communication on port `1111`
- Separate reader thread and input/writer loop
- Type `exit` to end the chat

## Requirements

Python 3.9+; no third-party packages are required.

## Run on one computer

1. Open a terminal in this folder and start the server:

   ```bash
   python server.py
   ```

2. Open a second terminal and start the client:

   ```bash
   python client.py
   ```

3. Type messages in either terminal. Enter `exit` to leave.

## Run on two computers on the same network

- Start `server.py` on the host computer.
- Find the host's local IP address.
- Edit `SERVER_HOST` in `client.py` to that IP, e.g. `192.168.1.203`.
- Allow inbound TCP port `1111` through the server computer's firewall.
- Run `client.py` on the other computer.

The server binds to `0.0.0.0:1111` so it can accept connections through its network interfaces. The client defaults to `127.0.0.1` for easy same-computer testing.

## Files

- `server.py` — server side
- `client.py` — client side
- `README.md` — instructions

This is a basic learning project and does not provide encryption, authentication, or multiple simultaneous clients.
