from abc import ABC
from ucimlrepo import dotdict, fetch_ucirepo

class Dataset(ABC):
    def __init__(self, id: int, name: str):
        self._data = fetch_ucirepo(id=id)
        self._name = name

    def get_dict(self) -> dotdict:
        return self._data

    def get_metadata(self):
        return self._data.metadata

    def get_variables_information(self):
        return self._data.variables