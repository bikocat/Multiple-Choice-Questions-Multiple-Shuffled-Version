
import logging
from dataclasses import dataclass

from .utilities.empty_format import format_question


log = logging.getLogger(__name__)
print(log)


@dataclass
class Template:
    """Template generation: provide number of question and choices"""

    n_quest: int
    n_choices: int

    def generate_template(self) -> None:
        format_question(self.n_quest, self.n_choices)
        log.info("Template generated")
