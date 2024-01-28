# test_client.py
import pytest
import socket
from unittest.mock import MagicMock
from unittest.mock import patch
from client import Client

@patch('socket.socket')
def test_start_client(mock_socket_class):
    mock_client_socket = MagicMock()
    mock_socket_class.return_value = mock_client_socket
    mock_client_socket.recv.side_effect = [b"Hello from server.", b""]

    client = Client("127.0.0.1", 8080)
    client.start()

    mock_socket_class.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
    mock_client_socket.connect.assert_called_once_with(("127.0.0.1", 8080))
    assert mock_client_socket.sendall.call_count == 1
    assert mock_client_socket.recv.call_count == 1 

@patch('socket.socket')
def test_send_message(mock_socket_class):
    mock_client_socket = MagicMock()
    mock_socket_class.return_value = mock_client_socket

    client = Client("127.0.0.1", 8080)
    client.send_message("Hello from client.")

    mock_client_socket.sendall.assert_called_once_with(b"Hello from client.")

@patch('socket.socket')
def test_stop_client(mock_socket_class):
    mock_client_socket = MagicMock()
    mock_socket_class.return_value = mock_client_socket

    client = Client("127.0.0.1", 8080)
    client.stop()

    mock_client_socket.close.assert_called_once()