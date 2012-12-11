%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary: 	Widgets for audio applications
Name: 		phat
Version: 	0.3.1
Release: 	4
License: 	GPL+
Group: 		System/Libraries
# Upstream's dead, RIP...no source location
Source0:	%{name}-%{version}.tar.bz2
Patch0:		phat-0.3.1-configure.patch
Requires:	docbook-dtd30-sgml
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
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std



%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}



%changelog
* Mon Feb 22 2010 Funda Wang <fwang@mandriva.org> 0.3.1-4mdv2010.1
+ Revision: 509759
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Aug 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.1-3mdv2009.0
+ Revision: 277215
- protect major in file list
- s,$RPM_BUILD_ROOT,%%{buildroot}
- add configure.patch:
  	+ allow external CFLAGS
  	+ add -lX11 to libs to fix build (underlinking)
  	+ don't build docs (breaks build, can't be bothered fixing)
- new license policy
- new devel policy
- drop unnecessary defines

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - import phat

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.1-2mdk
- Fix BuildRequires

* Sun Jul 24 2005 Austin Acton <austin@mandriva.org> 0.3.1-1mdk
- 0.3.1
- source URL

* Fri Jul 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.3-2mdk
- fix requires

* Mon Oct 4 2004 Austin Acton <austin@mandrake.org> 0.2.3-1mdk
- initial build
