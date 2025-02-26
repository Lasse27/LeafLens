import sys
import os
import datetime
from colorama import init, Fore, Style  # type:ignore

# ---
# Logging utility functions
# ---
init(autoreset=True)


def _logln(prefix: str, message: str):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    caller_frame = sys._getframe(2)
    caller_name = caller_frame.f_code.co_qualname
    caller_module = os.path.basename(caller_frame.f_code.co_filename)
    header = f"{caller_module}:{caller_name}"
    header_fixed = f"{header:<25.25}"
    print(f"[{prefix}{Style.RESET_ALL}] {time} [{header_fixed}] {message}")


def logln_info(message: str):
    _logln(Fore.CYAN + "INFO", message)


def logln_warning(message: str):
    _logln(Fore.YELLOW + "WARN", message)


def logln_error(message: str):
    _logln(Fore.RED + "EXER", message)


def beispiel_funktion():
    logln_info("Dies ist eine Log-Nachricht.")
    logln_warning("Dies ist eine Log-Nachricht.")
    logln_error("Dies ist eine Log-Nachricht.")


if __name__ == "__main__":
    beispiel_funktion()
