#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nautilus
Version  : 3.38.2
Release  : 47
URL      : https://download.gnome.org/sources/nautilus/3.38/nautilus-3.38.2.tar.xz
Source0  : https://download.gnome.org/sources/nautilus/3.38/nautilus-3.38.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: nautilus-bin = %{version}-%{release}
Requires: nautilus-data = %{version}-%{release}
Requires: nautilus-lib = %{version}-%{release}
Requires: nautilus-license = %{version}-%{release}
Requires: nautilus-locales = %{version}-%{release}
Requires: nautilus-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : docbook-xml
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk-doc
BuildRequires : libexif-dev
BuildRequires : libxslt
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(gnome-autoar-0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(tracker-sparql-3.0)
BuildRequires : pkgconfig(x11)

%description
=====
libgd
=====
Introduction
============
libgd is a library used by various GNOME 3 styled applications.
However, it is not a typical library, since it doesn't guarantee
API/ABI stability, nor does it has official releases tarballs. Only
the files actually used by your project will be shipped with its
tarball. Only the necessary dependencies will be checked during
configure time and used at runtime.

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


%package doc
Summary: doc components for the nautilus package.
Group: Documentation
Requires: nautilus-man = %{version}-%{release}

%description doc
doc components for the nautilus package.


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


%package man
Summary: man components for the nautilus package.
Group: Default

%description man
man components for the nautilus package.


%prep
%setup -q -n nautilus-3.38.2
cd %{_builddir}/nautilus-3.38.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605894706
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocs=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/nautilus
cp %{_builddir}/nautilus-3.38.2/LICENSE %{buildroot}/usr/share/package-licenses/nautilus/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/nautilus-3.38.2/libnautilus-extension/LICENSE %{buildroot}/usr/share/package-licenses/nautilus/9a647436aa2324c4cb849c6f3d31c392ed50d9bd
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
/usr/lib64/girepository-1.0/Nautilus-3.0.typelib
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
/usr/include/nautilus/libnautilus-extension/nautilus-extension-types.h
/usr/include/nautilus/libnautilus-extension/nautilus-file-info.h
/usr/include/nautilus/libnautilus-extension/nautilus-info-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-location-widget-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu-item.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu.h
/usr/include/nautilus/libnautilus-extension/nautilus-property-page-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-property-page.h
/usr/include/nautilus/nautilus-extension.h
/usr/lib64/libnautilus-extension.so
/usr/lib64/pkgconfig/libnautilus-extension.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libnautilus-extension/NautilusColumn.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusColumnProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusFileInfo.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusInfoProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusLocationWidgetProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusMenu.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusMenuProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusPropertyPage.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusPropertyPageProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/annotation-glossary.html
/usr/share/gtk-doc/html/libnautilus-extension/ch01.html
/usr/share/gtk-doc/html/libnautilus-extension/ch02.html
/usr/share/gtk-doc/html/libnautilus-extension/home.png
/usr/share/gtk-doc/html/libnautilus-extension/index.html
/usr/share/gtk-doc/html/libnautilus-extension/ix01.html
/usr/share/gtk-doc/html/libnautilus-extension/left-insensitive.png
/usr/share/gtk-doc/html/libnautilus-extension/left.png
/usr/share/gtk-doc/html/libnautilus-extension/libnautilus-extension-Extension-entry-points.html
/usr/share/gtk-doc/html/libnautilus-extension/libnautilus-extension.devhelp2
/usr/share/gtk-doc/html/libnautilus-extension/pt01.html
/usr/share/gtk-doc/html/libnautilus-extension/right-insensitive.png
/usr/share/gtk-doc/html/libnautilus-extension/right.png
/usr/share/gtk-doc/html/libnautilus-extension/style.css
/usr/share/gtk-doc/html/libnautilus-extension/up-insensitive.png
/usr/share/gtk-doc/html/libnautilus-extension/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnautilus-extension.so.1
/usr/lib64/libnautilus-extension.so.1.5.0
/usr/lib64/nautilus/extensions-3.0/libnautilus-image-properties.so
/usr/lib64/nautilus/extensions-3.0/libnautilus-sendto.so
/usr/lib64/nautilus/extensions-3.0/libtotem-properties-page.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nautilus/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/nautilus/9a647436aa2324c4cb849c6f3d31c392ed50d9bd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nautilus-autorun-software.1
/usr/share/man/man1/nautilus.1

%files locales -f nautilus.lang
%defattr(-,root,root,-)

