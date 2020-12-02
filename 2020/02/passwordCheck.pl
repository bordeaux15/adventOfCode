#!/usr/local/bin/perl

use strict;
use warnings;

#open (INPUT, "testInput.txt") || die "Can't open testInput.txt";
open (INPUT, "puzzleInput1.txt") || die "Can't open puzzleInput1.txt";

my @pwArray;
my $count;
my $minCount;
my $maxCount;
my $requiredCharacter;
my $pw;
my $validPw1 = 0;
my $validPw2 = 0;

while (my $line = <INPUT>) {
    chomp($line);
    ($minCount, $maxCount, $requiredCharacter, $pw) = split /[:\s-]+/, $line;
    
    #my $count = () = $pw =~ /\Q$requiredCharacter/g;
    @pwArray = split //, $pw;
    validatePasswords1();
    validatePasswords2();
}
    print "Valid password 1 count = $validPw1\n";
    print "Valid password 2 count = $validPw2\n";

exit (0);

sub validatePasswords1 {
    $count = 0;

    foreach my $char (@pwArray) {
        if ($char eq $requiredCharacter) {
            $count += 1;
        }
    }

    if ($minCount <= $count <= $maxCount) {
        $validPw1+= 1;
    }
}

sub validatePasswords2 {
    if (($pwArray[$minCount-1] eq $requiredCharacter) || ($pwArray[$maxCount-1] eq $requiredCharacter)) {
        if ($pwArray[$minCount-1] ne $pwArray[$maxCount-1]) {
            $validPw2 +=1;
        }
    }
}
