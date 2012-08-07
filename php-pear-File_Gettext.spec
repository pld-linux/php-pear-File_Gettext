%define		status		beta
%define		pearname	File_Gettext
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - GNU Gettext file parser
Summary(pl.UTF-8):	%{pearname} - parser plików GNU Gettext
Name:		php-pear-%{pearname}
Version:	0.4.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	78278dcb6d37b22bf0ad4736f01e1c73
URL:		http://pear.php.net/package/File_Gettext/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(pcre)
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reader and writer for GNU PO and MO files.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Za pomocą tej klasy możliwy jest odczyt i zapis z/do plików PO i MO.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/File_Gettext/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/*.php
%{php_pear_dir}/File/Gettext
