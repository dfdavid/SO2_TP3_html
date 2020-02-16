#!/usr/bin/perl
use strict;
use warnings;
use CGI;
my $cgi = new CGI;
print $cgi->header;
print $cgi->start_html('Hello World');
print $cgi->h1('Informacion del Sistema');
print $cgi->end_html();
exit;