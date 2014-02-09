Summary:	LuaSocket is the most comprehensive networking support library for the Lua language
Summary(hu.UTF-8):	LuaSocket egy hálózati kommunikációs könyvtár a Lua nyelvhez
Name:		lua-socket
Version:	3.0rc1
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	https://github.com/diegonehab/luasocket/archive/v3.0-rc1.tar.gz	
# Source0-md5:	08bd2f265b244eb4bf5c2c36bf89b759
URL:		http://luaforge.net/projects/luasocket/
BuildRequires:	lua51-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaSocket is the most comprehensive networking support library for the
Lua language. It provides easy access to TCP, UDP, DNS, SMTP, FTP,
HTTP, MIME and much more.

%description -l hu.UTF-8
LuaSocket egy hálózati kommunikációs könyvtár a Lua nyelvhez. Egy
egyszerű hozzáférést biztosít TCP, UDP, DNS, SMTP, FTP, HTTP,
MIME-hoz, és még sok máshoz.

%package devel
Summary:	Development headers for lua-socket
Group:		Development/Libraries
Requires:   lua51-devel

%description devel
Development headers for lua-socket.

%prep
%setup -q -n luasocket-3.0-rc1

%build
%{__make} \
	LUAINC=/usr/include/lua51 \
    INSTALL_TOP_LDIR=$RPM_BUILD_ROOT%{_datadir}/lua/5.1/ \
    INSTALL_TOP_CDIR=$RPM_BUILD_ROOT%{_libdir}/lua/5.1/

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	LUAINC=/usr/include/lua51 \
    INSTALL_TOP_LDIR=$RPM_BUILD_ROOT%{_datadir}/lua/5.1/ \
    INSTALL_TOP_CDIR=$RPM_BUILD_ROOT%{_libdir}/lua/5.1/ \
    install

install -d $RPM_BUILD_ROOT%{_includedir}/lua51/luasocket
install src/*.h $RPM_BUILD_ROOT%{_includedir}/lua51/luasocket/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEW README
%dir %{_libdir}/lua/5.1/mime
%dir %{_libdir}/lua/5.1/socket
%attr(755,root,root) %{_libdir}/lua/5.1/mime/core.so
%attr(755,root,root) %{_libdir}/lua/5.1/socket/core.so
%attr(755,root,root) %{_datadir}/lua/5.1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/lua51/luasocket
