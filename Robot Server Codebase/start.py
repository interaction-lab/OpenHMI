import subprocess
import time
import sys
from datetime import datetime
from BlossomServer import BlossomServer

BLOSSOM_SETUP = 15 # seconds
CTRL_DIR = "../Robot Control Codebase"
HOST_NAME = "localhost"
HTTP_PORT = 8080
DEBOUNCE = 0.1 # seconds or None
DRY_RUN = False

PROCESS_ARGS = [
	"python", 
	"{0}/start.py".format(CTRL_DIR), 
	"-b" # no Web UI
]

PATH_MAPPINGS = { # (seq_name, duration)
	"/none" : ("reset", 0.5),
	"/nod" : ("yes", 3.7),
	"/shake" : ("no", 3.7),
	"/tilt" : ("happy_upside", 5.6),
}

def play_seq(proc, seq_name):
	print("Play Sequence:", seq_name)
	proc.stdin.write("s\n")
	proc.stdin.write("{0}\n".format(seq_name))

def quit(proc):
	proc.stdin.write("q\n")

def imitate_cb(proc):
	last_path = None
	last_time = datetime.min
	play_path = None
	play_time = datetime.min
	def callback(path):
		# Filter out invalid paths, like /favicon.ico
		if path not in PATH_MAPPINGS.keys():
			return

		nonlocal last_path
		nonlocal last_time
		nonlocal play_path
		nonlocal play_time
		time = datetime.now()
		req_time_diff = (time - last_time).total_seconds()
		last_time = time
		same_path = last_path == path
		last_path = path
		if DEBOUNCE and DEBOUNCE > 0:
			if not same_path:
				return
			if req_time_diff < DEBOUNCE:
				return

		seq_name, duration = PATH_MAPPINGS[path]
		play_time_diff = (time - play_time).total_seconds()
		if play_path == path and play_time_diff < duration:
			return
		play_path = path
		play_time = time
		
		play_seq(proc, seq_name)
	return callback

def run():
	with subprocess.Popen(
		PROCESS_ARGS,
		cwd=CTRL_DIR,
		stdin=subprocess.PIPE,
		stdout=sys.stdout,
		stderr=sys.stderr,
		text=True,
		universal_newlines=True,
		bufsize=1 # line buffered, so we do not need to call flush()
		) as proc:

		time.sleep(BLOSSOM_SETUP)
		
		cb = imitate_cb(proc)
		server = BlossomServer(cb, hostname=HOST_NAME, port=HTTP_PORT)
		server.run()

		quit(proc) # proc.kill()

def dry_run():
	class DummyWriter:
		def write(self, content):
			pass
	class DummyProc:
		def __init__(self):
			self.stdin = DummyWriter()
	proc = DummyProc()

	cb = imitate_cb(proc)
	server = BlossomServer(cb, hostname=HOST_NAME, port=HTTP_PORT)
	server.run()

def main():
	if DRY_RUN:
		dry_run()
	else :
		run()

if __name__ == "__main__":
	main()
