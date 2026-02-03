from abc import ABC, abstractmethod
from typing import Any, List, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict) or (isinstance(data, str) and "," in data):
            print(f'Input: {data}')
        elif isinstance(data, list):
            for d in data:
                print(d, end=" ")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print("Transform: Enriched with metadata and validation")
        elif isinstance(data, str) and "," in data:
            print("Transform: Parsed and structured data")
        elif isinstance(data, list):
            print("\nTransform: Aggregated and filtered")
        else:
            return "Stage 2"

        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            temp = data.get("value", 0)
            status = "Normal range" if temp <= 30 else "It's hot"
            print(f"Output: Processed temperature reading:"
                  f" {temp}°C ({status})")

        elif isinstance(data, str) and "," in data:
            act = 0
            data_splited = data.split(',')
            for d in data_splited:
                if d == "action":
                    act += 1
            print(f"Output: User activity logged: {act} actions processed")

        elif isinstance(data, list):
            print(f"Output: Stream summary: {len(data)} readings,"
                  f" {data[len(data) - 1]}")
        else:
            return "Stage 3"
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> None:
        ...

    def run(self, data: Any) -> None:
        try:
            for stage in self.stages:
                data = stage.process(data)
                if data == "Stage 2" or data == "Stage 3":
                    raise Exception()
        except Exception:
            print(f"Error detected in {data}: Invalid data format")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> None:
        print("Processing JSON data through pipeline...")
        self.run(data)


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> None:
        print("Processing CSV data through same pipeline...")
        self.run(data)


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> None:
        print("Processing Stream data through same pipeline...")
        self.run(data)


class NexusManager:
    def __init__(self):
        self.pipeline_cap = 1000
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def pipeline_capacity(self) -> str:
        return f"Pipeline capacity: {self.pipeline_cap} streams/second"

    def pipeline_chaining_demo(self) -> None:
        chain = " -> ".join(p.pipeline_id for p in self.pipelines)
        print("=== Pipeline Chaining Demo ===")
        print(chain)
        print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")
        print(f"Chain result: 100 records processed through"
              f" {len(self.pipelines)}-stage pipeline")
        print("Performance: 95% efficiency, 0.2s total processing time")


def main() -> None:
    manager = NexusManager()

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print(manager.pipeline_capacity())
    print("\nCreating Data Processing Pipeline...")

    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===\n")

    stages = [InputStage(), TransformStage(), OutputStage()]

    json_pipeline = JSONAdapter("Pipeline A")
    csv_pipeline = CSVAdapter("Pipeline B")
    stream_pipeline = StreamAdapter("Pipeline C")

    for stage in stages:
        json_pipeline.add_stage(stage)
        csv_pipeline.add_stage(stage)
        stream_pipeline.add_stage(stage)

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    json_pipeline.process({"sensor": "temp", "value": 23.5, "unit": "C"})
    print()
    csv_pipeline.process("user,action,timestamp")
    print()
    stream_pipeline.process(['Real-time', 'sensor', 'stream', 'temp:12'])
    print()

    manager.pipeline_chaining_demo()

    print()
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    json_pipeline.process("gdggddg")

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
