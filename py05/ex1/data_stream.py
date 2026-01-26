from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union

class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str :
        ...

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(stream_id):
    pass

class TransactionStream(stream_id):
    pass

class EventStream(stream_id):
    pass


class StreamProcessor:
    pass