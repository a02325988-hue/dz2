import logging

logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w',format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s"
)
logging.debug("Debug Info")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

#w-write
#r-read


def divide(x, y):
    try:
        result = x / y
        logging.info(f"Division result {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Division error {e}")

#a = int(input("Enter a number: "))
#b = int(input("Enter another number: "))
#divide(a, b)

if 2 + 2 == 4
    print("in fact,2 + 2 equals 4")

assert 2 + 2 == 5, "2+2 equals 4,not 5"


