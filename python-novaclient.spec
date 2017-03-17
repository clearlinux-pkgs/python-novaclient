#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : python-novaclient
Version  : 7.1.0
Release  : 41
URL      : http://tarballs.openstack.org/python-novaclient/python-novaclient-7.1.0.tar.gz
Source0  : http://tarballs.openstack.org/python-novaclient/python-novaclient-7.1.0.tar.gz
Source99 : http://tarballs.openstack.org/python-novaclient/python-novaclient-7.1.0.tar.gz.asc
Summary  : Client library for OpenStack Compute API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-novaclient-bin
Requires: python-novaclient-python
Requires: Babel
Requires: iso8601
Requires: keystoneauth1
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: simplejson
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-Allow-image-ID-to-passed-in-directly.patch
Patch2: fast-poll.patch

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/python-novaclient.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package bin
Summary: bin components for the python-novaclient package.
Group: Binaries

%description bin
bin components for the python-novaclient package.


%package python
Summary: python components for the python-novaclient package.
Group: Default

%description python
python components for the python-novaclient package.


%prep
%setup -q -n python-novaclient-7.1.0
%patch1 -p1
%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489786149
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489786149
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nova

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
