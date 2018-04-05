%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	X terminal emulator for Xfce desktop environment
Name:		xfce4-terminal
Version:	0.8.7.3
Release:	1
Group:		Terminals
License:	GPLv2+
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.11
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
Requires:	vte2.91
Requires:	exo
Obsoletes:	Terminal <= 0.4.8
Obsoletes:	terminal < 0.4.8
Provides:	Terminal = %{version}
Provides:	terminal = %{version}

%description
Terminal is a modern, lightweight, and low memory cost terminal
emulator with tabs and multiple windows for the Xfce desktop
environment. It offers full-customization for the key bindings,
the aspect, the colors, and more.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%check
make check

%install
%makeinstall_std

desktop-file-install \
    --add-category="GTK" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} %{name}.lang

# (tpg) a workaround for mdvbz #57365
%pre
if [ $1 -gt 1 ] ; then
    if [ -d %{_docdir}/Terminal ]; then
	rm -rf %{_docdir}/Terminal
    fi
fi

%files -n %{name} -f %{name}.lang
%doc README ChangeLog NEWS AUTHORS HACKING THANKS
%dir %{_datadir}/xfce4/terminal
%dir %{_datadir}/xfce4/terminal/colorschemes
%{_bindir}/%{name}
%{_datadir}/applications/xfce4-terminal.desktop
%{_datadir}/gnome-control-center/default-apps/xfce4-terminal-default-apps.xml
%{_mandir}/man1/xfce4-terminal.1.*
%{_datadir}/xfce4/terminal/colorschemes/*.theme
%{_datadir}/xfce4/terminal/terminal-preferences.ui
