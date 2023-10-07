import socket
import time
import struct


class TCPScan:
	@staticmethod
	def scan(port, ip, timeout=5, stealth = False):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(timeout)

		if stealth:
			# ACK packet
			seq_num = 1000
			ack_num = 500
			ack_packet = struct.pack('!HHLLBBHHH', 8080, 80, seq_num, ack_num, 5<<4, 0, 0, 0, 0)

			# RST packet
			seq_num = 2000
			rst_packet = struct.pack('!HHLLBBHHH', 8080, 80, seq_num, 0, 5<<4, 0, 0, 0, 0)

		msg = b'test'

		start = time.time()

		sock.connect((ip, port))
		sock.send(msg)
		try:
			data = sock.recv(1024)
			end = time.time()
			elapsed = end - start
			print(f'{data.decode()} {elapsed}')
		#except Exception as e:
		#	print(f'Exception: {e}')
		finally:

			sock.close()


# Example
# import socket
# import struct
#
# # create a TCP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # connect to a remote server
# server_address = ('127.0.0.1', 8080)
# sock.connect(server_address)
#
# # construct an ACK packet
# seq_num = 1000
# ack_num = 500
# ack_packet = struct.pack('!HHLLBBHHH', 8080, 80, seq_num, ack_num, 5<<4, 0, 0, 0, 0)
#
# # send the ACK packet
# sock.send(ack_packet)
#
# # construct a RST packet
# seq_num = 2000
# rst_packet = struct.pack('!HHLLBBHHH', 8080, 80, seq_num, 0, 5<<4, 0, 0, 0, 0)
#
# # send the RST packet
# sock.send(rst_packet)
#
# # close the socket
# sock.close()