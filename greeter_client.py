from __future__ import print_function
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = helloworld_pb2_grpc.GreeterStub(channel)
		response = stub.SayHello(helloworld_pb2.HelloRequest(name='SHAHRIAR'))
	print("Greeter Client Received: "+ response.message )

if __name__ == '__main__':
	logging.basicConfig()
	run()