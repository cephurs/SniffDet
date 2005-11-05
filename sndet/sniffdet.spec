# $Id$

%define with_devel 1

Name: sniffdet
Summary: Remote sniffers detector for TCP/IP networks
Summary(pt_BR): Detector de sniffers remoto para redes TCP/IP
Version: 0.9
Release: 1ade
License: GPL
Group: Networking
Group(pt_BR): Rede
Group(es): Red
URL: http://sniffdet.sourceforge.net
Source0: sniffdet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libpcap-devel libnet-devel

%description
Sniffdet is an OpenSource implementation of a set of tests for
remote sniffers detection in TCP/IP network environments. It's
composed by a flexible and easy to use library plus
an application to run the tests.

%description -l pt_BR
Sniffdet � uma implementa��o aberta de um conjunto de testes
para detec��o remota de sniffers em redes TCP/IP. O Pacote � 
composto por uma biblioteca flex�vel e simples de usar al�m 
de uma aplica��o para execu��o dos testes.

%if %{with_devel}
%package devel
Summary: Development environment for sniffdet
Summary(pt_BR): Ambiente de desenvolvimento para sniffdet
Group: Development
Group(pt_BR): Desenvolvimento
PreReq: %{name} = %{version}-%{release}

%description devel
This package contains the sniffdet library, headers and manpages
necessary to developers who want to use the sniffdet API.
Notice that by now the sniffdet project provides only the static library.
The dynamic version will be created in 1.0 release.

%description -l pt_BR devel
Este pacote cont�m a biblioteca sniffdet, arquivos de inclus�o e
p�ginas man neces�rias a desenvolvedores que desejam utilizar a API do
sniffdet.

Note que at� o momento apenas a vers�o est�tica da biblioteca est� sendo
disponibilizada. A biblioteca din�mica ser� criada no lan�amento da
vers�o 1.0.
%endif

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	--bindir=%{_bindir} --sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} --includedir=%{_includedir} \
	--libdir=%{_libdir} --mandir=%{_mandir}

# parallel make is broken
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/RESOURCES doc/howitworks.txt
%doc CHANGES README BUGS TODO COPYING
%{_sbindir}/sniffdet
%dir %{_libdir}/sniffdet/plugins
%{_libdir}/sniffdet/plugins/*.so
%{_sysconfdir}/sniffdet.conf
%{_mandir}/man1/sniffdet.1*
%{_mandir}/man5/sniffdet.conf.5*

%if %{with_devel}
%files devel
%defattr(-,root,root,-)
%doc doc/*.c
%{_libdir}/libsniffdet.a
%{_includedir}/libsniffdet.h
%{_mandir}/man3/libsniffdet.3*
%endif

%changelog
* Fri Jul 04 2003 Ademar de Souza Reis Jr. <ademar@conectiva.com.br>
+ sniffdet-0.9-1ade
- New version packaged
- Added doc files

* Sun Jan 12 2003 Ademar de Souza Reis Jr. <ademar@conectiva.com.br>
+ sniffdet-0.8-1
- New version packaged

* Fri Dec 06 2002 Ademar de Souza Reis Jr. <ademar@conectiva.com.br>
+ sniffdet-0.7-2
- Disabled parallel make (it's b0rken)

* Mon Jun 24 2002 Ademar de Souza Reis Jr. <ademar@conectiva.com.br>
+ sniffdet-0.7-1
- package creation
