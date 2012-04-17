Summary:	Collection of Video4Linux utilities
Summary(pl.UTF-8):	Zbiór narzędzi do urządzeń Video4Linux
Name:		v4l-utils
Version:	0.8.8
Release:	1
License:	GPL v2+ (utilities), LGPL v2.1+ (libraries)
Group:		Applications/System
Source0:	http://linuxtv.org/downloads/v4l-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	40fdda3f4055ed818012d7a7b5ef5be5
URL:		http://hansdegoede.livejournal.com/
BuildRequires:	QtGui-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A series of utilities for media devices, allowing to handle the
proprietary formats available at most webcams (libv4l), and providing
tools to test V4L devices.

%description -l pl.UTF-8
Zbiór narzędzi do urządzeń multimedialnych, pozwalający obsługiwać
własnościowe formaty dostępne w większości kamer internetowych
(libv4l) oraz testować urządzenia V4L.

%package qt
Summary:	Qt-based V4L2 test Utility
Summary(pl.UTF-8):	Narzędzie testowe V4L2 oparte na Qt
License:	GPL v2+
Group:		X11/Applications

%description qt
Graphical Qt V4L2 control panel.

%description qt -l pl.UTF-8
Graficzny panel kontrolny V4L2 oparty na Qt.

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

%description -n libv4l-devel
Header files for libv4l libraries.

%description -n libv4l-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libv4l.

%prep
%setup -q

%if "%{pld_release}" == "ac"
%{__sed} -i 's/-fvisibility=hidden//' */Makefile
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -Wall" \
	CXXFLAGS="%{rpmcppflags} %{rpmcxxflags} -Wall" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

install utils/rds/rds-saa6588 $RPM_BUILD_ROOT%{_bindir}
install utils/xc3028-firmware/firmware-tool $RPM_BUILD_ROOT%{_bindir}/xc3028-firmware

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n libv4l -p /sbin/ldconfig
%postun -n libv4l -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO contrib
%attr(755,root,root) %{_bindir}/cx18-ctl
%attr(755,root,root) %{_bindir}/decode_tm6000
%attr(755,root,root) %{_bindir}/dvb-fe-tool
%attr(755,root,root) %{_bindir}/dvb-format-convert
%attr(755,root,root) %{_bindir}/dvbv5-scan
%attr(755,root,root) %{_bindir}/dvbv5-zap
%attr(755,root,root) %{_bindir}/ivtv-ctl
%attr(755,root,root) %{_bindir}/rds-saa6588
%attr(755,root,root) %{_bindir}/v4l2-*
%attr(755,root,root) %{_bindir}/xc3028-firmware
%attr(755,root,root) %{_sbindir}/v4l2-dbg

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qv4l2
%{_desktopdir}/qv4l2.desktop
%{_iconsdir}/hicolor/*/apps/qv4l2.*

%files -n ir-keytable
%defattr(644,root,root,755)
%dir %{_sysconfdir}/rc_keymaps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rc_keymaps/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rc_maps.cfg
/lib/udev/rules.d/70-infrared.rules
%attr(755,root,root) %{_bindir}/ir-keytable
%{_mandir}/man1/ir-keytable.1*

%files -n libv4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libv4l1.so.0
%attr(755,root,root) %{_libdir}/libv4l2.so.0
%attr(755,root,root) %{_libdir}/libv4lconvert.so.0
%dir %{_libdir}/libv4l
%attr(755,root,root) %{_libdir}/libv4l/*

%files -n libv4l-devel
%defattr(644,root,root,755)
%doc README.lib*
%attr(755,root,root) %{_libdir}/libv4l1.so
%attr(755,root,root) %{_libdir}/libv4l2.so
%attr(755,root,root) %{_libdir}/libv4lconvert.so
%{_includedir}/libv4l*.h
%{_pkgconfigdir}/libv4l1.pc
%{_pkgconfigdir}/libv4l2.pc
%{_pkgconfigdir}/libv4lconvert.pc
