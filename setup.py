# vim: fileencoding=utf-8

import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='qubeskicksecure',
        version=open('version').read().strip(),
        author='Invisible Things Lab',
        author_email='marmarek@invisiblethingslab.com',
        description='Qubes Kicksecure core-admin extension',
        license='GPL2+',
        url='https://www.qubes-os.org/',

        packages=('qubeskicksecure',),

        entry_points={
            'qubes.ext': [
                'qubeskicksecure = qubeskicksecure:QubesKicksecureExtension',
            ],
        }
    )
