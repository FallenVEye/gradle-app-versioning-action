
from git import Repo

def getSnapshotName():
    repo_name = Repo().active_branch.name
    if not repo_name.startswith("feature/"):
        return ""
    else:
        return repo_name.removeprefix("feature/").replace("/", "-").replace("_", "-")
