# Copyright 2022 The Nerfstudio Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Additional rich ui components"""

from contextlib import nullcontext

from rich.console import Console
from rich.progress import ProgressColumn
from rich.text import Text

CONSOLE = Console(width=120)


class ItersPerSecColumn(ProgressColumn):
    """Renders the iterations per second for a progress bar."""

    def __init__(self, suffix="it/s") -> None:
        super().__init__()
        self.suffix = suffix

    def render(self, task: "Task") -> Text:
        """Show data transfer speed."""
        speed = task.finished_speed or task.speed
        if speed is None:
            return Text("?", style="progress.data.speed")
        return Text(f"{speed:.2f} {self.suffix}", style="progress.data.speed")


def status(msg: str, spinner: str = "bouncingBall", verbose: bool = False):
    """A context manager that does nothing is verbose is True. Otherwise it hides logs under a message.

    Args:
        msg: The message to log.
        spinner: The spinner to use.
        verbose: If True, print all logs, else hide them.
    """
    if verbose:
        return nullcontext()
    return CONSOLE.status(msg, spinner=spinner)
