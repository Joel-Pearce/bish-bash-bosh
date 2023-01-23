from django.test import TestCase

from .functions import *


class print_string_challengeTests(TestCase):

    def test_if_correct_answer_is_given(self):
        answer = '''#!/bin/bash
                            echo "Hello World!"'''
        result, message = print_string_challenge(answer)
        self.assertEqual("Hello World!", result)

    def test_if_incorrect_answer_is_given(self):
        answer = '''#!/bin/bash
                            echo "Hello World"'''
        result, message = print_string_challenge(answer)
        self.assertNotEqual("Hello World!", result)

    def test_if_gibberish_answer_is_given(self):
        answer = '''regtregrdgdfgdfgfdg'''
        result, message = print_string_challenge(answer)
        self.assertNotEqual("Hello World!", result)



class set_variable_challengeTests(TestCase):

    def test_if_correct_answer_is_given(self):
        answer = '''#!/bin/bash
                            my_variable="Hello World!"'''
        result, message = set_variable_challenge(answer)
        self.assertEqual("Hello World!", result)

    def test_if_incorrect_answer_is_given(self):
        answer = '''#!/bin/bash
                            echo "Hello World!"'''
        result, message = set_variable_challenge(answer)
        self.assertNotEqual("Hello World!", result)

    def test_if_gibberish_answer_is_given(self):
        answer = '''regtregrdgdfgdfgfdg'''
        result, message = set_variable_challenge(answer)
        self.assertNotEqual("Hello World!", result)


class multiplication_challengeTests(TestCase):

    def test_if_correct_answer_is_given(self):
        answer = '''#!/bin/bash
                            my_variable="Hello World!"'''
        result, message = set_variable_challenge(answer)
        self.assertEqual("Hello World!", result)

    def test_if_incorrect_answer_is_given(self):
        answer = '''#!/bin/bash
                            echo "Hello World!"'''
        result, message = set_variable_challenge(answer)
        self.assertNotEqual("Hello World!", result)

    def test_if_gibberish_answer_is_given(self):
        answer = '''regtregrdgdfgdfgfdg'''
        result, message = set_variable_challenge(answer)
        self.assertNotEqual("Hello World!", result)




class AssessCallTests(TestCase):

    def test_if_correct_answer_is_given(self):
        self.assertEqual(assess_call('xxHello World!xxx', "Hello World!"), "Correct :)")

    def test_if_incorrect_answer_is_given(self):
        input = '''asdsadsadsadasdsa
                            echo "Hello World"'''
        self.assertEqual(assess_call(input, "Hello World!"), "Unfortunately, your script did not return the desired answer.")