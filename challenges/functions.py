import subprocess
import os

def challenge1_tests(script_string):
    file_path = 'challenges/code_submissions/challenge1.sh'
    f = open(file_path, 'w')
    f.write(script_string)
    f.close()
    os.chmod(file_path, 0o0777)
    result = subprocess.check_output('bash challenge1.sh', cwd='/home/joely/django_projects/bish_bash_bosh/challenges/code_submissions', shell=True)
    if str(result) == "b\'Hello World!\\n\'":
        message = "Correct :)"
    else:
        message = "Unfortunately, your script did not return the desired answer."

    return message
