#!/usr/local/bin/perl

use strict;
use warnings;

use Data::Dumper;

#open (INPUT, "testInput.txt") || die "Can't open testInput.txt";
#open (INPUT, "validPassportTest.txt") || die "Can't open validPassportTest.txt";
#open (INPUT, "invalidPassportsTest.txt") || die "Can't open invalidPassportsTest.txt";
open (INPUT, "puzzleInput1.txt") || die "Can't open puzzleInput1.txt";

my @passportArray;
my @requiredFields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid");
my $rec = {};
my $validPassports = 0;

while (my $line = <INPUT>) {
    chomp($line);

    if ($line ne '') {
        my @fields = split / /, $line;
        foreach my $field ( @fields ) {
            my ($key, $value) = split /:/, $field;
            $rec->{$key} = $value;
        }
    }
    else {
        push @passportArray, $rec;
        $rec = {};
    }
}

#take care of final record when there's no new line
push @passportArray, $rec;

foreach my $passport (@passportArray) {
    if (check_fields_exist(%$passport)) {
        if (check_fields_correct(%$passport)) {
            $validPassports += 1;
        }
    }
}

print "Valid Passports: $validPassports\n";

exit (0);

sub check_fields_exist {
    my $valid = 1;
    my (%fieldsToCheck) = @_;
    foreach my $requiredField (@requiredFields) {
        if (exists $fieldsToCheck{$requiredField}) {
            next;
        }
        else {
            $valid = 0;
            last;
        }
    }
    return $valid;
}

sub check_fields_correct {
    my (%fieldsToCheck) = @_;
    my ($value, $unit) = split (/(\D+)/, $fieldsToCheck{"hgt"});

    return (0) unless (1910 <= $fieldsToCheck{"byr"} <= 2002);
    return (0) unless (2010 <= $fieldsToCheck{"iyr"} <= 2020);
    return (0) unless (2020 <= $fieldsToCheck{"eyr"} <= 2030);
    return (0) unless ($fieldsToCheck{"pid"} =~ /^[0-9]{9}$/);
    return (0) unless ($fieldsToCheck{"hcl"} =~ /^#[0-9a-f]{6}$/);
    return (0) unless ($fieldsToCheck{"ecl"} =~ /^amb|blu|brn|gry|grn|hzl|oth$/);
    return (0) unless ($unit ne "");
    return (0) unless ($value ne "");
    if ($unit eq "cm") {
        return(0) unless (150 <= $value <= 193);
    } 
    elsif ($unit eq "in") {
        return(0) unless (59 <= $value <= 76);
    } 

    return (1);
}
    
