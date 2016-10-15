%define git 0

Summary:	Engine for running games developed with AGS (Adventure Game Studio)
Name:		ags
Version:	3.4.1
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	1
Source0:	https://github.com/adventuregamestudio/ags/archive/v.%{version}.tar.gz
%endif
License:	Artistic 2.0
Group:		Games/Adventure
Url:		http://github.com/adventuregamestudio
BuildRequires:	make
BuildRequires:	pkgconfig(allegro)
BuildRequires:	dumb-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)

%description
Engine for running games developed with AGS (Adventure Game Studio)

%files
%{_bindir}/ags

#----------------------------------------------------------------------------

%prep
%if %git
%setup -q -n %{name}-%{git}
%else
%setup -qn ags-v.%{version}
%endif
%apply_patches

%build
# Force clang -- gcc 6.x miscompiles ags
make -C Engine CC=clang CXX=clang++

%install
mkdir -p %{buildroot}%{_bindir}
make -C Engine install PREFIX=%{buildroot}%{_prefix}
