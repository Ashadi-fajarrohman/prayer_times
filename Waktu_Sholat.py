from math import *


def dms_to_dd(d, m, s):
    dd = d + float(m) / 60 + float(s) / 3600
    return dd


def dd_to_dms(dd):
    mnt, sec = divmod(dd * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    if sec > 30:
        mnt = mnt + 1
    mnt = mnt + 2
    if mnt >= 60:
        deg, mnt = deg + 1, mnt % 60
    return int(deg), int(mnt)



lintang = dms_to_dd(-6, -19, 0)
bujur = dms_to_dd(107, 0, 0)
deklinasi = dms_to_dd(4, 26, 0)
eot = dms_to_dd(0, -4, -1)
bd = dms_to_dd(105, 0, 0)  # bujur daerah

mp = 12 - eot  # meridian pass
kwd = (bujur - bd) / 15  # koreksi waktu daerah


def dzuhur():
    awal = dd_to_dms(mp - kwd)
    return awal


def ashar():
    cot_h = tan(radians(abs(lintang - deklinasi))) + 1
    h_ashar = degrees(atan(1 / cot_h))
    cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_ashar)) / cos(radians(lintang)) / cos(
        radians(deklinasi)))
    t = degrees(acos(cos_t))
    awal = dd_to_dms(mp + (t / 15) - kwd)
    return awal


def magrib():
    h_magrib = dms_to_dd(-1, 0, 0)
    cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_magrib)) / cos(radians(lintang)) / cos(
        radians(deklinasi)))
    t = degrees(acos(cos_t))

    awal = dd_to_dms(mp + (t / 15) - kwd)
    return awal


def isya():
    h_isya = dms_to_dd(-18, 0, 0)
    cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_isya)) / cos(radians(lintang)) / cos(
        radians(deklinasi)))
    t = degrees(acos(cos_t))

    awal = dd_to_dms(mp + (t / 15) - kwd)
    return awal


def subuh():
    h_subuh = dms_to_dd(-20, 0, 0)
    cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_subuh)) / cos(radians(lintang)) / cos(
        radians(deklinasi)))
    t = degrees(acos(cos_t))
    awal = dd_to_dms(mp - (t / 15) - kwd)
    return awal


def syuruq():
    h_syuruq = dms_to_dd(1, 0, 0)  # h = +1 derajat
    cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_syuruq)) / cos(radians(lintang)) / cos(
        radians(deklinasi)))
    t = degrees(acos(cos_t))

    awal = dd_to_dms(mp - (t / 15) - kwd)
    return awal


def duha():
    h_duha = dms_to_dd(3, 0, 0)
    cos_t = (tan(-(radians(lintang))) * tan(radians(deklinasi)) + sin(radians(h_duha)) / cos(radians(lintang)) / cos(
        radians(deklinasi)))
    t = degrees(acos(cos_t))
    awal = dd_to_dms(mp - (t / 15) - kwd)

    return awal


for i in range(7):
    if i == 1:
        print(subuh())
    elif i == 2:
        print(syuruq())
    elif i == 3:
        print(duha())
    elif i == 4:
        print(dzuhur())
    elif i == 5:
        print(ashar())
    elif i == 6:
        print(magrib())
    elif i == 7:
        print(isya())
    i += 1
