import subprocess
import os


def challenge1(script_string):
    result = ""
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message


def challenge2(script_string):
    result = ""
    script_string += "\necho $my_variable"
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return str(result)[2:-3], message


def assess_call(input, expected_output):
    if str(input)[2:-3] == expected_output:
        return "Correct :)"
    else:
        return "Unfortunately, your script did not return the desired answer."


def assign_challenge(input, no):
    match no:
        case 1:
            return challenge1(input)
        case 2:
            return challenge2(input)


