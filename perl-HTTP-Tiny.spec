Name:           perl-HTTP-Tiny
Version:        0.076
Release:        1%{?dist}
Summary:        Small, simple, correct HTTP/1.1 client
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTTP-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/HTTP-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Socket)
# IO::Socket::IP 0.32 is optional
# IO::Socket::SSL 1.56 is optional
BuildRequires:  perl(MIME::Base64)
# Mozilla::CA is optional
# Net::SSLeay 1.49 is an optional fall-back for IO::Socket::SSL
BuildRequires:  perl(Socket)
BuildRequires:  perl(Time::Local)
# Tests:
# Data::Dumper not used
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename) 
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::INET)
# IO::Socket::SSL 1.56 not needed
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Carp)
Requires:       perl(Fcntl)
Recommends:     perl(IO::Socket::IP) >= 0.32
Recommends:     perl(IO::Socket::SSL) >= 1.56
Requires:       perl(MIME::Base64)
Recommends:     perl(Mozilla::CA)
Requires:       perl(Time::Local)

%description
This is a very simple HTTP/1.1 client, designed for doing simple GET requests
without the overhead of a large framework like LWP::UserAgent.

It is more correct and more complete than HTTP::Lite. It supports proxies
(currently only non-authenticating ones) and redirection. It also correctly
resumes after EINTR.

%prep
%setup -q -n HTTP-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR='%{buildroot}'

%check
make test

%files
%doc LICENSE Changes CONTRIBUTING.mkdn eg README
%{perl_vendorlib}/*
%{_mandir}/man3/*
