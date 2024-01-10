#!/usr/bin/env python3

def main():
    ##create dictionary with 4key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ##display dictionary
    print(switch)

    ##prove that switch is a dictionary
    print(type(switch))

    ## display parts of dictionary
    print( switch["hostname"])
    print(switch["ip"])

    ##request fake key
    print(switch["lynx"])

if __name__ == "__main__":
    main()
