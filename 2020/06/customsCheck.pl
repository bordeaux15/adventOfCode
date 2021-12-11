#!/usr/local/bin/perl

use strict;
use warnings;

use Data::Dumper;

my %passengersHash;
my $groupCount = 0;

open (INPUT, "testInput.txt") || die "Can't open testInput.txt";
#open (INPUT, "puzzleInput.txt") || die "Can't open puzzleInput.txt";

while (my $line = <INPUT>) {
    chomp($line);
    if ($line eq "") {
        $groupCount += 1;
        next;
    }

    my $groupName = "group_" . $groupCount;

}
