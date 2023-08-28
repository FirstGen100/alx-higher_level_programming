#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as Err:
        sys.stderr.write("Exception: " + Err.args[0] + "\n")
        return None
