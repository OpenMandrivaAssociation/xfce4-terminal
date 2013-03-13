%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	X terminal emulator for Xfce desktop environment
Name:		xfce4-terminal
Version:	0.6.1
Release:	1
Group:		Terminals
License:	GPLv2+
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		xfce4-terminal-0.6.1-fix-format-string.patch
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
Requires:	vte >= 0.11.0
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
%apply_patches

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



%changelog
* Fri Apr 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.8-2
+ Revision: 789514
- rebuild

* Mon Jun 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.8-1
+ Revision: 687565
- update to new version 0.4.8

* Sat Apr 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.7-1
+ Revision: 652036
- update to new version 0.4.7
- drop patch 1, fixed by upstream

* Sat Mar 05 2011 Funda Wang <fwang@mandriva.org> 0.4.6-3
+ Revision: 642112
- rebuild

* Sun Feb 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.6-2
+ Revision: 636443
- drop patch 2, not needed anymore

* Sat Feb 05 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.6-1
+ Revision: 636283
- update to new version 0.4.6
- drop patch 0

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.5-6
+ Revision: 633046
- rebuild for new Xfce 4.8.0

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.5-5mdv2011.0
+ Revision: 594224
- rebuild

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.5-4mdv2011.0
+ Revision: 579621
- rebuild for new xfce 4.7.0

* Wed Sep 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.5-3mdv2011.0
+ Revision: 578785
- Patch2: add support for vte-0.25.91
- Patch1: fix small memory leak (mdv #61018)

* Sun Aug 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.5-2mdv2011.0
+ Revision: 564474
- rebuild for new vte and gtk

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.5-1mdv2011.0
+ Revision: 554446
- update to new version 0.4.5

* Tue Feb 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-2mdv2010.1
+ Revision: 499786
- some doc symlinks were replaced by a directories, and this breaks upgrade of terminal (mdvbz #57365)

* Mon Feb 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 499258
- update to new version 0.4.4
- fix file list

* Tue Oct 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 455039
- update to new version 0.4.2
- adapt to use upstream new URLs for sources

* Sat Sep 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-2mdv2010.0
+ Revision: 449614
- rebuild for new vte

* Wed Jul 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 398584
- update to new version 0.4.0

* Sat Jul 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.99.1-1mdv2010.0
+ Revision: 397028
- update to new version 0.2.99.1

* Mon Jul 13 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.90-1mdv2010.0
+ Revision: 395570
- drop all patches, they were fixed by upstream
- use stock icons
- update to new version 0.2.90
- bump vte version to 0.17.1

* Thu Jun 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.12-5mdv2010.0
+ Revision: 385025
- Patch3: fix tab activity on window size change

* Wed Jun 10 2009 Götz Waschk <waschk@mandriva.org> 0.2.12-4mdv2010.0
+ Revision: 384703
- rebuild for new vte

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 0.2.12-3mdv2010.0
+ Revision: 382205
- rebuild for new libvte

* Sun May 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.12-2mdv2010.0
+ Revision: 379249
- Patch2: fix always show tabs option

* Wed Apr 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.12-1mdv2010.0
+ Revision: 368748
- update to new version 0.2.12

* Sun Apr 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.10-4mdv2009.1
+ Revision: 364201
- Patch2: fall back to the SHELL environment variable
- Patch3: properly destroy the go menu
- code is fixed, so no need to disable format-strings error check

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.10-3mdv2009.1
+ Revision: 349169
- rebuild whole xfce

* Sat Feb 28 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.10-2mdv2009.1
+ Revision: 346149
- drop patch 2 as it was merged by upstream

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 0.2.10-1mdv2009.1
+ Revision: 345746
- Disable patch2

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 0.2.10

* Thu Jan 15 2009 Jérôme Soyer <saispo@mandriva.org> 0.2.8.3-1mdv2009.1
+ Revision: 329672
- New upstream release

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.8-6mdv2009.1
+ Revision: 294878
- rebuild for Xfce4.6 beta 1

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.2.8-5mdv2009.0
+ Revision: 269419
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - Patch2: blink the tab if there is any activity on background

* Wed Mar 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.8-3mdv2008.1
+ Revision: 188968
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.8-2mdv2008.1
+ Revision: 119173
- really apply patch 1
- add checks

* Tue Dec 04 2007 Jérôme Soyer <saispo@mandriva.org> 0.2.8-1mdv2008.1
+ Revision: 115338
- Add files
- Add Patches for fixing prefs
- New release and remove unneeded patch which is fixed upstream

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.6-5mdv2008.1
+ Revision: 110608
- add missing buildrequires
- update summary and description
- new license policy
- do not package COPYING and INSTALL files
- revert last change
- fix desktop entry

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.6-4mdv2008.0
+ Revision: 71398
- provide patch 1 (CVE-2007-3770)
- own directory
- drop X-MandrivaLinux

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.6-3mdv2008.0
+ Revision: 32838
- s/imagemagick/ImageMagick

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.6-2mdv2008.0
+ Revision: 32825
- drop old menu style
- tune up desktop file
- disable compiling static files
- spec file clean


* Tue Jan 23 2007 plouf <plouf> 0.2.6-1mdv2007.0
+ Revision: 112310
- New release 0.2.6

* Wed Dec 06 2006 Jérôme Soyer <saispo@mandriva.org> 0.2.5.8-0.rc2mdv2007.1
+ Revision: 91631
- Update to 2.5.8rc2

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix BuildRequires
    - import terminal-0.2.5.4-0.beta2.2mdv2007.0

* Wed Aug 02 2006 Charles A Edwards <eslrahc@mandriva.org> 0.2.5.4-0.beta2.2mdv2007.0
- rebuild for latest dbus
- use icon_cache marco

* Tue Jul 11 2006 Charles A Edwards <eslrahc@mandriva.org> 0.2.5.4-0.beta2.1mdv2007.0
- 0.2.5.4beta2

* Sat Jun 24 2006 Charles A Edwards <eslrahc@mandriva.org> 0.2.5.1-0.beta1.2mdv2007.0
- rebuild for libvte9
- BR & R
- drop Source1
- Xdg

* Wed Apr 26 2006 Jerome Soyer <saispo@mandriva.org> 0.2.5.1-0.beta1.1mdk
- Sat Apr 22 2006 trem <trem@mandriva.org> 0.2.5.1-0.beta1.1mdk
- 0.2.5.1beta1

* Fri Jan 27 2006 Frederic Crozat <fcrozat@mandriva.com> 0.2.4-4mdk
- Rebuild with latest dbus

* Mon Oct 31 2005 Eskild Hustvedt <eskild@mandriva.org> 0.2.4-3mdk
- Rebuild for new dbus

* Tue Aug 02 2005 Marcel Pol <mpol@mandriva.org> 0.2.4-2mdk
- buildrequires perl-XML-Parser, ImageMagick

* Wed May 25 2005 Marcel Pol <mpol@mandriva.org> 0.2.4-1mdk
- 0.2.4
- %%{1}mdv2007.1

* Thu Mar 17 2005 Charles A Edwards <eslrahc@mandrake.org> 0.2.4-0.pre1.1mdk
- 0.2.4pre1

* Sun Jan 09 2005 Charles A Edwards <eslrahc@mandrake.org> 0.2.2-1mdk
- 0.2.2

* Sat Dec 04 2004 Charles A Edwards <eslrahc@mandrake.org> 0.2.0-1mdk
- rebuild to use db4.3

