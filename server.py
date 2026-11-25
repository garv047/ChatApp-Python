
import socket
import threading

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 1111


def receive_messages(client_socket):
    """Receive messages from the client."""
    try:
        while True:
            message = client_socket.recv(1024)

            if not message:
                print("\nClient disconnected.")
                break

            message = message.decode("utf-8").strip()

            if message.lower() == "exit":
                print("\nClient ended the chat.")
                break

            print(f"\nClient: {message}")

    except OSError:
        pass


def main():
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print(f"Server started on port {SERVER_PORT}")
    print("Waiting for a client to connect...")

    client_socket, client_address = server_socket.accept()

    print(f"Client connected: {client_address}")
    print("Type 'exit' to end the chat.\n")

    # Start a thread to receive messages
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client_socket,),
        daemon=True
    )
    receive_thread.start()

    # Send messages to the client
    try:
        while True:
            message = input("You: ")

            client_socket.sendall(
                (message + "\n").encode("utf-8")
            )

            if message.lower() == "exit":
                break

    except OSError as error:
        print("Connection error:", error)

    finally:
        client_socket.close()
        server_socket.close()
        print("Server closed.")


if __name__ == "__main__":
    main()

