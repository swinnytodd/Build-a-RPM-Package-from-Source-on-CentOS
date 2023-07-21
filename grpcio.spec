%global srcname grpcio
Name:          python-%{srcname}
Summary:       A high performance, open-source universal RPC framework
License:       ASL 2.0
URL:           https://pypi.org/project/%{srcname}

Version:       1.50.0
Release:       1%{?dist}
Source0:       %{srcname}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: c-ares-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel

%description
A high performance, open-source universal RPC framework.

This package allows using gRPC in Python applications.


%package -n python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel >= 3.4
BuildRequires: python3-Cython
BuildRequires: python3-setuptools
BuildRequires: python3-six >= 1.5.2
Requires:      python3-six >= 1.5.2
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A high performance, open-source universal RPC framework.

This package allows using gRPC in Python 3 applications.


%prep
%autosetup -n %{srcname}-%{version}


%build
# Build against system libraries
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1

# Don't use the pre-generated C files
export GRPC_PYTHON_BUILD_WITH_CYTHON=1

# Use the Fedora CFLAGS/LDFLAGS
export GRPC_PYTHON_CFLAGS="%{optflags}"
export GRPC_PYTHON_LDFLAGS="%{__global_ldflags}"

%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.md
%{python3_sitearch}/grpc/
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info/

%changelog
* Wed Jun 28 2023 Amantur <aman91@bk.ru> - 8.7.0-1
- Initial RPM release.