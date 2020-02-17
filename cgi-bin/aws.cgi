#!/usr/bin/perl -w

use strict;
use warnings;
use CGI; #modulos
use CGI qw (:standard); #usamos este modulo para mostrar errores en la pagina
use CGI::Carp qw (fatalsToBrowser); 
use File::Basename;

my $consulta = new CGI;
my $anio= $consulta->param("anio");
my $dia= $consulta->param("dia");

print $consulta->header( -charset=>'utf-8'),$consulta->start_html( -title=>'Informacion AWS', -style=>{-src=>'style.css'}),$consulta->end_html;

#open(ARCHIVO, '>>','aws.txt');

for( my $hora = 0; $hora <24; $hora ++){
    my $valor = $hora;
    if ($valor <10){
        my $a = 0;
        my $c = $a.$valor;
        my $salida_consulta  = qx(aws --no-sign-request s3 ls s3://noaa-goes16/ABI-L2-CMIPF/$anio/$dia/$c/ 2>&1 | grep C13);
        my @lines = split /\n/,$salida_consulta;
        foreach my $line (@lines){
            print $consulta->b("$line </br>");
        }
        print ARCHIVO $salida_consulta;
    }else{
        my $salida_consulta = qx(aws --no-sign-request s3 ls s3://noaa-goes16/ABI-L2-CMIPF/$anio/$dia/$valor/ 2>&1 | grep C13);
        my @lines = split /\n/, $salida_consulta;
        foreach my $line (@lines){
            print $consulta->b("$line </br>");
        }
    }
        
}


