#
# Possible TODO: split mace2 ?
#
# Conditional build:
%bcond_with	tests		# build with tests
#
Summary:	Theorem Prover
Summary(pl):	Narzêdzie do dowodzenia twierdzeñ
Name:		otter
Version:	3.3f
Release:	1
License:	Public Domain (see Legal)
Group:		Applications/Science
Source0:	http://www-unix.mcs.anl.gov/AR/otter/dist33/%{name}-%{version}.tar.gz
# Source0-md5:	795711b307cc1316e08d3d4f46c998c9
URL:		http://www-unix.mcs.anl.gov/AR/otter/dist33/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Otter is designed to prove theorems stated in first-order logic with
equality. Otter's inference rules are based on resolution and
paramodulation, and it includes facilities for term rewriting, term
orderings, Knuth-Bendix completion, weighting, and strategies for
directing and restricting searches for proofs. Otter can also be used
as a symbolic calculator and has an embedded equational programming
system. Otter is a fourth-generation Argonne National Laboratory
deduction system whose ancestors (dating from the early 1960s) include
the TP series, NIUTP, AURA, and ITP.

Currently, the main application of Otter is research in abstract
algebra and formal logic. Otter and its predecessors have been used to
answer many open questions in the areas of finite semigroups, ternary
Boolean algebra, logic calculi, combinatory logic, group theory,
lattice theory, and algebraic geometry.

%description -l pl
Otter jest zaprojektowany do dowodzenia twierdzeñ wyra¿onych w logice
pierwszego rzêdu z równo¶ciami. Regu³y wnioskowania Ottera s± oparte
na rozwi±zywaniu i paramodulacji; zawieraj± u³atwienia do
przepisywania warunków, porz±dkowania warunków, dope³nienia
Knutha-Bendiksa, wa¿enia oraz strategie kierunkowania i ograniczania
wyszukiwania dowodów. Otter mo¿e byæ tak¿e u¿ywany jako kalkulator
symboliczny i posiada wbudowany system programowania równañ. Otter to
system dedukcji Argonne National Laboratory czwartej generacji,
którego przodkowie (pocz±wszy od wczesnych lat 1960-tych) obejmowa³y
seriê TP, NIUTP, AURA i ITP.

Aktualnie g³ówna aplikacja Ottera to praca badawcza dotycz±ca
abstrakcyjnej algebry i logiki formalnej. Otter i jego poprzedniki
by³y u¿ywane do odpowiadania na wiele pytañ w zakresie pó³grup
skoñczonych, trójkowej algebry boolowskiej, rachunków logicznych,
logiki kombinatorycznej, teorii grup, teorii krat oraz geometrii
algebraicznej.

%package doc
Summary:	Otter and Mace documentation
Summary(pl):	Dokumentacja do programów Otter i Mace
Group:		Documentation

%description doc
PDF documentation for Otter and Mace theorem proving programs.

%description doc -l pl
Dokumentacja w formacie PDF do programów Otter i Mace s³u¿±cych do
dowodzenia twierdzeñ.

%package examples
Summary:	Otter and Mace examples
Summary(pl):	Przyk³ady do programów Otter i Mace
Group:		Documentation

%description examples
Example proofs for Otter and Mace theorem proving programs.

%description examples -l pl
Przyk³adowe dowody do programów Otter i Mace s³u¿±cych do
dowodzenia twierdzeñ.

%prep
%setup -q

%build
%{__make} -C source all \
	CC="%{__cc}"

%{__make} -C mace2 all \
	CC="%{__cc}"

%if %{with tests}
%{__make} test-mace
%{__make} test-otter
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}}

install bin-Linux/* $RPM_BUILD_ROOT%{_bindir}
cp -rf examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -rf examples-mace2 $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Legal Changelog
%attr(755,root,root) %{_bindir}/*

%files doc
%defattr(644,root,root,755)
%doc documents/*.pdf

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
