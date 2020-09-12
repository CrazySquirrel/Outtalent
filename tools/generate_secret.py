import os

dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(dir_path, '../'))

secrets = []

for site in ['Leetcode']:
    site_path = os.path.join(root_path, site)

    for file in os.listdir(site_path):
        site_dir = os.path.join(site_path, file)
        if not os.path.isdir(site_dir): continue
        site_file = os.path.join(site_dir, '.secret')
        if not os.path.exists(site_file): continue
        secret = ('%s/%s' % (site, file)).replace(' ', '[[:space:]]')
        secrets.append(secret + '/** filter=git-crypt diff=git-crypt')

with open(os.path.join(root_path, '.gitattributes'), 'w') as readme:
    gitattributes = ['*.png filter=lfs diff=lfs merge=lfs -text',
                     '*.jpg filter=lfs diff=lfs merge=lfs -text',
                     '*.gif filter=lfs diff=lfs merge=lfs -text',
                     '*.svg filter=lfs diff=lfs merge=lfs -text',
                     ''] + sorted(secrets, key=lambda x: int(x[9:].split('.')[0]))
    readme.write('\n'.join(gitattributes))
