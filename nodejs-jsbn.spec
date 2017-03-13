%{?scl:%scl_package nodejs-jsbn}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name jsbn

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    0.1.0
Release:    2%{?dist}
Summary:    The jsbn library is a fast, portable implementation of large-number math in pure JavaScript, enabling public-key crypto and other applications on desktop and mobile browsers
License:    BSD
URL:        https://github.com/andyperlitch/jsbn.git
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
The jsbn library is a fast, portable implementation of large-number math in pure JavaScript, enabling public-key crypto and other applications on desktop and mobile browsers.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr example.html example.js index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.0-2
- Initial packaging

