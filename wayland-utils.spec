Summary:	wayland-info utility
Summary(pl.UTF-8):	Narzędzie wayland-info
Name:		wayland-utils
Version:	1.0.0
Release:	1
License:	MIT
Group:		Applications
#Source0Download: https://wayland.freedesktop.org/releases.html
Source0:	https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	714875aefb10e7f683cde24e58d033ad
URL:		https://wayland.freedesktop.org/
BuildRequires:	meson >= 0.47
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	wayland-devel >= 1.17.0
Requires:	wayland >= 1.17.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_bindir}/wayland-info
%{_mandir}/man1/wayland-info.1*
