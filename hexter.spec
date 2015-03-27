Name:       hexter
Summary:    Yamaha DX7 modeling DSSI plugin
Version:    1.0.2
Release:    1

Source:     https://sourceforge.net/projects/dssi/files/hexter/1.0.2/%{name}-%{version}.tar.gz
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
%doc ChangeLog COPYING AUTHORS README TODO
%{_libdir}/dssi/%{name}.so
%{_libdir}/dssi/%{name}/%{name}_gtk
%{_datadir}/%{name}/*.dx7
