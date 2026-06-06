import shutil
import subprocess
import sys
import os
import shlex


def main():
    built_ins = ["echo", "exit", "type", "pwd", "cd"]

    while True:
        command = input("$ ")

        parts = shlex.split(command)

        if not parts:
            continue

        cmd = parts[0]
        args = parts[1:]

        if cmd == "exit":
            sys.exit(0)
        elif cmd == "echo":
            print(" ".join(args))
        elif cmd == "cat":
            subprocess.run([cmd] + args)
        elif command.startswith("type "):
            if command[5:] in built_ins:
                print(f"{command[5:]} is a shell builtin")
            else:
                path = shutil.which(command[5:])
                if path:
                    print(f"{command[5:]} is {path}")
                else:
                    print(f"{command[5:]}: not found")
        elif command == "pwd" or command.startswith("pwd "):
            print(os.getcwd())
        elif command.startswith("cd "):
            path = command[3:].strip()

            if path == "~":
                path = os.path.expanduser("~")
            else:
                path = os.path.expanduser(path)

            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd: {path}: No such file or directory")
        else:
            parts = command.split()
            path = shutil.which(parts[0])

            if path:
                subprocess.run(parts)
            else:
                print(f"{parts[0]}: command not found")


if __name__ == "__main__":
    main()
