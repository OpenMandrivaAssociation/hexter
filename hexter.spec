%define name	hexter
%define version	0.5.9
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Yamaha DX7 modeling DSSI plugin
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.bz2
URL:		http://dssi.sourceforge.net/hexter.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	dssi-devel
BuildRequires:	liblo-devel
BuildRequires:	libalsa-devel
BuildRequires:	gtk2-devel

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
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS README TODO
%{_libdir}/dssi/%{name}.so
%{_libdir}/dssi/%{name}.la
%{_libdir}/dssi/%{name}/%{name}_gtk
%{_datadir}/%{name}/*.dx7

