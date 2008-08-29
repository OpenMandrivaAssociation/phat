%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary: 	Widgets for audio applications
Name: 		phat
Version: 	0.3.1
Release: 	%{mkrel 3}
License: 	GPL+
Group: 		System/Libraries
# Upstream's dead, RIP...no source location
Source0:	%{name}-%{version}.tar.bz2
Patch0:		phat-0.3.1-configure.patch
Requires:	docbook-dtd30-sgml
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk2-devel
BuildRequires:	gtk-doc
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

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname phat 0 -d}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use libraries from %{name}.

%prep
%setup -q
%patch0 -p1

%build
autoreconf
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

