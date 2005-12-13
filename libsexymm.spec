Summary:	Set of additional widgets for GTK+ (C++ bindings)
Summary(pl):	Zestaw dodatkowych kontrolek dla GTK+ (dowi±zania C++)
Name:		libsexymm
Version:	0.1.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://osiris.chipx86.com/projects/libsexy/releases/%{name}-%{version}.tar.gz
# Source0-md5:	f5efa414b48c204c7bac98451d5f6e99
URL:		http://chipx86.com/wiki/Libsexy
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	enchant-devel >= 0.4.0
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libsexy-devel >= 0.1.3
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of graphical widgets for GTK+ applications.

%description -l pl
Zestaw kontrolek graficznych dla programów opartych o GTK+.

%package devel
Summary:	Header files for libsexymm library
Summary(pl):	Pliki nag³ówkowe biblioteki libsexymm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	enchant-devel >= 0.4.0
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	gtkmm-devel >= 2.4.0
Requires:	libsexy-devel >= 0.1.3
Requires:	libxml2-devel >= 2.0

%description devel
Header files for libsexymm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libsexymm.

%package static
Summary:	Static libsexymm library
Summary(pl):	Statyczna biblioteka libsexymm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsexymm library.

%description static -l pl
Statyczna biblioteka libsexymm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libsexymm
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
