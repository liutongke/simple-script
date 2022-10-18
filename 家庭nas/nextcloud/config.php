<?php
$CONFIG = array (
  'htaccess.RewriteBase' => '/',
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'apps_paths' => 
  array (
    0 => 
    array (
      'path' => '/var/www/html/apps',
      'url' => '/apps',
      'writable' => false,
    ),
    1 => 
    array (
      'path' => '/var/www/html/custom_apps',
      'url' => '/custom_apps',
      'writable' => true,
    ),
  ),
  'instanceid' => 'ocsfsn14bzol',
  'passwordsalt' => 'W17mFGnmC3Uh0TJdvoKQds5irI+qhg',
  'secret' => 'XfM0Ew5KenalvYdoOjbnxygrJkTftAYKMOb2fVlGvzSAVW3Z',
  'trusted_domains' => 
  array (
    0 => '192.168.0.107:8080',
  ),
  'datadirectory' => '/var/www/html/data',
  'dbtype' => 'sqlite3',
  'version' => '23.0.0.10',
  'overwrite.cli.url' => 'http://192.168.0.107:8080',
  'installed' => true,
  'check_data_directory_permissions' => true,//扫描文件
  'filesystem_check_changes' => true//扫描文件夹 su /bin/bash -c "php /var/www/html/occ files:scan --all"
);
