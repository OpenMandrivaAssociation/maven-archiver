Name:		maven-archiver
Version:	3.6.6
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
BuildRequires:	maven-parent >= 50
BuildRequires:	mvn(org.apache.maven:maven-parent:pom::)
BuildRequires:	maven-shared >= 50
BuildRequires:	mvn(org.apache.maven.shared:maven-shared-components:pom::)
# maven-core, maven-artifact and maven-model are provided. The maven
# RPM does not provide those coordinates.
BuildRequires:	maven-components >= 3.10.0
BuildRequires:	mvn(org.apache.maven:maven-core)
BuildRequires:	mvn(org.apache.maven:maven-artifact)
BuildRequires:	mvn(org.apache.maven:maven-model)
BuildRequires:	plexus-archiver >= 4.15.0
BuildRequires:	plexus-interpolation >= 1.30.0
BuildRequires:	plexus-utils >= 3.6.2
# 3.2.1 still provides this coordinate. The generated mvn() Requires
# is unversioned.
Requires:	plexus-utils >= 3.6.2
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

Obsoletes:	maven-shared-archiver < %{EVR}
Provides:	maven-shared-archiver = %{EVR}

%description
Builds JAR manifests and archives from a Maven project. 3.6.6 builds
against Maven 3.10, Plexus Archiver 4.15.0, and Plexus Interpolation
1.30.0. Xpp3Dom comes from Plexus Utils 3.6.2. The default manifest
gains a Java-Version entry taken from the compiler release or target
when the project sets one. outputTimestamp is no longer limited to
the ZIP timestamp range. pom.properties is written in ISO-8859-1
through CachingWriter, with comments removed and the keys sorted, and
an unchanged file is left in place. The forceCreation flag no longer
overrides that.

%prep
%autosetup -n maven-archiver-maven-archiver-%{version}
# plexus-xml is not packaged. Utils 3.6.2 still contains Xpp3Dom and
# CachingWriter, which are the classes this source imports.
python - <<'PY'
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
old = (
    "    <dependency>\n"
    "      <groupId>org.codehaus.plexus</groupId>\n"
    "      <artifactId>plexus-xml</artifactId>\n"
    "    </dependency>\n"
)
new = (
    "    <dependency>\n"
    "      <groupId>org.codehaus.plexus</groupId>\n"
    "      <artifactId>plexus-utils</artifactId>\n"
    "      <version>3.6.2</version>\n"
    "    </dependency>\n"
)
prop = "    <version.plexus-xml>3.0.2</version.plexus-xml>\n"
if old not in text:
    raise SystemExit("plexus-xml dependency missing")
if prop not in text:
    raise SystemExit("plexus-xml property missing")
text = text.replace(old, new, 1).replace(prop, "", 1)
path.write_text(text)
PY

%files -f .mfiles
%doc README.md
