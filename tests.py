from functions.run_python_file import run_python_file


result1 = run_python_file("calculator", "main.py")
print(f"Result for current file:\n{result1}")


result2 = run_python_file("calculator", "main.py", ["3 + 5"])
print(f"Result for current file:\n{result2}")


result3 = run_python_file("calculator", "tests.py")
print(f"Result for current file:\n{result3}")


result4 = run_python_file("calculator", "../main.py")
print(f"Result for current file:\n{result4}")


result5 = run_python_file("calculator", "nonexistent.py")
print(f"Result for current file:\n{result5}")



