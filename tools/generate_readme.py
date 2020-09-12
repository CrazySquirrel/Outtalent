import os
import urllib.parse
import subprocess

secret_files = subprocess.Popen('git-crypt status -e',
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True).communicate()[0].decode('utf-8').splitlines()

secret_files = {x.replace('    encrypted: ', '').replace('../', '') for x in secret_files if 'README.md' in x}

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

    site_readme = [
        '# %s' % (site),
        ''
    ]

    tasks = []

    for file in os.listdir(site_path):
        if os.path.isdir(os.path.join(site_path, file)):
            tasks.append(file)

    for task in sorted(tasks, key=lambda x: int(x.split('.')[0])):
        is_secret = ('%s/%s/README.md' % (site, task)) in secret_files
        if is_secret:
            site_readme.append('* ~~%s~~ (Secret)' % (task))
        else:
            site_readme.append('* [%s](%s/README.md)' % (task, urllib.parse.quote(task)))

    with open(os.path.join(site_path, 'README.md'), 'w') as readme:
        readme.write('\n'.join(site_readme))

print('README.md UPDATED!!!')
