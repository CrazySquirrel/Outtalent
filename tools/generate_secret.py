import os

# Array.from(document.querySelectorAll('tr>td:nth-child(3) .fa-unlock')).map(v => parseInt(v.parentElement.parentElement.parentElement.parentElement.querySelector('td:nth-child(2)').innerText)).join(',')

secret_ids = {156, 157, 158, 159, 161, 163, 170, 186, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255,
              256, 259, 261, 265, 266, 267, 269, 270, 271, 272, 276, 277, 280, 281, 285, 286, 288, 291, 293, 294, 296,
              298, 302, 305, 308, 311, 314, 317, 320, 323, 325, 333, 339, 340, 346, 348, 351, 353, 356, 358, 359, 360,
              361, 362, 364, 366, 369, 370, 379, 408, 411, 418, 422, 425, 426, 428, 431, 439, 444, 465, 469, 471, 484,
              487, 489, 490, 499, 505, 510, 511, 512, 527, 531, 533, 534, 536, 544, 545, 548, 549, 550, 555, 562, 568,
              569, 570, 571, 573, 574, 577, 578, 579, 580, 582, 584, 585, 586, 588, 597, 602, 603, 604, 607, 608, 610,
              612, 613, 614, 615, 616, 618, 619, 624, 625, 631, 634, 635, 642, 644, 651, 656, 660, 663, 666, 681, 683,
              694, 702, 708, 711, 716, 723, 727, 734, 737, 742, 750, 751, 755, 758, 759, 760, 772, 774, 776, 800, 1045,
              1050, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070,
              1075, 1076, 1077, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1097, 1098, 1099, 1100, 1101, 1102, 1107,
              1112, 1113, 1118, 1119, 1120, 1121, 1126, 1127, 1132, 1133, 1134, 1135, 1136, 1141, 1142, 1148, 1149,
              1150, 1151, 1152, 1153, 1158, 1159, 1164, 1165, 1166, 1167, 1168, 1173, 1174, 1176, 1180, 1181, 1182,
              1183, 1188, 1193, 1194, 1196, 1197, 1198, 1199, 1204, 1205, 1211, 1212, 1213, 1214, 1215, 1216, 1225,
              1228, 1229, 1230, 1231, 1236, 1241, 1242, 1243, 1244, 1245, 1246, 1251, 1256, 1257, 1258, 1259, 1264,
              1265, 1270, 1271, 1272, 1273, 1274, 1279, 1280, 1285, 1294, 1303, 1308, 1321, 1322, 1327, 1336, 1341,
              1350, 1355, 1364, 1369, 1378, 1384, 1393, 1398, 1407, 1412, 1421, 1426, 1427, 1428, 1429, 1430, 1435,
              1440, 1445, 1454, 1459, 1468, 1469, 1474, 1479, 1484, 1485, 1490, 1495, 1500, 1501, 1506, 1511, 1516,
              1517, 1522, 1527, 1532, 1533, 1538, 1543, 1548, 1549, 1554, 1555, 1564, 1565, 1570, 1571, 1580, 1581,
              1586, 1587, 1596, 1597, 1602, 1607, 1612, 1613, 1618, 1623, 1628, 1633, 1634, 1635, 1644, 1645, 1650,
              1651, 1660, 1661, 1666, 1667, 1676, 1677, 1682, 1683, 1692, 1693, 1698, 1699, 1708, 1709, 1714, 1715,
              1724, 1729, 1730, 1731, 1740, 1741, 1746}

should_be_secret = set()
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
        is_secret_file = os.path.exists(site_file)
        id = file.split('.')[0]
        if id.isnumeric():
            id = int(id)
            if id in secret_ids:
                if is_secret_file:
                    pass
                else:
                    should_be_secret.add(id)
            else:
                if is_secret_file:
                    should_not_be_secret.add(id)
                else:
                    pass
        if not is_secret_file: continue
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
