# test_server.py
import pytest
import socket
from unittest.mock import MagicMock
from unittest.mock import patch
from pysocket.server import Server

@patch('socket.socket')
def test_start_server(mock_socket_class):
    mock_server_socket = MagicMock()
    mock_socket_class.return_value = mock_server_socket
    mock_connection = MagicMock()
    mock_server_socket.accept.return_value = (mock_connection, ('127.0.0.1', 8080))
    mock_connection.recv.side_effect = [b"Hello from client.", b""]

    server = Server("127.0.0.1", 8080)
    server.start()

    mock_socket_class.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
    mock_server_socket.bind.assert_called_once_with(("127.0.0.1", 8080))
    mock_server_socket.listen.assert_called_once()
    assert mock_server_socket.accept.call_count == 1
    assert mock_connection.sendall.call_count == 1
    assert mock_connection.recv.call_count == 1