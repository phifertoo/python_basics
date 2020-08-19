import logging

# if you want your debug output to 
logging.basicConfig(filename='debugging_log.txt', level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) to turn off all the debug calls (you can't do this with print())
# log levels: debug, info, warning, error, critical
# CRITICAL disables all logging. ERROR disables all logging except for CRITICAL.
logging.disable(logging.CRITICAL)


logging.debug('Start of program')

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
        # debug is the lowest level of debugging
        # critical is the highest level of debugging
        logging.debug('i is %s, Return value is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')