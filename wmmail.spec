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
BuildRoot:	/tmp/%{name}-%{version}-root

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

install -d $RPM_BUILD_ROOT/usr/X11R6/share/wmmail/{pixmaps,sounds} \
	$RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT \
	MANPATH=/usr/X11R6/share/man \
	install install.man

install sounds/* $RPM_BUILD_ROOT/usr/X11R6/share/wmmail/sounds
install sample.wmmailrc $RPM_BUILD_ROOT/usr/X11R6/share/wmmail/wmmailrc
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmmail

for i in pixmaps/*; do
	install $i/* $RPM_BUILD_ROOT/usr/X11R6/share/wmmail/pixmaps
done

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/* \
	README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(755,root,root) /usr/X11R6/bin/wmmail
/usr/X11R6/share/man/man1/*
/usr/X11R6/share/wmmail
/etc/X11/wmconfig/wmmail

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.59-2]
- initial release for PLD,
- package is FHS 2.0 compliant.
