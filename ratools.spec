Name:			ratools
Version:		0.5
Group:			Applications/Internet
Release:		2%{?dist}
Summary:		Framework for IPv6 Router Advertisements
License:		Apache License, Version 2.0
URL:			https://www.nonattached.net/ratools/index.html
Source:			https://github.com/danrl/ratools/archive/v0.5.tar.gz
Patch0:			ratools-0.5-LEVEL1_DCACHE.patch

%description
ratools is a fast, dynamic, multi-threading framework for creating, modifying
and sending IPv6 Router Advertisements (RA).

%prep
%setup -q
%patch0 -p1

%build
make -C src/ %{?_smp_mflags} rad
make -C src/ %{?_smp_mflags} ractl
make -C src/ %{?_smp_mflags} racomplete-ractl

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 751 bin/rad %{buildroot}%{_bindir}/rad
install -pm 751 bin/ractl %{buildroot}%{_bindir}/ractl

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
bin/racomplete-ractl > %{buildroot}%{_sysconfdir}/bash_completion.d/ractl

%files
%doc LICENSE README.md TODO.md
%{_bindir}/rad
%{_bindir}/ractl
%{_sysconfdir}/bash_completion.d/

%changelog
* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-2
- Add Patch for arm7hl

* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-1
- Initial packaging
