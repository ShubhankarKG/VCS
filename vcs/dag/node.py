class Node:
    def __init__(self):
        pass

    def serialize(self) -> str:
        raise NotImplementedError()

    @staticmethod
    def deserialize(data: str) -> 'Node':
        raise NotImplementedError()

    @staticmethod
    def deserialize_from_file(file_path: str) -> 'Node':
        raise NotImplementedError()
