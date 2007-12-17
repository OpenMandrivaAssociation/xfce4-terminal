%define oname Terminal
%define iconname %{oname}.png

Summary:	X terminal emulator for Xfce desktop environment
Name:		terminal
Version:	0.2.8
Release:	%mkrel 2
Group:		Terminals
License:	GPLv2+
URL:		http://www.xfce.org
Source0:	%{oname}-%{version}.tar.bz2
Patch0:		Terminal-0.2.0-Makefile.ins-Help.patch
# (saispo) take from debian terminal packages
Patch1:         Terminal-0.2.6-dont_refresh_prefs_too_much.patch
BuildRequires:	vte-devel >= 0.11.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	exo-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	libstartup-notification-1-devel
BuildRequires:	dbus-glib-devel
Requires:	vte >= 0.11.0
Requires:	exo

%description
Terminal is a modern, lightweight, and low memory cost terminal
emulator with tabs and multiple windows for the Xfce desktop
environment. It offers full-customization for the key bindings,
the aspect, the colors, and more.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
	--disable-static
%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32}/apps
convert icons/48x48/stock_terminal-general.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{iconname}
convert icons/48x48/stock_terminal-general.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{iconname}

desktop-file-install \
    --add-category="GTK" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{oname}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf  %{buildroot}

%files  -n %{name} -f %{oname}.lang
%defattr(-,root,root)
%doc README ChangeLog NEWS AUTHORS HACKING THANKS
%dir %{_datadir}/%{oname}
%{_bindir}/*
%{_datadir}/%{oname}/*
%{_datadir}/applications/*
%{_datadir}/doc/%{oname}/*
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/*/stock/navigation/*.png
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
