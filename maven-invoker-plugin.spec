Name:           maven-invoker-plugin
Version:        1.8
Release:        8%{?dist}
Summary:        Maven Invoker Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-invoker-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         pom-xml.patch

BuildArch: noarch

# Basic stuff
BuildRequires: jpackage-utils
BuildRequires: java-devel >= 1:1.6.0
# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-script-interpreter
BuildRequires: maven-invoker
BuildRequires: mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires: mvn(org.apache.maven.doxia:doxia-site-renderer)

# Others
BuildRequires: groovy

Provides:       maven2-plugin-invoker = 1:%{version}-%{release}
Obsoletes:      maven2-plugin-invoker <= 0:2.0.8

%description
The Maven Invoker Plugin is used to run a set of Maven projects. The plugin 
can determine whether each project execution is successful, and optionally 
can verify the output generated from a given project execution.
  

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%patch0

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.8-8
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 1.8-7
- Migrate away from mvn-rpmbuild (Resolves: #997508)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Apr  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-5
- Fix Requires and BuildRequires on Doxia; resolves: rhbz#950061
- Remove unneeded BR

* Sat Feb 16 2013 Michal Srb <msrb@redhat.com> - 1.8-4
- Migrate from maven-doxia to doxia subpackages (Resolves: #909238)
- Remove unnecessary BR on maven-doxia-tools

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 18 2013 Weinan Li <weli@redhat.com> 1.8-1
- Upgrade to 1.8

* Fri Jan 4 2013 David Xie <david.scriptfan@gmail.com> 1.7-2
- Add LICENSE and NOTICE files.

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 1.7-1
- Update to latest upstream.

* Tue Aug 21 2012 Tomas Radej <tradej@redhat.com> - 1.6-1
- Updated to v1.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 9 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5-5
- Build with maven 3.x.
- Use upstream source.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 Weinan Li <weli@redhat.com> -1.5-3
- R: maven-shared-invoker
- R: maven-shared-reporting-api
- R: maven-shared-reporting-impl
- Remove BR: maven2-plugin-changes
- Add BR: maven-shared-invoker

* Mon Jun 7 2010 Weinan Li <weli@redhat.com> - 1.5-2
- Fix incoherent version in changelog
- BR: maven-javadoc-plugin

* Thu Jun 3 2010 Weinan Li <weli@redhat.com> - 1.5-1
- Initial Package
