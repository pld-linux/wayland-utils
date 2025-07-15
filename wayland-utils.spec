Summary:	wayland-info utility
Summary(pl.UTF-8):	Narzędzie wayland-info
Name:		wayland-utils
Version:	1.2.0
Release:	1
License:	MIT
Group:		Applications
#Source0Download: https://wayland.freedesktop.org/releases.html
Source0:	https://gitlab.freedesktop.org/wayland/wayland-utils/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	736dbcefc534407d4e774087726844a1
URL:		https://wayland.freedesktop.org/
BuildRequires:	libdrm-devel >= 2.4.109
BuildRequires:	meson >= 0.47
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.20.0
BuildRequires:	wayland-protocols >= 1.24
BuildRequires:	xz
Requires:	libdrm >= 2.4.109
Requires:	wayland >= 1.20.0
Obsoletes:	wayland-info <= 0.0.1-0.20211213.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wayland-info is a utility for displaying information about the Wayland
protocols supported by a Wayland compositor.

%description -l pl.UTF-8
wayland-info to narzędzie do wyświetlania informacji o protokołach
Wayland obsługiwanych przez kompozytora Wayland.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_bindir}/wayland-info
%{_mandir}/man1/wayland-info.1*
