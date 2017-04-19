#!/usr/bin/env python3

import os
import subprocess

prefix = os.environ['MESON_INSTALL_PREFIX']
schemadir = os.path.join(os.environ['MESON_INSTALL_PREFIX'], 'share', 'glib-2.0', 'schemas')

if not os.environ.get('DESTDIR'):
    print('Compiling gsettings schemas...')
    subprocess.call(['glib-compile-schemas', schemadir])

    print('Copying built files')
    subprocess.call(['cp', '-rvf', os.path.join(os.environ['MESON_BUILD_ROOT'], 'elephas'),
                     os.environ['MESON_SOURCE_ROOT']])

    print('Installing via setuptools')
    subprocess.call(['pip3', 'install', '-r', 'requirements.txt', '--prefix=' + prefix],
                    cwd=os.environ['MESON_SOURCE_ROOT'])
    subprocess.call(['python3', 'setup.py', 'install', '--prefix=' + prefix],
                    cwd=os.environ['MESON_SOURCE_ROOT'])
