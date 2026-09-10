from data.dataset import Dataset
from data.iris.constants import IRIS_ID

class Iris(Dataset):
    def __init__(self) -> None:
        super().__init__(id=IRIS_ID, name="Iris")