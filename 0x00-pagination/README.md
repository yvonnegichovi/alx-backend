# 0x00 Pagination
## Overview
This project focuses on implementing pagination in a backend system. It explores various methods to paginate datasets, ensuring efficient data retrieval and handling edge cases, such as deletion resilience.

## Resources
- REST API Design: Pagination
- HATEOAS

## Learning Objectives
By the end of this project, you should be able to:

- Paginate a dataset using simple page and page_size parameters.
- Paginate a dataset with hypermedia metadata.
- Implement pagination that is resilient to deletions.

## Requirements
- Python 3.7 on Ubuntu 18.04 LTS
- Code must conform to PEP 8 style guidelines (pycodestyle 2.5.*)
- Each file should end with a new line.
- The first line of each script should be #!/usr/bin/env python3.
- Each module, class, and function must have a docstring.
- All functions and coroutines must be type-annotated.
- The Popular_Baby_Names.csv data file will be used.

## Tasks
0. Simple Helper Function
Implement a function index_range that takes two integer arguments, page and page_size, and returns a tuple containing the start and end indexes for pagination.

File: 0-simple_helper_function.py

python
def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end indexes for the given page and page size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
1. Simple Pagination
Copy index_range and implement the Server class. Add a get_page method to return the appropriate page of the dataset.

File: 1-simple_pagination.py

python
Copy code
import csv
from typing import List
from 0-simple_helper_function import index_range

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page from the dataset"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index] if start_index < len(self.dataset()) else []
2. Hypermedia Pagination
Extend the Server class to include a get_hyper method that returns a dictionary with pagination metadata.

File: 2-hypermedia_pagination.py

python
Copy code
import math

class Server:
    # (previous code...)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a page with hypermedia metadata"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
3. Deletion-Resilient Hypermedia Pagination
Enhance the Server class to handle deletions in the dataset without losing data integrity. Implement the get_hyper_index method.

File: 3-hypermedia_del_pagination.py

python
Copy code
from typing import Dict

class Server:
    # (previous code...)

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a page with deletion-resilient hypermedia metadata"""
        assert type(index) == int and 0 <= index < len(self.dataset())
        assert type(page_size) == int and page_size > 0
        data = []
        next_index = index
        for _ in range(page_size):
            if next_index in self.indexed_dataset():
                data.append(self.indexed_dataset()[next_index])
            next_index += 1
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
Repository Structure
Copy code
alx-backend/
├── 0x00-pagination/
│   ├── 0-simple_helper_function.py
│   ├── 1-simple_pagination.py
│   ├── 2-hypermedia_pagination.py
│   ├── 3-hypermedia_del_pagination.py
│   ├── Popular_Baby_Names.csv
│   └── README.md
└── README.md
