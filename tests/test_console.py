#!/usr/bin/python3
""" Unittests for console class and all its attributes and methods
"""
from console import HBNBCommand
from io import StringIO
import json
import os
import pep8
import sys
import unittest
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ Tests Console Class """

    def test_create(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NOPE")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_destroy(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NOPE")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_show(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NOPE")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_all(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all NOPE")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_update(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NOPE")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")
