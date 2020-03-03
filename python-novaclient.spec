#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : python-novaclient
Version  : 16.0.0
Release  : 67
URL      : http://tarballs.openstack.org/python-novaclient/python-novaclient-16.0.0.tar.gz
Source0  : http://tarballs.openstack.org/python-novaclient/python-novaclient-16.0.0.tar.gz
Source1  : http://tarballs.openstack.org/python-novaclient/python-novaclient-16.0.0.tar.gz.asc
Summary  : Client library for OpenStack Compute API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-novaclient-bin = %{version}-%{release}
Requires: python-novaclient-license = %{version}-%{release}
Requires: python-novaclient-python = %{version}-%{release}
Requires: python-novaclient-python3 = %{version}-%{release}
Requires: Babel
Requires: iso8601
Requires: keystoneauth1
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: simplejson
Requires: six
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : iso8601
BuildRequires : keystoneauth1
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : simplejson
BuildRequires : six
BuildRequires : util-linux

%description
========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/python-novaclient.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

============================================
Python bindings to the OpenStack Compute API
============================================

.. image:: https://img.shields.io/pypi/v/python-novaclient.svg
    :target: https://pypi.org/project/python-novaclient/
    :alt: Latest Version

This is a client for the OpenStack Compute API. It provides a Python API (the
``novaclient`` module) and a command-line script (``nova``). Each implements
100% of the OpenStack Compute API.

* License: Apache License, Version 2.0
* `PyPi`_ - package installation
* `Online Documentation`_
* `Launchpad project`_ - release management
* `Blueprints`_ - feature specifications
* `Bugs`_ - issue tracking
* `Source`_
* `Specs`_
* `How to Contribute`_
* `Release Notes`_

.. _PyPi: https://pypi.org/project/python-novaclient
.. _Online Documentation: https://docs.openstack.org/python-novaclient/latest
.. _Launchpad project: https://launchpad.net/python-novaclient
.. _Blueprints: https://blueprints.launchpad.net/python-novaclient
.. _Bugs: https://bugs.launchpad.net/python-novaclient
.. _Source: https://opendev.org/openstack/python-novaclient
.. _How to Contribute: https://docs.openstack.org/infra/manual/developers.html
.. _Specs: http://specs.openstack.org/openstack/nova-specs/
.. _Release Notes: https://docs.openstack.org/releasenotes/python-novaclient

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
Provides: pypi(python-novaclient)

%description python3
python3 components for the python-novaclient package.


%prep
%setup -q -n python-novaclient-16.0.0
cd %{_builddir}/python-novaclient-16.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583213665
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-novaclient
cp %{_builddir}/python-novaclient-16.0.0/LICENSE %{buildroot}/usr/share/package-licenses/python-novaclient/409fdc85b52da1c06e114e3806ae71336290fe4d
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
/usr/share/package-licenses/python-novaclient/409fdc85b52da1c06e114e3806ae71336290fe4d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
