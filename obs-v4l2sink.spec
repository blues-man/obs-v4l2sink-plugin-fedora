Name:           obs-v4l2sink
Version:        0.1.0 
Release:        1%{?dist}
Summary:        OBS Studio output plugin for Video4Linux2 device 

License:        GPLv2 
URL:            https://github.com/CatxFish/obs-v4l2sink/
Source0:        https://github.com/blues-man/obs-v4l2sink-plugin-fedora/raw/master/obs-v4l2sink-0.1.0.tar.gz

Requires:       obs-studio
Requires:       v4l2loopback  
BuildArch:      x86_64

%description
OBS Studio output plugin for Video4Linux2 device

%global debug_package %{nil}

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/usr/lib64/obs-plugins/

install -m 0644 v4l2sink.so %{buildroot}/usr/lib64/obs-plugins/v4l2sink.so

#%make_install


%files
%license LICENSE
/usr/lib64/obs-plugins/v4l2sink.so


%changelog
* Sun Sep 27 2020 Natale Vinto <nvinto@redhat.com>
- 
