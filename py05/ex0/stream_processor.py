from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        ...
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        ...


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")
        sum_nb = sum(d for d in data)
        len_nb = len(data)
        return f"Processed {len_nb} numeric values, sum={sum_nb}, avg={sum_nb/len_nb}"

        
    
    def validate(self, data: Any) -> bool:
        try:
            for d in data:
                d = int(d)
        except ValueError as e:
            print(f"Error: {e}")
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"
        

class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Initializing Text Processor...")
        print(f'Processing data: "{data}"')
        data_len = len(data)
        data_wods = data.split(' ', data_len)
        result = f"Processed text: {data_len} characters, {len(data_wods)} words"
        return result

    def validate(self, data: Any) -> bool:
        try:
            for d in data:
                d = str(d)
        except ValueError as e:
            print(f"Error: {e}")
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Initializing Log Processor...")
        print(f'Processing data: "{data}"')
        data_len = len(data)
        data_splited = data.split(':', data_len)
        result = f'[ALERT] {data_splited[0]} level detected: {data_splited[1]}'
        return result
    
    def validate(self, data: Any) -> bool:
        i = 0
        for c in data:
            if c == ':':
                i += 1
        if i > 1:
            return False
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def process_test(data, wichProcecss):
    d = wichProcecss
    if d.validate(data):
        result = d.process(data)
        output = d.format_output(result)
    print(output)


def polymorphic_test(data):
    print("Processing multiple data types through same interface...")
    d = DataProcessor()
    if d.validate(data):
        result = d.process(data)
        output = d.format_output(result)
    print(output)


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        data = [1, 2, 3]
        process_test(data, NumericProcessor())
        print()
        data_1 = 'Hello Nexus World'
        process_test(data_1, TextProcessor())
        print()
        data_1 = 'ERROR: Connection timeout'
        process_test(data_1, LogProcessor())
        print()
        polymorphic_test(data)
        
    except Exception as e:
        print(f"Error :{e}")
    
    


main()