from datetime import datetime, timedelta
from timer import sleep
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Timer')
    parser.add_argument(dest='TC', action='store', metavar='Complete_Time', help='Complete Time',nargs='?')
    parser.add_argument('-s', '--sec', action='store', metavar='SEC', help='Second', default=0, type=int)
    parser.add_argument('-m', '--min', action='store', metavar='MIN', help='Minute', default=0)
    parser.add_argument('-hr', '--hour', action='store', metavar='HR', help='Hour', default=0)
    args = parser.parse_args()
    t1 = datetime.now() + timedelta(hours=args.hour, minutes=args.min, seconds=args.sec)
    try:
        while True:
            t2 = datetime.now()
            print(t2)
            if t2 >= t1:
                print('time out')
                break
            sleep(1)
    except KeyboardInterrupt:
        print("\nFinished:")
#

