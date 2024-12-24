
#Error handling and exception
try:
    file = open("myData.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("oops! This flie does not exist")
except PermissionError:
        print(f"Error: You do not have permission to read the file.")
except IOError:
        print(f"Error: An I/O error occurred while trying to read the file.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")    
finally:
    print("It's was nice seeing this")
