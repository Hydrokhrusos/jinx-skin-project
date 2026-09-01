import json
import re
from pathlib import Path


SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
PROJECT_CONFIG = Path(__file__).resolve().parent.parent / "mod.config.json"


def read_project_version():
    config = json.loads(PROJECT_CONFIG.read_text(encoding="utf-8"))
    version = config.get("version", "")
    if not SEMVER.fullmatch(version):
        raise ValueError(f"Project version is not semantic: {version!r}")
    return version


VERSION = read_project_version()
