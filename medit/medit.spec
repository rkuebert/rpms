Name:		medit
Version:	1.2.0
Release:	1%{?dist}
Summary:	A programming and around-programming text editor

License:	LGPLv2+
URL:		http://mooedit.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mooedit/%{name}-%{version}.tar.bz2

BuildRequires:	gtk2-devel
BuildRequires:	pygtk2-devel
BuildRequires:	libxml2-devel
BuildRequires:	python-devel
BuildRequires:	libSM-devel
BuildRequires:	intltool

%description
A simple text editor with configurable syntax highlighting, configurable
keyboard accelerators, plugin support etc.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}

%check


%install
rm -rf %{buildroot}
%make_install


chmod a+x %{buildroot}%{_datarootdir}/%{name}-1/language-specs/check.sh
chmod a+x %{buildroot}%{_datarootdir}/%{name}-1/python/pyconsole.py

%find_lang medit-1
%find_lang medit-1-gsv

%files -f medit-1.lang -f medit-1-gsv.lang

%{_bindir}/medit
%{_datarootdir}/applications/medit.desktop
%{_datarootdir}/doc/medit-1/
%{_datarootdir}/icons/hicolor/48x48/apps/medit.png
%{_mandir}/man1/medit.1.gz
%{_datarootdir}/medit-1
%exclude %{_datadir}/icons/hicolor/icon-theme.cache

%doc

%changelog
* Mon Jun 29 2015 Roland Kuebert <roland@upic.de> - 1.2.0-1
- Initial RPM release
