# -*- coding:utf-8 -*-
import socket


def f1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 8889))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print(data)
                if not data:
                    break
                conn.send(data)


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
