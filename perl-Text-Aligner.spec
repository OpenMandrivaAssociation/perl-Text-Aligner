%define upstream_name    Text-Aligner
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


