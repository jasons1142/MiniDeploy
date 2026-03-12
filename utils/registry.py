import json
import os

REGISTRY = "apps.json"

def load_registry():
    if not os.path.exists(REGISTRY):
        return {}
    else:
        with open(REGISTRY) as f:
            return json.load(f)


def save_registry(registry):
    with open(REGISTRY, "w") as f:
        json.dump(registry, f)