# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer

bodyTemplate = r"<html><head><title>Notification Received</title></head><body><p>Request Path: %s</p></body></html>"

class BlossomHandler(BaseHTTPRequestHandler):

	def __init__(self, callback, *args):
		self._callback = callback
		BaseHTTPRequestHandler.__init__(self, *args)

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		body = bodyTemplate % self.path
		bodyBinary = bytes(body, "utf-8")
		self.wfile.write(bodyBinary)

		if self._callback and callable(self._callback):
			self._callback(self.path)

class BlossomServer:

	def __init__(self, callback, hostname = "localhost", port=80):
		self._hostname = hostname
		self._port = port
		def handler(*args):
			BlossomHandler(callback, *args)
		self._server = HTTPServer((self._hostname, self._port), handler)

	def run(self):
		print("Server started at http://%s:%s" % (self._hostname, self._port))
		with self._server:
			try:
				self._server.serve_forever()
			except KeyboardInterrupt:
				pass
		print("Server stopped.")

if __name__ == "__main__":	 
	callback = lambda p : print(p)
	web_server = BlossomServer(callback)
	web_server.run()
