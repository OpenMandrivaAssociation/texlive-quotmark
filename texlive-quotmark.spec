Name:		texlive-quotmark
Version:	15878
Release:	2
Summary:	Consistent quote marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quotmark
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotmark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotmark.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotmark.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of ensuring consistent quote marks
throughout your document. The style can be changed either via
package option or command. The package detects if babel or
ngerman have been loaded, and will use the punctuation marks
appropriate for the current language.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/quotmark/quotmark-UKenglish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-USenglish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-afrikaans.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-brazil.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-bulgarian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-catalan.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-croatian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-czech.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-danish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-dutch.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-estonian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-finnish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-frenchb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-germanb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-greek.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-hebrew.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-icelandic.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-irish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-italian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-magyar.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-ngermanb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-norsk.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-polish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-portuges.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-romanian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-russianb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-serbian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-slovak.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-slovene.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-sorbian.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-spanish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-swedish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-swiss.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-turkish.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-ukraineb.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark-welsh.def
%{_texmfdistdir}/tex/latex/quotmark/quotmark.sty
%doc %{_texmfdistdir}/doc/latex/quotmark/CHANGES
%doc %{_texmfdistdir}/doc/latex/quotmark/README
%doc %{_texmfdistdir}/doc/latex/quotmark/quotmark.pdf
%doc %{_texmfdistdir}/doc/latex/quotmark/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/quotmark/quotmark.dtx
%doc %{_texmfdistdir}/source/latex/quotmark/quotmark.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
