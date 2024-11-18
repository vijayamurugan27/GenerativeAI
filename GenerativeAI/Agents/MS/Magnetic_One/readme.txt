It is a more generalist task agent from Microsoft.

It has five Agents
 
1) Orchestrator. Main agent that orchestrates the other four Agents.
2) Web surfer. - Surf the web for more information.
3) File Surfer. - surfing the files.
4) Coder. - for coding
5) Computer Terminal. - for running the code.

when a task is given.
	1) Reading an image, 
	2) Writing a python code. 
	3) Running a python code.
	4) using the output from the python code. A pdf document.
	5) Reading he C++ source code, and compiling the code, running it, and returning the answer.

consider this kind of complex task.
	File surfer to locate the file and reading the image.
	Coder agent codes the python code.
	terminal agent runs the code.
	using the web surfer to navigating to the URL, and extract the C++ code
	Coder to analyse the C++ code.
	the Terminal agent to execute the code.


if a task is given to Orchestrator agent , 
	it prepares the list of steps to steps involved to complete the task.
	also it check for all the tasks are being completed, is the progress being made, 
	what is the next speaker and what is the next speaker instruction.
	this process goes in a loop, when even a task comes to the Orchestrator.

Based on the next speaker and the next speaker instruction , 
the orchestrator it sends information to the relevant agent to the relevant perform task.
once after the subtask. is complete. and marked as done. And the whole task is complete.






