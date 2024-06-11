import os

from dotenv import load_dotenv
import socket

import my_kmnet

load_dotenv()


def udp_server(host="127.0.0.1", port=12345):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host, port)
    sock.bind(server_address)

    print(f"UDP server up and listening on {host}:{port}")

    while True:
        data, address = sock.recvfrom(2048)
        data_str = data.decode()
        commands = data_str.split("\n")

        for command in commands:
            try:
                parts = command.split(",")
                call_type = parts[0]
                function = parts[1]
                params = parts[2:]
                call_result = my_kmnet.my_kmnet_functions[function](*params)
                if call_type == "call_return":
                    sock.sendto(bytes(str(call_result), "utf-8"), address)
            except Exception as call_error:
                print(call_error)


if __name__ == "__main__":
    my_kmnet.init(
        os.environ["KMBOX_IP"], os.environ["KMBOX_PORT"], os.environ["KMBOX_MAC"]
    )
    my_kmnet.monitor("10000")

    try:
        udp_server()
    except Exception as e:
        print(e)
        my_kmnet.unmask_all()
