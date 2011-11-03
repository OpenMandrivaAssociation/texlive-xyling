# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xyling
# catalog-date 2007-03-13 09:23:19 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-xyling
Version:	1.1
Release:	1
Summary:	Draw syntactic trees, etc., for linguistics literature, using xy-pic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xyling
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The macros in this package model the construction of linguistic
tree structures as a genuinely graphical problem: they contain
two types of objects, BRANCHES and NODE LABELS, and these are
positioned relative to a GRID. It is essential that each of
these three elements is constructed independent of the other
two, and hence they can be modified without unwanted side
effects. The macros are based on the xy-pic package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xyling/xyling.sty
%doc %{_texmfdistdir}/doc/latex/xyling/README
%doc %{_texmfdistdir}/doc/latex/xyling/xyli-doc.pdf
%doc %{_texmfdistdir}/doc/latex/xyling/xyli-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
