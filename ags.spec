Summary:	Engine for running games developed with AGS (Adventure Game Studio)
Name:		ags
Version:	3.6.0.9
%if ! 0%{?git}
Release:	2
Source0:	https://github.com/adventuregamestudio/ags/archive/v.%{version}.tar.gz
%else
Release:	1.%git.1
Source0:	%{name}-%{git}.tar.xz
%endif
#Patch1:		ags-3.5.0.24-compile.patch
License:	Artistic 2.0
Group:		Games/Adventure
Url:		http://github.com/adventuregamestudio
BuildRequires:	make
BuildRequires:	pkgconfig(allegro)
BuildRequires:	dumb-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	SDL2_sound-devel

%description
Engine for running games developed with AGS (Adventure Game Studio)

%files
%{_bindir}/ags

#----------------------------------------------------------------------------

%prep
%if 0%{?git}
%autosetup -p1 -n %{name}-%{git}
%else
%autosetup -p1 -n ags-v.%{version}
%endif

%build
# Force clang -- gcc 6.x miscompiles ags
make -C Engine CC=clang CXX=clang++

%install
mkdir -p %{buildroot}%{_bindir}
make -C Engine install PREFIX=%{buildroot}%{_prefix}
