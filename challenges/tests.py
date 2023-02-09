from django.test import TestCase

from .functions import *


class print_string_challengeTests(TestCase):

    def test_if_correct_answer_is_given(self):
        answer = '''#!/bin/bash
                            echo "Hello World!"'''
        message = print_string_challenge(answer)
        self.assertEqual("Correct :)", message)

    def test_if_incorrect_answer_is_given(self):
        answer = '''#!/bin/bash
                            echo "Hello World"'''
        message = print_string_challenge(answer)
        self.assertNotEqual("Correct :)", message)

    def test_if_gibberish_answer_is_given(self):
        answer = '''regtregrdgdfgdfgfdg'''
        message = print_string_challenge(answer)
        self.assertNotEqual("Correct :)", message)



class set_variable_challengeTests(TestCase):

    def test_if_correct_answer_is_given(self):
        answer = '''#!/bin/bash
                            my_variable="Hello World!"'''
        message = set_variable_challenge(answer)
        self.assertEqual("Correct :)", message)

    def test_if_incorrect_answer_is_given(self):
        answer = '''#!/bin/bash
                            echo "Hello World!"'''
        message = set_variable_challenge(answer)
        self.assertNotEqual("Correct :)", message)

    def test_if_gibberish_answer_is_given(self):
        answer = '''regtregrdgdfgdfgfdg'''
        message = set_variable_challenge(answer)
        self.assertNotEqual("Correct :)", message)


class multiplication_challengeTests(TestCase):

    def test_multiplication_challenge(self):
        script_string = '#!/bin/bash\necho $(($1 * $2))'
        message = multiplication_challenge(script_string)
        assert message == "Correct :)"

    def test_multiplication_challenge_incorrect_output(self):
        script_string = '#!/bin/bash\necho $(($1 ** $2))'
        message = multiplication_challenge(script_string)
        assert message == "Unfortunately, your script did not return the desired answer."

    def test_multiplication_challenge_with_syntax_error(self):
        script_string = '43534543534543'
        message = multiplication_challenge(script_string)
        assert message == "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"


class addition_challengeTests(TestCase):

    def test_addition_challenge(self):
        script_string = '#!/bin/bash\necho $(($1 + $2))'
        message = addition_challenge(script_string)
        assert message == "Correct :)"

    def test_addition_challenge_incorrect_output(self):
        script_string = '#!/bin/bash\necho $(($1 ** $2))'
        message = addition_challenge(script_string)
        assert message == "Unfortunately, your script did not return the desired answer."

    def test_addition_challenge_with_syntax_error(self):
        script_string = '43534543534543'
        message = addition_challenge(script_string)
        assert message == "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"


class subtraction_challengeTests(TestCase):

    def test_subtraction_challenge(self):
        script_string = '#!/bin/bash\necho $(($1 - $2))'
        message = subtraction_challenge(script_string)
        assert message == "Correct :)"

    def test_subtraction_challenge_incorrect_output(self):
        script_string = '#!/bin/bash\necho $(($1 ** $2))'
        message = subtraction_challenge(script_string)
        assert message == "Unfortunately, your script did not return the desired answer."

    def test_subtraction_challenge_with_syntax_error(self):
        script_string = '43534543534543'
        message = subtraction_challenge(script_string)
        assert message == "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"


class division_challengeTests(TestCase):

    def test_division_challenge(self):
        script_string = '#!/bin/bash\necho $(($1 / $2))'
        message = division_challenge(script_string)
        assert message == "Correct :)"

    def test_division_challenge_incorrect_output(self):
        script_string = '#!/bin/bash\necho $(($1 ** $2))'
        message = division_challenge(script_string)
        assert message == "Unfortunately, your script did not return the desired answer."

    def test_division_challenge_with_syntax_error(self):
        script_string = '43534543534543'
        message = division_challenge(script_string)
        assert message == "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"



class AssessCallTests(TestCase):

    def test_if_correct_answer_is_given(self):
        self.assertEqual(assess_call('xxHello World!xxx', "Hello World!"), "Correct :)")

    def test_if_incorrect_answer_is_given(self):
        input = '''asdsadsadsadasdsa
                            echo "Hello World"'''
        self.assertEqual(assess_call(input, "Hello World!"), "Unfortunately, your script did not return the desired answer.")