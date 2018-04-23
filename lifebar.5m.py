#!/usr/bin/env python

# <bitbar.title>Life Bar</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>hachibu</bitbar.author>
# <bitbar.author.github>hachibu</bitbar.author.github>
# <bitbar.desc>Displays how much life you have left. Set your birth and death in the script.</bitbar.desc>
# <bitbar.image>https://raw.githubusercontent.com/hachibu/lifebar/master/images/screenshot.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/hachibu/lifebar</bitbar.abouturl>

from datetime import datetime

birth = datetime(1984, 1, 2)
death = datetime(2074, 1, 2)

today = datetime.now()
life_seconds = (death - birth).total_seconds()
left_seconds = (death - today).total_seconds()

print('{:.0f}% :skull:'.format(left_seconds / life_seconds * 100))
print('---')
print('{:,d} days left'.format(int(left_seconds / (3600 * 24))))
print('{:,d} hours left'.format(int(left_seconds / 3600)))
print('{:,d} minutes left'.format(int(left_seconds / 60)))
