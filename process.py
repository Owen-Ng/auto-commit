import subprocess


def execute():
    f = open("./file.txt", "a")
    f.write(" ")
    f.close()
    subprocess.run(["git", "status", ";"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "'ew'"])
    subprocess.run(["git", "push"])
# CompletedProcess(args=['C:\\Program Files\\Git\\bin\\bash.exe', '-c', 'ls'], returncode=0,
#                  stdout=b'README.md\n__pycache__\nconda_create.sh\nenvs\nmain.py\ntest.sh\nzipped\n')
