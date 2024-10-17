# Spec is based on Alberto Altieri's work in MIB

Name:		iwscanner
Version:	0.2.4
Release:	2
Summary:	Wireless scanner based on iwtools
URL:		https://kuthulu.com/iwscanner/index.php
License:	LGPLv2+
Group:		Networking/Other
Source:		http://kuthulu.com/iwscanner/%{name}-%{version}.tgz
Source1:	kuthulu-%{name}.desktop
BuildArch:	noarch
Requires:	pygtk2.0
Requires:	wireless-tools
# for kdesu
Requires:	kdebase4-runtime

%description
A simple NetStumbler like wireless scanner based on iwtools.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}

# wrapper script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash

kdesu /usr/share/iwscanner/iwscanner.py
EOF
%__chmod 755 %{buildroot}%{_bindir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# datafiles
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp * %{buildroot}%{_datadir}/%{name}/

%clean
%__rm -rf %{buildroot}

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop



%changelog
* Wed Mar 07 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2.4-1mdv2011.0
+ Revision: 782662
- imported package iwscanner

