from datetime import datetime, timezone
from vcs import constants
from vcs.crypto.hash import hash_of_repo


class CommitNode:
    def __init__(self, commit_message: str, commit_user: str, branch: str = constants.DEFAULT_BRANCH):
        # commit_user -> email of user, for now
        self.commit_message = commit_message
        self.commit_user = commit_user
        self.branch_name = branch
        self.parents_hashes = []
        self.children_hashes = []
        self.type = constants.COMMIT_CUMULATIVE
        self.repo_hash = hash_of_repo()
        self.timestamp = int(datetime.now(tz=timezone.utc).timestamp() * 1000)

    def serialize(self) -> str:
        raise NotImplementedError()

    @staticmethod
    def deserialize(data: str) -> 'CommitNode':
        raise NotImplementedError()

    @staticmethod
    def deserialize_from_file(file_path: str) -> 'CommitNode':
        raise NotImplementedError()

    def convert_to_cumulative_node(self):
        if self.type != constants.COMMIT_CUMULATIVE:
            raise NotImplementedError()
            self.type = constants.COMMIT_CUMULATIVE

    def convert_to_full_node(self):
        if self.type != constants.COMMIT_FULL:
            raise NotImplementedError()
            self.type = constants.COMMIT_FULL

    @staticmethod
    def make_child_node(parent: 'CommitNode'):
        raise NotImplementedError

    @staticmethod
    def commit():
        raise NotImplementedError
