Summary: wmmail is a "mail-checker" like xbiff.
Name: wmmail
Version: 0.59
Release: 1
Source: wmmail-%{version}.tar.gz
Patch: wmmail-0.59-global.patch
Copyright: GPL
Group: X11/Utilities
BuildRoot: /var/tmp/wmmail-root

%description
wmmail is a "mail-checker" like xbiff. It is largely based on asmail, but 
has been modified to work with WindowMaker instead of AfterStep. See the 
man page for more information.

%prep
%setup -q
%patch -p1

%build
xmkmf
make EXTRA_LIBRARIES="-lSM -lICE" all
strip wmmail

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

mkdir -p $RPM_BUILD_ROOT/usr/share/wmmail/{pixmaps,sounds}
install -m 644 sounds/* $RPM_BUILD_ROOT/usr/share/wmmail/sounds
for i in pixmaps/*; do
    install -m 644 $i/* $RPM_BUILD_ROOT/usr/share/wmmail/pixmaps
done
install -m 644 sample.wmmailrc $RPM_BUILD_ROOT/usr/share/wmmail/wmmailrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README sample.wmmailrc
/usr/X11R6/bin/wmmail
/usr/X11R6/man/man1/wmmail.1x
/usr/share/wmmail
