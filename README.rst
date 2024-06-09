============
The Scenario
============
We've been asked to create a tool that will export a system's user information into formats that various other departments can use. The tool will be able to export usernames, IDs, home directories, and shells in either JSON or CSV format. No information about system users themselves will be included in the files. By default, the Python tool will display the information as JSON to stdout, but the --format flag will allow a person to specify CSV as an alternative export type. Additionally, if we want the information going to a file instead of stdout, we can specify it by using the --path flag.

==========
Objectives
==========
We need to accomplish a few things before we can call them done. To finish them all, we'll be working from this list:

* Create package
* Implement CLI interface
* Format user information
* Write JSON and CSV
* Wire the pieces together
* Install the hr tool

==================
Create the Package
==================
We're in our home directory, /home/user/. If we do a quick ls, we'll see our home directory is empty. Let's start right off by making another directory and getting into it:

>>> [user@$host]$ mkdir hr
>>> [user@$host]$ cd hr

Then we'll make a spot for our code:

>>> [user@$host hr]$ mkdir -p src/hr
>>> [user@$host hr]$ touch src/hr/__init__.py
>>> [user@$host hr]$ touch README.rst

We don't necessarily need to do all of this, but this is how to make a bonafide Python package we might share with other people.

Because we want to work on this in isolation, in case we have some dependencies that might differ from the installed environment, we're going to use pipenv, which creates a virtual environment. Fire that up with this:

>>> [user@$host hr]$ pipenv --python python3.7

We'll see a bunch of output, ending with Creating a Pipfile for this project...

Now, in /home/user/hr/, if we run `pipenv shell`, we can actually activate the environment. The prompt will change, and now we'll see our virtualenv name preceding the rest of it:

>>> (hr) [user@$host hr]$

======================
Install the `hr` Tool
======================

Once all the coding is done as per the files available in git repository, it is time to try out the utility by installing the `hr` tool.

Let's get out of the virtual environment. Once we type exit, we'll get dropped back into a regular command prompt.

>>> (hr) [user@$host hr]$ exit
>>> [user@$host hr]$

We need to install our application, and we're going to do it with pip.

>>> [user@$host hr]$ pip3.7 install --user -e .

Let's dissect that command. pip 3.7 install is what installs a python package. --user is a flag that will just install this program locally for our user, rather than system-wide. The -e . is saying, "Install the package that's sitting right here in this environment using setup.py."

Once we run that, there should be a bit of output (with Successfully installed hr near the end), and we'll be back at a command prompt.

Now, if we run the program hr, with no arguments, it should fetch us some user information in JSON format and spit it out to the screen:

>>> [user@$host hr]$ hr

[user@$host hr]$ hr

.. code-block:: json
	[
	  {
		"name": "cloud_user",
		"id": 1000,
		"home": "/home/cloud_user",
		"shell": "/bin/bash"
	  },
	  {
		"name": "centos",
		"id": 1001,
		"home": "/home/centos",
		"shell": "/bin/bash"
	  },
	  {
		"name": "ssm-user",
		"id": 1002,
		"home": "/home/ssm-user",
		"shell": "/bin/bash"
	  }
	]
