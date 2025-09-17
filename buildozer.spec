[app]

# Application info
title = UPI QR
package.name = upiqr
package.domain = org.antick
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Python packages required
requirements = python3,kivy,qrcode,pillow

# Orientation
orientation = portrait
fullscreen = 0

# Icon (optional, you can add your own)
#icon.filename = %(source.dir)s/data/icon.png

# Android settings
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.minapi = 21
android.api = 33
android.ndk = 25b
android.ndk_api = 21
android.sdk = 33
android.build_tools_version = 34.0.0   # ✅ Added line
android.gradle_dependencies =

# Entry point
# android.entrypoint = org.kivy.android.PythonActivity

# Python for Android
p4a.bootstrap = sdl2

# Skip byte compile
# android.no-byte-compile-python = False

[buildozer]
log_level = 2
warn_on_root = 1
