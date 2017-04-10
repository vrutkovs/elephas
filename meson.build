project('elephas', 'c', version : '0.98', meson_version : '>= 0.36.0')

python = find_program('python3')
intltool_merge = find_program('intltool-merge')
itstool = find_program('itstool')
msgfmt = find_program('msgfmt')

conf = configuration_data()
conf.set('pkgdatadir', join_paths(
    get_option('prefix'), get_option('datadir'), meson.project_name()))
conf.set('localedir', join_paths(
    get_option('prefix'), get_option('localedir'), meson.project_name()))

conf.set('PACKAGE_VERSION', '0.1.0')
conf.set('PACKAGE_URL', 'https://github.com/vrutkovs/elephas')

subdir('po')
subdir('data')
subdir('elephas')

meson.add_install_script('meson_install.py')
