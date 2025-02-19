#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: e36a856
#
Name     : libpng
Version  : 1.6.47
Release  : 87
URL      : https://sourceforge.net/projects/libpng/files/libpng16/1.6.47/libpng-1.6.47.tar.gz
Source0  : https://sourceforge.net/projects/libpng/files/libpng16/1.6.47/libpng-1.6.47.tar.gz
Summary  : Loads and saves PNG files
Group    : Development/Tools
License  : GPL-2.0 MIT zlib-acknowledgement
Requires: libpng-bin = %{version}-%{release}
Requires: libpng-lib = %{version}-%{release}
Requires: libpng-license = %{version}-%{release}
Requires: libpng-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdb
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
================================
See the note about version numbers near the top of `png.h`.
See `INSTALL` for instructions on how to install libpng.

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
%setup -q -n libpng-1.6.47
cd %{_builddir}/libpng-1.6.47
pushd ..
cp -a libpng-1.6.47 build32
popd
pushd ..
cp -a libpng-1.6.47 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739988782
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-intel-sse --enable-hardware-optimizations
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-intel-sse --enable-hardware-optimizations   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
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
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739988782
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpng
cp %{_builddir}/libpng-%{version}/ci/LICENSE_MIT.txt %{buildroot}/usr/share/package-licenses/libpng/218fc8c15534e8840cbff5801582c450c97869ab || :
cp %{_builddir}/libpng-%{version}/contrib/gregbook/COPYING %{buildroot}/usr/share/package-licenses/libpng/80b6f4fcbc19d7431482cba012e86f587828c1ba || :
cp %{_builddir}/libpng-%{version}/contrib/gregbook/LICENSE %{buildroot}/usr/share/package-licenses/libpng/aa4b9207aaff26bc16c562d6cd766a9eed49af1e || :
cp %{_builddir}/libpng-%{version}/contrib/pngexif/LICENSE_MIT.txt %{buildroot}/usr/share/package-licenses/libpng/218fc8c15534e8840cbff5801582c450c97869ab || :
cp %{_builddir}/libpng-%{version}/contrib/pngminus/LICENSE.txt %{buildroot}/usr/share/package-licenses/libpng/91ab0c4ef71808e897ae26ca560ddf987a072b7b || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/libpng.la
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/png-fix-itxt
/V3/usr/bin/pngfix
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
/usr/lib64/libpng.so
/usr/lib64/libpng16.so
/usr/lib64/pkgconfig/libpng.pc
/usr/lib64/pkgconfig/libpng16.pc
/usr/share/man/man3/libpng.3
/usr/share/man/man3/libpngpf.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpng.la
/usr/lib32/libpng.so
/usr/lib32/libpng16.so
/usr/lib32/pkgconfig/32libpng.pc
/usr/lib32/pkgconfig/32libpng16.pc
/usr/lib32/pkgconfig/libpng.pc
/usr/lib32/pkgconfig/libpng16.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpng16.so.16.47.0
/usr/lib64/libpng16.so.16
/usr/lib64/libpng16.so.16.47.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpng16.so.16
/usr/lib32/libpng16.so.16.47.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpng/218fc8c15534e8840cbff5801582c450c97869ab
/usr/share/package-licenses/libpng/80b6f4fcbc19d7431482cba012e86f587828c1ba
/usr/share/package-licenses/libpng/91ab0c4ef71808e897ae26ca560ddf987a072b7b
/usr/share/package-licenses/libpng/aa4b9207aaff26bc16c562d6cd766a9eed49af1e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/png.5
