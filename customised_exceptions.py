def function():
    # Code that may raise a custom exception
    # if condition:
        raise Exception("Error description")

try:
    function()
except Exception as e:
    print(f"Error: {str(e)}")