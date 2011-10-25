# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           maven-archiver
Version:        2.4.1
Release:        5
Summary:        Maven Archiver
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/

# svn export https://svn.apache.org/repos/asf/maven/shared/tags/maven-archiver-2.4.1 maven-archiver
# tar caf maven-archiver-2.4.1-src.tar.xz maven-archiver/
Source0:        %{name}-%{version}-src.tar.xz
Source1:        %{name}-depmap.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-shared-jar
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-archiver >= 1.0-0.1.a7
BuildRequires:  plexus-utils
BuildRequires:  apache-commons-parent

Requires:       maven2 >= 0:2.0.4-9
Requires:       plexus-archiver >= 1.0-0.1.a7
Requires:       plexus-interpolation
Requires:       plexus-utils

Requires(post):   jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
Provides: maven-shared-archiver = %{version}-%{release}
Obsoletes: maven-shared-archiver < %{version}-%{release}

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}

#tests don't compile with maven 2.2.1
rm -fr src/test/java/org/apache/maven/archiver/*.java

%build

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
    -e \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE1} \
    install javadoc:javadoc


%install
rm -rf $RPM_BUILD_ROOT
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

# Copy file and create unversioned symlink
install -pm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Copy pom
install -pm 644 pom.xml \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-maven-archiver.pom
%add_to_maven_depmap org.apache.maven maven-archiver %{version} JPP maven-archiver

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_datadir}/maven2/poms/JPP-maven-archiver.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/*

