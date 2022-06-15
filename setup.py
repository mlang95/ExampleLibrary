from setuptools import find_packages, setup
setup(
  name = "levenshtein",
  packages = find_packages(),
  version = "0.1.0",
  description = "Levenshtein is used to demonstrate how similar two strings are",
  license = "",
  install_requires = ["numpy"],
  setup_requires = [],
  tests_requires = [],
  test_suite = "tests",
)
