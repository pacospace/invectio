import sys
import os
from pathlib import Path
from setuptools import setup
from setuptools.command.test import test as TestCommand

HERE = os.path.dirname(os.path.realpath(__file__))


class Test(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = [
            "tests/",
            "--timeout=2",
            "--cov=./invectio",
            "--capture=no",
            "--verbose",
            "-l",
            "-s",
            "-vv",
        ]

    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        sys.exit(pytest.main(self.pytest_args))


setup(
    install_requires=(Path(HERE) / "requirements.txt").read_text(),
    cmdclass={"test": Test},
)
