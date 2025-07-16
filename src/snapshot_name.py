
import os
import datetime
from git import Repo

def getSnapshotName():
    
    repo = Repo()
    branch_name = repo.active_branch.name
    if not branch_name.startswith("feature/"):
        return ""
    else:
        snapshot_name = branch_name.removeprefix("feature/").replace("/", "-").replace("_", "-")

        match os.getenv("INPUT_UNIQUE_SNAPSHOT").casefold():
            case "":
                pass
            case "commit":
                snapshot_name += "-" + str(repo.head.commit)
            case "date-time":
                snapshot_name += "-" + datetime.datetime.now().strftime("%d-%m-%H-%M")
            case _:
                raise ValueError("Unknown unique snapshot type")

        return snapshot_name