Summary:	Mingw32 Binary Utility Development Utilities - DirectX 7.0 API
Summary(pl):	Zestaw narz�dzi mingw32 - API DirectX 7.0
Name:		crossmingw32-dx70
Version:	7.0
Release:	1
Epoch:		1
License:	Free (libs), (c) Microsoft Corporation (headers)
Group:		Development/Libraries
# headers are Copyright (C) 19xx Microsoft Corporation - what about license???
# (even if distributable, are they "Free"?!)
Source0:	http://alleg.sourceforge.net/files/dx70_mgw.zip
URL:		http://www.mingw.org/
ExclusiveArch:	%{ix86}
Provides:	crossmingw32-w32api-dx
Obsoletes:	crossmingw32-w32api-dx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		arch		%{_prefix}/%{target}

%define		__unzip		unzip -q -o
# strip fails on static COFF files
%define		no_install_post_strip 1

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains DirectX 7.0 API includes and libraries.

%description -l pl
crossmingw32 jest kompletnym systemem do kroskompilacji, pozwalaj�cym
budowa� aplikacje MS Windows pod Linuksem u�ywaj�c bibliotek mingw32.
System sk�ada si� z binutils, gcc z g++ i objc, libstdc++ - wszystkie
generuj�ce kod dla platformy i386-mingw32, oraz z bibliotek w formacie
COFF.

Ten pakiet zawiera pliki nag��wkowe i biblioteki API DirectX 7.0.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/{include,lib}

mv -f lib/src/*.htm .
rm -rf lib/src

cp -fa include/* $RPM_BUILD_ROOT%{arch}/include
cp -fa lib/* $RPM_BUILD_ROOT%{arch}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc directx.htm
%{arch}/include/*
%{arch}/lib/*