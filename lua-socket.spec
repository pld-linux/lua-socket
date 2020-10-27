%define		subver	rc1
%define		rel	3
Summary:	LuaSocket - the most comprehensive networking support library for the Lua language
Summary(hu.UTF-8):	LuaSocket egy hálózati kommunikációs könyvtár a Lua nyelvhez
Summary(pl.UTF-8):	LuaSocket - najpełniejsza biblioteka sieciowa dla języka Lua
Name:		lua-socket
Version:	3.0
Release:	0.%{subver}.%{rel}
License:	MIT-like
Group:		Development/Languages
Source0:	https://github.com/diegonehab/luasocket/archive/v%{version}-%{subver}.tar.gz
# Source0-md5:	08bd2f265b244eb4bf5c2c36bf89b759
URL:		http://luaforge.net/projects/luasocket/
BuildRequires:	lua51-devel >= 5.1.5-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaSocket is the most comprehensive networking support library for the
Lua language. It provides easy access to TCP, UDP, DNS, SMTP, FTP,
HTTP, MIME and much more.

%description -l hu.UTF-8
LuaSocket egy hálózati kommunikációs könyvtár a Lua nyelvhez. Egy
egyszerű hozzáférést biztosít TCP, UDP, DNS, SMTP, FTP, HTTP,
MIME-hoz, és még sok máshoz.

%description -l pl.UTF-8
LuaSocket to najpełniejsza biblioteka sieciowa dla języka Lua. Daje
łatwy dostęp do TCP, UDP, DNS, SMTP, FTP, HTTP, MIME i wielu innych.

%package devel
Summary:	Development headers for lua-socket
Summary(pl.UTF-8):	Pliki programistyczne lua-socket
Group:		Development/Libraries
Requires:	lua51-devel >= 5.1.5-7

%description devel
Development headers for lua-socket.

%description devel -l pl.UTF-8
Pliki programistyczne lua-socket.

%prep
%setup -q -n luasocket-%{version}-%{subver}

%build
%{__make} \
	CC="%{__cc} %{rpmcppflags} %{rpmcflags}" \
	LD="%{__cc} %{rpmldflags}" \
	LUAINC=%{_includedir}/lua5.1 \
	INSTALL_TOP_LDIR=$RPM_BUILD_ROOT%{_datadir}/lua/5.1/ \
	INSTALL_TOP_CDIR=$RPM_BUILD_ROOT%{_libdir}/lua/5.1/

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LUAINC=%{_includedir}/lua51 \
	INSTALL_TOP_LDIR=$RPM_BUILD_ROOT%{_datadir}/lua/5.1/ \
	INSTALL_TOP_CDIR=$RPM_BUILD_ROOT%{_libdir}/lua/5.1/ \

install -d $RPM_BUILD_ROOT%{_includedir}/lua5.1/luasocket
cp -p src/*.h $RPM_BUILD_ROOT%{_includedir}/lua5.1/luasocket

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEW README TODO WISH
%dir %{_libdir}/lua/5.1/mime
%attr(755,root,root) %{_libdir}/lua/5.1/mime/core.so
%dir %{_libdir}/lua/5.1/socket
%attr(755,root,root) %{_libdir}/lua/5.1/socket/core.so
%{_datadir}/lua/5.1/ltn12.lua
%{_datadir}/lua/5.1/mime.lua
%{_datadir}/lua/5.1/socket.lua
%{_datadir}/lua/5.1/socket

%files devel
%defattr(644,root,root,755)
%{_includedir}/lua5.1/luasocket
