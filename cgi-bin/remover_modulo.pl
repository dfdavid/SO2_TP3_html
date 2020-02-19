#!/usr/bin/perl

use CGI;
use strict;
use warnings FATAL => 'all';


my $cgi = new CGI();
my $nombre_modulo = $cgi->param('module');

no strict 'refs';
system "/home/sampaxx/Documents/SO2_TP3_html/cgi-bin/modulos/wrappers/rmmod $nombre_modulo";
print $cgi-> redirect('http://192.168.1.5/modulos.html');

