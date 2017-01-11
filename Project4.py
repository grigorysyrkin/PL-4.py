import threading, queue
try:
	import Queue
except:
	import queue as Queue

class Token:
	"""docstring for Token"""
	def __init__(self, data, recipient):
		# super(Token, self).__init__()
		self.data= data
		self.recipient = recipient

def thread(i, t):
	global q
	if t.recipient == i:
		string = "Token has reached the recipient"
		q.put(string)
	else:
		# print("nextIteration")
		print(5)
		nextThread = threading.Thread(target=thread, name="thr", args=(i + 1, t))
		nextThread.start()

token = Token(3, 5)
q = Queue.Queue(10)

initThread = threading.Thread(target=thread, args=(1, token))
initThread.start()
print(q.get())