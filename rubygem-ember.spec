%define oname ember

Name:       rubygem-%{oname}
Version:    0.3.0
Release:    %mkrel 1
Summary:    eRuby template processor
Group:      Development/Ruby
License:    ISC License
URL:        http://snk.tuxfamily.org/lib/ember/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Ember (EMBEdded Ruby) is an eRuby template processor that allows debugging,
reduces markup, and improves composability of eRuby templates.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

# Move manpages to mandir
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man/* %{buildroot}/%{_mandir}
rmdir %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/ember
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CREDITS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/man.html
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_mandir}/man1/%{oname}.1.*
