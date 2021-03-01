
# import socket

# a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# location = ("127.0.0.1", 80)

# result_of_check = a_socket.connect_ex(location)


# if result_of_check == 0:

#     print("Port is open")

# else:

#     print("Port is not open")

import socket
from contextlib import closing


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        # pick a free port between 1024 and 65535
        s.bind(('localhost', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(s.getsockname()[1])
        return s.getsockname()[1]


# find_free_port()
