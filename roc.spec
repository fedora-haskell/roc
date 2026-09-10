%global debug_package %{nil}

%global forgeurl https://github.com/roc-lang/roc
%global version0 0.0.1
%global commit cd0ecc57bdc3ee1ca89235b4dfcd4e7d4a523116
%forgemeta

%bcond release 1

Name:           roc
Version:        %{forgeversion}
Release:        0.1%{?dist}
Summary:        A fast, friendly, functional language

License:        UPL-1.0
URL:            https://www.roc-lang.org
Source0:        %{forgesource}

#BuildRequires:  gcc-c++
#BuildRequires:  libffi-devel
BuildRequires:  zig > 0.16
BuildRequires:  zig-srpm-macros
BuildRequires:  zlib-devel
ExclusiveArch:  %{zig_arches}
#ExclusiveArch:  x86_64 aarch64

%description
A general functional programming inspired from Elm


%prep
%forgesetup


%build
zig build roc


%install
mkdir -p %{buildroot}%{_bindir}
cp -p zig-out/bin/roc %{buildroot}%{_bindir}


%files
%license LICENSE legal_details
%doc README.md examples
%{_bindir}/roc*


%changelog
* Thu Sep 10 2026 Jens Petersen <petersen@redhat.com> - 0.0.1^20260910gitcd0ecc5-0.1
- update to latest snapshot: now uses zig

* Tue Apr 16 2024 Jens Petersen <petersen@redhat.com> - 0.0.1-1
- initial package
