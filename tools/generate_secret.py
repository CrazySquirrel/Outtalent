import os

# Array.from(document.querySelectorAll('tr>td:nth-child(3) .fa-unlock')).map(v => parseInt(v.parentElement.parentElement.parentElement.parentElement.querySelector('td:nth-child(2)').innerText)).join(',')

should_be_secret = {339, 346, 359, 511, 577, 584, 586, 613, 760, 1050, 1068, 1069, 1082, 1085, 1086, 1119, 1134, 1148,
                    1165, 1173, 1180, 1213, 1251, 1279, 1280, 1303, 1327, 1350, 1378, 1407, 1435, 1469, 1474, 1484,
                    1511, 1517, 1527, 1565, 1571, 1581}

should_not_be_secret = set()

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
        id = file.split('.')[0]
        if id.isnumeric():
            id = int(id)
            if id not in should_be_secret: should_not_be_secret.add(id)
            if id in should_be_secret: should_be_secret.remove(id)
        secret = ('%s/%s' % (site, file)).replace(' ', '[[:space:]]')
        secrets.append(secret + '/** filter=git-crypt diff=git-crypt')

with open(os.path.join(root_path, '.gitattributes'), 'w') as readme:
    gitattributes = ['*.png filter=lfs diff=lfs merge=lfs -text',
                     '*.jpg filter=lfs diff=lfs merge=lfs -text',
                     '*.gif filter=lfs diff=lfs merge=lfs -text',
                     '*.svg filter=lfs diff=lfs merge=lfs -text',
                     ''] + sorted(secrets, key=lambda x: int(x[9:].split('.')[0]))
    readme.write('\n'.join(gitattributes))

if should_not_be_secret:
    print('Should not be secret: %s' % (', '.join(map(str, should_not_be_secret))))

if should_be_secret:
    print('Should be secret: %s' % (', '.join(map(str, should_be_secret))))
