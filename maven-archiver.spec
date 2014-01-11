%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-archiver
Version:        2.5
Release:        8.1%{?dist}
Epoch:          0
Summary:        Maven Archiver
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-archiver/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-shared-jar
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-archiver >= 2.1-1
BuildRequires:  plexus-utils
BuildRequires:  apache-commons-parent

Provides:       maven-shared-archiver = %{version}-%{release}
Obsoletes:      maven-shared-archiver < %{version}-%{release}

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%pom_add_dep org.apache.maven:maven-core
# tests don't compile with maven 2.2.1
rm -fr src/test/java/org/apache/maven/archiver/*.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-7
- Build with xmvn

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-6
- Add missing license files

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:2.5-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.5-2
- Add versioned BR/R on plexus-archiver and rebuild

* Wed Feb 15 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.5-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 6 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.2-1
- Update to 2.4.2 upstream release.

* Mon Sep 19 2011 Tomas Radej <tradej@redhat.com> - 0:2.4.1-7
- Fixed dep on maven-core artifact
- Minor fixes

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-6
- Build with maven 3.x.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-4
- Add missing BR.

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-3
- Remove tests as they don't compile.

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-2
- BR java-devel >= 1:1.6.0.

* Sat May 29 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-1
- Update to 2.4.1.

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.4-1
- Update to 2.4.

* Mon Dec 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-3
- BR maven-surefire-provider-junit.

* Mon Aug 31 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-2
- Fix line length.
- Own only specific fragment and pom.

* Wed May 20 2009 Fernando Nasser <fnasser@redhat.com> 0:2.2-1
- Fix license
- Update instructions to obtain sources
- Refresh source tar ball

* Thu Jul 26 2007 Deepak Bhole <dbhole@redhat.com> 0:2.2-0jpp.1
- Initial build
