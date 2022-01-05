#!/usr/bin/env python3

import argparse
import codecs
import socket

def create_response(command: str, text: str):
    # TODO: implement responses for commands
    response = f'Warning: command {command} not implemented'

    return response

def client(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while True:
            command = input('Enter command: ')
            text = input('Enter text: ')

            sock.sendto(f'{command}|:|{text}'.encode(), (host, port))
            payload, server = sock.recvfrom(4096)
            print(payload.decode())

def server(host: str, port: int):
    # TODO: create socket and bind it to the endpoint

        while True:
            # TODO: receive request

            response = create_response(command, text)

            # TODO: send response

parser = argparse.ArgumentParser(description='Client and server for UDP echo', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--endpoint', type=str, default='localhost:12110', help='Endpoint on which the server runs or to which the client connects')
subparsers = parser.add_subparsers(dest='{client, server}')
subparsers.required = True
parser_client = subparsers.add_parser('client')
parser_client.set_defaults(func=client)
parser_server = subparsers.add_parser('server')
parser_server.set_defaults(func=server)

args = parser.parse_args()
host = args.endpoint.split(':')[0]
port = int(args.endpoint.split(':')[1])

args.func(host, port)
