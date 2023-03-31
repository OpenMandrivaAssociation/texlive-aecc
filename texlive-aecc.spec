Name:		texlive-aecc
Version:	1.0
Release:	3
Summary:	TeXLive aecc package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aecc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aecc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive aecc package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/aecc
%{_texmfdistdir}/fonts/vf/public/aecc
%{_texmfdistdir}/tex/latex/aecc
%doc %{_texmfdistdir}/doc/fonts/aecc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
