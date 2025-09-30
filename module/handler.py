
class FileHandler:
    def __init__(self, file_path: str, chunk_size=1024*1024):
        self.file_path = file_path
        self.chunk_size = chunk_size

    def read_chunks(self):
        with open(self.file_path, 'rb') as f:
            while chunk := f.read(self.chunk_size):
                yield chunk

    @staticmethod
    def write_chunks(file_path, chunks):
        with open(file_path, 'wb') as f:
            for chunk in chunks:
                f.write(chunk)
