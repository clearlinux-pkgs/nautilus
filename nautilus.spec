#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nautilus
Version  : 3.26.2
Release  : 15
URL      : https://download.gnome.org/sources/nautilus/3.26/nautilus-3.26.2.tar.xz
Source0  : https://download.gnome.org/sources/nautilus/3.26/nautilus-3.26.2.tar.xz
Summary  : A library to create Nautilus view extensions
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: nautilus-bin
Requires: nautilus-data
Requires: nautilus-lib
Requires: nautilus-doc
Requires: nautilus-locales
BuildRequires : desktop-file-utils
BuildRequires : docbook-xml
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : libexif-dev
BuildRequires : libxslt
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(gnome-autoar-0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(tracker-sparql-2.0)
BuildRequires : pkgconfig(x11)
BuildRequires : python3
Patch1: 0001-autostart-desktop-file-goes-to-usr-share-xdg-and-not.patch

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
Requires: nautilus-data

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
Requires: nautilus-lib
Requires: nautilus-bin
Requires: nautilus-data
Provides: nautilus-devel

%description dev
dev components for the nautilus package.


%package doc
Summary: doc components for the nautilus package.
Group: Documentation

%description doc
doc components for the nautilus package.


%package lib
Summary: lib components for the nautilus package.
Group: Libraries
Requires: nautilus-data

%description lib
lib components for the nautilus package.


%package locales
Summary: locales components for the nautilus package.
Group: Default

%description locales
locales components for the nautilus package.


%prep
%setup -q -n nautilus-3.26.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518035031
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -D enable-packagekit=false -D enable-selinux=false -D with-introspection=true -D enable-packagekit=false -D enable-gtk-doc=true builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang nautilus

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nautilus
/usr/bin/nautilus-autorun-software
/usr/bin/nautilus-desktop

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Nautilus-3.0.typelib
/usr/share/appdata/org.gnome.Nautilus.appdata.xml
/usr/share/applications/nautilus-autorun-software.desktop
/usr/share/applications/nautilus-classic.desktop
/usr/share/applications/org.gnome.Nautilus.desktop
/usr/share/dbus-1/services/org.freedesktop.FileManager1.service
/usr/share/dbus-1/services/org.gnome.Nautilus.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
/usr/share/gnome-shell/search-providers/nautilus-search-provider.ini
/usr/share/icons/hicolor/16x16/apps/org.gnome.Nautilus.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.Nautilus.png
/usr/share/icons/hicolor/24x24/apps/org.gnome.Nautilus.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.Nautilus.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.Nautilus.png
/usr/share/icons/hicolor/512x512/apps/org.gnome.Nautilus.png
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Nautilus-symbolic.svg
/usr/share/xdg/autostart/nautilus-autostart.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/nautilus/libnautilus-extension/nautilus-column-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-column.h
/usr/include/nautilus/libnautilus-extension/nautilus-extension-types.h
/usr/include/nautilus/libnautilus-extension/nautilus-file-info.h
/usr/include/nautilus/libnautilus-extension/nautilus-info-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-location-widget-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu-item.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-menu.h
/usr/include/nautilus/libnautilus-extension/nautilus-property-page-provider.h
/usr/include/nautilus/libnautilus-extension/nautilus-property-page.h
/usr/lib64/libnautilus-extension.so
/usr/lib64/pkgconfig/libnautilus-extension.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/libnautilus-extension/NautilusColumn.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusColumnProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusFileInfo.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusInfoProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusLocationWidgetProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusMenu.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusMenuItem.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusMenuProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusPropertyPage.html
/usr/share/gtk-doc/html/libnautilus-extension/NautilusPropertyPageProvider.html
/usr/share/gtk-doc/html/libnautilus-extension/ch01.html
/usr/share/gtk-doc/html/libnautilus-extension/home.png
/usr/share/gtk-doc/html/libnautilus-extension/index.html
/usr/share/gtk-doc/html/libnautilus-extension/ix01.html
/usr/share/gtk-doc/html/libnautilus-extension/left-insensitive.png
/usr/share/gtk-doc/html/libnautilus-extension/left.png
/usr/share/gtk-doc/html/libnautilus-extension/libnautilus-extension-NautilusModule.html
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
/usr/lib64/libnautilus-extension.so.1.4.0
/usr/lib64/nautilus/extensions-3.0/libnautilus-sendto.so

%files locales -f nautilus.lang
%defattr(-,root,root,-)

