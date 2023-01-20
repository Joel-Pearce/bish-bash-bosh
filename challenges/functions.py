import subprocess
import os


def challenge1(script_string):
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return message


def challenge2(script_string):
    print(script_string)
    try:
        result = subprocess.check_output(script_string, shell=True)
        message = assess_call(result, "Hello World!")
    except:
        message = "Your scipt has returned a non-zero exit code. Did you forget to include #!/bin/bash at the beginning of the script?"
    return message


def assess_call(input, expected_output):
    if str(input)[2:-3] == expected_output:
        return "Correct :)"
    else:
        return "Unfortunately, your script did not return the desired answer."




