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
    data_files=[('/etc/systemd/system',['init/glowd.service']),
                ('/etc/init.d',['init/glowd'])],
 )
