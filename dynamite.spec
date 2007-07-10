Summary:	Library to extract data compressed with PKWARE Data Compression Library
Summary(pl.UTF-8):	Biblioteka do dekompresji danych spakowanych biblioteką kompresji PKWARE
Name:		dynamite
Version:	0.1
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	5e99d9172f60b8084cc6f6ba1a8c8261
Patch0:		%{name}-am.patch
URL:		http://www.synce.org/index.php/Dynamite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to extract data compressed with PKWARE Data Compression
Library.

%description -l pl.UTF-8
Biblioteka do dekompresji danych spakowanych biblioteką kompresji
danych PKWARE Data Compression Library.

%package devel
Summary:	Header files for dynamite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dynamite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for dynamite library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dynamite.

%package static
Summary:	Static dynamite library
Summary(pl.UTF-8):	Statyczna biblioteka dynamite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static dynamite library.

%description static -l pl.UTF-8
Statyczna biblioteka dynamite.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/dynamite
%attr(755,root,root) %{_libdir}/libdynamite.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdynamite.so
%{_libdir}/libdynamite.la
%{_includedir}/libdynamite.h
%{_aclocaldir}/dynamite.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libdynamite.a
