from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            sum_nb = sum(int(d) for d in data)
            len_nb = len(data)
            return f"Processed {len_nb} numeric values, sum={sum_nb}, avg={sum_nb/len_nb}"
        except Exception as e:
            return f"Error: {e}"


    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        try:
            for d in data:
                d = float(d)
            return True
        except (ValueError, TypeError):
            return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        data_len = len(data)
        data_wods = data.split()
        return f"Processed text: {data_len} characters, {len(data_wods)} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            data_len = len(data)
            data_splited = data.split(':', 1)
            return f'[ALERT] {data_splited[0]} level detected: {data_splited[1]}'
        except IndexError:
            return "Error: Invalid log format"
    
    def validate(self, data: Any) -> bool:
        i = 0
        for c in data:
            if c == ':':
                i += 1
        return (isinstance(data, str) and i == 1)


def numeric_process_test(data: Any) -> None:
    print("Initializing Numeric Processor...")
    d = NumericProcessor()
    if d.validate(data):
        print(f"Processing data: {data}")
        print("Validation: Numeric data verified")
        result = d.process(data)
        output = d.format_output(result)
    print(f"Output: {output}")


def text_process_test(data: Any) -> None:
    print("Initializing Text Processor...")
    d = TextProcessor()
    if d.validate(data):
        print(f'Processing data: "{data}"')
        print("Validation: Text data verified")
        result = d.process(data)
        output = d.format_output(result)
    print(f"Output: {output}")


def log_process_test(data: Any) -> None:
    print("Initializing Log Processor...")
    d = LogProcessor()
    if d.validate(data):
        print(f'Processing data: "{data}"')
        print("Validation: Log entry verified")
        result = d.process(data)
        output = d.format_output(result)
    print(f"Output: {output}")

def polymorphic_test(data: Any, processor: DataProcessor, i: int) -> None:
    if processor.validate(data):
        result = processor.process(data)
        output = processor.format_output(result)
        print(f"Result {i}: {output}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric_process_test([1, 2, 3])
    print()
    text_process_test("Hello Nexus World")
    print()
    log_process_test("ERROR: Connection timeout")
    print("\nProcessing multiple data types through same interface...")

    polymorphic_test([1, 2, 3], NumericProcessor(), 1)
    polymorphic_test("Hello Nexus World", TextProcessor(), 2)
    polymorphic_test("INFO: System ready", LogProcessor(), 3)

main()