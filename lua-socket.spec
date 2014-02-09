Summary:	LuaSocket is the most comprehensive networking support library for the Lua language
Summary(hu.UTF-8):	LuaSocket egy hálózati kommunikációs könyvtár a Lua nyelvhez
Name:		lua-socket
Version:	2.0.2
Release:	2
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/2664/luasocket-%{version}.tar.gz
# Source0-md5:	41445b138deb7bcfe97bff957503da8e
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
%setup -q -n luasocket-%{version}
echo "LUAINC=-I/usr/include/lua51" >> config
sed -i "s|INSTALL_TOP_SHARE=.*|INSTALL_TOP_SHARE=$RPM_BUILD_ROOT%{_datadir}/lua/5.1/|" config
sed -i "s|INSTALL_TOP_LIB=.*|INSTALL_TOP_LIB=$RPM_BUILD_ROOT%{_libdir}/lua/5.1/|" config

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

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
