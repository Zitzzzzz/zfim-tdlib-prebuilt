# zfim-tdlib-prebuilt

Clean-room prebuilt **TDLib C JSON API (`libtdjson` / `tdjson.dll` / `tdjson.xcframework`)** binaries built exclusively from official upstream sources for [zFim](https://github.com/magicxlll/zFim):

- **TDLib (`tdlib/td`)**: Boost Software License 1.0 (`BSL-1.0`) — pinned commit `03220f6b3043c6fd7785fbf0901d63f19ad19974` (v1.8.70)
- **OpenSSL**: `openssl-3.4.1` (`Apache-2.0`), statically linked into `tdjson`

## Shipped Release Artifacts

| Target | Artifact Archive | Notes |
|---|---|---|
| Android `armeabi-v7a` | `tdjson-android-armeabi-v7a.tar.gz` | NDK API 23 (`MiTV4` Android 6.0.1 compatible), `c++_static`, `-flto=thin -Oz`, stripped |
| Android `arm64-v8a` | `tdjson-android-arm64-v8a.tar.gz` | NDK API 23, `-Wl,-z,max-page-size=16384` (16 KB ELF `PT_LOAD` aligned for Android 15), `c++_static`, `-flto=thin -Oz`, stripped |
| Windows `x64` | `tdjson-windows-x64.zip` | `tdjson.dll` with static OpenSSL 3.4.1 & zlib (`x64-windows-static-md`) |
| macOS `arm64` / universal | `tdjson-macos.tar.gz` | `libtdjson.dylib` (`@rpath/libtdjson.dylib`), static OpenSSL 3.4.1, stripped |
| iOS | `tdjson-ios-xcframework.zip` | `libtdjson.xcframework` (`iphoneos` arm64 + `iphonesimulator` arm64) |
| Checksums | `manifest.json` | JSON index with version metadata and SHA-256 checksums for every artifact |

All artifacts are compiled cleanly via GitHub Actions in `.github/workflows/build-tdlib.yml`.
