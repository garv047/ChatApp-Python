
import socket
import threading

SERVER_HOST = "127.0.0.1"  # Change to server's IP for another computer
SERVER_PORT = 1111


def receive_messages(client_socket):
    """Receive messages from the server."""
    try:
        while True:
            message = client_socket.recv(1024)

            if not message:
                print("\nServer disconnected.")
                break

            message = message.decode("utf-8").strip()

            if message.lower() == "exit":
                print("\nServer ended the chat.")
                break

            print(f"\nServer: {message}")

    except OSError:
        pass


def main():
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to server!")
        print("Type 'exit' to leave the chat.\n")

        # Start a separate thread to receive messages
        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,),
            daemon=True
        )
        receive_thread.start()

        # Send messages to the server
        while True:
            message = input("You: ")

            client_socket.sendall(
                (message + "\n").encode("utf-8")
            )

            if message.lower() == "exit":
                break

    except ConnectionRefusedError:
        print("Could not connect. Make sure the server is running.")

    except OSError as error:
        print("Connection error:", error)

    finally:
        client_socket.close()
        print("Client closed.")


if __name__ == "__main__":
    main()
