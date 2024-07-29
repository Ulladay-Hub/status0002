import shlex
from .file_system import VirtualFileSystem

class PyEnv:
    def __init__(self):
        self.vfs = VirtualFileSystem()

    def call(self, command):
        """Simulate running a shell command in the virtual environment."""
        command_parts = shlex.split(command)
        if command_parts[0] == 'ls':
            return self.vfs.ls()
        elif command_parts[0] == 'echo':
            output = ' '.join(command_parts[1:])
            self.vfs.echo(output)
        else:
            raise NotImplementedError(f"Command '{command_parts[0]}' is not implemented in the virtual environment.")

    def newTXTfile(self, filename, content):
        self.vfs.create_file(filename, content)
