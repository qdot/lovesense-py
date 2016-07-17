import pytest
import lovesense
import os

###############################################################################
# Test Decorators
###############################################################################


def toy_only(func):
    def wrapper(*args, **kwargs):
        if "LOVESENSE_SERIAL_PORT" not in os.environ.keys():
            pytest.skip("Toy only test, skipping.")
        with lovesense.LovesenseSerialSync(os.environ["LOVESENSE_SERIAL_PORT"]) as ls_toy:
            func(toy=ls_toy)
    return wrapper


def emulator_only(func):
    def wrapper(*args, **kwargs):
        if "LOVESENSE_SERIAL_PORT" in os.environ.keys():
            pytest.skip("Emulator only test, skipping.")
        with lovesense.LovesenseEmulatorSync() as ls_toy:
            func(ls=ls_toy)
    return wrapper


def toy_or_emulator(func):
    def wrapper(*args, **kwargs):
        if "LOVESENSE_SERIAL_PORT" in os.environ.keys():
            with lovesense.LovesenseSerialSync(os.environ["LOVESENSE_SERIAL_PORT"]) as ls_toy:
                func(toy=ls_toy)
        else:
            with lovesense.LovesenseEmulatorSync() as ls_toy:
                func(ls=ls_toy)
    return wrapper


###############################################################################
# Tests
###############################################################################


def test_missing_serial():
    import serial
    with pytest.raises(serial.serialutil.SerialException):
        lovesense.LovesenseSerialSync("not-a-port")


def test_wrong_serial():
    with pytest.raises(lovesense.LovesenseIOError):
        lovesense.LovesenseSerialSync(1)
