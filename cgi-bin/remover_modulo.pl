#!/usr/bin/perl

use CGI;
use strict;
use warnings FATAL => 'all';


my $cgi = new CGI();
my $nombre_modulo = $cgi->param('module');

no strict 'refs';
system "/home/sampaxx/PhpstormProjects/untitled/cgi-bin/modulos/wrappers/rmmod $nombre_modulo";
print $cgi-> redirect('http://localhost/modulos.html');

