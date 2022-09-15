import datetime

import pytest

from approvaltests import verify
from approvaltests.utilities.logger.simple_logger import SimpleLogger


def log_from_inner_method():
    with SimpleLogger.use_markers() as m:
        name = "Example"
        SimpleLogger.variable("name", name)
        for _ in range(0, 142):
            SimpleLogger.hour_glass()


def test_standard_logger():
    output = SimpleLogger.log_to_string()
    with SimpleLogger.use_markers() as m:
        log_from_inner_method()

    verify(output)


def test_timestamps():
    output = SimpleLogger.log_to_string()
    count = -1

    def create_applesauce_timer():
        dates = [
            datetime.datetime.fromtimestamp(0.0),
            datetime.datetime.fromtimestamp(0.5),
            datetime.datetime.fromtimestamp(2.0),
            datetime.datetime.fromtimestamp(1050),
            datetime.datetime.fromtimestamp(1052),
        ]
        nonlocal count
        count = count + 1
        return dates[count]

    SimpleLogger.logger.timer = create_applesauce_timer
    SimpleLogger.show_timestamps(True)
    SimpleLogger.event("1")
    SimpleLogger.event("2")
    SimpleLogger.event("3")
    SimpleLogger.event("4")
    SimpleLogger.warning(Exception("Oh no you didn't!"))
    verify(output)



def test_switching() -> None:
    output = SimpleLogger.log_to_string()
    #log everything
    log_everything()
    #toggle all
    # switches query, warning, message, variable, event, hourglass, markers
    #cycle through the switches and log everything
    verify(output)


def log_everything():
    with SimpleLogger.use_markers() as m:
        SimpleLogger.query("Select * from people")
        SimpleLogger.variable("Nonsense", "foo")
        SimpleLogger.event("Testing")
        SimpleLogger.message("Something random")
        for a in range(1, 13):
            SimpleLogger.hour_glass()
        try:
            infinity = 1/0
        except Exception as e :
            SimpleLogger.warning(e)