%global tl_name quotmark
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Consistent quote marks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quotmark
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quotmark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quotmark.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quotmark.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a means of ensuring consistent quote marks
throughout your document. The style can be changed either via package
option or command, and the package detects language selections (from the
babel or ngerman packages), and uses the punctuation marks appropriate
for the current language. The author now considers the package obsolete,
and recommends use of csquotes in its place.

