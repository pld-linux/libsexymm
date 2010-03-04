Summary:	Set of additional widgets for GTK+ (C++ bindings)
Summary(pl.UTF-8):	Zestaw dodatkowych kontrolek dla GTK+ (dowiązania C++)
Name:		libsexymm
Version:	0.1.9
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://releases.chipx86.com/libsexy/libsexymm/%{name}-%{version}.tar.gz
# Source0-md5:	77c8ae69084e478a6b090ec6e5ae26bf
Patch0:		%{name}-ac.patch
URL:		http://chipx86.com/wiki/Libsexy
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.10.1
BuildRequires:	libsexy-devel >= 0.1.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of graphical widgets for GTK+ applications.

%description -l pl.UTF-8
Zestaw kontrolek graficznych dla programów opartych o GTK+.

%package devel
Summary:	Header files for libsexymm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsexymm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.10.1
Requires:	libsexy-devel >= 0.1.9

%description devel
Header files for libsexymm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsexymm.

%package static
Summary:	Static libsexymm library
Summary(pl.UTF-8):	Statyczna biblioteka libsexymm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsexymm library.

%description static -l pl.UTF-8
Statyczna biblioteka libsexymm.

%prep
%setup -q
%patch0 -p1

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
%{_libdir}/libsexymm
%{_includedir}/libsexymm
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
