# var originOptions = {
# 		message: 'hello world',
# 		cascade: 1,
# 		brightness: 1,
# 		vertical: true
# 	};
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--device', help='string, sevensegment or matrix', type=str, default='sevensegment')
parser.add_argument('--message', help='string, "hello world"', type=str, default='hello world')
parser.add_argument('--cascade', help='integer, how many devices concated', type=int, default=1)
parser.add_argument('--brightness', help='integer from 1 to 16', type=int, default=1)
parser.add_argument('--vertical', help='boolean, device concated in which direction', type=bool)
args = parser.parse_args()
print args.device