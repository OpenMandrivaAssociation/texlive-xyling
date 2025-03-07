Name:		texlive-xyling
Version:	15878
Release:	2
Summary:	Draw syntactic trees, etc., for linguistics literature, using xy-pic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xyling
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros in this package model the construction of linguistic
tree structures as a genuinely graphical problem: they contain
two types of objects, BRANCHES and NODE LABELS, and these are
positioned relative to a GRID. It is essential that each of
these three elements is constructed independent of the other
two, and hence they can be modified without unwanted side
effects. The macros are based on the xy-pic package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xyling/xyling.sty
%doc %{_texmfdistdir}/doc/latex/xyling/README
%doc %{_texmfdistdir}/doc/latex/xyling/xyli-doc.pdf
%doc %{_texmfdistdir}/doc/latex/xyling/xyli-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
