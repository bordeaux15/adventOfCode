#!/usr/local/bin/perl

use strict;
use warnings;

use Data::Dumper;

my $rowNumber;
my $aisleNumber;
my $seatId;
my $maxSeatId = 0;
my $minSeatId = 0;

#open (INPUT, "testInput.txt") || die "Can't open testInput.txt";
open (INPUT, "puzzleInput.txt") || die "Can't open puzzleInput.txt";

while (my $line = <INPUT>) {
    chomp($line);

    my ($rowId, $aisleId) = split /([LR]+)/, $line;
    $rowNumber   = find_location($rowId, 127, 0);
    $aisleNumber = find_location($aisleId, 7, 0);
    
    $seatId = $rowNumber * 8 + $aisleNumber;
    if ($seatId < $minSeatId) {
        $minSeatId = $seatId ;
    }
    if ($seatId > $maxSeatId) {
        $maxSeatId = $seatId;
    }
}
print "Max Seat Id: $maxSeatId\n";
print "Min Seat Id: $minSeatId\n";

exit (0);

sub find_location {
    my ($idString, $upper, $lower) = @_;
    my $finalChar = chop $idString;
    my @idArray = split //, $idString;
    
    foreach my $idChar (@idArray) {
        my $span = ($upper - $lower + 1) / 2;
        if ($idChar =~ /[BR]/) {
            $lower = $lower + $span;
        }
        else {
            $upper = $upper - $span;
        }
    }

    if ($finalChar =~ /[BR]/) {
        return ($upper);
    } else {
        return ($lower);
    }
}

