%define name 	phat
%define version 0.3.1
%define release %mkrel 2

%define major 	0
%define libname %mklibname %name %major

Summary: 	Widgets for audio applications
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://www.gazuga.net/phat.php
License: 	GPL
Group: 		System/Libraries
Source: 	http://www.gazuga.net/phatfiles/%{name}-%{version}.tar.bz2
Requires:	docbook-dtd30-sgml
BuildRequires:	gtk2-devel gtk-doc
BuildRequires:  libgnomecanvas2-devel 

%description
PHAT is a collection of GTK+ widgets geared toward pro-audio apps. The goal
is to eliminate duplication of effort and provide some standardization
(well, at least for GTK+ apps).

%package -n %{libname}
Summary: Widgets for audio applications
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
PHAT is a collection of GTK+ widgets geared toward pro-audio apps. The goal
is to eliminate duplication of effort and provide some standardization
(well, at least for GTK+ apps).

%package -n %{libname}-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %{libname} = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use libraries from %name.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_bindir/*
%doc %_datadir/gtk-doc/html/%name
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%_libdir/pkgconfig/*.pc
%_includedir/%name

