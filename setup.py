from __future__ import print_function

# detect systemd
def have_systemd():
    from subprocess import check_output

    def get_pid(name):
        try:
            return [int(i) for i in check_output(["pidof",name]).split()]
        except:
            return []
    return True if 1 in get_pid("systemd") else False

etc_files = []
import os
if os.uname()[0] == 'Linux':
    if have_systemd():
        print("Detected systemd")
        etc_files.append(('/etc/systemd/system',['init/glowd.service']))
    else:
        print("Detected sysvinit")
        etc_files.append(('/etc/init.d',['init/glowd']))
    if not os.path.exists('/etc/glowd.conf'):
        etc_files.append('/etc',['glowd.conf'])

from setuptools import setup
setup(
    name='glow',
    version='0.1.0',
    description='Control your LED strip via the network.',
    url='https://github.com/jmechnich/glow',
    author='Joerg Mechnich',
    author_email='joerg.mechnich@gmail.com',
    license='MIT',
    packages=[
        'glow',
    ],
    scripts=[
        'glowd',
    ],
    data_files=etc_files,
 )
