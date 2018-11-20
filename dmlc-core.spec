#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dmlc-core
Version  : 0.3
Release  : 4
URL      : https://github.com/dmlc/dmlc-core/archive/v0.3.tar.gz
Source0  : https://github.com/dmlc/dmlc-core/archive/v0.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: dmlc-core-lib = %{version}-%{release}
Requires: dmlc-core-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : openjdk9-dev
BuildRequires : openssl-dev
BuildRequires : python3
Patch1: 0001-Add-SOVERSION-to-dmlc.so-don-t-install-doc.patch

%description
This document is generated by sphinx.
Make sure you cloned the following repos in the root.

%package dev
Summary: dev components for the dmlc-core package.
Group: Development
Requires: dmlc-core-lib = %{version}-%{release}
Provides: dmlc-core-devel = %{version}-%{release}

%description dev
dev components for the dmlc-core package.


%package lib
Summary: lib components for the dmlc-core package.
Group: Libraries
Requires: dmlc-core-license = %{version}-%{release}

%description lib
lib components for the dmlc-core package.


%package license
Summary: license components for the dmlc-core package.
Group: Default

%description license
license components for the dmlc-core package.


%prep
%setup -q -n dmlc-core-0.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542735342
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1542735342
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dmlc-core
cp LICENSE %{buildroot}/usr/share/package-licenses/dmlc-core/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/dmlc/any.h
/usr/include/dmlc/array_view.h
/usr/include/dmlc/base.h
/usr/include/dmlc/blockingconcurrentqueue.h
/usr/include/dmlc/common.h
/usr/include/dmlc/concurrency.h
/usr/include/dmlc/concurrentqueue.h
/usr/include/dmlc/config.h
/usr/include/dmlc/data.h
/usr/include/dmlc/endian.h
/usr/include/dmlc/input_split_shuffle.h
/usr/include/dmlc/io.h
/usr/include/dmlc/json.h
/usr/include/dmlc/logging.h
/usr/include/dmlc/lua.h
/usr/include/dmlc/memory.h
/usr/include/dmlc/memory_io.h
/usr/include/dmlc/omp.h
/usr/include/dmlc/optional.h
/usr/include/dmlc/parameter.h
/usr/include/dmlc/recordio.h
/usr/include/dmlc/registry.h
/usr/include/dmlc/serializer.h
/usr/include/dmlc/thread_group.h
/usr/include/dmlc/thread_local.h
/usr/include/dmlc/threadediter.h
/usr/include/dmlc/timer.h
/usr/include/dmlc/type_traits.h
/usr/lib64/libdmlc.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdmlc.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dmlc-core/LICENSE
