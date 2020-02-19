#!/usr/bin/perl

#print "Content-Type: text/html\n\n";

use warnings;
use CGI;
use strict;
my $PROGNAME = "subir_modulo.pl";
my $cgi = new CGI();
my $upfile = $cgi->param('module');
my $filename = GetBasename($upfile);
#system("pwd");
no strict 'refs';

if ($filename =~ m/\.ko$/){
if (! open(OUTFILE, ">loaded_modules/${filename}") ) {  #https://www.tutorialspoint.com/perl/perl_files.htm
		print "Error abriendo archivo para escritura\n";
		exit(-1);
	}
} else {
	print "Archivo no es del tipo .ko\n";
	exit(-1);
}
my $nBytes = 0;
my $totBytes = 0;
my $buffer = "";
binmode($upfile);
while ( $nBytes = read($upfile, $buffer, 1024) ) {
	print OUTFILE $buffer;
	$totBytes += $nBytes;
}
close(OUTFILE);

#en esta linea se invoca a traves de este script el ejecutable 'insmod' el cual tendra los permisos de root para instalar el modulo en el kernel
system "/home/sampaxx/Documents/SO2_TP3_html/cgi-bin/modulos/wrappers/insmod /home/sampaxx/Documents/SO2_TP3_html/cgi-bin/loaded_modules/$filename";

use strict 'refs';
print $cgi->redirect('http://192.168.1.5/modulos.html');

sub GetBasename {
my $fullname = shift; # https://perldoc.perl.org/functions/shift.html
	my(@parts);
	# check which way our slashes go.
	if ( $fullname =~ /(\\)/ ) {
		@parts = split(/\\/, $fullname);
	} else {
		@parts = split(/\//, $fullname);
	}
	return(pop(@parts));
}



