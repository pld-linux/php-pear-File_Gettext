
%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       Gettext
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - GNU Gettext file parser
Summary(pl):	%{_pearname} - parser plik�w GNU Gettext
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c1f8cd6ffc2169044f232b8c0f2ca9dd
URL:		http://pear.php.net/package/File_Gettext/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reader and writer for GNU PO and MO files.

This class has in PEAR status: %{_status}.

%description -l pl
Za pomoc� tej klasy mo�liwy jest odczyt i zapis z/do plik�w PO i MO.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
