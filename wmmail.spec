Summary:	wmmail - a "mail-checker" for WindowMaker
Summary(pl):	wmmail - program do sprawdzania poczty dla WindowMakera
Name:		wmmail
Version:	0.59
Release:	2
Copyright:      GPL
Group:          X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://shells.technojunkie.com/~scorpio/%{name}-%{version}.tar.gz
Source1:	wmmail.wmconfig
Patch:		wmmail-global.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6
%define	_mandir	%{_prefix}/man

%description
wmmail is a "mail-checker" like xbiff. It is largely based on asmail, but 
has been modified to work with WindowMaker instead of AfterStep.

%description -l pl
wmmail jest programem do sprawdzania poczty, podobnie jak xbiff.
Oparty jest w znacznej mierze na programie asmail, zmodyfikowanym
w sposób umo¿liwiaj±cy pracê programu w ¶rodowisku WindowMakera.

%prep
%setup -q
%patch -p1

%build
xmkmf
make EXTRA_LIBRARIES="-lSM -lICE" CDEBUGFLAGS="$RPM_OPT_FLAGS" all
strip wmmail

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{pixmaps,sounds} \
        $RPM_BUILD_ROOT/etc/X11/wmconfig

make install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install sample.wmmailrc $RPM_BUILD_ROOT%{_datadir}/%{name}/wmmailrc
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

for i in pixmaps/*; do
	install $i/* $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps
done

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/%{name}
/etc/X11/wmconfig/%{name}

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.59-2]
- initial release for PLD,
- package is FHS 2.0 compliant.
