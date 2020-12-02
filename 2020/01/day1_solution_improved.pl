#!/usr/local/bin/perl

#use strict;
#use warnings;

#use lib qw (/home/mborto/perl5/lib/perl5/);
use Algorithm::Combinatorics qw(combinations);
use Getopt::Std;

my @expenses;
my $expenseLength = 0;

open (INPUT, "puzzleInput.txt") || die "Can't open puzzleInput";
#open (INPUT, "puzzleSample.txt") || die "Can't open puzzleInput";

while (my $line = <INPUT>) {
    chomp($line);
    push(@expenses, $line); 
}

compute_answer(\@expenses, 2);
compute_answer(\@expenses, 3);

sub compute_answer {
    my ($list, $comboSize) = @_;    

    print "ComboSize is: $comboSize\n";

    my $iter = combinations($list, $comboSize);

    while (my $c = $iter->next) {
        my $sum    = 0; #initialize to zero for sums
        my $answer = 1; #initialize to one for multiplication

        foreach my $entry (@{$c}) {
            $sum    += $entry;
            $answer *= $entry;
        }

        if ($sum == 2020) {
            print "@{$c}\n";
            print "Sum is: $sum\n";
            print "Answer is: $answer\n\n";
            last;
        }
    }
}

exit (0);

