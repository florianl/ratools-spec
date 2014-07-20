%global _hardened_build 1

Name:			ratools
Version:		0.5.3
Release:		3%{?dist}
Summary:		Framework for IPv6 Router Advertisements
License:		ASL 2.0
URL:			https://www.nonattached.net/ratools
Source0:		https://github.com/danrl/ratools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd

%description
Ratools is a fast, dynamic, multi-threading framework for creating, modifying
and sending IPv6 Router Advertisements (RA).

%prep
%setup -q

%build
CFLAGS="%{?optflags}"				\
LDFLAGS="%{?__global_ldflags}"		\
%{__make} %{?_smp_mflags} -C src/

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -pm 0755 bin/rad %{buildroot}%{_bindir}/rad
%{__install} -pm 0755 bin/ractl %{buildroot}%{_bindir}/ractl

%{__mkdir_p} %{buildroot}%{_sysconfdir}/bash_completion.d/*
%{__install} -pm 0644 bash-completion.d/ractl.sh %{buildroot}%{_sysconfdir}/bash_completion.d/ractl

%{__mkdir_p} %{buildroot}%{_mandir}/man8
%{__install} -pm 0644 man/*.8 %{buildroot}%{_mandir}/man8

%{__mkdir_p} %{buildroot}%{_unitdir}
%{__install} -pm 0644 systemd/ratools-rad.service %{buildroot}%{_unitdir}/ratools-rad.service
%{__install} -pm 0644 systemd/ratools-rad.socket %{buildroot}%{_unitdir}/ratools-rad.socket

%post
%systemd_post ratools-rad.service

%preun
%systemd_preun ratools-rad.service

%postun
%systemd_postun_with_restart ratools-rad.service

%files
%doc LICENSE README.md TODO.md example.conf
%{_bindir}/rad
%{_bindir}/ractl
# Setting (noreplace) for the bash-completion is a bad idea,
# since this file is NOT config as meant to be customized by the user.
# https://bugzilla.redhat.com/show_bug.cgi?id=1100899#c6
%config %{_sysconfdir}/bash_completion.d/ractl
%{_mandir}/man8/*.8*
%{_unitdir}/ratools-rad.service
%{_unitdir}/ratools-rad.socket

%changelog
* Sun Jul 20 2014 Florian Lehner <dev@der-flo.net> - 0.5.3-3
- Replace mkdir and install with its macro

* Wed Jun 18 2014 Florian Lehner <dev@der-flo.net> - 0.5.3-2
- Use macroized scriptlets for systemd

* Mon Jun 16 2014 Florian Lehner <dev@der-flo.net> - 0.5.3-1
- Move ractl.8-manpage from section 1 to section 8
- Add rad.8-manpage
- Add Systemd files
- Move config.example to example.conf

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Florian Lehner <dev@der-flo.net> 0.5.2-3
- add manpage

* Sat May 31 2014 Florian Lehner <dev@der-flo.net> 0.5.2-2
- Add comment about not using noreplace
- Rename Source0 after downloading

* Fri May 30 2014 Florian Lehner <dev@der-flo.net> 0.5.2-1
- Update to new version
- Use smp_mflags while make

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
- Initial packaging (#1100899)
