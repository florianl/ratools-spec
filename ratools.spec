%global _hardened_build 1

Name:			ratools
Version:		0.5
Release:		3%{?dist}
Summary:		Framework for IPv6 Router Advertisements
License:		ASL 2.0
URL:			https://www.nonattached.net/ratools
Source0:		https://github.com/danrl/ratools/archive/v%{version}.tar.gz
# Patch to run on arm7hl has applied to upstream
# https://github.com/danrl/ratools/commit/97b19489debc342c81b19337875765f098cf5543
Patch0:			ratools-0.5-LEVEL1_DCACHE.patch

%description
ratools is a fast, dynamic, multi-threading framework for creating, modifying
and sending IPv6 Router Advertisements (RA).

%prep
%setup -q
%patch0 -p1

%build
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
%config %{_sysconfdir}/bash_completion.d/*

%changelog
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

* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-2
- Add Patch for arm7hl

* Fri May 23 2014 Florian Lehner <dev@der-flo.net> 0.5-1
- Initial packaging
