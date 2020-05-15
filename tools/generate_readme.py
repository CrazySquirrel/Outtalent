import os
import urllib.parse

dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(dir_path, '../'))

GIT_ULR_PREFIX = 'https://github.com/CrazySquirrel/Outtalent/tree/master'

SITES = ['Leetcode']

result = [
    '# Algorithms, data structures and programming solutions.',
    ''
]

for site in SITES:
    result.append('* [%s](%s/%s)' % (site, GIT_ULR_PREFIX, urllib.parse.quote(site)))

    tasks = []

    for file in os.listdir(os.path.join(root_path, site)):
        if os.path.isdir(os.path.join(root_path, site, file)):
            tasks.append(file)

    for task in sorted(tasks, key=lambda x: int(x.split('.')[0])):
        result.append('\t* [%s](%s/%s/%s)' % (task, GIT_ULR_PREFIX, site, urllib.parse.quote(task)))

    result.append('')

with open(os.path.join(root_path, 'README.md'), 'w') as readme:
    readme.write('\r\n'.join(result))

print('README.md UPDATED!!!')
