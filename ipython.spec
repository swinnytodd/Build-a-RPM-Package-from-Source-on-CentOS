# Этот файл должен быть размещен в директории ~/rpmbuild/SPECS/

%global        __python         %{__python3}
%global        __python_version %( %{__python} -c "import sys; print(sys.version[:3])")

Name:           ipython
Version:        8.7.0
Release:        1%{?dist}
Summary:        Enhanced interactive Python shell

License:        BSD
URL:            https://ipython.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-stack-data
Requires:       python3


%global iPython provides a rich toolkit to help you make the most out of using python interactively.

%description
%{ipython_desc_base}
 

Summary:        An enhanced interactive Python shell
%{?python_provide:%python_provide python3-ipython}
%{?python_provide:%python_provide python3-ipython-console}
Provides:       ipython3 = %{version}-%{release}
Provides:       ipython = %{version}-%{release}
Provides:       python3-ipython-console = %{version}-%{release}
Obsoletes:      python3-ipython-console < 5.3.0-1
Conflicts:      python2-ipython < 7

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%{_bindir}/ipython3
%{_bindir}/ipython
%{_mandir}/man1/ipython.*

 
%dir %{python3_sitelib}/IPython
%{python3_sitelib}/IPython/external
%{python3_sitelib}/IPython/__pycache__/
%{python3_sitelib}/IPython/*.py*
%dir %{python3_sitelib}/IPython/testing
%{python3_sitelib}/IPython/testing/__pycache__/
%{python3_sitelib}/IPython/testing/*.py*
%{python3_sitelib}/IPython/testing/plugin
%{python3_sitelib}/ipython-%{version}-py%{python3_version}.egg-info/
 
%{python3_sitelib}/IPython/core/
%{python3_sitelib}/IPython/extensions/
%{python3_sitelib}/IPython/lib/
%{python3_sitelib}/IPython/terminal/
%{python3_sitelib}/IPython/utils/
%exclude %{python3_sitelib}/IPython/*/tests/
%{python3_sitelib}/IPython/sphinxext/
/usr/bin/ipython3.9

%changelog
* Wed Jun 28 2023 Amantur <aman91@bk.ru> - 8.7.1-1
- Initial RPM release.


