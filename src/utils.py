from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent

def get_data_path(subfolder: str, filename: str) -> Path:
    return get_project_root() / "data" / subfolder / filename