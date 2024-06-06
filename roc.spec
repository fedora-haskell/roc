%global forgeurl https://github.com/roc-lang/roc
%global version0 0.0.1
%global commit c75f3ccd6c6b42005e5fc1fff3363ba91410e138
%forgemeta

%bcond release 1

Name:           roc
Version:        %{forgeversion}
Release:        0.1%{?dist}
Summary:        A fast, friendly, functional language

License:        UPL-1.0
URL:            https://www.roc-lang.org
Source0:        %{forgesource}

BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
#BuildRequires:  lld16
BuildRequires:  llvm16-devel
BuildRequires:  rust
BuildRequires:  zig > 0.11
#BuildRequires:  zig-srpm-macros
BuildRequires:  zlib-devel
#ExclusiveArch:  %%{zig_arches}
ExclusiveArch:  x86_64 aarch64

%description
A general functional programming inspired from Elm


%prep
%forgesetup


%build
env LLVM_SYS_160_PREFIX=%{_libdir}/llvm16 cargo build %{?with_release:--release}


%install
mkdir -p %{buildroot}%{_bindir}
cp -p target/%{?with_release:release}%{!?with_release:debug}/{roc,roc-docs,roc_language_server,roc_wasm_interp} %{buildroot}%{_bindir}


%files
%license LICENSE
%doc examples
%{_bindir}/roc*


%changelog
* Tue Apr 16 2024 Jens Petersen <petersen@redhat.com> - 0.0.1-1
- initial package
