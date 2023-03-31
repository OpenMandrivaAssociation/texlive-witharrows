Name:		texlive-witharrows
Version:	63087
Release:	2
Summary:	"Aligned" math environments with arrows for comments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/witharrows
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/witharrows.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/witharrows.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/witharrows.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an environment WithArrows which is
similar to the environment aligned of amsmath (and mathtools),
but gives the possibility to draw arrows on the right side of
the alignment. These arrows are usually used to give
explanations concerning the mathematical calculus presented.
The package requires the following other LaTeX packages: expl3,
footnote, l3keys2e, tikz, and xparse.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/witharrows
%{_texmfdistdir}/tex/generic/witharrows
%doc %{_texmfdistdir}/doc/generic/witharrows

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
