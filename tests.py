from functions.get_file_content import get_file_content


result1 = get_file_content("calculator", "main.py")
print(f"Result for current file:\n{result1}")


result2 = get_file_content("calculator", "pkg/calculator.py")
print(f"Result for current file:\n{result2}")


result3 = get_file_content("calculator", "/bin/cat")
print(f"Result for current file:\n{result3}")


result4 = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"Result for current file:\n{result4}")
