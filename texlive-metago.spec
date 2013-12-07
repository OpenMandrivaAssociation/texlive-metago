# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/metago
# catalog-date 2008-09-08 11:32:46 +0200
# catalog-license lppl
# catalog-version 0.9
Name:		texlive-metago
Version:	0.9
Release:	5
Summary:	MetaPost output of Go positions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metago
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metago.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metago.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9-2
+ Revision: 753856
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9-1
+ Revision: 718995
- texlive-metago
- texlive-metago
- texlive-metago
- texlive-metago

