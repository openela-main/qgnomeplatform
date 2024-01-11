
Name:           qgnomeplatform
Version:        0.8.4
Release:        2%{?dist}
Summary:        Qt Platform Theme aimed to accommodate Gnome settings

License:        LGPLv2+
URL:            https://github.com/MartinBriza/QGnomePlatform
Source0:        https://github.com/MartinBriza/QGnomePlatform/archive/%{version}/QGnomePlatform-%{version}.tar.gz

# Upstream patches
Patch0:         qgnomeplatform-use-more-updated-window-states-value.patch

BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gtk3-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  libinput-devel
BuildRequires:  libXrender-devel
BuildRequires:  qt5-qtbase-devel >= 5.12.0
BuildRequires:  qt5-qtbase-static >= 5.12.0
BuildRequires:  qt5-qtwayland-devel >= 5.12.0

BuildRequires:  libadwaita-qt5-devel >= 1.3.1
Requires:       adwaita-qt5%{?_isa}

BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
QGnomePlatform is a Qt Platform Theme aimed to accommodate as much of
GNOME settings as possibleand utilize them in Qt applications without
modifying them - making them fit into the environment as well as possible.


%prep
%autosetup -p1 -n  QGnomePlatform-%{version}


%build
%cmake

%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_qt5_libdir}/libqgnomeplatform.so
%{_qt5_libdir}/qt5/plugins/platformthemes/libqgnomeplatformtheme.so
%{_qt5_libdir}/qt5/plugins/wayland-decoration-client/libqgnomeplatformdecoration.so

%changelog
* Fri Apr 01 2022 Jan Grulich <jgrulich@redhat.com> - 0.8.4-2
- Rebuild (Qt 5.15.3)
  Resolves: bz#2061415

* Mon Jan 24 2022 Jan Grulich <jgrulich@redhat.com> - 0.8.4-1
- 0.8.4 (sync with Fedora)
  Resolves: bz#2041342

* Mon Aug 23 2021 Jan Grulich <jgrulich@redhat.com> - 0.8.0-1
- 0.8.0
  Resolves: bz#1968290

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.7.1-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon May 03 2021 Jan Grulich <jgrulich@redhat.com> - 0.7.1-1
- Sync with Fedora - update to 0.7.1
  Resolves: bz#1951151

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.7.0-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Jan Grulich <jgrulich@redhat.com> - 0.7.0-2
- QXdgDesktopFileDialog: backport upstream fixes

* Thu Dec 17 2020 Jan Grulich <jgrulich@redhat.com> - 0.7.0-1
- 0.7.0

* Fri Nov 27 10:56:10 CET 2020 Jan Grulich <jgrulich@redhat.com> - 0.6.90-3
- rebuild (qt5) for eln

* Mon Nov 23 07:54:44 CET 2020 Jan Grulich <jgrulich@redhat.com> - 0.6.90-2
- rebuild (qt5)

* Wed Sep 30 2020 Jan Grulich <jgrulich@redhat.com> - 0.6.90-1
- 0.6.90

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 0.6.1-3
- rebuild (qt5)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Jan Grulich <jgrulich@redhat.com> - 0.6.1-1
- 0.6.1

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.6.0-4
- rebuild (qt5)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.6.0-2
- rebuild (qt5)

* Wed Nov 20 2019 Jan Grulich <jgrulich@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Fri Oct 04 2019 Jan Grulich <jgrulich@redhat.com> - 0.5.90-1
- Update to 0.5.90

* Thu Oct 03 2019 Jan Grulich <jgrulich@redhat.com> - 0.5-17
- Link decorations against qtx11extras

* Fri Sep 27 2019 Jan Grulich <jgrulich@redhat.com> - 0.5-16
- Set XCURSOR_SIZE only on wayland

* Fri Sep 27 2019 Jan Grulich <jgrulich@redhat.com> - 0.5-15
- Add support for double-click to maximize windows

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.5-14
- rebuild (qt5)

* Wed Aug 28 2019 Jan Grulich <jgrulich@redhat.com> - 0.5-13
- Fix cursor size on wayland

* Thu Aug 15 2019 Jan Grulich <jgrulich@redhat.com> - 0.5-12
- Add Gnome-like wayland decorations
  BUG: bz#1732129

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.5-10
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.5-9
- rebuild (qt5)

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.5-8
- rebuild (qt5), use %%make_build

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.5-6
- rebuild (qt5)

* Wed Dec 05 2018 Jan Grulich <jgrulich@redhat.com> - 0.5-1
- Update to 0.5

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 0.4-3
- rebuild (qt5)

* Fri Aug 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.4-2
- rebuild

* Tue Jul 24 2018 Jan Grulich <jgrulich@redhat.com> - 0.4-1
- Update to 0.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3-11
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3-10
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 0.3-9
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 0.3-7
- rebuild (qt5)

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.3-6
- rebuild (qt5)

* Mon Oct 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.3-5
- rebuild (qt5)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.3-2
- rebuild (qt5)

* Mon May 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.3-1
- Update to 0.3

* Mon May 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2-17.20170206git
- rebuild (Qt 5.9)

* Fri Mar 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2-16.20170206git
- fresh 20170206 snapshot (#1438024)

* Thu Mar 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2-15.20161205git
- rebuild (Qt 5.8)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14.20161205git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Jan Grulich <jgrulich@redhat.com> - 0.2-13.20161205git
- Fix crash in font dialog (bz#1378003)

* Thu Dec 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-12.20161024git
- rebuild (qt5)

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> 0.2-11.20161024git
- release++

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> 0.2-10.20161024git.2
- branch rebuild (qt5)

* Mon Oct 24 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-10.20161024git
- Fix Gtk3 dialogs on wayland

* Mon Jul 18 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-9.20160718git
- Fix not working dialogs

* Sun Jul 17 2016 Rex Dieter <rdieter@fedoraproject.org> 0.2-8.20160621git
- rebuild (qt5-qtbase)

* Wed Jul 13 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-7.20160621git
- Remove runtime dependency on GDM

* Wed Jun 29 2016 Rex Dieter <rdieter@fedoraproject.org> 0.2-6.20160621git
- rebuild (qt5)

* Tue Jun 21 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-5.20160621git
- Don't fallback to gtk+ style

* Fri Jun 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-4.20160531git
- arch'd adwaita-qt5 runtime dep
- use system %%_qt5_version macro, instead of by-hand one here
- BR: qt5-qtbase-private-devel (helps track hard qt5-qtbase runtime dep)

* Fri Jun 10 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-3.20160531git
- rebuild (qt5-qtbase)

* Mon Jun 06 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-2.20160531git
- Add runtime dependency on adwaita-qt5 (bz#1332103)

* Tue May 31 2016 Jan Grulich <jgrulich@redhat.com> - 0.2-1.20160531git
- Update to latest git snapshot

* Wed Apr 20 2016 Jan Grulich <jgrulich@redhat.com> - 0.1-5
- Pull in upstream changes

* Wed Mar 16 2016 Jan Grulich <jgrulich@redhat.com> - 0.1-4
- Improve font size

* Thu Feb 25 2016 Jan Grulich <jgrulich@redhat.com> - 0.1-3
- Revert usage of qgnomeplatform.env in GDM

* Thu Feb 25 2016 Jan Grulich <jgrulich@redhat.com> - 0.1-2
- Install qgnomeplatform.env to gdm to automatically use it after we log in

* Tue Feb 16 2016 Jan Grulich <jgrulich@redhat.com> - 0.1-1
- First version
