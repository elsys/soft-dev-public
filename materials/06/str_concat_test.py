from typing import Generator
from os import getpid
from subprocess import run
from sys import argv
from timeit import default_timer as timer
from collections import UserString
from dataclasses import dataclass
from random import choice
from string import ascii_lowercase
from array import array
from io import StringIO
from datetime import datetime


@dataclass()
class Performance:
    """Class for keeping track of function performance"""

    index: int
    time: float = -1
    output_size: int = -1
    process_size: int = -1
    description: str = ""

    def __str__(self):
        return (
            f"func: {self.index}\n"
            f"description: {self.description}\n"
            f"time: {self.time}\n"
            f"output size: {self.output_size:,} bytes\n"
            f"process size: {self.process_size:,} bytes"
        )


class MutableString(UserString):

    # Append to string
    def append(self, string: str) -> None:
        self.data += string


def str_gen(str_size: int, gen_loops: int) -> Generator[str, None, None]:
    """Used for performance testing with concatenation. String chars don't matter, however they are randomly generated"""

    random_string = "".join(f"{choice(ascii_lowercase)}" for letter in range(str_size))

    for i in range(gen_loops):
        yield random_string


def func1(generator: Generator[str, None, None]):
    """Using += operator."""

    out_str = ""

    for iter in generator:
        out_str += iter

    ps_stats()
    return out_str


def func2(generator: Generator[str, None, None]):
    """Appends strings to a string list. Once done, join them."""

    str_list = []
    for iter in generator:
        str_list.append(iter)
    out_str = "".join(str_list)
    ps_stats()
    return out_str


def func3(generator: Generator[str, None, None]):
    """Uses an in-memory stream of text."""

    file_str = StringIO()

    for iter in generator:
        file_str.write(iter)

    out_str = file_str.getvalue()
    ps_stats()
    return out_str


def func4(generator: Generator[str, None, None]):
    """Creates a string list using list comprehension and then joins it."""

    out_str = "".join([iter for iter in generator])

    ps_stats()
    return out_str


def func5(generator: Generator[str, None, None]):
    """Uses += with f'strings'."""

    out_str = ""

    for iter in generator:
        out_str += f"{iter}"

    ps_stats()
    return out_str


def func6(generator: Generator[str, None, None]):
    """Uses += with old fstrings (.format)"""

    out_str = ""

    for iter in generator:
        out_str += "{}".format(iter)

    ps_stats()
    return out_str


def func7(generator: Generator[str, None, None]):
    """Uses += with string placeholders(interpolation operator)"""

    out_str = ""

    for iter in generator:
        out_str += "%s" % (iter)

    ps_stats()
    return out_str


def func8(generator: Generator[str, None, None]):
    """Creates a string list(f'strings') using list comprehension and then joins it."""

    out_str = "".join([f"{iter}" for iter in generator])

    ps_stats()
    return out_str


# Slow - Don't use with high-performance test
def func9(generator: Generator[str, None, None]):
    """
    Using a unicode array.
    Each character of the string must be converted to unicode.
    """

    char_array = array("u")
    for iter in generator:
        # simulate a string
        for uchar in iter.encode("utf-8"):
            char_array.append(chr(uchar))
    ps_stats()
    return char_array.tounicode()


# Very slow - Don't use with high-performance test
def func10(generator: Generator[str, None, None]):
    """Appending to a mutable string."""

    out_str = MutableString("")

    for iter in generator:
        out_str.append(iter)

    ps_stats()
    return out_str


def ps_stats():
    global process_size
    ps = run("ps -up " + str(pid), shell=True, capture_output=True, text=True).stdout
    process_size = ps.split()[15]


def call_func(num: int, tests: Generator[str, None, None]) -> Performance:
    global process_size
    start = timer()
    func_name = f"func{num}"
    func = eval(func_name)
    result = func(tests)
    end = timer()

    if type(tests) == Generator:
        print(result)

    return Performance(
        index=num,
        time=end - start,
        output_size=len(result),
        process_size=int(process_size),
        description=func.__doc__,
    )


# example user input: python str_concat_test.py <OPT: func number>
if __name__ == "__main__":
    pid = getpid()

    # rapid test settings
    rapid_str_size = 10
    rapid_concat_amount = 100000

    # long str test settings
    long_str_size = 10000
    long_concat_amount = 1000

    print(
        f"Rapid test: Concatenating strings of size {rapid_str_size:,} {rapid_concat_amount:,} times"
    )
    print(
        f"Long test: Concatenating strings of size {long_str_size:,} {long_concat_amount:,} times\n\n"
    )

    # used to measure performance when concatenating small strings to a large one

    # run individual func
    if len(argv) == 2:
        print("\n\nRAPID STR CONCATENATION TESTS\n\n")
        print(call_func(argv[1], str_gen(rapid_str_size, rapid_concat_amount)))
        print("\n\nLONG STR CONCATENATION TESTS\n\n")
        print(call_func(argv[1], str_gen(long_str_size, long_concat_amount)))
    else:
        # run all funcs

        # create a list to store performance

        performance_rapid = []
        performance_long = []

        # run tests on all funcs and append performance to list
        try:
            i = 1

            while True:
                performance_rapid.append(
                    call_func(i, str_gen(rapid_str_size, rapid_concat_amount))
                )
                performance_long.append(
                    call_func(i, str_gen(long_str_size, long_concat_amount))
                )
                i += 1
        except NameError as e:
            # print(e)
            pass

        # sort list by time
        performance_rapid = sorted(performance_rapid, key=lambda func: func.time)
        performance_long = sorted(performance_long, key=lambda func: func.time)

        # print result
        print("\n\nRAPID STR CONCATENATION TESTS\n\n")
        for func in performance_rapid:
            print(func)
            print("\n")

        # Note that since random string are generated of this size it also adds time
        print("\n\nLONG STR CONCATENATION TESTS\n\n")
        for func in performance_long:
            print(func)
            print("\n")

        # write result to file
        with open(
            f"{datetime.today().strftime('%Y%m%d%H%M%S')}concat_res.txt", "w"
        ) as f:

            f.write(
                f"Rapid test: Concatenating strings of size {rapid_str_size:,} {rapid_concat_amount:,} times\n\n"
            )
            for func in performance_rapid:
                f.write(func.__str__())
                f.write("\n\n")

            f.write(
                f"\nLong test: Concatenating strings of size {long_str_size:,} {long_concat_amount:,} times\n\n"
            )
            for func in performance_long:
                f.write(func.__str__())
                f.write("\n\n")

            f.close()
