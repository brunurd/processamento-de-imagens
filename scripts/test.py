import subprocess


def test():
    subprocess.call([
        "coverage",
        "run", "-m", "pytest",
        "--junitxml=./tests_report/junit.xml",
        "-s", "--maxfail=1",
    ])

    subprocess.call(["coverage", "report", "--fail-under=80", "-m"])

    subprocess.call(["coverage", "html", "-d", "tests_report"])


if __name__ == "__main__":
    test()
