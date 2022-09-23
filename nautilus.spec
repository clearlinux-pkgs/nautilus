#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nautilus
Version  : 43.0
Release  : 62
URL      : https://download.gnome.org/sources/nautilus/43/nautilus-43.0.tar.xz
Source0  : https://download.gnome.org/sources/nautilus/43/nautilus-43.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: nautilus-bin = %{version}-%{release}
Requires: nautilus-data = %{version}-%{release}
Requires: nautilus-lib = %{version}-%{release}
Requires: nautilus-license = %{version}-%{release}
Requires: nautilus-locales = %{version}-%{release}
Requires: dconf
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk-doc
BuildRequires : libexif-dev
BuildRequires : libportal-dev
BuildRequires : libxslt
BuildRequires : pkgconfig(cloudproviders)
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(gnome-autoar-0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libportal)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(tracker-sparql-3.0)
BuildRequires : pkgconfig(x11)

%description
# nautilus
[![Pipeline status](https://gitlab.gnome.org/GNOME/nautilus/badges/master/pipeline.svg)](https://gitlab.gnome.org/GNOME/nautilus/commits/master)

%package bin
Summary: bin components for the nautilus package.
Group: Binaries
Requires: nautilus-data = %{version}-%{release}
Requires: nautilus-license = %{version}-%{release}

%description bin
bin components for the nautilus package.


%package data
Summary: data components for the nautilus package.
Group: Data

%description data
data components for the nautilus package.


%package dev
Summary: dev components for the nautilus package.
Group: Development
Requires: nautilus-lib = %{version}-%{release}
Requires: nautilus-bin = %{version}-%{release}
Requires: nautilus-data = %{version}-%{release}
Provides: nautilus-devel = %{version}-%{release}
Requires: nautilus = %{version}-%{release}

%description dev
dev components for the nautilus package.


%package lib
Summary: lib components for the nautilus package.
Group: Libraries
Requires: nautilus-data = %{version}-%{release}
Requires: nautilus-license = %{version}-%{release}

%description lib
lib components for the nautilus package.


%package license
Summary: license components for the nautilus package.
Group: Default

%description license
license components for the nautilus package.


%package locales
Summary: locales components for the nautilus package.
Group: Default

%description locales
locales components for the nautilus package.


%prep
%setup -q -n nautilus-43.0
cd %{_builddir}/nautilus-43.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663959962
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocs=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/nautilus
cp %{_builddir}/nautilus-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/nautilus/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/nautilus-%{version}/libnautilus-extension/LICENSE %{buildroot}/usr/share/package-licenses/nautilus/9a647436aa2324c4cb849c6f3d31c392ed50d9bd || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang nautilus

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nautilus
/usr/bin/nautilus-autorun-software

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Nautilus-4.0.typelib
/usr/share/applications/nautilus-autorun-software.desktop
/usr/share/applications/org.gnome.Nautilus.desktop
/usr/share/dbus-1/services/org.freedesktop.FileManager1.service
/usr/share/dbus-1/services/org.gnome.Nautilus.Tracker3.Miner.Extract.service
/usr/share/dbus-1/services/org.gnome.Nautilus.Tracker3.Miner.Files.service
/usr/share/dbus-1/services/org.gnome.Nautilus.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Nautilus.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Nautilus.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Nautilus-symbolic.svg
/usr/share/metainfo/org.gnome.Nautilus.appdata.xml
/usr/share/nautilus/ontology/nautilus.description
/usr/share/nautilus/ontology/nautilus.ontology
/usr/share/tracker3/domain-ontologies/org.gnome.Nautilus.domain.rule

%files dev
%defattr(-,root,root,-)
/usr/include/nautilus/libnautilus-extension/nautilus-column-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-column.h
/usr/include/nautilus/libnautilus-extension/nautilus-extension-enum-types.h
/usr/include/nautilus/libnautilus-extension/nautilus-file-info.h
/usr/include/nautilus/libnautilus-extension/nautilus-info-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu.h
/usr/include/nautilus/libnautilus-extension/nautilus-properties-item.h
/usr/include/nautilus/libnautilus-extension/nautilus-properties-model-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-properties-model.h
/usr/include/nautilus/nautilus-extension.h
/usr/lib64/libnautilus-extension.so
/usr/lib64/pkgconfig/libnautilus-extension-4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnautilus-extension.so.4
/usr/lib64/nautilus/extensions-4/libnautilus-image-properties.so
/usr/lib64/nautilus/extensions-4/libtotem-properties-page.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nautilus/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/nautilus/9a647436aa2324c4cb849c6f3d31c392ed50d9bd

%files locales -f nautilus.lang
%defattr(-,root,root,-)

