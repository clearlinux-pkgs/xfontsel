#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : xfontsel
Version  : 1.1.0
Release  : 4
URL      : https://www.x.org/releases/individual/app/xfontsel-1.1.0.tar.gz
Source0  : https://www.x.org/releases/individual/app/xfontsel-1.1.0.tar.gz
Source1  : https://www.x.org/releases/individual/app/xfontsel-1.1.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT X11
Requires: xfontsel-bin = %{version}-%{release}
Requires: xfontsel-data = %{version}-%{release}
Requires: xfontsel-license = %{version}-%{release}
Requires: xfontsel-man = %{version}-%{release}
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xaw7)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xt)

%description
xfontsel application provides a simple way to display the X11 core
protocol fonts known to your X server, examine samples of each, and
retrieve the X Logical Font Description ("XLFD") full name for a font.

%package bin
Summary: bin components for the xfontsel package.
Group: Binaries
Requires: xfontsel-data = %{version}-%{release}
Requires: xfontsel-license = %{version}-%{release}

%description bin
bin components for the xfontsel package.


%package data
Summary: data components for the xfontsel package.
Group: Data

%description data
data components for the xfontsel package.


%package license
Summary: license components for the xfontsel package.
Group: Default

%description license
license components for the xfontsel package.


%package man
Summary: man components for the xfontsel package.
Group: Default

%description man
man components for the xfontsel package.


%prep
%setup -q -n xfontsel-1.1.0
cd %{_builddir}/xfontsel-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657508386
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1657508386
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfontsel
cp %{_builddir}/xfontsel-1.1.0/COPYING %{buildroot}/usr/share/package-licenses/xfontsel/2224b59891a816e6b608547bebe9b6ca225abd64
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfontsel

%files data
%defattr(-,root,root,-)
/usr/share/X11/app-defaults/XFontSel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfontsel/2224b59891a816e6b608547bebe9b6ca225abd64

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfontsel.1
