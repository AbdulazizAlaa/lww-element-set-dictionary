from datetime import date
from typing import Optional


class Dictionary:
    def __init__(self):
        self._add_set: dict = {}
        self._remove_set: dict = {}

    def _check_add(self, target_set: dict, word: str, timestamp: date) -> None:
        if word in target_set:
            current_timestamp: date = target_set[word]
            if timestamp < current_timestamp:
                timestamp = current_timestamp

        target_set[word] = timestamp

    def add(self, word: str, timestamp: date) -> None:
        self._check_add(self._add_set, word, timestamp)

    def remove(self, word: str, timestamp: date) -> None:
        self._check_add(self._remove_set, word, timestamp)

    def checkExists(self, word: str) -> bool:
        if(word not in self._add_set):
            return False

        if(word not in self._remove_set):
            return True

        if(self._remove_set[word] > self._add_set[word]):
            return False

        return True

    def get(self) -> list:
        words_list = []
        for word in self._add_set:
            if (word not in self._remove_set) or (self._add_set[word] >= self._remove_set[word]):
                words_list.append(word)
        return words_list
