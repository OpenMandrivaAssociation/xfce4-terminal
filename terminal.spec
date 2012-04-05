%define oname Terminal
%define iconname %{oname}.png
%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	X terminal emulator for Xfce desktop environment
Name:		terminal
Version:	0.4.8
Release:	2
Group:		Terminals
License:	GPLv2+
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{oname}-%{version}.tar.bz2
BuildRequires:	vte-devel >= 0.17.1
BuildRequires:	perl(XML::Parser)
BuildRequires:	exo-devel >= 0.7.2
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	libstartup-notification-1-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	intltool
Requires:	vte >= 0.11.0
Requires:	exo

%description
Terminal is a modern, lightweight, and low memory cost terminal
emulator with tabs and multiple windows for the Xfce desktop
environment. It offers full-customization for the key bindings,
the aspect, the colors, and more.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x \
	--disable-static \
	--enable-dbus
%make

%check
make check

%install
%makeinstall_std

desktop-file-install \
    --add-category="GTK" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{oname} %{oname}.lang

# (tpg) a workaround for mdvbz #57365
%pre
if [ $1 -gt 1 ] ; then
    if [ -d %{_docdir}/Terminal ]; then
	rm -rf %{_docdir}/Terminal
    fi
fi

%files  -n %{name} -f %{oname}.lang
%doc README ChangeLog NEWS AUTHORS HACKING THANKS
%dir %{_datadir}/%{oname}
%{_bindir}/*
%{_datadir}/%{oname}/*
%{_datadir}/applications/*
%{_datadir}/gnome-control-center/default-apps/Terminal-default-apps.xml
%{_datadir}/doc/%{oname}/*
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/*/stock/navigation/*.png
%{_datadir}/pixmaps/*
%{_mandir}/*/*
