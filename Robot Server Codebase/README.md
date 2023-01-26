# Introduction

This folder contains a program that bridging OpenSense and Blossom.
We call it `OpenSense-Blossom Bridge` (or `Bridge` in-short).

# How It Works

It starts Blossom in a sub-process then starts an HTTP web server.
Whenever the server receives a request, it asks Blossom play a sequence through standard input.
With that, OpenSense can send messages to Blossom by making HTTP requests.

# Prerequisites

Here, we suppose your Blossom can be driven by its official software.
If you have not completed it, you can follow the setup steps listed on its [official repository](https://github.com/hrc2/blossom-public). *That repository is also included in this OpenHMI repository.*

Basically, by following those steps, you (optionally) create a virtual environment and download some python modules.
Then you got an application (or applications) that can drive Blossom move.
However, in this example, we only need the application's Command Line Interface (CLI). So, if its Web UI or Mobile Application is not working, you do not need to make them work.
Its CLI lets you type in a sequence name and it will play that sequence.

> By the way, if you run Blossom CLI on Windows and it posts messages like "Error opening port, try: sudo chmod 777 COM<a_port_number>" and refuses to scan remaining serial ports.
> And you know your Blossom is assigned a serial port number larger than the port in the message.
> You can comment out the line `127` of its `config.py` (e.g. turning "`sys.exit(1)`" to "`# sys.exit(1)`").

# How to Run It

The Blossom's official CLI software will be referred as `Blossom driver` in this manual to distinguish it from Blossom robot hardware or other softwares.

This OpenSense-Blossom Bridge is simple, and it only relies on python's [Standard Libraries](https://docs.python.org/3/library/).
That means you **do not** need to install additional python modules.

To run the Bridge, just run `start.py` in this folder (e.g. "`python start.py`"). *Please make sure your command shell's current working directory is set to this folder.*

> If you want to run Blossom driver in a virtual python environment. Depending on the virtual environment module/software's implementation, you may need to either run the Bridge in that same virtual environment, or change the python command using an argument, or modify the code.

You may want to check its supported arguments, you can use "`-h`" argument to get a list of them (e.g. "`python start.py -h`").
The Bridge will wait for Blossom driver for seconds (default to 15) before it spins up a web server.

To test the Bridge, open your web browser, and access links like [localhost:8080/nod](http://localhost:8080/nod), [localhost:8080/shake](http://localhost:8080/shake), [localhost:8080/tilt](http://localhost:8080/tilt). You can keep refreshing the web page (by pressing F5 or refresh button) to simulate a continuous recognition result data stream.

To stop the Bridge, press `Ctrl-C`.

Once you have the Bridge run, you can set it running aside and move on to [steps of configuring OpenSense](../OpenSense%20Workspace/README.md).
