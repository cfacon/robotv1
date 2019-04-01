import subprocess
import os
import server as srv
#import robotv1.server as srv

os.chdir("/home/pi/robotRelease/robotv1")

def git(*args):
    return subprocess.check_call(['git'] + list(args))

git("remote", "set-url", "origin", "https://cfacon:git1Secret,42@github.com/cfacon/robotv1.git")
git("pull")

srv.start()
