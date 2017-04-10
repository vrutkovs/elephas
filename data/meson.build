gnome = import('gnome')

custom_target('com.github.Elephas.desktop',
    output : 'com.github.Elephas.desktop',
    input : 'com.github.Elephas.desktop.in',
    command : [intltool_merge, '--desktop-style', podir, '@INPUT@', '@OUTPUT@'],
    install : true,
    install_dir : join_paths(get_option('datadir'), 'applications')
)

about_dialog = configure_file(
    input : 'AboutDialog.ui.in',
    output : 'AboutDialog.ui',
    configuration : conf
)

gnome.compile_resources('elephas',
    'com.github.Elephas.gresource.xml',
    gresource_bundle: true,
    install: true,
    install_dir: join_paths(get_option('datadir'), 'elephas'),
    dependencies: [about_dialog])

install_data('com.github.Elephas.gschema.xml', install_dir: join_paths(get_option('datadir'), 'glib-2.0', 'schemas'))
