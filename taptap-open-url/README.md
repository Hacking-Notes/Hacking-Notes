# TapTap – "Open a URL" action

Patch for [KieronQuinn/TapTap](https://github.com/KieronQuinn/TapTap) (commit `e4dce33`, v1.6.2) adding an
**Open a URL** action under the *Launch* category. Assign it to double tap (or triple tap); when adding it you
are asked for the URL, which is then opened with your default browser/handler whenever the gesture fires.
URLs without a scheme (e.g. `google.com`) get `https://` added.

The APK is built by `.github/workflows/build-taptap-open-url.yml` and committed to `apk/`.

Install notes: it's a debug-signed build with the same package name as the official app, so uninstall the
official Tap, Tap first (back up your settings from the app's backup option if you want them).
