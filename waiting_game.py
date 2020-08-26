import time
import random

def waiting_game():
    """a function to calculate the time between two enters"""
    target = random.randint(2,4) # target seconds to wait
    print('\nYour target time is {} seconds'.format(target))
    
    input(' ---Press Enter to Begin--- ')
    #return a float value of the current time in fractional second
    start = time.perf_counter()
    
    input('\n...Press Enter again after {} seconds...'.format(target))
    #calculate the elapsed time
    elapsed = time.perf_counter() - start
    
    print('\nElapsed time: {0:.3f} seconds'.format(elapsed))
    if elapsed == target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
        print('({0:.3f} seconds too fast)'.format(target - elapsed))
    else:
        print('({0:.3f} seconds too slow)'.format(elapsed - target))
