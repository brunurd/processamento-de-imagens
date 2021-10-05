import sys
import pylint


def lint():
    sys.argv += ["sigal_gallery", "scripts"]
    pylint.modify_sys_path()
    pylint.run_pylint()


if __name__ == "__main__":
    lint()
