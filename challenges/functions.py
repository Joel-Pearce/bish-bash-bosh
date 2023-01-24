import subprocess
import os
import shlex


def print_string_challenge(script_string):
    result = ""
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message


def set_variable_challenge(script_string):
    result = ""
    script_string += "\necho $my_variable"
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message


def multiplication_challenge(script_string):
    result = ""
    file_path = "multiplication.sh"
    create_code_submission(file_path, script_string)

    test_inputs = [(2, 3, 6), (4, 5, 20), (6, 7, 42)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message


def addition_challenge(script_string):
    result = ""
    file_path = "multiplication.sh"
    create_code_submission(file_path, script_string)

    test_inputs = [(2, 3, 5), (4, 5, 9), (6, 7, 13)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message


def substraction_challenge(script_string):
    result = ""
    file_path = "multiplication.sh"
    create_code_submission(file_path, script_string)

    test_inputs = [(2, 3, -1), (4, 5, -1), (6, 7, -1)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message


def division_challenge(script_string):
    result = ""
    file_path = "multiplication.sh"
    create_code_submission(file_path, script_string)

    test_inputs = [(10, 2, 5), (10, 5, 2), (100, 10, 10)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message



def assess_call(input, expected_output):
    if str(input)[2:-3] == str(expected_output):
        return "Correct :)"
    else:
        return "Unfortunately, your script did not return the desired answer."


def assign_challenge(input, no):
    match no:
        case 1:
            return print_string_challenge(input)
        case 2:
            return set_variable_challenge(input)
        case 3:
            return multiplication_challenge(input)


def create_code_submission(file_path, file_contents):
    with open(file_path, "w") as f:
        f.write(file_contents)
    f.close()
    os.chmod(file_path, 0o0777)



