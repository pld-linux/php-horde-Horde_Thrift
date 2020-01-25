%define		status		stable
%define		pearname	Horde_Thrift
Summary:	%{pearname} - Thrift
Name:		php-horde-Horde_Thrift
Version:	1.0.1
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	487452daeb7513e7606984b873eb6de9
URL:		https://github.com/horde/horde/tree/master/framework/Thrift/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.horde.org)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Packaged version of the PHP Thrift client

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Thrift.php
%dir %{php_pear_dir}/Horde/Thrift
# this looks weird. external pkg needed?
%{php_pear_dir}/Horde/Thrift/thrift_root
