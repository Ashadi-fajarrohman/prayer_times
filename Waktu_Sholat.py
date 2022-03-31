from math import *


def dms_to_dd(d, m, s):
    dd = d + float(m) / 60 + float(s) / 3600
    return dd


def dd_to_dms(dd):
    mnt, sec = divmod(dd * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    if sec > 30:
        mnt = mnt+1
    return deg, mnt+2


lintang = dms_to_dd(-6, -19, 0)
bujur = dms_to_dd(107, 0, 0)
deklinasi = dms_to_dd(4, 26, 0)
eot = dms_to_dd(0, -4, -1)
bd = dms_to_dd(105, 0, 0)  # bujur daerah

mp = 12 - eot  # meridian pass
kwd = (bujur - bd) / 15  # koreksi waktu daerah

# sholat dzuhur
dzuhur = mp - kwd
print(dd_to_dms(dzuhur))
# print(dzuhur)

# sholat ashar
cot_h = tan(radians(abs(lintang - deklinasi))) + 1
h_ashar = degrees(atan(1 / cot_h))

cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_ashar)) / cos(radians(lintang)) / cos(
    radians(deklinasi)))
t = degrees(acos(cos_t))

ashar = mp + (t / 15) - kwd
print(dd_to_dms(ashar))

# sholat magrib
h_magrib = dms_to_dd(-1, 0, 0)
cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_magrib)) / cos(radians(lintang)) / cos(
    radians(deklinasi)))
t = degrees(acos(cos_t))

magrib = mp + (t / 15) - kwd
print(dd_to_dms(magrib))

# sholat isya
h_isya = dms_to_dd(-18, 0, 0)
cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_isya)) / cos(radians(lintang)) / cos(
    radians(deklinasi)))
t = degrees(acos(cos_t))

isya = mp + (t / 15) - kwd
print(dd_to_dms(isya))

# sholat subuh
h_subuh = dms_to_dd(-20, 0, 0)
cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_subuh)) / cos(radians(lintang)) / cos(
    radians(deklinasi)))
t = degrees(acos(cos_t))

subuh = mp - (t / 15) - kwd
print(dd_to_dms(subuh))

# sholat syuruq
h_syuruq = dms_to_dd(-1, 0, 0)
cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_syuruq)) / cos(radians(lintang)) / cos(
    radians(deklinasi)))
t = degrees(acos(cos_t))

syuruq = mp - (t / 15) - kwd
print(dd_to_dms(syuruq))

# waktu duha
h_duha = dms_to_dd(3, 0, 0)
cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_duha)) / cos(radians(lintang)) / cos(
    radians(deklinasi)))
t = degrees(acos(cos_t))

duha = mp - (t / 15) - kwd
print(dd_to_dms(duha))

# waktu dengan ihtiyat
