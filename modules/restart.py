import os
from pathlib import Path

from modules.paths_internal import script_path


def is_restartable() -> bool:
    """
    Return True if the li is restartable (i.e. there is something watching to restart it with)
    """
    return bool(os.environ.get('HIT_NOBODY_RESTART'))


def restart_program() -> None:
    """creates file tmp/restart and immediately stops the process, which li.bat/li.sh interpret as a command to start li again"""

    tmpdir = Path(script_path) / "tmp"
    tmpdir.mkdir(parents=True, exist_ok=True)
    (tmpdir / "restart").touch()

    stop_program()


def stop_program() -> None:
    os._exit(0)
