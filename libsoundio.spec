Name:           libsoundio
Version:        2.0.0
Release:        1%{?dist}
Summary:        C library for cross-platform real-time audio input and output
License:        MIT
URL:            http://libsound.io/

Source0:        https://github.com/andrewrk/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	cmake3
BuildRequires:	gcc
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)

%description
C library providing cross-platform audio input and output. The API is suitable
for real-time software such as digital audio workstations as well as consumer
software such as music players.

This library is an abstraction; however in the delicate balance between
performance and power, and API convenience, the scale is tipped closer to the
former. Features that only exist in some sound backends are exposed.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%cmake3 \
   -DBUILD_STATIC_LIBS=OFF
%make_build

%install
%make_install

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc README.md
%{_bindir}/sio_list_devices
%{_bindir}/sio_microphone
%{_bindir}/sio_record
%{_bindir}/sio_sine
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sat Jan 11 2020 Simone Caronni <negativo17@gmail.com> - 2.0.0-1
- First build.

