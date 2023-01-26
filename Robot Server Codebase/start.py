# -*- coding: utf-8 -*-

import subprocess
import time
import sys
import argparse
from datetime import datetime
from BlossomServer import BlossomServer

PATH_MAPPINGS = {
	"/none" : ("reset", 0.5),
	"/nod" : ("yes", 3.7),
	"/shake" : ("no", 3.7),
	"/tilt" : ("happy_upside", 5.6),
}
"""
Hard coded mappings of HTTP request paths and Blossom sequences.
Item format is (seq_name, duration_in_seconds).
"""

def play_seq(proc, seq_name):
	"""Send message to Blossom to play a sequence."""
	print("Play Sequence:", seq_name)
	proc.stdin.write("s\n")
	proc.stdin.write("{0}\n".format(seq_name))

def quit(proc):
	"""Send message to Blossom to exit."""
	proc.stdin.write("q\n")

def seq_cb(proc, debouncing = None):
	"""
	Creates a callable for the server's request handler.
	The callable will ask Blossom play sequences based on in-coming request paths.
	"""
	last_path = None
	last_time = datetime.min
	play_path = None
	play_time = datetime.min

	def callback(path):
		# Filter out invalid paths, like / and /favicon.ico
		if path not in PATH_MAPPINGS.keys():
			return

		# Debouncing
		nonlocal last_path
		nonlocal last_time
		time = datetime.now()
		req_time_diff = (time - last_time).total_seconds()
		last_time = time
		same_path = last_path == path
		last_path = path
		if debouncing and debouncing > 0:
			if not same_path:
				return
			if req_time_diff < debouncing:
				return

		seq_name, duration = PATH_MAPPINGS[path]

		# Preventing a sequence being started again while it is playing
		nonlocal play_path
		nonlocal play_time
		play_time_diff = (time - play_time).total_seconds()
		if play_path == path and play_time_diff < duration:
			return
		play_path = path
		play_time = time
		
		# Play the sequence
		play_seq(proc, seq_name)

	return callback

def run(args):
	"""Run Blossom and server."""
	process_args = [
		"python", 
		"{0}/start.py".format(args.ctrl_dir), 
		"-b", # We do not use its Web UI
	]
	with subprocess.Popen(
		process_args,
		cwd=args.ctrl_dir,
		stdin=subprocess.PIPE,
		stdout=sys.stdout,
		stderr=sys.stderr,
		text=True,
		universal_newlines=True,
		bufsize=1 # line buffered mode, so we do not need to call flush()
		) as proc:

		print("Waiting Blossom driver for {0} second(s).".format(args.setup_time))
		time.sleep(args.setup_time)
		
		callback = seq_cb(proc, args.debouncing)
		server = BlossomServer(callback, hostname=args.hostname, port=args.http_port)
		server.run()

		print("Shutting down Blossom.")
		quit(proc) # or use proc.kill()

def dry_run(args):
	"""Run the server only. This method is for testing."""
	class DummyWriter:
		def write(self, content):
			pass
	class DummyProc:
		def __init__(self):
			self.stdin = DummyWriter()
	proc = DummyProc()

	callback = seq_cb(proc, args.debouncing)
	server = BlossomServer(callback, hostname=args.hostname, port=args.http_port)
	server.run()

def get_args():
	"""Provide argument definitions and parse arguments."""
	parser = argparse.ArgumentParser(
		prog="OpenSense-Blossom Bridge",
		description="Runs an HTTP server to bridging OpenSense and Blossom (single-way) data transmission."
	)
	parser.add_argument(
		"-n", 
		"--dry_run", 
		action="store_true", 
		dest="dry_run", 
		help="Run the server without running Blossom driver. Handy for testing.",
	)
	parser.add_argument(
		"-p",
		"--port",
		metavar="PORT",
		action="store",
		type=int,
		default=8080,
		dest="http_port",
		help="The port number that the server listens to. Default to 8080.",
	)
	parser.add_argument(
		"-a",
		"--address",
		action="store",
		type=str,
		default="localhost",
		dest="hostname",
		help="Hostname of the server. Default to localhost.",
	)
	parser.add_argument(
		"-d",
		"--debouncing",
		action="store",
		type=float,
		dest="debouncing",
		help="Time in seconds used for command debouncing, or None to disable. Default to None.",
	)
	parser.add_argument(
		"-b",
		"--blossom",
		action="store",
		type=str,
		default="../Robot Control Codebase",
		dest="ctrl_dir",
		help="Blossom driver directory, where its 'start.py' located. Default to '../Robot Control Codebase'.",
	)
	parser.add_argument(
		"-s",
		"--setup",
		action="store",
		type=float,
		default=15,
		dest="setup_time",
		help="Wait time in seconds for letting Blossom driver initialize. Default to 15.",
		# For simplicity, we are not detecting Blossom's state from its output.
	)
	args = parser.parse_args()
	return args

def main():
	args = get_args()
	if args.dry_run:
		print("Running without Blossom.")
		dry_run(args)
	else :
		run(args)

if __name__ == "__main__":
	main()
