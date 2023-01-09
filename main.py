import unittest
from HtmlTestRunner import HTMLTestRunner


def main():
    modules_to_test = unittest.defaultTestLoader.discover(start_dir='tests/', pattern='*.py', top_level_dir=None)
    HTMLTestRunner(output='./test-reports').run(modules_to_test)


if __name__ == '__main__':
    main()
