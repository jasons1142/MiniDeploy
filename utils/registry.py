# utils/registry.py


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
    
def register_app(app_name, path):
    registry = load_registry()

    if app_name in registry:
        print(f"{app_name} is already in the registry")
        return
    
    registry[app_name] = {"path": path, "status": "running"}

    save_registry(registry)

def remove_app(app_name):
    registry = load_registry()

    if app_name in registry:
        registry.pop(app_name)
    else:
        print(f"{app_name} not in the registry")
        return
    
    save_registry(registry)

def list_apps():
    registry = load_registry()

    if not registry:
        print("No deployed apps")
    
    else:
        for app_name, value in registry.items():
            print(f"{app_name} - {value["status"]}")


        