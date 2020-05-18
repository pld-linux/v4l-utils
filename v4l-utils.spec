#
# Conditional build:
%bcond_without	udev	# using libudev to detect device name
#
Summary:	Collection of Video4Linux utilities
Summary(pl.UTF-8):	Zbiór narzędzi do urządzeń Video4Linux
Name:		v4l-utils
Version:	1.18.1
Release:	1
License:	GPL v2+ (utilities), LGPL v2.1+ (libraries)
Group:		Applications/System
Source0:	https://linuxtv.org/downloads/v4l-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	ff2dd75970683be9a301ed949b3372b3
Patch0:		%{name}-link.patch
Patch1:		%{name}-glibc.patch
URL:		https://linuxtv.org/wiki/index.php/V4l-utils
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	Qt5Core-devel >= 5.0
BuildRequires:	Qt5Gui-devel >= 5.0
BuildRequires:	Qt5OpenGL-devel >= 5.0
BuildRequires:	Qt5Widgets-devel >= 5.0
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
# for bpf
BuildRequires:	clang
BuildRequires:	elfutils-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5.0
%{?with_udev:BuildRequires:	udev-devel}
BuildRequires:	xorg-lib-libX11-devel
Requires:	libv4l = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# ELF files with some special architecture inside
%define		_noautostrip	/lib/udev/rc_keymaps/.*

%description
A series of utilities for media devices, allowing to handle the
proprietary formats available at most webcams (libv4l), and providing
tools to test V4L devices.

%description -l pl.UTF-8
Zbiór narzędzi do urządzeń multimedialnych, pozwalający obsługiwać
własnościowe formaty dostępne w większości kamer internetowych
(libv4l) oraz testować urządzenia V4L.

%package qt
Summary:	Qt-based V4L2 capture and test utilities
Summary(pl.UTF-8):	Oparte na Qt narzędzia V4L2 do przechwytywania obrazu i testowania
License:	GPL v2+
Group:		X11/Applications
Requires:	Qt5Core >= 5.0
Requires:	Qt5Gui >= 5.0
Requires:	Qt5OpenGL >= 5.0
Requires:	Qt5Widgets >= 5.0
Requires:	libv4l = %{version}-%{release}

%description qt
Graphical Qt V4L2 control panel and capture utility.

%description qt -l pl.UTF-8
Graficzny panel kontrolny V4L2 i narzędzie do przechwytywania obrazu
oparte na Qt.

%package -n ir-keytable
Summary:	Alter keymaps of Remote Controller devices
Summary(pl.UTF-8):	Zmiana map klawiszy urządzeń do zdalnego sterowania
License:	GPL v2+
Group:		Applications/Console

%description -n ir-keytable
Dump, Load or Modify IR receiver input tables. This package allows one
to change the keymap of controller receivers. Those receivers are
found as infrared receivers on DVB sticks or on framegrabber cards.
Via ir-keytable the mapping from a scancode to the generated event can
be customized and made persistent.

%description -n ir-keytable -l pl.UTF-8
ir-keytable to narzędzie pozwalające na zrzucanie, wczytywanie i
modyfikowanie tablic wejściowych odbiorników podczerwieni (IR). Ten
pakiet pozwala na zmianę tablic klawiszy odbiorników pilotów.
Odbiorniki podczerwieni występują na interfejsach DVB lub kartach
framegrabberów. Dzięki użyciu ir-keytable można zmienić i zachować
odwzorowania między skankodami a generowanymi zdarzeniami.

%package -n libv4l
Summary:	Abstraction layer on top of video4linux2 devices
Summary(pl.UTF-8):	Warstwa abstrakcji dla urządzeń video4linux2
License:	LGPL v2.1+
Group:		Libraries

%description -n libv4l
Collection of libraries which adds a thin abstraction layer on top of
video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices
without having to write seperate code for different devices in the
same class.

%description -n libv4l -l pl.UTF-8
libv4l to zestaw bibliotek dodający niewielką warstwę abstrakcji dla
urządzeń video4linux2. Celem tej warstwy jest ułatwienie autorom
aplikacji obsługi szerokiej gamy urządzeń bez pisania osobnego kodu
dla różnych urządzeń tej samej klasy.

%package -n libv4l-devel
Summary:	Header files for libv4l libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libv4l
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libv4l = %{version}-%{release}
%{?with_udev:Requires:	udev-devel}

%description -n libv4l-devel
Header files for libv4l libraries.

%description -n libv4l-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libv4l.

%package -n libv4l-static
Summary:	Static libv4l libraries
Summary(pl.UTF-8):	Statyczne biblioteki libv4l
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libv4l-devel = %{version}-%{release}

%description -n libv4l-static
Static libv4l libraries.

%description -n libv4l-static -l pl.UTF-8
Statyczne biblioteki libv4l.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-libdvbv5 \
	%{?with_udev:--with-libudev}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/rds-saa6588/rds-saa6588 $RPM_BUILD_ROOT%{_bindir}
install contrib/xc3028-firmware/firmware-tool $RPM_BUILD_ROOT%{_bindir}/xc3028-firmware

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libv4l/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libv4l/plugins/*.la

%find_lang libdvbv5
%find_lang v4l-utils

# for find-debuginfo.sh
export EXCLUDE_FROM_STRIP="%{_noautostrip}"

%clean
rm -rf $RPM_BUILD_ROOT

# handle transition from libv4l 0.8.x (.so.0 used to be libraries, not symlinks)
%pretrans -n libv4l
for f in libv4l1 libv4l2 libv4lconvert ; do
	if [ ! -h %{_libdir}/${f}.so.0 ]; then
		rm -f %{_libdir}/${f}.so.0
	fi
done

%post   -n libv4l -p /sbin/ldconfig
%postun -n libv4l -p /sbin/ldconfig

%files -f v4l-utils.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO contrib
%attr(755,root,root) %{_bindir}/cec-compliance
%attr(755,root,root) %{_bindir}/cec-ctl
%attr(755,root,root) %{_bindir}/cec-follower
%attr(755,root,root) %{_bindir}/cx18-ctl
%attr(755,root,root) %{_bindir}/decode_tm6000
%attr(755,root,root) %{_bindir}/dvb-fe-tool
%attr(755,root,root) %{_bindir}/dvb-format-convert
%attr(755,root,root) %{_bindir}/dvbv5-daemon
%attr(755,root,root) %{_bindir}/dvbv5-scan
%attr(755,root,root) %{_bindir}/dvbv5-zap
%attr(755,root,root) %{_bindir}/ir-ctl
%attr(755,root,root) %{_bindir}/ivtv-ctl
%attr(755,root,root) %{_bindir}/media-ctl
%attr(755,root,root) %{_bindir}/rds-ctl
%attr(755,root,root) %{_bindir}/rds-saa6588
%attr(755,root,root) %{_bindir}/v4l2-compliance
%attr(755,root,root) %{_bindir}/v4l2-ctl
%attr(755,root,root) %{_bindir}/v4l2-sysfs-path
%attr(755,root,root) %{_bindir}/xc3028-firmware
%attr(755,root,root) %{_sbindir}/v4l2-dbg
%{_mandir}/man1/cec-compliance.1*
%{_mandir}/man1/cec-ctl.1*
%{_mandir}/man1/cec-follower.1*
%{_mandir}/man1/dvb-fe-tool.1*
%{_mandir}/man1/dvb-format-convert.1*
%{_mandir}/man1/dvbv5-scan.1*
%{_mandir}/man1/dvbv5-zap.1*
%{_mandir}/man1/ir-ctl.1*
%{_mandir}/man1/v4l2-compliance.1*
%{_mandir}/man1/v4l2-ctl.1*

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qv4l2
%attr(755,root,root) %{_bindir}/qvidcap
%{_desktopdir}/qv4l2.desktop
%{_desktopdir}/qvidcap.desktop
%{_iconsdir}/hicolor/*/apps/qv4l2.*
%{_iconsdir}/hicolor/*/apps/qvidcap.*
%{_mandir}/man1/qv4l2.1*
%{_mandir}/man1/qvidcap.1*

%files -n ir-keytable
%defattr(644,root,root,755)
%dir %{_sysconfdir}/rc_keymaps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rc_maps.cfg
/lib/udev/rc_keymaps
/lib/udev/rules.d/70-infrared.rules
%attr(755,root,root) %{_bindir}/ir-keytable
%{_mandir}/man1/ir-keytable.1*
%{_mandir}/man5/rc_keymap.5*

%files -n libv4l -f libdvbv5.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvbv5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdvbv5.so.0
%attr(755,root,root) %{_libdir}/libv4l1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libv4l1.so.0
%attr(755,root,root) %{_libdir}/libv4l2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libv4l2.so.0
%attr(755,root,root) %{_libdir}/libv4l2rds.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libv4l2rds.so.0
%attr(755,root,root) %{_libdir}/libv4lconvert.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libv4lconvert.so.0
%attr(755,root,root) %{_libdir}/v4l1compat.so
%attr(755,root,root) %{_libdir}/v4l2convert.so
%dir %{_libdir}/libv4l
%attr(755,root,root) %{_libdir}/libv4l/ov511-decomp
%attr(755,root,root) %{_libdir}/libv4l/ov518-decomp
%attr(755,root,root) %{_libdir}/libv4l/v4l1compat.so
%attr(755,root,root) %{_libdir}/libv4l/v4l2convert.so
%dir %{_libdir}/libv4l/plugins
%attr(755,root,root) %{_libdir}/libv4l/plugins/libv4l-mplane.so

%files -n libv4l-devel
%defattr(644,root,root,755)
%doc README.lib*
%attr(755,root,root) %{_libdir}/libdvbv5.so
%attr(755,root,root) %{_libdir}/libv4l1.so
%attr(755,root,root) %{_libdir}/libv4l2.so
%attr(755,root,root) %{_libdir}/libv4l2rds.so
%attr(755,root,root) %{_libdir}/libv4lconvert.so
%{_includedir}/libv4l*.h
%{_includedir}/libdvbv5
%{_pkgconfigdir}/libdvbv5.pc
%{_pkgconfigdir}/libv4l1.pc
%{_pkgconfigdir}/libv4l2.pc
%{_pkgconfigdir}/libv4l2rds.pc
%{_pkgconfigdir}/libv4lconvert.pc

%files -n libv4l-static
%defattr(644,root,root,755)
%{_libdir}/libdvbv5.a
%{_libdir}/libv4l1.a
%{_libdir}/libv4l2.a
%{_libdir}/libv4l2rds.a
%{_libdir}/libv4lconvert.a
