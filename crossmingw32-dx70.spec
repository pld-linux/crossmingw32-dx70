Summary:	MinGW32 binary utility development utilities - DirectX 7.0 API
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne dla MinGW32 - API DirectX 7.0
Name:		crossmingw32-dx70
Version:	7.0
Release:	4
Epoch:		1
License:	Free (libs), (c) Microsoft Corporation (headers)
Group:		Development/Libraries
# headers are Copyright (C) 19xx Microsoft Corporation - what about license???
# (even if distributable, are they "Free"?!)
Source0:	http://alleg.sourceforge.net/files/dx70_mgw.zip
# Source0-md5:	8a57b4c81a296d75f75d7a9810ae59a0
Source1:	http://www.libsdl.org/extras/win32/common/directx-devel.tar.gz
# Source1-md5:	389a36e4d209c0a76bea7d7cb6315315
BuildRequires:	unzip
Requires:	crossmingw32-runtime
Provides:	crossmingw32-dx = 7.0
Obsoletes:	crossmingw32-dx
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
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains DirectX 7.0 API includes and libraries.

%description -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera pliki nagłówkowe i biblioteki API DirectX 7.0.

%prep
%setup -q -c
mkdir extras
cd extras
tar zxf %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/{include,lib}

mv -f lib/src/*.htm .
rm -rf lib/src
rm -rf include/src

cp -fa include/* $RPM_BUILD_ROOT%{arch}/include
cp -fa lib/* $RPM_BUILD_ROOT%{arch}/lib

cp extras/include/directx.h $RPM_BUILD_ROOT%{arch}/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc directx.htm
%{arch}/include/d3d*.h
%{arch}/include/d3d*.inl
%{arch}/include/ddraw.h
%{arch}/include/dinput*.h
%{arch}/include/dls1.h
%{arch}/include/dls2.h
%{arch}/include/dmdls.h
%{arch}/include/dmerror.h
%{arch}/include/dmksctrl.h
%{arch}/include/dmus*.h
%{arch}/include/dplay.h
%{arch}/include/dplobby.h
%{arch}/include/directx.h
%{arch}/include/dsetup.h
%{arch}/include/dsound.h
%{arch}/include/dvp.h
%{arch}/include/dxfile.h
%{arch}/include/dxsdk.inc
%{arch}/include/multimon.h
%{arch}/include/rmxfguid.h
%{arch}/include/rmxftmpl.h
%{arch}/include/rmxftmpl.x
%{arch}/lib/libd3dim.a
%{arch}/lib/libd3drm.a
%{arch}/lib/libd3dxof.a
%{arch}/lib/libddraw.a
%{arch}/lib/libdinput.a
%{arch}/lib/libdplayx.a
%{arch}/lib/libdsetup.a
%{arch}/lib/libdsound.a
%{arch}/lib/libdxguid.a
