from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union

class DataStream(ABC):

    def __init__(self):
        self.count_op = 0
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str :
        ...

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
    
    def process_batch(self, data_batch: List[Any]) -> str :
        data = {}
        try:
            for d_b in data_batch:
                d = d_b.split(':')
                data[d[0]] = int(d[1])
            return f"{len(data)}  readings processed, avg temp: {data["temp"]}°C"
        except Exception as e:
            print(f"Error: {e}")

class TransactionStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id

    def ff(self):
        self.count_op += 1
        

class EventStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
    
    def ff(self):
        self.count_op += 1


class StreamProcessor:
    pass


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    data = {"streams":{
        "SENSOR_001": {"type": "Environmental Data", "Data": [{'temp':22.5}, {'humidity':65}, {'pressure':1013}]},
        "TRANS_001": {"type": "Financial Data"},
        "EVENT_001": {"type": " System Events"}
    }}


    for key in data["streams"].items():
        SensorStream(key)
        TransactionStream(key)
        EventStream(key)


dat = [{'temp':22.5}, {'humidity':65}, {'pressure':1013}]

for d in dat:
    for k, v in d.items():
        print(f"{k}:{v} ,", end="")