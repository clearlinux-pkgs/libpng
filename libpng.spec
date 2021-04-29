#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpng
Version  : 1.6.37
Release  : 62
URL      : https://sourceforge.net/projects/libpng/files/libpng16/1.6.37/libpng-1.6.37.tar.xz
Source0  : https://sourceforge.net/projects/libpng/files/libpng16/1.6.37/libpng-1.6.37.tar.xz
Summary  : Loads and saves PNG files
Group    : Development/Tools
License  : GPL-2.0 Libpng MIT zlib-acknowledgement
Requires: libpng-bin = %{version}-%{release}
Requires: libpng-lib = %{version}-%{release}
Requires: libpng-license = %{version}-%{release}
Requires: libpng-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdb
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : zlib-dev32

%description
=================================================
See the note about version numbers near the top of png.h.
See INSTALL for instructions on how to install libpng.

%package bin
Summary: bin components for the libpng package.
Group: Binaries
Requires: libpng-license = %{version}-%{release}

%description bin
bin components for the libpng package.


%package dev
Summary: dev components for the libpng package.
Group: Development
Requires: libpng-lib = %{version}-%{release}
Requires: libpng-bin = %{version}-%{release}
Provides: libpng-devel = %{version}-%{release}
Requires: libpng = %{version}-%{release}

%description dev
dev components for the libpng package.


%package dev32
Summary: dev32 components for the libpng package.
Group: Default
Requires: libpng-lib32 = %{version}-%{release}
Requires: libpng-bin = %{version}-%{release}
Requires: libpng-dev = %{version}-%{release}

%description dev32
dev32 components for the libpng package.


%package lib
Summary: lib components for the libpng package.
Group: Libraries
Requires: libpng-license = %{version}-%{release}

%description lib
lib components for the libpng package.


%package lib32
Summary: lib32 components for the libpng package.
Group: Default
Requires: libpng-license = %{version}-%{release}

%description lib32
lib32 components for the libpng package.


%package license
Summary: license components for the libpng package.
Group: Default

%description license
license components for the libpng package.


%package man
Summary: man components for the libpng package.
Group: Default

%description man
man components for the libpng package.


%prep
%setup -q -n libpng-1.6.37
cd %{_builddir}/libpng-1.6.37
pushd ..
cp -a libpng-1.6.37 build32
popd
pushd ..
cp -a libpng-1.6.37 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604898788
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --enable-intel-sse --enable-hardware-optimizations
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-intel-sse --enable-hardware-optimizations   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export FFLAGS="$FFLAGS -m64 -march=haswell"
export FCFLAGS="$FCFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --enable-intel-sse --enable-hardware-optimizations
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1604898788
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpng
cp %{_builddir}/libpng-1.6.37/LICENSE %{buildroot}/usr/share/package-licenses/libpng/fc3951ba26fe1914759f605696a1d23e3b41766f
cp %{_builddir}/libpng-1.6.37/contrib/gregbook/COPYING %{buildroot}/usr/share/package-licenses/libpng/80b6f4fcbc19d7431482cba012e86f587828c1ba
cp %{_builddir}/libpng-1.6.37/contrib/gregbook/LICENSE %{buildroot}/usr/share/package-licenses/libpng/aa4b9207aaff26bc16c562d6cd766a9eed49af1e
cp %{_builddir}/libpng-1.6.37/contrib/pngminus/LICENSE.txt %{buildroot}/usr/share/package-licenses/libpng/29883b5b9150592328072643614229f6d320bc6e
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/png-fix-itxt
/usr/bin/haswell/pngfix
/usr/bin/libpng-config
/usr/bin/libpng16-config
/usr/bin/png-fix-itxt
/usr/bin/pngfix

%files dev
%defattr(-,root,root,-)
/usr/include/libpng16/png.h
/usr/include/libpng16/pngconf.h
/usr/include/libpng16/pnglibconf.h
/usr/include/png.h
/usr/include/pngconf.h
/usr/include/pnglibconf.h
/usr/lib64/haswell/libpng.so
/usr/lib64/haswell/libpng16.so
/usr/lib64/libpng.so
/usr/lib64/libpng16.so
/usr/lib64/pkgconfig/libpng.pc
/usr/lib64/pkgconfig/libpng16.pc
/usr/share/man/man3/libpng.3
/usr/share/man/man3/libpngpf.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpng.so
/usr/lib32/libpng16.so
/usr/lib32/pkgconfig/32libpng.pc
/usr/lib32/pkgconfig/32libpng16.pc
/usr/lib32/pkgconfig/libpng.pc
/usr/lib32/pkgconfig/libpng16.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libpng16.so.16
/usr/lib64/haswell/libpng16.so.16.37.0
/usr/lib64/libpng16.so.16
/usr/lib64/libpng16.so.16.37.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpng16.so.16
/usr/lib32/libpng16.so.16.37.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpng/29883b5b9150592328072643614229f6d320bc6e
/usr/share/package-licenses/libpng/80b6f4fcbc19d7431482cba012e86f587828c1ba
/usr/share/package-licenses/libpng/aa4b9207aaff26bc16c562d6cd766a9eed49af1e
/usr/share/package-licenses/libpng/fc3951ba26fe1914759f605696a1d23e3b41766f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/png.5
