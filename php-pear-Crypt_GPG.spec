%define		status		stable
%define		pearname	Crypt_GPG
Summary:	%{pearname} - GNU Privacy Guard (GPG)
Summary(pl.UTF-8):	%{pearname} - Gnu Privacy Guard (GPG)
Name:		php-pear-%{pearname}
Version:	1.6.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	824430837954be93c6c9b9def5691a64
URL:		http://pear.php.net/package/Crypt_GPG/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Suggests:	php-posix
Obsoletes:	php-pear-Crypt_GPG-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an object oriented interface to GNU Privacy
Guard (GPG). It requires the GPG executable to be on the system.

Though GPG can support symmetric-key cryptography, this package is
intended only to facilitate public-key cryptography.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten dostarcza zorientowanego obiektowo interfejsu do narzędzi
Gnu Privacy Guard (GPG). Wymagana jest obecność tych narzędzi w
systemie.

Chociaż GPG wspiera kryptografię klucza symetrycznego, pakiet ten w
założeniu ma wspierać kryptografię klucza publicznego.

Ta klasa ma w PEAR status: %{status}.

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
%doc docs/Crypt_GPG/README.md
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/GPG
%{php_pear_dir}/Crypt/GPG.php
%{php_pear_dir}/Crypt/GPGAbstract.php
