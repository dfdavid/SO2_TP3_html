#!/usr/bin/env perl

use strict;
use warnings;
use CGI;
use Cwd;
my $consulta = CGI->new;

print $consulta->header( -charset=>'utf-8'), $consulta->start_html( -title=>'pc_info', -style=>{-src=>'style.css'}), $consulta->end_html;

print $consulta->h2("INFORMACION GENERAL DE HARDWARE");
print $consulta->h3("INFORMACION DE MEMORIA:");

my $mem_info = qx(cat /proc/meminfo);
my @lines=split /\n/, $mem_info;
foreach my $line(@lines){
  print $consulta->b("$line <br>");
}
print $consulta->h3("INFORMACION DEl PROCESADOR:");
#traigo la informacion del procesador ejecutando el comando lscpu por consola con la funcion qx
my $ls_cpu = qx(lscpu);
my @lines=split /\n/, $ls_cpu;
foreach my $line(@lines){ #imprimo lo que me devuelve la variable
  print $consulta->b("$line <br>");
}

#traigo la informacion de Uptime
print $consulta->h3("INFORMACION DE UPTIME:");
my $up_time = qx(uptime);
my @lines= split /\n/, $up_time;
foreach my $line(@lines){
  print $consulta->b("$line <br>");
}

#traigo la informacion de Uptime
print $consulta->h3("FECHA Y HORA:");
my $f_h = qx(date);
my @lines=split /\n/, $f_h;
foreach my $line(@lines){
  print $consulta->b("$line <br>");
}
