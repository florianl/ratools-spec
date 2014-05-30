%global _hardened_build 1

Name:			ratools
Version:		0.5.2
Release:		1%{?dist}
Summary:		Framework for IPv6 Router Advertisements
License:		ASL 2.0
URL:			https://www.nonattached.net/ratools
Source0:		https://github.com/danrl/ratools/archive/v%{version}.tar.gz

%description
ratools is a fast, dynamic, multi-threading framework for creating, modifying
and sending IPv6 Router Advertisements (RA).

%prep
%setup -q

%build
CFLAGS="%{?optflags}"				\
LDFLAGS="%{?__global_ldflags}"		\
make -C src/

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/rad %{buildroot}%{_bindir}/rad
install -pm 0755 bin/ractl %{buildroot}%{_bindir}/ractl

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/*
install -pm 0644 bash-completion.d/ractl.sh %{buildroot}%{_sysconfdir}/bash_completion.d/ractl

%files
%doc LICENSE README.md TODO.md config.example
%{_bindir}/rad
%{_bindir}/ractl
 %config %{_sysconfdir}/bash_completion.d/ractl

%changelog
* Fri May 30 2014 Florian Lehner <dev@der-flo.net> 0.5.2-1
- Update to new version

* Mon May 26 2014 Florian Lehner <dev@der-flo.net> 0.5-3
- Set permissions on files properly
- Correct misspelling of the license
- Don't let the package own a directory of another package
- Add missing 'config.example' to docs-section
- Rename Source to Source0
- Use macro in Source0-URL
- Remove index.html from URL
- Remove Group-tag
- Add information about Patch0
- Add _hardend_build
- Fix issue on installing bash_completion.d
- Add CFLAGS and LDFLAGS options in front of make
- Use noreplace

* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-2
- Add Patch for arm7hl

* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-1
- Initial packaging
