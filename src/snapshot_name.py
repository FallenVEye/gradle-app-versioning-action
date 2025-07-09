
import os
from git import Repo

def getSnapshotName():
    is_unique = os.getenv("INPUT_UNIQUE_SNAPSHOT")

    repo = Repo()
    repo_name = repo.active_branch.name
    if not repo_name.startswith("feature/"):
        return ""
    else:
        snapshot_name = repo_name.removeprefix("feature/").replace("/", "-").replace("_", "-")
        if is_unique:
            snapshot_name += str(repo.head.commit)
        return snapshot_name