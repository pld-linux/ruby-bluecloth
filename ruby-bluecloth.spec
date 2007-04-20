Summary:	BlueCloth - Markdown Humane Web Text for Ruby
Summary(pl.UTF-8):	BlueCloth - obsługa formatu tekstowego dla WWW Markdown w języku Ruby
Name:		ruby-bluecloth
Version:	1.0.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.deveiate.org/code/BlueCloth-1.0.0.tar.bz2
# Source0-md5:	41d385b4ed147630cd922aa50475670b
URL:		http://www.whytheluckystiff.net/ruby/bluecloth/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	sed >= 4.0
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BlueCloth is a module for using Markdown in Ruby. Markdown is a text
format. A very simple text format. Another stab at making readable
text that can be converted to HTML.

%description -l pl.UTF-8
BlueCloth to moduł do używania Markdown w Rubym. Markdown to format
tekstowy. Bardzo prosty format tekstowy. Kolejny krok do tworzenia
czytelnego tekstu, który może być konwertowany do HTML-a.

%prep
%setup -q -n BlueCloth-%{version}
sed -i -e '1s,#!.*/bin/ruby18,#!%{_bindir}/ruby,' bin/*

%build
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
