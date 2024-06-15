import os
from dotenv import load_dotenv
import socket
import my_kmnet

load_dotenv()


def tcp_server(host="0.0.0.0", port=12345):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    sock.bind(server_address)
    sock.listen(1)  # Listen for incoming connections

    print(f"TCP server up and listening on {host}:{port}")

    while True:
        connection, client_address = sock.accept()
        try:
            print(f"Connection from {client_address}")

            while True:
                data = connection.recv(2048)
                if not data:
                    break
                data_str = data.decode()
                commands = data_str.split("\n")

                for command in commands:
                    try:
                        parts = command.split(",")
                        call_type = parts[0]
                        function = parts[1]
                        params = parts[2:]
                        call_result = my_kmnet.my_kmnet_functions[function](*params)
                        # call_result = "Ok"
                        if call_type == "call_return":
                            connection.sendall(bytes(str(call_result), "utf-8"))
                        else:
                            connection.sendall(b"OK")
                    except Exception as call_error:
                        print("call_error: {}".format(call_error))
            my_kmnet.unmask_all()
        except Exception as _e:
            # print("connection error:", _e)
            my_kmnet.unmask_all()
        finally:
            print("Connection closed")
            connection.close()


if __name__ == "__main__":
    my_kmnet.init(
        os.environ["KMBOX_IP"], os.environ["KMBOX_PORT"], os.environ["KMBOX_MAC"]
    )
    my_kmnet.monitor("10000")

    try:
        tcp_server()
    except Exception as e:
        print("error:", e)
    finally:
        my_kmnet.unmask_all()
