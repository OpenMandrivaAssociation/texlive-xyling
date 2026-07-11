%global tl_name xyling
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Draw syntactic trees, etc., for linguistics literature, using xy-pic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xyling
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The macros in this package model the construction of linguistic tree
structures as a genuinely graphical problem: they contain two types of
objects, BRANCHES and NODE LABELS, and these are positioned relative to
a GRID. It is essential that each of these three elements is constructed
independent of the other two, and hence they can be modified without
unwanted side effects. The macros are based on the xy-pic package.

