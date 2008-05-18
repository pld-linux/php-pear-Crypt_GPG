%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	GPG
%define		_status		beta
%define		_pearname	Crypt_GPG
Summary:	%{_pearname} - GNU Privacy Guard (GPG)
Summary(pl.UTF-8):	%{_pearname} - Gnu Privacy Guard (GPG)
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a982c7ade6bd77af6026eaa1706c7139
URL:		http://pear.php.net/package/Crypt_GPG/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an object oriented interface to GNU Privacy
Guard (GPG). It requires the GPG executable to be on the system.

Though GPG can support symmetric-key cryptography, this package is
intended only to facilitate public-key cryptography.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza zorientowanego obiektowo interfejsu do narzędzi
Gnu Privacy Guard (GPG). Wymagana jest obecność tych narzędzi w
systemie.

Chociaż GPG wspiera kryptografię klucza symetrycznego, pakiet ten w
założeniu ma wspierać kryptografię klucza publicznego.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/GPG
%{php_pear_dir}/Crypt/GPG.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Crypt_GPG
