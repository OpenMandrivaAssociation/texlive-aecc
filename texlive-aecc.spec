# revision 28574
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-aecc
Version:	20131013
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
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccr10.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccr5.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccr6.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccr7.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccr8.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccr9.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/aecc/aeccti10.tfm
%{_texmfdistdir}/fonts/vf/public/aecc/aeccr10.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccr5.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccr6.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccr7.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccr8.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccr9.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccsc10.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccsl10.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccsl9.vf
%{_texmfdistdir}/fonts/vf/public/aecc/aeccti10.vf
%{_texmfdistdir}/tex/latex/aecc/aecc.sty
%{_texmfdistdir}/tex/latex/aecc/t1aeccr.fd
%doc %{_texmfdistdir}/doc/fonts/aecc/COPYING
%doc %{_texmfdistdir}/doc/fonts/aecc/MANIFEST
%doc %{_texmfdistdir}/doc/fonts/aecc/README
%doc %{_texmfdistdir}/doc/fonts/aecc/aeccfonts.tex
%doc %{_texmfdistdir}/doc/fonts/aecc/aefonts.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aehax5.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aehaxit.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aehaxrm.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aehaxsc.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aehaxsl.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aehaxss.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aelatin.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aelatint.mtx
%doc %{_texmfdistdir}/doc/fonts/aecc/aesample.tex
%doc %{_texmfdistdir}/doc/fonts/aecc/aet1.etx
%doc %{_texmfdistdir}/doc/fonts/aecc/bxittest.tex
%doc %{_texmfdistdir}/doc/fonts/aecc/clean
%doc %{_texmfdistdir}/doc/fonts/aecc/germtest.tex
%doc %{_texmfdistdir}/doc/fonts/aecc/go
%doc %{_texmfdistdir}/doc/fonts/aecc/install
%doc %{_texmfdistdir}/doc/fonts/aecc/makepl
%doc %{_texmfdistdir}/doc/fonts/aecc/ot1tt.etx
%doc %{_texmfdistdir}/doc/fonts/aecc/slitest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
