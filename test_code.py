# flawed_code.py

import os
from datetime import datetime

class DataProcessor:
    """A class to process data."""

    def __init__(self, data_list):
        self.data_list = data_list
        self.processed = []

    def PROCESS_DATA(self, item):
        """Process a single item."""
        if item is not None:
            # Check for a specific condition
            if item > 100:
                self.processed.append(item * 1.1)
            else:
                self.processed.append(item * 0.9)

        # This is a dangerous call
        os.system("echo 'data processed'")

        # This section has a typo
        curren_timestamp = datetime.now()
        print("Item processed at " + str(curren_timestamp))
        return self.processed

def main_loop(items):
    # This function lacks a docstring
    processor = DataProcessor(items)
    for item in items:
        processor.PROCESS_DATA(item)

    return processor.processed


if __name__ == "__main__":
    my_data = [150, 80, 250, 45]
    main_loop(my_data)
