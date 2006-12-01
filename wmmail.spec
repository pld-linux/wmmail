# TODO: FHS (what is /usr/GNUstep???)
Summary:	wmmail - a "mail-checker" for WindowMaker
Summary(pl):	wmmail - program do sprawdzania poczty dla WindowMakera
Name:		wmmail
Version:	0.64
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://ww.eecg.utoronto.ca/~chanb/WMMail.app/WMMail.app-%{version}.tar.gz
# Source0-md5:	fc596db9f2f6b52eec3a303178106c8e
Source1:	%{name}.desktop
URL:		http://www.eecg.toronto.edu/cgi-bin/cgiwrap/chanb/index.cgi?wmmail
BuildRequires:	FHS-fixes
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libPropList-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__aclocal}
%{__autoconf}
%configure

%{__make} \
	EXTRA_LIBRARIES="-lSM -lICE" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{pixmaps,sounds} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1

install src/WMMail $RPM_BUILD_ROOT%{_bindir}
install doc/wmmail.man $RPM_BUILD_ROOT%{_mandir}/man1/wmmail.1
#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog doc/Help.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_prefix}/GNUstep/Apps/WMMail.app
%{_prefix}/GNUstep/Apps/WMMail.app/Anims
%{_prefix}/GNUstep/Apps/WMMail.app/Defaults
%{_prefix}/GNUstep/Apps/WMMail.app/Sounds
%{_mandir}/man1/*
#%%{_desktopdir}/docklets/wmmail.desktop
