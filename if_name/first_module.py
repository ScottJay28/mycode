#!/usr/bin/env python3
print("This code will always execute.")

def main():
    print("This code belongs to the main function in module 1.")
    print("Module #1 Name=", __name__)
if __name__ == "__main__":
    print("Code is being run directly from Python.")
    main()
else:
    print("Code is being run indirectly from import.")
