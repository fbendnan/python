from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str: ...

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {"stream_id": self.stream_id, "processed": self.processed_count}

class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"
        self.stream_name = "Sensor"

    def process_batch(self, data_batch: List[Any]) -> str:
        values: Dict[str, float] = {}
        try:
            for item in data_batch:
                key, value = item.split(":")
                values[key] = float(value)

            self.processed_count += len(data_batch)
            avg_temp: float = values.get("temp", 0.0)

            return (
                f"Sensor analysis: {len(values)} readings processed, "
                f"avg temp: {avg_temp}°C"
            )
        except ValueError as e:
            print(f"Error: {e}")

class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"
        self.stream_name = "Transaction"

    def process_batch(self, data_batch: List[Any]) -> str:
        buy: int = 0
        sell: int = 0

        for item in data_batch:
            key, value = item.split(":")
            if key == "buy":
                buy += int(value)
            elif key == "sell":
                sell += int(value)

        self.processed_count += len(data_batch)
        net_flow: int = buy - sell

        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: +{net_flow} units"
        )

class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"
        self.stream_name = "Event"


    def process_batch(self, data_batch: List[Any]) -> str:
        errors: int = sum(1 for e in data_batch if e == "error")
        self.processed_count += len(data_batch)

        return f"Event analysis: {len(data_batch)} events, " f"{errors} error detected"

class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data: Dict[str, List[Any]]) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("\nBatch 1 Results:")

        for stream in self.streams:
            batch: List[Any] = data.get(stream.stream_id)
            stream.process_batch(batch)

            label: str = stream.stream_name
            print(f"- {label} data: {stream.processed_count} operations processed")

def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    data: Dict[str, List[Any]] = {
        "SENSOR_001": ["temp:22.5", "humidity:65", "pressure:1013"],
        "TRANS_001": ["buy:100", "sell:150", "buy:75"],
        "EVENT_001": ["login", "error", "logout"],
    }

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: {data['SENSOR_001']}")
    print(sensor.process_batch(data["SENSOR_001"]))

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}")
    print(f"Processing transaction batch: {data['TRANS_001']}")
    print(transaction.process_batch(data["TRANS_001"]))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing event batch: {data['EVENT_001']}")
    print(event.process_batch(data["EVENT_001"]))

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    processor.process_all(data)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


main()
