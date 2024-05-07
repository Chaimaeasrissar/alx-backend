#!/usr/bin/env python3
'''Simple Helper functions'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
<<<<<<< HEAD
        '''Retrieves the index range and page size'''
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)
=======
    """Retrieves the index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
    
>>>>>>> 9ff56be1f7f7e0930af0e296883c02f8cb5cb829
