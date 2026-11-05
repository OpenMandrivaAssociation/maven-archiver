Name:		maven-archiver
Version:	3.6.4
Release:	1
Summary:	Maven archive and manifest helpers
Group:		Development/Java
License:	ASL 2.0
URL:		https://maven.apache.org/shared/maven-archiver/
Source0:	https://github.com/apache/maven-archiver/archive/refs/tags/maven-archiver-%{version}.tar.gz
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	maven-shared
# maven-core is provided. The maven RPM does not provide that coordinate.
BuildRequires:	maven-components
BuildRequires:	plexus-archiver
BuildRequires:	plexus-interpolation
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

Obsoletes:	maven-shared-archiver < %{EVR}
Provides:	maven-shared-archiver = %{EVR}

%description
Builds JAR manifests and archives from a Maven project. The POM asks
for Plexus Archiver 4.10 and Plexus Interpolation 1.28. The packaged
jars are 4.4 and 1.27; the resolver uses the installed artifact.

%prep
%autosetup -n maven-archiver-maven-archiver-%{version}

%files -f .mfiles
%doc README.md
