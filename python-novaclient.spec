#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : python-novaclient
Version  : 10.3.0
Release  : 44
URL      : http://tarballs.openstack.org/python-novaclient/python-novaclient-10.3.0.tar.gz
Source0  : http://tarballs.openstack.org/python-novaclient/python-novaclient-10.3.0.tar.gz
Source99 : http://tarballs.openstack.org/python-novaclient/python-novaclient-10.3.0.tar.gz.asc
Summary  : Client library for OpenStack Compute API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-novaclient-bin
Requires: python-novaclient-python3
Requires: python-novaclient-license
Requires: python-novaclient-python
Requires: Babel
Requires: Sphinx
Requires: iso8601
Requires: keystoneauth1
Requires: openstackdocstheme
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: reno
Requires: simplejson
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-novaclient package.
Group: Binaries
Requires: python-novaclient-license

%description bin
bin components for the python-novaclient package.


%package license
Summary: license components for the python-novaclient package.
Group: Default

%description license
license components for the python-novaclient package.


%package python
Summary: python components for the python-novaclient package.
Group: Default
Requires: python-novaclient-python3

%description python
python components for the python-novaclient package.


%package python3
Summary: python3 components for the python-novaclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-novaclient package.


%prep
%setup -q -n python-novaclient-10.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532381979
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-novaclient
cp LICENSE %{buildroot}/usr/share/doc/python-novaclient/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nova

%files license
%defattr(-,root,root,-)
/usr/share/doc/python-novaclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
