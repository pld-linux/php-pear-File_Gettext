%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Gettext
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - GNU Gettext file parser
Summary(pl):	%{_pearname} - parser plik�w GNU Gettext
Name:		php-pear-%{_pearname}
Version:	0.3.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a89095de7b2ea259953a6aac9700213d
URL:		http://pear.php.net/package/File_Gettext/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.1.0
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reader and writer for GNU PO and MO files.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc� tej klasy mo�liwy jest odczyt i zapis z/do plik�w PO i MO.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
