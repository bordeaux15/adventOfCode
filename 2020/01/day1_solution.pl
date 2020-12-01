#!/usr/local/bin/perl

use strict;
use Getopt::Std;

my @expenses;
my $expenseLength = 0;

open (INPUT, "puzzleInput.txt") || die "Can't open puzzleInput";

while (my $line = <INPUT>) {
    chomp;
    push(@expenses, $line); 
}

#0 indexed length of array
$expenseLength = @expenses - 1;

for my $expenseIdx (0 .. $expenseLength) { 
    my $baseExpense = $expenses[$expenseIdx];

    for my $expenseIdx1 ($expenseIdx .. $expenseLength) {
        my $baseExpense1 = $expenses[$expenseIdx1]; {

            for my $expenseCheck ($expenseIdx1 .. $expenseLength) {
                if ($baseExpense + $baseExpense1 + $expenses[$expenseCheck] == 2020) {
                    my $answer = $baseExpense * $baseExpense1 * $expenses[$expenseCheck]; 
                    print "Expense 0 = $baseExpense";
                    print "Expense 1 = $baseExpense1";
                    print "Expense 2 = $expenses[$expenseCheck]";
                    print "Answer    = $answer\n"; 
                }
            }
        }
    }
}

exit (0);
