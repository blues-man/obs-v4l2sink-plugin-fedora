# obs-v4l2sink-plugin-fedora
Fedora 31 and 32 RPM package for [OBS Studio](https://obsproject.com/) [v4l2sink plugin](https://github.com/CatxFish/obs-v4l2sink/)

The RPM has been created extracting the library from the available [Ubuntu package](https://github.com/CatxFish/obs-v4l2sink/releases/download/0.1.0/obs-v4l2sink.deb) from repo's releases.

This will place the plugin inside `/usr/lib64/obs-plugins/v4l2sink.so` that can be used after the virtual camera device has been created.

# Install

## From Fedora Copr

Install Fedora Copr repo to resolve all dependencies. It will install `obs-studio` package from [RPM Fusion](https://rpmfusion.org/) and `v4l2loopback` package from [copr/sentry](https://copr.fedorainfracloud.org/coprs/sentry/v4l2loopback/) if those are not available
```
$ sudo dnf copr enable bluesman/obs-v4l2sink
$ sudo dnf install --nogpgcheck obs-v4l2sink
```

The GPG check fails on rpmfusion and sentry packages, skipping for the moment will let those install.

## From RPM (Fedora 32)

### Install RPM Fusion

Follow doc for your Fedora version: https://rpmfusion.org/Configuration

Then install OBS:
```
$ sudo dnf install obs-studio
```

### Install v4l2loopback

Install from Copr

```
$ sudo dnf copr enable sentry/v4l2loopback
$ sudo dnf install v4l2loopback
```

### Install obs-v4l2sink

```
$ rpm -ivh obs-v4l2sink-0.1.0-1.fc32.x86_64.rpm
```

# Usage

Start module:

```
$ sudo modprobe v4l2loopback video_nr=42 card_label="obs-cam" exclusive_caps=1
```

* Start OBS, Tools->v4l2sink

* Select device `/dev/video42`

* Press Start

