%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname    mate-file-manager-sendto

Summary:        Send files from caja using with mail or IM
Name:           caja-sendto
Version:        1.6.0
Release:        4
URL:            http://www.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz
License:        GPLv2+
Group:          Graphical desktop/Other

BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(mate-desktop-2.0)
BuildRequires:  pkgconfig(mate-doc-utils)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gupnp-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pidgin-devel
# BuildRequires:  gupnp-av-devel
BuildRequires:  gajim

Provides:       %{oname}-sendto-gajim 
Provides:       %{oname}-sendto-email
Provides:       %{oname}-sendto-evolution

%rename %{oname}

Suggests:       %{name}-bluetooth
Requires:       caja

%description
This application provides integration between caja and mail or IM clients.
It adds a Caja context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package pidgin
Summary:    Send files from caja to pidgin
Group:      Graphical desktop/Other
Requires:   pidgin
Requires:   %{name} = %{version}
Provides:   %{name}-sendto-gaim
Provides:   %{oname}-sendto-pidgin = %{version}-%{release}

%description pidgin
This application provides integration between caja and pidgin.  It
adds a Caja context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.


%package upnp
Summary:   Send files from nautilus via UPNP
Group:     Graphical desktop/Other
Requires:  %{name} = %{version}
%rename    %{oname}-upnp

%description upnp
This application provides integration between caja and UPNP.
It adds a Caja context menu component ("Send To...") and allows sending
files to UPNP media servers.

%package devel
Summary:  Development files for %{name}
Group:    Graphical desktop/Other
Provides: %{name}-devel = %{version}-%{release}

%description devel
This package provides development files needed to build plugins upon
%{name}-sendto.

%prep
%setup -q -n %{oname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/caja-sendto
%{_datadir}/MateConf/gsettings/caja-sendto-convert
%{_datadir}/caja-sendto/ui/caja-sendto.ui
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so

%files pidgin
%{_libdir}/caja-sendto/plugins/libnstpidgin.so

%files upnp
%{_libdir}/caja-sendto/plugins/libnstupnp.so

%files devel
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc
%{_datadir}/gtk-doc/html/caja-sendto

