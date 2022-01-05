#!/usr/bin/env python3

import argparse
import grpc
import kv_pb2
import kv_pb2_grpc


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')
subparsers.required = True
parser_insert = subparsers.add_parser('insert')
parser_insert.add_argument('key', type=str)
parser_insert.add_argument('value', type=str)
parser_lookup = subparsers.add_parser('lookup')
parser_lookup.add_argument('key', type=str)
parser_keys = subparsers.add_parser('keys')

args = parser.parse_args()

# TODO: connect to the server and execute RPCs

if args.command == 'insert':
    pass
elif args.command == 'lookup':
    pass
elif args.command == 'keys':
    pass
