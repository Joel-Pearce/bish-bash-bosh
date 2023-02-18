import subprocess
import os
import shlex

# tests script by comparing output to ensure is "Hello World!"
def print_string_challenge(script_string):
    result = ""
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    results = {'Input': 'N/A', 'Output': str(result)[2:-3]}
    return message, results

# tests script by echoing the variable 'my_variable' to ensure is "Hello World!"
def set_variable_challenge(script_string):
    result = ""
    script_string += "\necho $my_variable"
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    results = {'Input': '', 'Output': str(result)[2:-3]}
    return message, results

# range of inputs and outputs to test challenge, will break if script incorrect
def multiplication_challenge(script_string):
    result = ""
    file_path = "multiplication.sh"
    create_code_submission(file_path, script_string)
    results = {'Input': 'N/A', 'Output': ''}

    test_inputs = [(2, 3, 6), (4, 5, 20), (6, 7, 42)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                results['Input'] = str(x) + ', ' + str(y)
                results['Output'] = str(result)[2:-5]
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    os.remove(file_path)
    results['Input'] = str(x) + ', ' + str(y)
    results['Output'] = str(result)[2:-5]
    return message, results


def addition_challenge(script_string):
    result = ""
    file_path = "addition.sh"
    create_code_submission(file_path, script_string)
    results = {'Input': '', 'Output': ''}

    test_inputs = [(2, 3, 5), (4, 5, 9), (6, 7, 13)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                results['Input'] = str(x) + ', ' + str(y)
                results['Output'] = str(result)[2:-5]
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    os.remove(file_path)
    results['Input'] = str(x) + ', ' + str(y)
    results['Output'] = str(result)[2:-5]
    return message, results


def subtraction_challenge(script_string):
    result = ""
    file_path = "subtraction.sh"
    create_code_submission(file_path, script_string)
    results = {'Input': '', 'Output': ''}

    test_inputs = [(2, 3, -1), (4, 5, -1), (6, 7, -1)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                results['Input'] = str(x) + ', ' + str(y)
                results['Output'] = str(result)[2:-5]
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    os.remove(file_path)
    results['Input'] = str(x) + ', ' + str(y)
    results['Output'] = str(result)[2:-5]
    return message, results


def division_challenge(script_string):
    result = ""
    file_path = "divsion.sh"
    create_code_submission(file_path, script_string)
    results = {'Input': '', 'Output': ''}

    test_inputs = [(10, 2, 5), (10, 5, 2), (100, 10, 10)]

    for x, y, expected_output in test_inputs:
        try:
            result = subprocess.check_output(shlex.split('bash ' + file_path + ' ' + str(x) + ' ' + str(y)))
            message = assess_call(result, expected_output)
            if message == "Unfortunately, your script did not return the desired answer.":
                results['Input'] = str(x) + ', ' + str(y)
                results['Output'] = str(result)[2:-5]
                break
        except Exception as e:
            print(e)
            message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    os.remove(file_path)
    results['Input'] = str(x) + ', ' + str(y)
    results['Output'] = str(result)[2:-5]
    return message, results


# the return value from check_output needs to be trimmed; this method trims it and ensures it matches with expected output
def assess_call(input, expected_output):
    if str(input)[-5:] == "\\r\\n\'":
        input = str(input)[2:-5]
    else:
        input = str(input)[2:-3]
    if input == str(expected_output):
        return "Correct :)"
    else:
        return "Unfortunately, your script did not return the desired answer."

# return correct challenge no.
def assign_challenge(input, no):
    match no:
        case 1:
            return print_string_challenge(input)
        case 2:
            return set_variable_challenge(input)
        case 3:
            return multiplication_challenge(input)
        case 4:
            return addition_challenge(input)
        case 5:
            return subtraction_challenge(input)
        case 6:
            return division_challenge(input)

# create file with code submission that will later be called by check_output method
def create_code_submission(file_path, file_contents):
    with open(file_path, "w") as f:
        f.write(file_contents)
    f.close()
    os.chmod(file_path, 0o0777)



