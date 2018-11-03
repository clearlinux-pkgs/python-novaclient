#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-novaclient
Version  : 11.1.0
Release  : 47
URL      : http://tarballs.openstack.org/python-novaclient/python-novaclient-11.1.0.tar.gz
Source0  : http://tarballs.openstack.org/python-novaclient/python-novaclient-11.1.0.tar.gz
Source99 : http://tarballs.openstack.org/python-novaclient/python-novaclient-11.1.0.tar.gz.asc
Summary  : Client library for OpenStack Compute API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-novaclient-bin = %{version}-%{release}
Requires: python-novaclient-license = %{version}-%{release}
Requires: python-novaclient-python = %{version}-%{release}
Requires: python-novaclient-python3 = %{version}-%{release}
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
Requires: sphinxcontrib-apidoc
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-novaclient package.
Group: Binaries
Requires: python-novaclient-license = %{version}-%{release}

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
Requires: python-novaclient-python3 = %{version}-%{release}

%description python
python components for the python-novaclient package.


%package python3
Summary: python3 components for the python-novaclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-novaclient package.


%prep
%setup -q -n python-novaclient-11.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541272735
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-novaclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-novaclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nova

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-novaclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
