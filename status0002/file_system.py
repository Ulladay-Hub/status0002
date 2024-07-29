class VirtualFileSystem:
    def __init__(self):
        self.files = {}

    def ls(self):
        """List all files in the virtual environment."""
        return '\n'.join(self.files.keys())

    def echo(self, output):
        """Append content to a file."""
        filename, content = output.split('>>')
        filename = filename.strip()
        content = content.strip()
        if filename in self.files:
            self.files[filename] += '\n' + content
        else:
            self.files[filename] = content

    def create_file(self, filename, content):
        """Create a new text file with the given content."""
        self.files[filename] = content
