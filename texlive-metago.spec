%global tl_name metago
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	MetaPost output of Go positions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metago
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metago.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metago.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows you to draw Go game positions with MetaPost. Two
methods of usage are provided, either using the package
programmatically, or using the package via a script (which may produce
several images).

