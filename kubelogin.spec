%define debug_package %{nil}
%define gopkg github.com/int128

Name: kubelogin
Version: 1.17.1
Release: 1%{?dist}
BuildArch: x86_64
Summary: kubectl plugin for Kubernetes OpenID Connect authentication
License: Apache-2.0
URL: https://%{gopkg}/%{name}
Requires: kubernetes-client

Source0: https://%{gopkg}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: golang >= 1.12
BuildRequires: git

%description
This is a kubectl plugin for Kubernetes OpenID Connect (OIDC)
authentication, also known as kubectl oidc-login.

This is designed to run as a client-go credential plugin. When you run
kubectl, kubelogin opens the browser and you can log in to the
provider. Then kubelogin gets a token from the provider and kubectl
access Kubernetes APIs with the token.

%prep
%setup

mkdir -p src/%{gopkg}
mv $(ls | grep -v "^src$") src/%{gopkg}/.

%build
pushd src/%{gopkg}
make

%install
pushd src/%{gopkg}

BIN_DIR=%{buildroot}/usr/bin
mkdir -p ${BIN_DIR}
cp kubelogin ${BIN_DIR}/kubectl-oidc_login

popd

mv src/%{gopkg}/*.md .
mv src/%{gopkg}/LICENSE .

%files
%license LICENSE
%doc *.md
/usr/bin/*
