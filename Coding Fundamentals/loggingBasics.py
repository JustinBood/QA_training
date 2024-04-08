import logging

logging.basicConfig(filename='sample.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(message)s')

def add(x, y):
    result = x + y
    return logging.debug(f' Add: {x} + {y} = {result}')

def subtract(x, y):
    result = x - y
    return logging.debug(f' Subtract: {x} - {y} = {result}')

add(6, 8)
subtract(6, 8)

