1. markdown snippets
2. powershell scripts
    add mdsnippets
3. starter projects
4. options support
5. check all uses of default reporter in tests
6. make code more pythonic (method overloads vs default parameters)
7. change setup.py to pull in requirements.txt - and check requirements
8. Fail test if there are duplicate names - pylint ?
9. python type hints - use mypy linter to check it - see code snippet below
10. Agree on defaults: should be \n instead of os specific when writing, BOM on new file creation,
     the new file creation handles writing with correct encoding
11. combination approvals needs line ending option
12. add checks to twine in github actions
13. use BLACK for formatting
15. error output is too confusing
20. add tests to test the installed library - integration or system tests. For example, to confirm that JSON reporter files work. tox might help us.

  def test_mypy(self) -> None:
       try:
           import mypy.api
       except ImportError:
           print("mypy not found")
           self.skipTest("mypy not found")
       stdout, stderr, exit_code = mypy.api.run([
           '--config-file', 'mypy.ini',
           SCRIPT_DIR,
       ])
       self.assertEqual(0, exit_code, "\n\n" + stdout + stderr)
21. linter - add flake8 to pycharm and tox
22. Add documentation.
23. Look at issues https://github.com/approvals/ApprovalTests.Python/issues
24. add options to signature
25. Randomize order of tests in pytest plugin


Authors:
@claremacrae
@objarni
@tdpreece
@emilybache
@rzijp
@obestwalter
