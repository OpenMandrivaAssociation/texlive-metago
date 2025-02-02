Name:		texlive-metago
Version:	15878
Release:	2
Summary:	MetaPost output of Go positions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metago
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metago.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metago.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to draw Go game positions with MetaPost.
Two methods of usage are provided, either using the package
programmatically, or using the package via a script (which may
produce several images).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/metago/metago.mp
%doc %{_texmfdistdir}/doc/metapost/metago/README
%doc %{_texmfdistdir}/doc/metapost/metago/example-program.mp
%doc %{_texmfdistdir}/doc/metapost/metago/example-program.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-1.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-2.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-3.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-4.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-5.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-6.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-7.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script-8.pdf
%doc %{_texmfdistdir}/doc/metapost/metago/example-script.mp
%doc %{_texmfdistdir}/doc/metapost/metago/script.go

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
