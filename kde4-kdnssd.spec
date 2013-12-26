# TODO
# - fix kopete-tool-{avdeviceconfig,smpppdcs} summaries/descriptions (copy-pastos!)
# - BR phonon-devel
# - FILES update
#
# Conditional build:
#
%define		_state		stable
%define		orgname		kdnssd
%define		qtver		4.8.3

Summary:	DNS-SD Services Watcher
Summary(pl.UTF-8):	Nadzorowanie usług DNS-SD
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	Artistic
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	bef2a384bdf682f255eed879ac51fb93
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdenetwork-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DNS-SD Services Watcher.

%description -l pl.UTF-8
Nadzorowanie usług DNS-SD.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DMOZPLUGIN_INSTALL_DIR=%{_browserpluginsdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kded_dnssdwatcher.so
%attr(755,root,root) %{_libdir}/kde4/kio_zeroconf.so
%{_datadir}/apps/remoteview/zeroconf.desktop
%{_datadir}/kde4/services/kded/dnssdwatcher.desktop
%{_datadir}/kde4/services/zeroconf.protocol
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
