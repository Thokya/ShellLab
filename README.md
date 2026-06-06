# ShellLab 🐚

An experimental Unix-like shell built in Python to explore how shells, processes, and command execution work under the hood.

ShellLab started as a fun weekend project driven by curiosity: *What actually happens when we type a command into a terminal and press Enter?*

Instead of treating the shell as a black box, this project aims to build core shell functionality from scratch while learning more about operating systems, process management, and Python.

## Why ShellLab?

As software engineers, we use terminals every day:

```bash
ls
cd projects
python app.py
git status
```

But what really happens when these commands are executed?

ShellLab is an attempt to answer that question by building a simple shell from scratch and gradually adding features found in modern Unix shells.

The goal is not to replace Bash, Zsh, or Fish.

The goal is to learn, experiment, and have fun.

## Current Features

### Built-in Commands

* `echo`
* `pwd`
* `cd`
* `type`
* `exit`

### External Command Execution

ShellLab can locate and execute commands available on your system PATH.

Example:

```bash
$ python --version
Python 3.13.0

$ git --version
git version 2.x.x
```

### Command Parsing

Commands are parsed using Python's `shlex` module, allowing proper handling of quoted arguments.

Example:

```bash
$ echo "hello world"
hello world
```

### Directory Navigation

Supports changing directories and navigating to the user's home directory.

```bash
$ cd ~

$ pwd
/home/user
```

## Example Session

```bash
$ pwd
/Users/john/projects

$ echo Hello ShellLab
Hello ShellLab

$ type python
python is /usr/bin/python

$ cd ~

$ pwd
/Users/john

$ exit
```

## Technologies Used

* Python 3
* subprocess
* os
* shutil
* shlex

## What I've Learned So Far

Building ShellLab has helped me understand:

* Shell built-ins vs external commands
* PATH resolution
* Process execution
* Working directories
* Command parsing
* How terminals interact with operating systems

## Contributing

Contributions, suggestions, and discussions are welcome.

If you're learning about shells, operating systems, or Python internals, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Final Note

ShellLab is intentionally built as a learning-first project.

The code may not be perfect, but every feature is an opportunity to understand how real shells work behind the scenes.

If this project helps you learn something new, feel free to star the repository ⭐
