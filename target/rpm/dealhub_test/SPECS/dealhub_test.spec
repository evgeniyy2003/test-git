%define _unpackaged_files_terminate_build 0
%define __jar_repack 0
Name: dealhub_test
Version: 1.3
Release: SNAPSHOT20210114132642
Summary: dealhub_test
License: Prop License (c), DealHub
Distribution: Test 1.0
Group: Application/Collectors
Packager: DealHub
autoprov: yes
autoreq: yes
Prefix: /opt/rpm-test
BuildArch: noarch
BuildRoot: /home/devops/git/test-git/target/rpm/dealhub_test/buildroot

%description

%install

if [ -d $RPM_BUILD_ROOT ];
then
  mv /home/devops/git/test-git/target/rpm/dealhub_test/tmp-buildroot/* $RPM_BUILD_ROOT
else
  mv /home/devops/git/test-git/target/rpm/dealhub_test/tmp-buildroot $RPM_BUILD_ROOT
fi

%files

%attr(755,root,-)  "/opt/rpm-test/calc"
%attr(755,root,-)  "/opt/rpm-test/calc.jar"
%attr(755,root,-) "/opt/rpm-test/lib"
