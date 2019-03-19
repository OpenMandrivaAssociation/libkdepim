%define major 5
%define libname %mklibname KF5Libkdepim %{major}
%define devname %mklibname KF5Libkdepim -d

Name: libkdepim
Epoch: 3
Version:  18.12.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release: 2
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for PIM handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5DBus)
%if %mdvver < 3000001
BuildRequires: cmake(Qt5Network)
%endif
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5UiPlugin)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5Designer)
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5AkonadiSearch)
BuildRequires: cmake(KF5AkonadiMime)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Ldap)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5AkonadiContact)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5CalendarCore)

%description
KDE library for PIM handling.

%package -n %{libname}
Summary: KDE library for PIM handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for PIM handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkdepim

%files -f libkdepim.lang
%{_sysconfdir}/xdg/libkdepim.categories
%{_sysconfdir}/xdg/libkdepim.renamecategories
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_datadir}/kdepimwidgets
%{_datadir}/kservices5/kcmldap.desktop
%{_libdir}/qt5/plugins/designer/kdepimwidgets.so
%{_libdir}/qt5/plugins/designer/kdepimakonadiwidgets.so
%{_libdir}/qt5/plugins/kcm_ldap.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
