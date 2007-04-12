%define oname 		Terminal
%define version 	0.2.6
%define iconname 	%{oname}.png

Summary:		X Terminal Emulator
Name:			terminal
Version:		%{version}
Release:		%mkrel 1
License:		GPL
URL:			http://www.os-cillation.com/
Source:			%{oname}-%{version}.tar.bz2 
Patch:                	Terminal-0.2.0-Makefile.ins-Help.patch
Group:			Terminals
BuildRoot:		%{_tmppath}/%{name}-buildrrot
Requires:		vte >= 0.11.0 exo
BuildRequires:		vte-devel >= 0.11.0
BuildRequires:		perl(XML::Parser)
BuildRequires:          exo-devel
BuildRequires:		ImageMagick
BuildRequires:          desktop-file-utils

%description
Advanced lightweight Terminal Emulator for the X windowing system.

%prep
%setup -q -n %{oname}-%{version}
%patch -p1 

%build
%configure2_5x --enable-nls
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}} 
install -m 644 icons/48x48/stock_terminal-general.png %{buildroot}%{_liconsdir}/%{iconname}
convert icons/48x48/stock_terminal-general.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert icons/48x48/stock_terminal-general.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname} 

cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}):\
	command="%{_bindir}/%{name} --disable-server" \
	icon="%{iconname}" \
	title="Terminal" \
	longtitle="X Terminal Emulator" \
	needs="x11" \
	section="System/Terminals" \
        xdg="true"
EOF

desktop-file-install --vendor="" \
--add-category="GTK" \
--add-category="X-MandrivaLinux-TerminalEmulator" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{oname}

%post
%update_menus
%update_icon_cache hicolor
 
%postun
%clean_menus  
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files  -n %{name} -f %{oname}.lang
%defattr(-,root,root)
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS HACKING THANKS
%{_bindir}/*
%{_datadir}/%{oname}/*
%{_datadir}/applications/*
%{_datadir}/doc/%{oname}/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/16x16/stock/navigation/*.png
%{_datadir}/icons/hicolor/24x24/stock/navigation/*.png
%{_datadir}/icons/hicolor/48x48/stock/navigation/*.png
%{_datadir}/pixmaps/* 
%{_mandir}/man1/*.1*
%_menudir/*
%_iconsdir/%iconname
%_liconsdir/%iconname
%_miconsdir/%iconname



