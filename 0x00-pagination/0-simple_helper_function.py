#!/usr/bin/env python3
'''Simple Helper functions'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
<<<<<<< HEAD
<<<<<<< HEAD
        '''Retrieves the index range and page size'''
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)
=======
    """Retrieves the index range from a given page and page size.
    """
=======
    '''Retrieves the index range and page size'''
>>>>>>> 6fcfb2183194583f712d391291ca4de5de0f22df
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
    
>>>>>>> 9ff56be1f7f7e0930af0e296883c02f8cb5cb829
