from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, IntEnum
import textwrap
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="dialogue.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# -----------
# Dataclasses and Enums
# -----------

@dataclass
class User:
    age: int
    name: str
    gender: str
    city: str | None = None


class MODIFY_USER_OPTION(StrEnum):
    """Yes or no to first user info question."""
    Y = "Y"
    N = "N"


class USER_FIELDS(IntEnum):
    """User value for modifying user input."""
    AGE = 1
    NAME = 2
    GENDER = 3
    CITY = 4

# -----------
# Main Logic
# -----------

class UserProcessor:

    def __init__(self, user_input: User):
        self.age = user_input.age
        self.name = user_input.name
        self.gender = user_input.gender
        self.city = user_input.city
        self.modified = False


    def __str__(self) -> str:
        """Return nicely formatted user info."""
        return textwrap.dedent(
            f"""
            Current user information.

            Age: {self.age}
            Name: {self.name}
            Gender: {self.gender}
            City: {self.city}
            """
        ).strip()


    def process_user(self) -> None:
        """Ask whether to modify the user and run the modifier if requested.

        This uses a simple loop to validate the Y/N response instead of recursion.
        """
        while True:
            modify_user_input = input("Would you like to modify the user? (Y/N): ").strip().upper()
            if modify_user_input in (MODIFY_USER_OPTION.Y, MODIFY_USER_OPTION.N):
                break
            print("Please enter 'Y' or 'N'.")

        if modify_user_input == MODIFY_USER_OPTION.Y:
            self._modify_user_option()


    def _modify_user_option(self) -> None:
        """Interactively modify a single user field."""
        while True:
            try:
                user_field_option = int(
                    input(
                        "What would you like to modify?\n\n1) Age\n2) Name\n3) Gender\n4) City\nEnter choice (1-4): "
                    ).strip()
                )
                if user_field_option not in range(1, 5):
                    raise ValueError("choice out of range")
            except Exception as e:
                logger.error("Invalid selection: %s", e)
                print("Please enter a number 1-4.")
                continue
            break

        modified_value = input("What do you want the new value to be? ").strip()

        match user_field_option:
            case USER_FIELDS.AGE:
                try:
                    self.age = int(modified_value)
                except ValueError:
                    logger.error("Invalid age entered; keeping previous value.")
                    return
            case USER_FIELDS.NAME:
                self.name = modified_value
            case USER_FIELDS.GENDER:
                self.gender = modified_value
            case USER_FIELDS.CITY:
                self.city = modified_value

        self.modified = True
        logger.info("User %s was modified. Values: <%s, %s, %s>", self.name, self.age, self.gender, self.city)


    def summarize(self) -> str:
        """Return and log a one-line summary of the user."""
        summary = f"User {self.name} is a {self.age}-year-old {self.gender} from {self.city}."
        logging.info(summary)
        return summary



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(prog="UserProcessor", description="Args for the dialogue.")

    parser.add_argument("-a", "--age", type=int, required=True, help="(int) Age of the user.")
    parser.add_argument("-n", "--name", type=str, required=True, help="(str) Name of the user.")
    parser.add_argument("-g", "--gender", type=str, required=True, help="(str) Gender of the user.")
    parser.add_argument("-c", "--city", type=str, default="(Unknown)", help="(str) City of the user.")

    args = parser.parse_args()

    input_user = User(
        args.age,
        args.name,
        args.gender,
        args.city,
    )

    new_user = UserProcessor(input_user)
    new_user.process_user()
    new_user.summarize()
    print(f"User was modified: {new_user.modified}")
