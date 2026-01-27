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
                data[d[0]] = float(d[1])
            return f"{len(data)}  readings processed, avg temp: {data["temp"]}°C"
        except Exception as e:
            print(f"Error: {e}")

class TransactionStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str :
        data = {}
        buy = 0
        sell = 0
        try:
            for d_b in data_batch:
                d = d_b.split(':')
                data[d[0]] = int(d[1])
            for key, value in data.items():
                if key == 'buy':
                    buy += value
                elif key == 'sell':
                    sell += value
            return f"{len(data)} operations, net flow: +{buy - sell} units"
        except Exception as e:
            print(f"Error: {e}")
    
        

class EventStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
    
    def process_batch(self, data_batch: List[Any]) -> str :
        count_errors = 0
        try:
            for event in data_batch:
                if event == 'error':
                    count_errors += 1
            return f"{len(data_batch)} events, {count_errors} error detected"
        except Exception as e:
            print(f"Error: {e}")
    


class StreamProcessor:
    def __init__(self):
        self.streams = []
        self.data_streams = []

    def store_streams(self, stream, data_stream):
        self.streams += [stream]
        self.data_streams += [data_stream]

    def stream_processor(self):
        i: int= 0
        result_batch: str = ""
        for stream in self.streams():
            result_batch += stream.process_batch(self.data_streams[i])
            print(result_batch)
            i += 1


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    data = {"streams":{
        "SENSOR_001": {"type": "Environmental Data", "Data": ['temp:22.5', 'humidity:65', 'pressure:1013']},
        "TRANS_001": {"type": "Financial Data", "Data": ['buy:100', 'sell:150', 'buy:75']},
        "EVENT_001": {"type": " System Events", "Data": ['login', 'error', 'logout']}
    }}


    print()

    for key in data["streams"].items():
        SensorStream(key)
        TransactionStream(key)
        EventStream(key)


main()