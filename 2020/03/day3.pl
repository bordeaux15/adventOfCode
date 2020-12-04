#!/usr/local/bin/perl

use strict;
use warnings;

use Data::Dumper;

#open (INPUT, "testInput.txt") || die "Can't open testInput.txt";
open (INPUT, "puzzleInput1.txt") || die "Can't open puzzleInput1.txt";

my @map;
my $maxMapRow = 0;
my $maxMapCol = 0;
my $treesMultiplied = 1;

while (my $line = <INPUT>) {
    chomp($line);
    my @row = split //, $line;
    push @map, [ @row ];
}

$maxMapRow = @map;
$maxMapCol = @{ $map[0] };

print "Array Rows: $maxMapRow\n";
print "Array Cols: $maxMapCol\n";

traverseMap(1, 1);
traverseMap(3, 1);
traverseMap(5, 1);
traverseMap(7, 1);
traverseMap(1, 2);

print "Trees Multiplied: $treesMultiplied\n";

exit (0);


sub traverseMap {
    my ($right, $down) = @_;
    my $row = 0;
    my $col = 0;
    my $treeCount = 0;

    while ($row < $maxMapRow-1) {
        $col += $right;
        $row += $down;
        
        #handle the repeating map by moving back to start of row
        if ($col > ($maxMapCol-1)) {
            $col = $col % $maxMapCol;
        }

        #print "Col: $col, ";
        #print "Row: $row: ";
        #print "Char: $map[$row][$col]\n";
        if ($map[$row][$col] eq "#") {
            $treeCount++;
        }
    }
    print "Trees Encountered: $treeCount\n";
    $treesMultiplied *= $treeCount;
}
