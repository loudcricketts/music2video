from colorama import Fore, Back, Style
from datetime import datetime


class Printer:
    def __init__(self, logging_level: int, show_timestamp: bool = False):
        # Logging Levels
        # 0 - Nothing
        # 1 - Errors Only
        # 2 - Warnings
        # 3 - Everything
        self.logging_level = int(logging_level)
        # Message Level
        # 0 - Nothing (Do not use this)
        # 1 - Error
        # 2 - Warning
        # 3 - Info
        self.message_level_prefix = (
            "You shouldn't see this",
            f"{Fore.RED}{'ERROR'.rjust(8)}{Style.RESET_ALL}: ",
            f"{Fore.YELLOW}{'WARNING'.rjust(8)}{Style.RESET_ALL}: ",
            f"{Fore.LIGHTBLUE_EX}{'INFO'.rjust(8)}{Style.RESET_ALL}: ",
        )
        self.show_timestamp = show_timestamp

    # Print Function
    def p(self, message_level: int, message: str) -> None:
        # Ensure message_level is valid
        if message_level < len(self.message_level_prefix) and message_level > 0:
            # Print only if message_level is lower than logging_level
            if message_level > self.logging_level:
                return
            if self.show_timestamp:
                timestamp = "[" + datetime.now().strftime("%H:%M:%S") + "]"
            else:
                timestamp = ""

            print(timestamp + self.message_level_prefix[message_level] + message)
        else:
            print(
                f'Fatal: Message level "{message_level}" for message "{message}" is out of range.'
            )
        return
