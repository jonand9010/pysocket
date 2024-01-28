# test_integration.py
import pytest
import threading
from server import Server
from client import Client

def test_client_server_integration():
    # Start the server in a separate thread
    server = Server("127.0.0.1", 8080)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # Start the client in the main thread
    client = Client("127.0.0.1", 8080)
    client.start()

    # Add assertions to check that the client and server are communicating correctly
    assert client.last_received_message == "Hello from server."
    assert server.last_received_message == "Hello from client."


    # Stop the server and client
    client.stop()
    server.stop()

    # Wait for the server thread to finish
    server_thread.join()