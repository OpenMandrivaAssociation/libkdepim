%define major 5
%define libname %mklibname KF5Libkdepim %{major}
%define devname %mklibname KF5Libkdepim -d

Name: libkdepim
Epoch: 3
Version:	23.08.5
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	2
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for PIM handling
URL: https://kde.org/
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
BuildRequires: cmake(KPim5Akonadi)
BuildRequires: cmake(KPim5AkonadiSearch)
BuildRequires: cmake(KPim5AkonadiMime)
BuildRequires: cmake(KPim5Mime)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KPim5Ldap)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KPim5AkonadiContact)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5CalendarCore)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

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
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkdepim

%files -f libkdepim.lang
%{_datadir}/qlogging-categories5/libkdepim.categories
%{_datadir}/qlogging-categories5/libkdepim.renamecategories
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_libdir}/qt5/plugins/designer/kdepim5widgets.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{tags,qch}
