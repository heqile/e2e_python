import test_data.globals
import pytest
from os.path import dirname, abspath


def main():
    test_data.globals.initialize_data(dirname(abspath(__file__)), "PROD")
    pytest.cmdline.main()


if __name__ == "__main__":
    main()