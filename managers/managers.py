class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return "inside enter"

    def open(self, mode='a'):
        self.file = open(self.filename, mode)

    def close(self):
        self.file.close()

    def read(self):
        return self.file.readlines()

    def write(self, data):
        self.file.writelines(data)

    def __exit__(self,exc_type, exc_value, exc_traceback):
        return "Inside Exit"

# Usage
with FileManager('example.txt') as file_manager:
    file_manager.open('a')  # Open the file in write mode
    file_manager.write("Hello, World!\n")
    file_manager.write("This is a line.\n")
    print(file_manager.read())
    file_manager.close()

# After the 'with' block, the file is automatically closed.
