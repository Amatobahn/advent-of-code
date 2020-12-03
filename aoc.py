# -*- coding: utf-8 -*-
"""

"""
from configparser import RawConfigParser
import enum
import os
from pathlib import Path
import re
import pip._vendor.requests as requests

_URL = "https://adventofcode.com/{year}/day/{day}"


def _get_user_session() -> (dict, None):
    path = Path(os.getcwd()).joinpath("config.ini")
    if path.exists():
        parser = RawConfigParser()
        parser.read(path)
        if "session" in parser["DEFAULT"]:
            session_id = parser.get("DEFAULT", "session")
            return {"session": session_id}
        raise RuntimeError("key 'session' not found section DEFAULT")
    raise RuntimeError("Configuration file not found")


class PuzzlePart(enum.Enum):
    A = 1
    B = 2


class AdventUser(object):
    def __init__(self):
        self._session = _get_user_session()
        self.input_url = _URL + "/input"
        self.submit_url = _URL + "/answer"

    def get_puzzle(self, day, year):
        return Puzzle(day, year, self)


class Puzzle(object):
    def __init__(self, day, year, user: AdventUser = None):
        self.day = day
        self.year = year
        self._user = user
        self.input = self._get_input() or ""

    def _get_input(self):
        uri = self._user.input_url.format(day=self.day, year=self.year)
        session = _get_user_session()
        if session:
            response = requests.get(uri, cookies=session)
            if not response.ok:
                raise RuntimeWarning("Unexpected Response")
            data = response.text
            return data.rstrip("\r\n")

    def submit(self, answer, part: PuzzlePart):
        if answer in [u"", b"", None, b"None", u"None"]:
            raise RuntimeWarning("Answer is Empty or None")
        answer = str(answer)

        submit_uri = self._user.submit_url.format(day=self.day, year=self.year)
        session = _get_user_session()
        if session:
            response = requests.post(
                submit_uri,
                cookies=session,
                data={"level": part.value, "answer": answer}
            )

            if not response.ok:
                raise RuntimeWarning("Non-200 response for POST call")

            message = response.text
            if "That's the right answer" in message:
                print(f"the answer {answer} is CORRECT")
            elif "Did you already complete it" in message:
                print(f"Already completed with the answer {answer}")
            elif "That's not the right answer" in message:
                print(f"The answer {answer} is INCORRECT")
            elif "You gave an answer too recently" in message:
                wait_pattern = r"You have (?:(\d+)m )?(\d+)s left to wait"
                try:
                    [(minutes, seconds)] = re.findall(wait_pattern, message)
                except ValueError:
                    print(message)
                else:
                    wait_time = int(seconds)
                    if minutes:
                        wait_time += 60 * int(minutes)
                    print(f"You need to wait {wait_time} seconds to submit")
            return response



