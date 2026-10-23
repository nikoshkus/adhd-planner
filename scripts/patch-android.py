#!/usr/bin/env python3
"""Донастроює згенерований Capacitor-проєкт android/: дозволи, іконка сповіщень, версія, lint.
Запуск: python3 scripts/patch-android.py <номер_збірки>"""
import re, sys, pathlib

run = sys.argv[1] if len(sys.argv) > 1 else "1"
root = pathlib.Path("android/app")

# 1. Дозволи в AndroidManifest.xml
mf = root / "src/main/AndroidManifest.xml"
xml = mf.read_text(encoding="utf-8")
perms = [
    '<uses-permission android:name="android.permission.READ_CALENDAR" />',
    '<uses-permission android:name="android.permission.WRITE_CALENDAR" />',
    '<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />',
    '<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" android:maxSdkVersion="32" />',
    '<uses-permission android:name="android.permission.USE_EXACT_ALARM" />',
    '<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />',
    '<uses-permission android:name="android.permission.VIBRATE" />',
]
add = []
for p in perms:
    name = re.search(r'android:name="([^"]+)"', p).group(1)
    if name not in xml:
        add.append("    " + p)
if add:
    xml = xml.replace("</manifest>", "\n".join(add) + "\n</manifest>")
    mf.write_text(xml, encoding="utf-8")
print("Manifest: додано дозволів:", len(add))

# 2. Іконка сповіщень (біла «галочка»)
d = root / "src/main/res/drawable"
d.mkdir(parents=True, exist_ok=True)
(d / "ic_stat_myday.xml").write_text(
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<vector xmlns:android="http://schemas.android.com/apk/res/android"\n'
    '    android:width="24dp" android:height="24dp"\n'
    '    android:viewportWidth="24" android:viewportHeight="24">\n'
    '    <path android:fillColor="#FFFFFFFF"\n'
    '        android:pathData="M9,16.2L4.8,12l-1.4,1.4L9,19 21,7l-1.4,-1.4z"/>\n'
    '</vector>\n',
    encoding="utf-8",
)

# 3. Версія застосунку й вимкнення lint для release
bg = root / "build.gradle"
g = bg.read_text(encoding="utf-8")
g, n1 = re.subn(r'versionCode(\s*=)?\s*\d+', f'versionCode {run}', g, count=1)
g, n2 = re.subn(r'versionName(\s*=)?\s*"[^"]*"', f'versionName "1.0.{run}"', g, count=1)
if "checkReleaseBuilds" not in g:
    g, n3 = re.subn(r'(\n\s*android\s*\{\s*\n)',
                    r'\1    lint {\n        checkReleaseBuilds = false\n        abortOnError = false\n    }\n',
                    g, count=1)
else:
    n3 = 0
bg.write_text(g, encoding="utf-8")
print(f"build.gradle: versionCode={n1} versionName={n2} lint={n3}")
if not (n1 and n2):
    print("УВАГА: не вдалося замінити версію, перевірте android/app/build.gradle")
