import string
import threading
import socket
 
observers = {}
data = {}
 
class gestionaClientes(threading.Thread):

	def __init__(self, socket):
		threading.Thread.__init__(self)
		self.conn = socket
		self.conectado = False

	def run(self):
		while True:
			self.data = self.conn.recv( 1024 )

			if 'CHANGE' in self.data:
				key = self.data.split(" ")[1]
				value = " ".join(self.data.split(" ")[2:])
				data[key] = value
				self.notify(key)
				print(data)

			if 'WATCH' in self.data:
				key = self.data.split(" ")[1]
				if key not in observers:
					observers[key] = [self.conn]
				else:
					observers[key].append(self.conn)
	 
	 
		self.conn.close() 
 
	def notify(self,key):
		if key in observers:
			for i in observers[key]:
					if i != self.conn:
						i.send("the new value for key "+key+" is "+data[key])


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ( socket.gethostname(), 9000 ) )
s.listen( 5 )
while(True):
	conn, addr = s.accept()
	gestionaClientes(conn).start()