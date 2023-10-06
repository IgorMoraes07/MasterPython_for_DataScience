# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")

# TODO: Try out each of the log levels
logging.debug("Thia is a debug-level message")
logging.info("Thia is a info message")
logging.warning("Thia is a warning message")
logging.error("Thia is a error message")
logging.critical("Thia is a critical message")

# TODO: Output formatted strings to the log
x = "string"
y = 10
logging.info(f"Here's a {x} variable and int: {y}")
