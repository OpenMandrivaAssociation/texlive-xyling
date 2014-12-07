# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xyling
# catalog-date 2007-03-13 09:23:19 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-xyling
Version:	1.1
Release:	9
Summary:	Draw syntactic trees, etc., for linguistics literature, using xy-pic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xyling
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xyling.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 757725
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719955
- texlive-xyling
- texlive-xyling
- texlive-xyling

