Name:       hexter
Summary:    Yamaha DX7 modeling DSSI plugin
Version:    1.0.1
Release:    2

Source:     http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
URL:        http://dssi.sourceforge.net/hexter.html
License:    GPLv2+
Group:      Sound

BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)

%description
hexter is a software synthesizer that models the sound generation of a Yamaha
DX7 synthesizer. It can easily load most DX7 patch bank files, accept patch
editing commands via MIDI sys-ex messages (ALSA systems only), and recreate the
sound of the DX7 with greater accuracy than any previous open-source emulation
(that the author is aware of....)

hexter operates as a plugin for the Disposable Soft Synth Interface (DSSI).
DSSI is a plugin API for software instruments (soft synths) with user
interfaces, permitting them to be hosted in-process by audio applications.

%prep
%setup -q

%build
alias libtoolize=true
%configure2_5x
%make

%install
%makeinstall

%files
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS README TODO
%{_libdir}/dssi/%{name}.so
%{_libdir}/dssi/%{name}/%{name}_gtk
%{_datadir}/%{name}/*.dx7



%changelog
* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.6.2-3
+ Revision: 793831
- rebuild, spec cleanup

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-2mdv2011.0
+ Revision: 611093
- rebuild

* Mon Dec 07 2009 Jérôme Brenier <incubusss@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 474465
- new version 0.6.2
- fix license tag

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.9-3mdv2009.0
+ Revision: 246855
- rebuild
- fix description-line-too-long

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.5.9-1mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import hexter


* Sat Apr  1 2006 Austin Acton <austin@mandriva.org> 0.5.9-1mdk
- spec from Pedro Lopez-Cabanillas <plcl@users.sourceforge.net>
- initial package
