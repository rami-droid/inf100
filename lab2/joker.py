import json
import pathlib as Path

with open('joker.json', 'r') as f:
    data = json.load(f)

nums = data['grunntall']

def guess_num(n):
    if n > 4:
        return 'ned'
    else:
        return 'opp'

for number in nums:
    print(guess_num(number))