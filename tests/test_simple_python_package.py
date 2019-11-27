#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `simple_python_package` package."""


import unittest
from click.testing import CliRunner

from simple_python_package import simple_python_package
from simple_python_package import cli


class TestSimple_python_package(unittest.TestCase):
    """Tests for `simple_python_package` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.hello_message = "Hello from Simple Python Package"

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'simple_python_package.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_say_hello(self):
        output = simple_python_package.hello()
        assert(output == self.hello_message)

