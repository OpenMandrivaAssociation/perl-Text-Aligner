%define upstream_name    Text-Aligner
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A single function to justify strings to various alignment styles
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Aligner-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Text::Aligner exports a single function, align(), which is used to justify
strings to various alignment styles. The alignment specification is the
first argument, followed by any number of scalars which are subject to
alignment.

The operation depends on context. In list context, a list of the justified
scalars is returned. In scalar context, the justified arguments are joined
into a single string with newlines appended. The original arguments remain
unchanged. In void context, in-place justification is attempted. In this
case, all arguments must be lvalues.

Align() also does one level of scalar dereferencing. That is, whenever one
of the arguments is a scalar reference, the scalar pointed to is aligned
instead. Other references are simply stringified. An undefined argument is
interpreted as an empty string without complaint.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 657850
- rebuild for updated spec-helper

* Sun Sep 19 2010 Shlomi Fish <shlomif@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 579811
- import perl-Text-Aligner


