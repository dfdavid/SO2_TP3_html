#!/usr/bin/perl -T
use strict;
use warnings FATAL => 'all';
use CGI ':standard';
print header;
print start html ('hello world :)');
print h1 ('hello world h1 :):)');
print end html;
exit
