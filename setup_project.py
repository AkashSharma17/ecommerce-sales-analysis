"""
Project structure initializer for the Ecommerce Sales Analysis Pipeline.
Run once to create the required folder hierarchy.
"""

from pathlib import Path

FOLDERS = [
    "data/raw",
    "data/cleaned",
    "data/processed",
    "logs",
    "notebooks",
    "src/"
]


def create_project_structure():
    """Create all required project directories if they do not already exist."""
    for folder in FOLDERS:
        Path(folder).mkdir(parents=True, exist_ok=True)
    print("Project structure created successfully.")


if __name__ == "__main__":
    create_project_structure()