Summary:	wmmail - a "mail-checker" for WindowMaker
Summary(pl):	wmmail - program do sprawdzania poczty dla WindowMakera
Name:		wmmail
Version:	0.64
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://ww.eecg.utoronto.ca/~chanb/WMMail.app/WMMail.app-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.eecg.toronto.edu/cgi-bin/cgiwrap/chanb/index.cgi?wmmail
BuildRequires:	XFree86-devel
BuildRequires:	libPropList-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
wmmail is a "mail-checker" like xbiff. It is largely based on asmail,
but has been modified to work with WindowMaker instead of AfterStep.

%description -l pl
wmmail jest programem do sprawdzania poczty, podobnie jak xbiff.
Oparty jest w znacznej mierze na programie asmail, zmodyfikowanym w
sposób umo¿liwiaj±cy pracê programu w ¶rodowisku WindowMakera.

%prep
%setup -q -n WMMail.app-%{version}

%build
aclocal
%{__autoconf}
%configure

%{__make} EXTRA_LIBRARIES="-lSM -lICE" CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{pixmaps,sounds} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1

install src/WMMail $RPM_BUILD_ROOT%{_bindir}/
install doc/wmmail.man $RPM_BUILD_ROOT%{_mandir}/man1/wmmail.1
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README ChangeLog doc/Help.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_prefix}/GNUstep/Apps/WMMail.app
%{_prefix}/GNUstep/Apps/WMMail.app/Anims/*
%{_prefix}/GNUstep/Apps/WMMail.app/Defaults/*
%{_prefix}/GNUstep/Apps/WMMail.app/Sounds/*
%{_mandir}/man1/*
#%{_applnkdir}/DockApplets/wmmail.desktop
