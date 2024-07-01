#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-UPnP
Version  : 1.4.6
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/S/SK/SKONNO/Net-UPnP-1.4.6.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SK/SKONNO/Net-UPnP-1.4.6.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-upnp-perl/libnet-upnp-perl_1.4.6-1.debian.tar.xz
Summary  : 'Perl extension for UPnP'
Group    : Development/Tools
License  : BSD-3-Clause
Requires: perl-Net-UPnP-license = %{version}-%{release}
Requires: perl-Net-UPnP-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Net::UPnP version 1.4.6
===========================
how to install the module, any machine dependencies it may have (for
example C compilers and installed libraries) and any other information
that should be provided before the module is installed.

%package dev
Summary: dev components for the perl-Net-UPnP package.
Group: Development
Provides: perl-Net-UPnP-devel = %{version}-%{release}
Requires: perl-Net-UPnP = %{version}-%{release}

%description dev
dev components for the perl-Net-UPnP package.


%package license
Summary: license components for the perl-Net-UPnP package.
Group: Default

%description license
license components for the perl-Net-UPnP package.


%package perl
Summary: perl components for the perl-Net-UPnP package.
Group: Default
Requires: perl-Net-UPnP = %{version}-%{release}

%description perl
perl components for the perl-Net-UPnP package.


%prep
%setup -q -n Net-UPnP-1.4.6
cd %{_builddir}
tar xf %{_sourcedir}/libnet-upnp-perl_1.4.6-1.debian.tar.xz
cd %{_builddir}/Net-UPnP-1.4.6
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-UPnP-1.4.6/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-UPnP
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Net-UPnP/8f5b1549c0656019c12ff818e140fe1fff18f9d7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::UPnP.3
/usr/share/man/man3/Net::UPnP::AV::Container.3
/usr/share/man/man3/Net::UPnP::AV::Content.3
/usr/share/man/man3/Net::UPnP::AV::Item.3
/usr/share/man/man3/Net::UPnP::AV::MediaRenderer.3
/usr/share/man/man3/Net::UPnP::AV::MediaServer.3
/usr/share/man/man3/Net::UPnP::ActionResponse.3
/usr/share/man/man3/Net::UPnP::ControlPoint.3
/usr/share/man/man3/Net::UPnP::Device.3
/usr/share/man/man3/Net::UPnP::GW::Gateway.3
/usr/share/man/man3/Net::UPnP::HTTP.3
/usr/share/man/man3/Net::UPnP::HTTPResponse.3
/usr/share/man/man3/Net::UPnP::QueryResponse.3
/usr/share/man/man3/Net::UPnP::Service.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-UPnP/8f5b1549c0656019c12ff818e140fe1fff18f9d7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
