#
# Conditional build:
%bcond_without	apidocs		# Doxygen documentation
%bcond_without	qt		# Qt (5) based tools
%bcond_without	static_libs	# static libraries
#
Summary:	Collection of Video4Linux utilities
Summary(pl.UTF-8):	Zbiór narzędzi do urządzeń Video4Linux
Name:		v4l-utils
Version:	1.26.1
Release:	1
License:	GPL v2+ (utilities), LGPL v2.1+ (libraries)
Group:		Applications/System
Source0:	https://linuxtv.org/downloads/v4l-utils/%{name}-%{version}.tar.xz
# Source0-md5:	a3565a8ccc427dcce52845c2b8880c28
URL:		https://linuxtv.org/wiki/index.php/V4l-utils
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5.0
BuildRequires:	Qt5Gui-devel >= 5.0
BuildRequires:	Qt5OpenGL-devel >= 5.0
BuildRequires:	Qt5Widgets-devel >= 5.0
BuildRequires:	qt5-build >= 5.0
%endif
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel
BuildRequires:	alsa-lib-devel
# for bpf
BuildRequires:	clang
%{?with_apidocs:BuildRequires:	doxygen >= 1.8.6}
BuildRequires:	elfutils-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	json-c-devel >= 0.15
BuildRequires:	libbpf-devel >= 0.7
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	meson >= 0.54
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	json-c >= 0.15
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
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	Qt5Core >= 5.0
Requires:	Qt5Gui >= 5.0
Requires:	Qt5OpenGL >= 5.0
Requires:	Qt5Widgets >= 5.0
Requires:	hicolor-icon-theme
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
Requires:	udev-devel

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

%package -n libv4l-apidocs
Summary:	API documentation for libv4l libraries
Summary(pl.UTF-8):	Dokumentacja API biblioteki libv4l
Group:		Documentation
BuildArch:	noarch

%description -n libv4l-apidocs
API documentation for libv4l libraries.

%description -n libv4l-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libv4l.

%package -n iconv-v4l
Summary:	Conversion modules for TV broadcasting encodings
Summary(pl.UTF-8):	Moduły konwersji do kodowań używanych w telewizji
Group:		Libraries
Requires:	iconv

%description -n iconv-v4l
Conversion modules for TV broadcasting encodings: ARIB-STD-B24,
EN300-468-TAB00.

%description -n iconv-v4l -l pl.UTF-8
Moduły konwersji do kodowań używanych w telewizji: ARIB-STD-B24,
EN300-468-TAB00.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	%{!?with_apidocs:-Ddoxygen-doc=false} \
	-Dlibdvbv5=enabled \
%if %{without qt}
	-Dqv4l2=disabled \
	-Dqvidcap=disabled \
%endif

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install build/contrib/rds-saa6588/rds-saa6588 $RPM_BUILD_ROOT%{_bindir}
install build/contrib/xc3028-firmware/xc3028-firmware $RPM_BUILD_ROOT%{_bindir}/xc3028-firmware

install -d $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules.d
%{__mv} $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules.d/gconv-modules-v4l.conf

%find_lang libdvbv5
%find_lang v4l-utils

# for find-debuginfo.sh
export EXCLUDE_FROM_STRIP="%{_noautostrip}"

%clean
rm -rf $RPM_BUILD_ROOT

%post qt
%update_desktop_database_post
%update_icon_cache hicolor

%postun qt
%update_desktop_database_postun
%update_icon_cache hicolor

# handle transition from libv4l 0.8.x (.so.0 used to be libraries, not symlinks)
%pretrans -n libv4l
for f in libv4l1 libv4l2 libv4lconvert ; do
	if [ ! -h %{_libdir}/${f}.so.0 ]; then
		rm -f %{_libdir}/${f}.so.0
	fi
done

%post   -n libv4l -p /sbin/ldconfig
%postun -n libv4l -p /sbin/ldconfig

%posttrans -n iconv-v4l
%{_sbindir}/iconvconfig --nostdlib -o %{_libdir}/gconv/gconv-modules.cache %{_libdir}/gconv

%files -f v4l-utils.lang
%defattr(644,root,root,755)
%doc ChangeLog README.md TODO contrib/{cobalt-ctl,parsers,pci_traffic}
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
%attr(755,root,root) %{_bindir}/v4l2-tracer
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
%{_mandir}/man1/v4l2-tracer.1*

%if %{with qt}
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
%endif

%files -n ir-keytable
%defattr(644,root,root,755)
%dir %{_sysconfdir}/rc_keymaps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rc_maps.cfg
%{systemdunitdir}/systemd-udevd.service.d/50-rc_keymap.conf
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
%attr(755,root,root) %{_libdir}/libv4l2tracer.so
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

%if %{with static_libs}
%files -n libv4l-static
%defattr(644,root,root,755)
%{_libdir}/libdvbv5.a
%{_libdir}/libv4l1.a
%{_libdir}/libv4l2.a
%{_libdir}/libv4l2rds.a
%{_libdir}/libv4lconvert.a
%endif

%if %{with apidocs}
%files -n libv4l-apidocs
%defattr(644,root,root,755)
%{_docdir}/v4l-utils
%endif

%files -n iconv-v4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gconv/ARIB-STD-B24.so
%attr(755,root,root) %{_libdir}/gconv/EN300-468-TAB00.so
%{_libdir}/gconv/gconv-modules.d/gconv-modules-v4l.conf
