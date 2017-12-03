# -*- coding:utf-8 -*-
import os
from distutils.core import setup
print(os.getcwd())

setup(name='testSetub', version='1.0', description='This is just setub test', author='Liy'
      , py_modules=['TestSetub.SendMsg', 'TestSetub.RecvMsg'])