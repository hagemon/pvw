import os
import json

# Get the path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create a subdirectory called "config" if it doesn't exist
config_dir = os.path.join(script_dir, "config")
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

# Create a JSON config file if it doesn't exist
config_file = os.path.join(config_dir, "config.json")
if not os.path.exists(config_file):
    config = {"venv_path": "~/pvw"}
    with open(config_file, "w") as f:
        json.dump(config, f)


def config_path():
    return config_file


if __name__ == "__main__":
    print(config_path())
