%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Gettext
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - GNU Gettext file parser
Summary(pl.UTF-8):	%{_pearname} - parser plików GNU Gettext
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f3bdf70544be2ef82565078cd0f9e097
URL:		http://pear.php.net/package/File_Gettext/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reader and writer for GNU PO and MO files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Za pomocą tej klasy możliwy jest odczyt i zapis z/do plików PO i MO.

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
