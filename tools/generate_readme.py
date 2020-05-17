import os
import urllib.parse

dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(dir_path, '../'))

GIT_ULR_PREFIX = 'https://github.com/CrazySquirrel/Outtalent/tree/master'

SITES = ['Leetcode']

global_readme = [
    '# Algorithms, data structures and programming solutions.',
    ''
]

for site in SITES:
    site_path = os.path.join(root_path, site)

    global_readme.append('* [%s](%s/%s)' % (site, GIT_ULR_PREFIX, urllib.parse.quote(site)))

    site_readme = [
        '# %s' % (site),
        ''
    ]

    tasks = []

    for file in os.listdir(site_path):
        if os.path.isdir(os.path.join(site_path, file)):
            tasks.append(file)

    for task in sorted(tasks, key=lambda x: int(x.split('.')[0])):
        global_readme.append('\t* [%s](%s/%s/%s)' % (task, GIT_ULR_PREFIX, site, urllib.parse.quote(task)))
        site_readme.append('* [%s](%s/%s/%s)' % (task, GIT_ULR_PREFIX, site, urllib.parse.quote(task)))

    global_readme.append('')

    with open(os.path.join(site_path, 'README.md'), 'w') as readme:
        readme.write('\r\n'.join(site_readme))

with open(os.path.join(root_path, 'README.md'), 'w') as readme:
    readme.write('\r\n'.join(global_readme))

print('README.md UPDATED!!!')
