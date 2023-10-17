from setuptools import setup
from setuptools.command.install import install
import os


class PvwWrapperInstall(install):
    def run(self):
        if os.name != "nt":
            self.wrapper_install()
        install.run(self)

    def wrapper_install(self):
        print("wrap")


setup(cmdclass={"install": PvwWrapperInstall})
