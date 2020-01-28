import mlflow
import json
import os


def log(content, name, rm=True):
    if name.endswith(".txt"):
        with open(name, "w") as file:
            file.writelines(content)
    elif name.endswith(".json"):
        with open(name, "w") as file:
            json.dump(content, file)
    else:
        mlflow.log_metric(content, name)
    mlflow.log_artifact(name)
    if rm:
        os.remove(name)
