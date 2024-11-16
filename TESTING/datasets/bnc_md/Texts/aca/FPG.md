# Design of computer data files

## DIRECT FILE ORGANIZATION

### 6.1 Introduction

Records can be retrieved directly from files that have been organized in many ways.
In this chapter we shall be dealing with files that have been designed to make direct record retrieval as easy and rapid as possible.
These are known as directly organized files.
It is possible to process the records in a directly organized file either directly, using the keys in any desired order, or serially, taking the records in the order they are stored and ignoring their keys.

Both direct and serial processing of directly organized files are dealt with in this chapter.
Direct processing of files organized sequentially or using the indexed sequential technique is covered in the chapters devoted to those types of organization.

Records are often processed in a random order.
A bank cannot predict which of its customers wish to withdraw or deposit money on any given day; a travel firm cannot control which of its package tours will be booked at a particular time.
Customers arrive as a result of their own decisions, and not in an order dictated by the travel agent or bank.
As these transactions are not predictable they present a processing problem.
When an immediate response is not required, the transactions can be collected into batches, sorted into a key sequence that matches the appropriate master file, and processed sequentially.
However, if the customer is waiting for an immediate answer, there is no time for this.
The record has to be checked at once - to see if a booking is available, for example - and this means that the file has to be referenced without preparatory sorting or processing.

As the records are processed in a sequence that cannot be predetermined, we are faced with the problem that we know the key or control number of the record but have no indication of its location in storage.
It would be possible to search through the file until the record was located, but this technique, and the more refined methods available for searching sequential files in which there is no direct relationship between the record key and its storage location, are too slow for the needs of most enquiry systems.
We must look for a way of establishing a relationship between the key of the record and its address, and using this relationship to retrieve the record rapidly.

The relationship can take several forms.
First, it can be an index of every record position in the file; modifications of this method lead to indexed sequential files, and are dealt with in Chapter 7.
Second, each record can be stored at an address that is directly related to its key, e.g. at the address which is the same as the key (record 20 in address 20 and so on).
This type of file is known as a self-indexing or self-addressing file.
If it is not possible to find a relationship of this sort, some other method of assigning addresses to keys has to be found.
Usually, a suitable algorithm is used to convert keys to addresses; the file is then described as a randomized file, and the algorithm used is called a randomizing algorithm.
The process is often also described as hashing.

The application of these methods of assigning storage positions to records is discussed in detail in this chapter, and reference tables are provided to aid the file designer.
This is followed by sections on optimizing the performance of direct files, and on the practical steps that can be taken to maximize the efficiency of these files in operation.

### 6.2 Self-indexing

#### Continuous key sequences

If record keys are numeric and there are not many gaps in the sequence, it is often possible to allocate a storage position based directly on the key.
In the simplest case, records with keys such as 00 000 to 99 999 could be allocated to any contiguous set of 100000 storage positions.
Some direct access devices have available storage areas starting from 00 000 or 00001, and addressed by a simple number.
When devices of this type are available, the storing of records with a continuous set of keys is straightforward.
However, the conversion from a numeric user-address to a device address in terms of cylinders and records is carried out by the manufacturer's software, and thus involves an overhead of both primary storage space and CPU time.

If locations with the same addresses as the record keys are available, then each record is stored in the appropriate position, and a record can be retrieved by the use of the relationship:

If a contiguous area of storage is available elsewhere, or if the keys are continuous but start at a figure outside the range of the storage addresses available, an addition or subtraction will be needed.
In this case: where β is a constant.

For example, if 20 000 records with keys [UNK] are to be stored in locations [UNK], then:

An additional factor arises when keys do not go up in ones, but in twos, threes, fives, tens or some other increment.
In this case, to allow for the increment not being unity, the relationship becomes: where α and β are constants.

An example of this might be keys 00 003, 00006, 00 009, 00012, etc., to be stored in positions 00352, 00 353,....
Then:

As explained in Chapter 2, many disks have a discontinuous or complex address format.
An example of this is the IBM disk range, in which the basic form of disk address is CCHHR, where:

- CC is a two-character cylinder number;

- HH is a two-character head number;

- R is a one-character record number.

R starts from record 1 on each track, as record 0 is a control record.

Because there is no record 0, the nearest that can be obtained to a continuous set of numbers will be: Thus addresses: are missing.
Such a near-continuous set of numbers can only be obtained if nine records are stored per track, and this will usually not be the best number of records for the file under consideration.
Normally we shall have sets of addresses of the form:

As calculations in main storage take very little time, it is well worthwhile converting the key values into this form by means of an algorithm.
For example: a file is to be stored on a 3380 disk, fourteen records per track, starting at cylinder 23.
The record keys are continuous starting from 14 836; the position of a record with the key 15 302 would be calculated as follows: i.e. this is the 467th record in the file: This means that it will be stored as the fifth record on the thirty-fourth track of the file.
As there are fifteen tracks per cylinder on the 3380, this means that the record address will be cylinder 25, track 3 (the fourth track on the cylinder because IBM use track numbers starting from 0), record 5.
The full address will be [UNK] The general formula here is that, with: where we consider only the integer part of the division.
If the remainder is R: where we consider only the integer part of the division.
Let the remainder be R'; then [UNK]

This calculation may look cumbersome, but it takes very little time and provides record storage positions very effectively.
Integer arithmetic should be used, to avoid the problems of approximate answers.
If necessary, considerably more complex calculations are justified because of the speed of internal storage operations, and because use of such a calculation allows the unbroken key sequence to be exploited.
Manufacturers usually provide relative record addressing which carries out these calculations for the user.

#### Broken key sequences

Inherently continuous sequences Although the key sequence in a new file is often continuous, gaps will usually soon occur.
Customers turn elsewhere or go out of business, old product numbers are replaced by new, and so on.
The advantage of being able to store such a file on a direct access device in addresses which are directly related to the key then has to be balanced against the waste of space involved.
A self-indexing file can be referenced sequentially by normal sequential processing, and directly using a single seek because of the relations between key and storage address.
No other file organization can achieve this, so it is worth accepting a fairly low packing density to retain the file in this form.
If direct access capacity is a limitation, a loss of 15 - 20 per cent of space will still compare well with other file organizations (see Chapter 7 and the calculations of packing density for randomly organized direct files later in this chapter).
Where access time is the vital criterion and direct access storage is abundant, a packing density of as little as 50 per cent is justifiable for a file accessed both directly and sequentially.
Where maximum direct access throughput is essential, even lower packing densities may be accepted (see the average space used by randomized files to compare, p. 310).
Unused storage positions should be filled with dummy records, so that they can be recognized at once.

In setting up a file with a number of dummy records, these dummies will be filled with a character such as & or •that will be tested for during serial processing.
The problem should not arise during direct processing, as every valid key has a corresponding record.
If it does, then an error will be indicated.
However, the test for a dummy must be carried out during direct processing to guard against an invalid key being processed (see Fig. 6.1).

This technique is only directly applicable to fixed-length records.
It can be applied to variable-length records by padding or the use of fixed-length [UNK] buckets for variable records, as discussed previously.
In the latter case addressing will probably only point to a bucket number, and in searching the bucket for a particular record using the direct technique it will no longer be an error to detect a dummy record, but part of the search.

Naturally broken sequences Record keys often do not start as an unbroken sequence.
In a simple case, we might have the following key set: These thirty-four records need only 34 storage positions, but if they were stored in self-indexing form they would take up 359 storage positions, and there would be five gaps of 91, 1, 1, 94 and 138 positions respectively.
These gaps can be eliminated by a sequence of tests of the type shown below: The gaps are eliminated as shown in Fig. 6.2.

Typically, keys form broken sequences because they contain separate items of information.
For example, a product code used as a key may contain sections for such fields as:

There may be room left for additions to the number of products, product types, factories, categories, etc.
This can lead to a series of continuous keys with gaps left in it at intervals.
This can be converted into a continuous sequence of keys so long as the various constants involved in the key are known.
For example, if the category can take the values 1 to 7, the factory number can be 01 to 11, the product type can be 01 to 37, and the number of products in the type can range from 001 to 999, with 147 being the largest required at present (the number varies with type), then we might have the following runs of continuous numbers made up of the digits representing the category, factory, product type and number of products:

These runs of continuous numbers have to be turned into a single sequence, starting from 1.
There are 2849 runs of numbers; as given above the most in one run is 147, and the least shown is 84.
One way of combining these runs into a single sequence is shown in Fig. 6.3.

This process requires a table of 2849 entries, each showing the cumulative total of records up to the start of that set.
To ensure that all the product types for a given category and factory are kept together, the following algorithm is used: This arranges for every product type for category 1 and factory 1 to come first, and every factory in category 1 to precede those in category 2.
If this routine is written in a programming language such as PL/1, Algol or Fortran, the calculation is not necessary; the subscript facility can be used, and the table entries referenced as TABLE (CAT, FAC, PROD).
In the example shown in Fig. 6.3, the entry required would be TABLE (1, 1, 3).

This example requires a large table; if there is not room in primary storage for such a table it is not possible to handle the file as a self-indexing file, and a different method of addressing must be used.
It is almost always a lack of storage space, or the fact that the file is dynamic and so cannot be loaded in a single operation, that prevents self-indexing, and not the time taken to carry out the calculations.

Before leaving the subject of self-indexing, it is worth mentioning perfect hash functions.
These generally refer to finding a self-indexing function for tables in main storage; Jaeschke has developed a method originally proposed by Cichell, and he has shown that, however complicated the key sequence is, a self-indexing function can be found for up to 40 keys so that they fit exactly into a table with the same number of storage positions.
For larger tables - up to about 1000 keys - a more approximate but less time-consuming method due to Sprugnoli can be used.
The small size of these 'files' make such techniques applicable only to main storage tables; in that sphere, they are very useful.

### 6.3 Algorithmic addressing

The keys used for many data files are not suited to any practical self-indexing transformation, so other methods of establishing a relationship between record keys and storage addresses have been developed.
What is needed is a transformation - usually called an algorithm - that can be carried out on a key to yield a storage address.
Naturally, it must always yield the same address from the same key.
Any such transformation will involve the compression of a diffuse key set, containing many gaps, into a much smaller range of addresses; if this is not the case, the file should be self-indexed.
Whatever the size and complexity of the key, the factors that control the transformation are the same.
They are:

- 1 The number of addresses to be generated.
This will depend on the number of records if each record is to have its own address.
If groups of records are to be stored in buckets, it will be related to the number of buckets required.

- 2 The direct access space required and, in some cases, its distribution.
It is desirable to have a single file area, both for efficient file processing and for simplicity, but this is not always possible.
At all events the user will have to estimate the amount of direct access storage space the file needs, and this will affect the algorithm used.
A number of techniques are available to handle files that have dynamic space requirements, and these are discussed later.

- 3 The direct access starting address.
It will not be enough to produce a set of generated addresses corresponding to the number of record storage positions required.
They will also have to start from the specified starting address on the device, and must all lie within the allocated range.
The process will be as shown in Fig. 6.4.

Assume that n records are to be stored, and N addresses are available for record storage.
Transformation of keys into addresses by an algorithm will produce r addresses.

The relationship between r, n and N is: Ideally just one key would be associated with each address and every address available would be used.
In this case [UNK].
In practice neither condition is likely to be met.
The factors determining how closely the ideal case can be approached are examined in the following sections.

#### How synonyms occur

Sometimes two or more record keys are transformed by an algorithm into the same address.
The first record to be allocated that address can be stored there, and is described as the home record.
Any subsequent record to be allocated to that address has to be stored elsewhere.
It is called a synonym, and will overflow from its natural home address because that is already full.
The situation is modified when records are stored in buckets holding several records, but synonyms still occur.
This is examined later (see p. 173).
As a synonym is not held at the address the program has computed, a further search is needed to find it.
This leads to loss of time, and synonyms are the reason that algorithmically addressed files give a slower response than self-indexing files; home records are retrieved just as quickly.
Much of the rest of this chapter shows how to minimize the number of synonyms, and to reduce the effect of those that remain.

It might seem that a suitable algorithm could be found which would not generate synonyms.
This is very unlikely.
In some cases the algorithm will spread the addresses evenly over the allocated storage area, and in the ideal case will have an equal probability of generating any address within that area; in other cases the existing key order can be used to improve the efficiency of record storage.
In either case some addresses will be generated more than once, while others will not be generated at all.
A different set of keys will produce a different set of synonyms, and of unused record spaces.
Statistically, however, the chance of avoiding synonyms altogether is vanishingly small.
Heising has pointed out that if n records are randomized into N addresses, there are N n possible record distributions, only [UNK] of which allocate no more than one record to any address.
If 4000 records are stored in 5000 addresses then only one algorithm in every [UNK] will achieve this, which rules out a search for a perfect randomizing algorithm on a trial-and-error basis.

This can be seen in a qualitative way by considering the party game in which participants guess how many people would need to be asked their birthdays, on average, to find two with birthdays on the same day.
Many people will answer 365 (or 366!).
Some will answer 365/2 or 183 for safety.
Few will guess that a group of twenty-three will, on average, contain two people with birthdays on the same day.
This is followed by experimental proof, to general surprise.
As twenty-three birthdays spread at random over 365 addresses can cause duplication, it is not surprising that no randomizing algorithm can avoid synonyms when packing thousands of records into a set of addresses that is only 10-20 per cent greater than the number of records!

When records are randomly distributed among the available addresses, the probability of 0, 1, 2,..., x records being allocated to any given address that can hold a single record can be calculated as follows:

Let the number of records be defined as n and the total address locations as N. This corresponds with the symbols used in equation (6.1).
When records are randomized to N locations the probability of any particular address being generated due to the transformation of a single key is 1/N.
As a result of n records being allocated, the probability of a given location having been allocated x records is given by the terms of the binomial expression: Thus [UNK] This expression is precise.
However, it has the disadvantage that it is not general, but has to be calculated separately for every n and N.

When n and N are very much larger than 1, which applies in any normal data file, the Poisson distribution may be used as an approximation to the binomial.
The derivation of this is given in statistics textbooks and practical examples of its application, and an assessment of the closeness of the approximation, are given later in this chapter (see p. 169).

The advantage of using the Poisson distribution is that p (x) now depends on the value of the ratio (n/N).
This represents the packing density of the file, and is much more general than n or N used independently, as all files with the same packing density give the same results irrespective of the value of N and n.

From the Poisson distribution:

By evaluating the above expression for x and setting [UNK]... we can obtain the corresponding probabilities that a given address will have: and so on.
Where a file area contains N addresses we can expect: In theory we could provide just sufficient space in the file for all the records.
This would certainly simplify equation (6.3) to yield: but it is clear intuitively that we cannot completely fill the file, as the last available storage position would on average be half the file area away from the last record's computed address.
We shall look at ways of choosing a more suitable packing density in more detail later (see p. 172).

### 6.4 Methods of randomizing

Whenever an algorithm is used to store a direct file, the implication is that self-indexing is not practical.
This usually means that the keys of the file are too diffuse to store directly, and the key range has to be compressed by using an algorithm.
There are two possibilities: either to exploit the existing key order - if that is possible - or to completely destroy that order, and to allocate keys to addresses as randomly as possible.
Both of these options are examined below.

#### Order-preserving algorithms

##### 1 Using the low order part of a key

Where a key is a long number, consisting perhaps of ten digits, but we only have 8000 records and hence need only to allocate 10 000 storage positions, we could use the last four digits of the key as a storage address.
This is suspect because keys may always end in 2, 5, or some other specific number, or always be divisible by 2, 5 or some such constant.
There might also be a departmental or other code in the centre of the key, and we might obtain all the records in three areas starting with numbers such as 03, 05 or 07 if the choice of storage address is unfortunate.
This is analysed further elsewhere.
This technique can, however, give very good results if the low order digits of the key are consecutive integers with few gaps.

##### 2 Using middle or upper order parts of a key

The same considerations dictate against the use of either of these as storage addresses.
It may not be obvious that order exists in the key sequence, yet it may be present and damaging.

##### 3 End folding

A ten-digit key such as 1 234 567 890 may be reduced to 'fit' 50 000 storage positions by carrying out the steps: This method is fairly effective.
It destroys the original key pattern more completely than operations 1 and 2 above, but retains the ability to separate keys that are part of consecutive runs.
This can lead to results that improve on perfect randomization, but it depends on the key sequence and is not reliable (see Buchholz and Lum et al.
for further details).

##### 4 Division by a non-prime

If we divide a large key by an appropriate number - probably dictated by the file storage area - and use the remainder as an address, this will provide a precise method of fitting addresses to available storage.
For example, if we have 98 000 positions of storage in which to store the records, from 50 001 to 148 000, we could carry out the following calculation: The record address is 124 790.
This process looks effective, but the last three digits of the key are unchanged by the division.
It turns out that any number divided by 98 000 will give a remainder with the last three digits unchanged, as 98000 itself is divisible by 1000.
This means that the last part of the original key pattern remains: if this includes a code of, say, 05 then randomization will be incomplete.
For that reason a divisor should be chosen that is not itself divisible by 2, 3, 5, 10 or any of their simple multiples.
In our example the divisor is divisible by 1000, which leads to three unchanged digits.
Buchholz has shown that non-prime odd numbers can give very good results, but are not reliable unless they have no divisors less than about 19.
This choice is also discussed by Lum et al.

##### 5 Division by a prime

The logical extension of avoiding multiples of 2, 3, 5, 10, etc., is to use a large prime number.
This usually leads to removal of the effect of any repeating pattern such as a 2, 5 or 0 in the last digit because every digit in the number divided is involved in the division, and so may be altered.
However, sequences of keys differing by one will yield remainders differing by one.
So long as two key sequences do not produce overlapping remainders this can achieve results considerably better than true randomization.
The process is as follows:

- a) Decide on a packing density for the file.
If n records are to be stored in N addresses, this packing density (α) will be [UNK] Let n be 85 000.
A suitable α might be 85 per cent (this is discussed in more detail later).
In our example this would mean that [UNK] storage positions would be required for the file.

- b) Select a prime near to 100 000 - say 99 991 - and divide.
The remainders of this division will lie in the range 0-99 990.
If the storage area does not start at 0, then a simple addition will convert this figure to the address range required.

- c) The number of synonyms resulting from this process should be compared with those to be expected from perfect randomization; see p. 166 for methods of doing this.
If the results are similar to or better than those predicted theoretically, the transformation is satisfactory.
If not, a different prime number should be selected and the process repeated.

- c) In selecting a prime number, primes of the form [UNK] should be avoided, where B is the number base and k a small integer.
This is because the binomial expansion of [UNK] shows that the remainder will contain superposed m digit groups of the original key.
This tendency remains for small integer values of k, reducing as k increases in size.
Thus primes such as 4999, 7001, 79 999, etc., are best not used for decimal keys.

A table of prime numbers, selected so that they are not too near to a factor of ten, and close enough in value to allow any packing density to be selected within half of a percent, is given in Appendix 4.
Decimal keys should be retained in decimal form; alpha or alphanumeric keys are best handled in binary.

Some prime numbers can usually be found that give a good transformation - in fact it is the high probability that any suitable prime chosen will do so, allied to the ease with which this technique can be used to fit any number of records into precisely the required storage space, that makes this such a convenient method.
However, if a number of primes have failed, it may be sensible to consider complete randomization.

##### 6 Order-preserving algorithms in general

A large number of order-preserving algorithms were examined by Amble and Knuth, showing how they compared for completion of successful and unsuccessful searches for records.
Many of these are suitable only for table searching in main storage, but the principles are of interest to direct file designers.
Ouksel presented a method in which parts of the original key such as area code, factory number and part type can be retained by the use of bit tables.
Garg and Gotlieb have developed a method that is related to interpolation searching, and in which the algorithm is based on an analysis of the key sequence, rather than on a presupposition such as the effectiveness of any particular procedure - say mid-square or division.
Order-preserving algorithms are still being developed, but the success of division shows that order-preserving algorithms are an important resource to the file designer.

#### Genuinely randomizing algorithms

##### 1 Square the key and select a part

This depends on squaring the whole or part of the key, and taking a number of digits from the centre of the resulting value.
An example might be: This gives a potential range of addresses between 000 000 and 999 999.
The records can be compressed into some other range such as 250 000 by repetitive subtraction of 250 000, and the method usually gives very good randomization.
It is often not convenient to square a large integer so a selected part of the key may be squared instead.
This technique is not always as effective as division, but does achieve a nearly random distribution, and so is useful when it is not possible to exploit any existing order in the key sequence.

##### 2 Selecting digits from different parts of the key

Sometimes, rather than selecting a single part of the key, several areas are used.
This may operate as follows: This would normally be expected to produce results rather worse than the mid-square method, but it has proved to be very effective on occasions (see p. 169 for further discussion).

##### 3 Quadratic and quadratic quotient hashing

These two techniques, due to Maurer (quadratic hashing) and Bell (quadratic quotient hashing), can be used to eliminate primary and secondary clustering of keys after division.
Primary clustering results from runs of keys, in that they will be allocated to adjacent storage positions after division; this is dispersed by quadratic hashing, in which the final storage position of the record depends on a function of the remainder from the original division, summed with a function of the square of the remainder.
This does separate members of a run of keys, but it fails to separate two or more records that randomize to a particular storage position.
Bell termed this 'secondary clustering' and showed that, by using both the quotient and the remainder from the original division, it was possible to eliminate it.

These two techniques are primarily intended for use in table searching in main storage, and are only incidentally usable for direct files; it is worth noting that they are intended to eliminate the order-preserving properties of division, while using division as a convenient randomizing algorithm.

#### Examples of randomizing algorithms in practice

Although small files cannot be used to analyse the way in which randomization techniques perform, they are useful to demonstrate the essential features of these techniques.
The ways in which division, mid-square and end-folding operate are illustrated below.

##### 1 Division

Assume that a 'mini-file' of seventeen records is to be stored as a direct file, and that the file is to be 85 per cent packed.
The file will therefore require twenty storage positions.
Seventeen random numbers in the range 000 to 200 (representing the record keys) can be selected by choosing the first numbers within the required range occurring in a random number table.
They are in the following order: 059, 035, 078, 136, 171, 148, 005, 135, 010, 196, 057, 187, 110, 100, 030, 127, 197.

These numbers are divided by 19, to give remainders in the range 0 to 18.
This leaves the twentieth position of the storage area as an 'overflow', since no record will randomize to it.
In effect, the key range 000-200 is cut into 19 digit sections, and the remainders that result from the division in each section are superposed on each other to provide the record addresses.
The records in the same section cannot randomize to the same address, so that synonyms arise by records in different sections having the same remainder.

The result of this operation, for the keys given above, is shown in Fig. 6.5 (a).

As a result of dividing by 19 there will be six synonyms - 00, 02, 02, 05, 15 and 16.
This is [UNK] or 32.4 per cent of the total, and compares with an 'expected' value of 32.63 per cent.
This is sheer chance, but suggests a good average result from the use of the algorithm!

This set of keys is intended to be random and so has no order to preserve.
If a key includes fields to indicate district, stock classification or the like, runs of keys will occur in the key sequence.
Division will avoid keys in the same run clashing, and causing synonyms.
Seventeen records are to be stored as an 85 per cent packed direct file.
Consider the key set: The remainders after the division by 19 are shown in Fig. 6.5 (b).

The very good performance of division reported in some cases (Lum, Yuen and Dodd, Severance and Duhne), and relatively poor performance in others (Kaimann), is likely to have been the result of few or many clashes of this kind.
Because there are fewer runs of keys than separate keys, the results of division are likely to be more variable than those of genuine randomization.
However, division has a fundamental advantage, which is the reason for its good performance: no two records in any single section into which the key sequence is 'cut' by division can interfere with any other in the same section, because no two different numbers can have both the same quotient and the same remainder.
Effectively, this means that if the file has been 'cut' into m sections, the effective packing density of the file - from the point of view of records colliding and causing synonyms - is:

##### 2 Mid-square

In this case we square the whole key and take a centre part of it to allocate the records to buckets.
In order to fit the result of selecting two decimal digits (a maximum value of 99) into a range of twenty storage positions, 20 is subtracted repetitively from the two digits until the result is less than 20.

This process gives eight synonyms (00, 02, 02, 04, 08, 10, 10, 10).
It is rather unexpected that most of the values obtained are even.
This is not a general result, and shows that this algorithm, which gives [UNK] or 47 per cent of synonyms, does not suit this key set.
The reader might like to check that, if the second and third digits are used instead of the third and fourth, there will be seven synonyms instead of eight (00, 01, 01, 04, 09, 12, 12).
However, this is still not a good result.

Applying the same algorithm to the other key set, the results are shown at the top of the next page.

This gives a reasonable result in terms of synonyms: six out of seventeen, or 35 per cent.
The reader may care to confirm that, if the third and fourth digits are selected instead, there will be eight synonyms.

##### 3 End-folding

Usually we would be satisfied with the results of one or other of the first two techniques.
Out of interest, we will try one other method on these key sets - end-folding.
This involves 'folding' one part of the key under the rest and adding.
If the value we get is more than 19, we will subtract 20 repetitively until it is brought into the range 0 to 19.
For example: Interestingly, this creates only four synonyms, and is thus a very effective algorithm.

With the five runs of keys, the resulting addresses are:

Here, the number of synonyms is three.
In general, end-folding does not achieve such good results, but this illustrates how - with a very small 'file' and key size - results can be variable.
In this case, due to the form of key and the end-folding digits chosen, end-folding is acting very similarly to an order-preserving algorithm.

### 6.5 Testing for successful randomization

After an algorithm has been selected, it is wise to ensure that it will be successful before using it in a program.
A reasonable guide will be if it produces results near to or better than those predicted by equation (6.3).
The algorithm and the file keys have to be analysed, which can be done either by writing an analysis program and inputting the keys, transforming them into addresses and recording the numbers of synonyms, or by using a standard analysis program.
This is obtainable from manufacturers or from many bureaux, and will give numbers of synonyms, their distribution and comparisons with the 'ideal' randomized distribution.

Kaimann has carried out a series of randomizing experiments, based on a file of 48 950 records.
These were randomized to 100 000 storage positions.
We shall examine the results of his experiments and compare them with the results that we would expect if the records were perfectly randomized.
In order to decide this we shall calculate the expected probability that an address will contain no record, one record only, one synonym (two records allocated to one address), two synonyms and so on.
It was stated earlier that the Poisson distribution was a satisfactory approximation to the binomial in a case such as this; to test this assertion both equation (6.2) and equation (6.3) have been used to calculate the expected 'perfectly randomized' results.

Using equation (6.2) derived from the binomial theorem, the probability that an address will have x records allocated to it is: Now: Thus [UNK]

This looks formidable, and the probabilities for higher values of x are complicated to calculate.
However, an iterative method of calculation can be developed from equation (6.2) as follows:

Using equations (6.6) and (6.7) we can calculate a starting value, p (0), and a factor by which this and each succeeding value is to be multiplied to yield the next value.
This is [UNK] This binomial figure is relatively easy to calculate, but the Poisson values derived from equation (6.3) are a great deal simpler, in particular the starting value p (0).
Equation (6.3) stated that: From this: Dividing the probabilities for x and (x - 1):

As the Poisson calculations also provide general rather than specific figures, it would be preferable to use them if there is no reason to reject the results.
Using equations (6.9) and (6. 10) the required Poisson values can be calculated very rapidly; they are particularly suited to a pocket calculator, as the starting value can be calculated and then modified by multiplying the contents of the calculator by the packing density and dividing by the next value of 'x': 1 when the calculator holds p (0), 2 when it holds p (1) and so on.

The values obtained for binary and Poisson probabilities are shown in Table 6.1 for the case where a file of 48 950 records is randomized to 100 000 storage positions.
It is clear from the table that the correspondence between binomial and Poisson values is very close.
For a file of this size, no value has been altered materially due to the simplification of using Poisson values.
In any real case a variation of several hundred from the predicted value would be expected due to chance alone, while predictions based on the two methods do not differ by as much as one record in any file examined by the author.
For this reason the simpler and more general Poisson calculations are used from now on in this book.

One of the most comprehensive studies of the results of randomization trials that has been reported was due to Kaimann.
The values tabulated [UNK] here give us a measure of comparison for Kaimann's experimental results.
Fig. 6.6 shows the theoretical curve for the values of p (0) to p (7), taken from Table 6. 1, plotted against equivalent curves for the following techniques:

- 1 The remainder after division by 100000, i.e. the last digits of the nine-digit key.

- 2 The five high-order digits of the key used directly as an address.

- 3 The middle five digits of the square of the key.

- 4 Five of the six junior digits, discarding the thousands digit and combining the rest.

- 5 Five of the digits from the nine-digit key, two from the first five and three from the next four, e.g. for 987 654 321:

- 6 The remainder after division of the key by the largest prime under 100000 (99 991).

Table 6.2 shows the number of addresses that have been allocated the stated number of records per address (up to seven), and the percentage of the total number of records in the file that was successfully allocated by each of the six algorithms used by Kaimann.

The very wide differences between the results achieved by different randomization techniques are shown in Table 6.2 and Fig. 6.7.
However, none of the results given here indicate randomization that is fully successful.
It is interesting that a fairly ad-hoc method of transformation (Test 5) is in most respects more successful than division by a prime number.
This suggests that by chance some underlying order in the key sequence has affected randomization.
However, the number of long synonym chains is less after division by a prime than by this digit selection.
A further search for a successful algorithm - probably for a more suitable prime - is indicated in [UNK] [UNK] a case like this.
As the key range, nine digits, is potentially 10 000 times the address range, 100 000, even division can only be expected to equal or very marginally improve on perfect randomization.

### 6.6 Minimizing the effect of synonyms

Now that the inevitability of synonyms occurring has been made clear, we must consider how to deal with them.
This can best be described in a series of steps:

- 1 Ensure that the number of synonyms is at a minimum.
This can be achieved by the selection of a suitable bucket size, packing density, randomizing algorithm and record-loading technique.

- 2 Use an efficient method of storing and retrieving the synonyms generated.

- 3 Arrange that the most frequently referenced records are in the home positions.

- 4 Reorganize the file at intervals - unless a randomization technique that allocates space as it is required has been used.

Each of these measures is examined in detail below.

#### Minimizing the number of synonyms

##### Packing density and bucket size

If we decide to store each record in a storage position able to hold only one record, even a perfectly random distribution will give a high proportion of synonyms.
Table 6.3 has been calculated using equation (6.6.).

The table is built up by calculating p (0), and hence the probability that any given address would not have a home record allocated to it.
Multiplying this by 100 and subtracting the result from 100 per cent, we obtain the percentage of addresses that will contain home records.
This is shown in the second row.
Subtraction of this figure from the total of all the records as a percentage of the addresses, i.e. from the packing density, gives the number of synonyms as a percentage of the addresses.
This figure is expressed as a percentage of the records in the bottom row.

For 30 per cent packing the calculation is as follows:

A glance at the percentages of synonyms shows that even when the file is [UNK] only 20 per cent packed, almost 10 per cent of the file will be stored as synonyms.
When we wish to retrieve a synonym, the algorithm will give an 'incorrect' address.
Whatever method of storing synonyms is used, time will be lost as a result.
Some way must be found to reduce the number of synonyms, in order to increase the efficiency of direct retrieval.

If buckets large enough to hold several records are used, we can expect that these buckets will be more evenly filled than individual records fill single addresses; this can be examined using the Poisson distribution.

Equation (6.3) for randomization to individual addresses is: Let the number of buckets be B; then during a single address calculation each bucket location has a probability of being generated of (1/B), and a probability (1 - 1/B) that it will not be generated.
Assuming the number of buckets is large, the Poisson distribution can once more be used as an approximation to the binomial distribution.
Then: Note that the value (n/B) will now usually exceed unity, and that the packing density of the file will depend on how many records can be stored in each bucket.
To calculate p (0) substitute (n/B) for (n/N) in equation (6.8): and also, modifying equation (6.9):

The percentage of records that will be stored as synonyms, for any given bucket size and packing density, can be derived as follows (the full explanation of the calculations is given in reference 15):

Let the packing density be p and the number of records per bucket be r.
The percentage of synonyms to be expected for any given case, assuming that record allocation to addresses is entirely random and that synonyms are only stored after all home records, is as follows:

Define the total file storage capacity as 1.
The sum of the probabilities for space to which records have not been allocated, P EMPTY, is: The rest of the total file area must therefore hold home records, i.e. [UNK] (Note: The proportion of the file area that contains home records is calculated indirectly rather than directly, because the sum of home record probabilities is made up of an infinite series, while that of the empty positions is finite, as is clear from equation (6.13).)

As the packing density is α, a proportion α of the total file area will hold records when the loading process is complete.
The probability of a record becoming a synonym is therefore given by subtracting the proportion of the file area occupied by home records from the total proportion of the file area taken up by the file, that is α.
[UNK] The user will normally wish to express this as a percentage of the records loaded, which is: The value of P SYNONYMS can be calculated using an iterative procedure by combining the expressions given in equations (6. 13) and (6.15):

This expression can be summed iteratively, as the first term within the brace has the value [UNK].
Let this be [UNK].
Then each successive term is obtained by using the relationship:

Table 6.4 shows the expected percentage of overflow records when records are randomized to buckets containing from one to 600 records.
The table shows figures down to 0.01 per cent of synonyms, and Fig. 6.7 is useful for extrapolation between values, and understanding the overall relationship between bucket size and packing density.

From the table and figure, it is clear that far fewer records will be displaced if we randomize to a multi-record bucket rather than to an individual record position.
For example, with a file that is only 50 per cent packed, we must expect 21.31 per cent of the records not to be stored in their home record positions if we randomize to a specific address.
Using buckets capable of holding only two records will improve this figure to 10.36 per cent.
If we use buckets of eight records at a time, less than 1 per cent of the records will be synonyms, and this is reduced to 0.
1 per cent for buckets of fifteen records.

Hence it is clear that, if records are randomized to individual storage positions or to small buckets, many records will become synonyms.
Unless the records are stored singly there is no corresponding improvement in speed of finding the desired record, because the access comb will reach the track at a point decided by chance, and there will be an average delay of at least half a revolution before the start of the record is reached.

The advantage of single records is that they can be stored in CKD format - with separate keys - and the track can be scanned for a particular record without having to read unwanted records into main storage.
Multiple record buckets cannot be handled in this way, as groups of records that randomize to the same bucket do not generally have anything else in common, so that the whole bucket has to be searched to see if the desired record is in it.
So, although there is clearly an argument for using buckets that are as large as possible, over-large buckets will mean that an extended search through the bucket will be required to locate the desired record.

Since there are advantages both in storing records singly and in using large buckets, one solution is to randomize to a track but to store records singly in CKD format.
This is particularly useful when manufacturers' software is available (as for example SEARCH ON KEY for IBM computers) to carry out the search automatically.
Although a number of writers suggest that [UNK] a full-track bucket is always too large, they are talking of a bucket that has to be transferred as a whole into and out of main storage.
The solution suggested above allows the very low synonym levels of a multi-record bucket - in this case a track - to be combined with the CKD format of individually stored records, which makes it possible to search the whole track and retrieve only the desired record.
As very few records will not be on their home tracks, this procedure is extremely efficient.

Fig. 6.8 shows how increased bucket size delays the onset of synonym occurrence in a well randomized file.

The curves show divergence from the relationship [UNK] (for n records stored individually), (for records stored in buckets with a capacity of [UNK] ten records), and [UNK] (for buckets with a fifty-record capacity).
They thus show the number of synonyms created, assuming a perfect randomizing algorithm, for various packing factors.
Randomizing to buckets with a capacity of ten records markedly decreases the number of synonyms, and there is a further decrease if buckets with a capacity of fifty records are used.

Appendix 5 provides extended synonym tables and curves for more precise work in this field.
In general, the file designer will choose a bucket size and packing density that reduce the percentage of synonyms to an acceptable level, bearing in mind the increased retrieval times large bucket size can cause.
As is made clear below, bucket size may also affect the algorithm chosen.

#### Randomizing algorithm

In choosing an algorithm, the file designer will aim to minimize the number of synonyms.
The key type and format should be assessed, to decide on the occurrence and frequency of runs of keys.
The range of key values, divided by the number of addresses to be generated (the calculation is shown on page 161), will indicate the potential improvement, over and above the synonym percentages predicted by the Poisson distribution, that can be aimed for.
practical trials will indicate the success of any algorithms the designer selects, and this step in file design should never be omitted.

For general guidance on choice of algorithm, the author has compared the number of accesses observed by Lum et al.
in practical trials with the theoretically predicted number, for buckets holding five, ten, twenty and fifty records.
The results of this comparison are shown in Fig. 6.9.

As can be seen from the figure, for buckets holding five records division is not as effective as mid-square (which closely approximates the 'theoretical' figures) for packing densities above 0.7.
For buckets holding ten records, division is superior up to a packing density of about 0.85, while for larger bucket sizes division is more efficient at all packing densities.

In general, the success of a randomizing method is partly dependent on the technique used to store synonyms, and this will be discussed further in a later section of the chapter (see p. 184).
However, it is fair to say that division is usually the most efficient technique if synonyms are to be handled by chaining or tagging, but that if they are to be stored using the consecutive spill technique, bucket size and packing density should also be considered before a decision on randomizing method is made.

Before leaving randomizing algorithms, it should be made clear that the treatment of them here is based on the assumption that the file size, once created, can only be altered when the file is reorganized.
Records can be added of course, but this will increase the packing density.

There is a great deal of interest at present in developing hashing algorithms for files that may vary in size.
This is usually termed dynamic hashing; a particularly useful review of these techniques is given by Sachs-Davies et al., describing both extendible hashing, in which a set of buckets [UNK] is referenced via a directory, and linear hashing, which is genuinely a direct technique in that there is no directory.
Both of these methods suffer from oscillations in performance associated with their mode of action, and neither performs as well as'static' randomization methods.

A form of extendible hashing that does not suffer from oscillations and is claimed to outperform most indexing methods, was reported by Lomet He named the method bounded index exponential hashing; it is not strictly a direct technique, and suffers from the drawback that the file packing density is generally low, but offers many advantages for files which can grow at a rate that cannot be accommodated in a static system.

Designers looking for examples of how to code randomizing algorithms should consult Snader, who gives examples of various functions coded in Fortran, Basic and Pascal; Morris, who gives Fortran code both for chaining and hashing; and Johnson and Cooper, who provide comprehensive coded examples in COBOL.

#### File loading

When a direct file is loaded for the first time, we may have little or no information about the individual records that make it up.
However, it is still possible to keep the number of synonyms to a minimum.
Records will be read into primary storage, their keys will be transformed by the algorithm being used, and if the address the algorithm produces is free they will be stored in that address on the direct access device.
When a record turns out to be a synonym, there are two alternatives: these are to store the synonym at once, in which case the process is called a one-pass load, or to load it in two passes, which is called a two-pass load.
A one-pass load will result in the creation of unnecessary synonyms, as shown in Fig. 6. 10.

To avoid the creation of extra synonyms, the file has to be loaded in two passes.
On the first pass, all the home records are loaded, but synonyms are not.
On the second pass, all the synonyms are loaded.
This process maximizes the number of home records in the file, and so maximizes the number of records that can be retrieved without further searching.

All the calculations carried out so far have assumed that it is possible to allocate any number of records to a given address.
This is implied in the calculations, as no allowance has been made to store the synonyms that arise in other free addresses.
Instead, the number of synonyms has been calculated, but they have then been ignored by the mathematics, and so have not interfered with the 'storage' of other records.
This is precisely the process that occurs during a two-pass load, as the synonyms are stored on the second pass.

Although the calculations available in the literature have very largely assumed that direct files are loaded using two passes, there are a number of cases in which a one-pass load occurs in practice.
These are:

- 1 If a simple one-pass load is used for the file.

- 2 Whenever records are added to an existing file, as both home and synonym records from the original load have already been stored; in this case the probability of an addition that is a potential home record being prevented from taking up its home position by a synonym that was loaded earlier is high.

- 3 In databases that offer the CALC option - as each record is loaded when it is added to the database, whether it is a home or synonym.

To estimate the number of synonyms that occur during creation of a direct [UNK] file using a one-pass load, let us examine the result of storing n records at random in N addresses, on the assumption that each record has to be stored at once and each address can hold only one record.

The first record will be stored in its calculated address.

The second record has a probability of 1/N of becoming a synonym.

The nth record has a probability (n - 1) /N of becoming a synonym.

Summing this series of probabilities, and dividing by the number of records loaded, we obtain:

For files of more than a few hundred records, ½N can be ignored.
Thus the proportion of records stored as synonyms will be roughly equivalent to half the packing density in a file created using a single-pass load, and with single record buckets.

The author has developed an iterative method of calculating the synonym percentages that would be expected as a result of loading buckets of various capacities to a range of packing densities.
These results have been confirmed using simulation techniques, and are given in Table 6.5; they should be compared with Table 6.4.
The divergence between the two loading techniques depends on packing density, and for single record buckets it is almost 10 per cent - one record in ten - for an 85 per cent packed file.
Although the difference is less marked for multiple record buckets, it is still significant.

To provide quick reference for the file designer the data in Table 6.5 has been plotted in Fig. 6.11.

As the penalty that a one-pass load imposes in terms of extra synonyms is very quickly understood when it is shown visually, Fig. 6.12 compares the results of one-pass and two-pass loads for a number of bucket sizes.

#### Storing and retrieving synonyms

When a record cannot be placed in its home position, it must be stored at an address that can be located quickly.
There are three widely used methods of doing this and we shall look at each in turn, assessing their advantages and drawbacks.

##### 1 Consecutive spill (also called progressive overflow)

The simplest method of storage is to place a synonym in the first vacant record position following its home address.
(This applies in just the same way if records are being randomized to multiple records buckets.
The record is stored in the first bucket with available space following the original home bucket.)
This method of storage, in which there is no link or pointer to the synonym from its home bucket, is called consecutive spill or progressive overflow.
Record retrieval takes place as follows.

- 1 Seek the home address.

- 2 Check whether the records or records in the home address have the required key.

- 3 If not, search the rest of the track.
If the record is not found on the track, search the rest of the cylinder.
Note that, if the key that has been requested is not present on the file, the unsuccessful search length is potentially limited only by the size of the file.

Very few records will not find a place anywhere on the cylinder.
Take for example a file that is 90 per cent packed, and can hold 250 records per cylinder.
In this case the cylinder can be treated as a very large bucket.
From Table 6.4, 99.86 per cent of records will be stored in their home cylinder and only 0.14 per cent will overflow on to another cylinder.
As the packing density is usually lower than this and the number of records per cylinder greater, overflow from a cylinder is not usually a problem.
It is shown in [UNK] Appendix 7 that, for a cylinder holding one hundred records and with other conditions as given above, the average retrieval time for all the records in the file will be 0.78R, where R is the rotation time of the device.
This compares with 0.5R for a self-indexing file.

A potential drawback of consecutive spill is that, while this method of handling synonyms can be effective in some circumstances to retrieve records that are held in a file, it is not a good method of dealing with records that are not in the file.
As there is no way of knowing how many synonyms exist for any given home address, an unsuccessful search might require half the file to be scanned on average.
The usual way to limit this search commitment is to place a synonym in any free position on its home cylinder, and in an independent area if no free space can be found in the cylinder.
A second method is to note the longest search required to find a free storage position when synonyms are stored, and to limit searches to this length during retrieval.

##### 2 Chaining

The second method generally available for synonym handling is to chain together all the records that randomize to the same address.
A chain takes the form shown in Fig. 6. 13.
The home record storage area holds the address of the first synonym.
This holds the address of the second synonym, and so on.
A null link indicates the end of the chain.

If it is found that the home record is not the one required, the link address is used.
This points to the second record that randomized to the home address.
The chain is followed until the desired record is located or the end of the chain is reached.
It eliminates the need to search the file sequentially.

The calculations involved in assessing the effect of chaining synonyms are complicated.
For that reason they are given in detail in Appendix 6, The Effect of Synonym Storage Techniques on Search Times.
Only the conclusions are discussed here.

Records randomized to individual record positions, with 90 per cent packing and ten record positions per track, give the following figures:

This shows that about one record in every 500 (0.2 per cent) will be part of a chain of six records.
Of these, one-sixth (0.03 per cent) will be home records and an equal number will be first, second, third, fourth and fifth synonyms.
At this packing density the average search time for a given record is 0.732R, where R is the device rotation time.

When records are randomized to larger buckets - in this case we will examine ten record buckets - this will cause fairly long chains.
Fig. 6.14 shows the pattern of record allocation for 80 per cent and 90 per cent packing.
Buckets can hold ten records only, and any further records 'allocated' to a bucket will become part of a synonym chain.

Fig. 6.14 shows that quite long chains must be expected.
For 90 per cent packing, just more than one bucket in every 200 (0.53 per cent) will have a chain of eight or more synonyms.
A more detailed analysis shows the following:

As 91.4 per cent of records will be located in their home buckets, the advantage of having relatively few synonyms outweighs the disadvantage of there being some long chains.
The average search time for 90 per cent packed records stored in ten record buckets is 0.654R.
This figure is a great deal better than that for the consecutive spill method of handling overflows, and even chained records randomized to individual addresses show an advantage over consecutive spill.

A price has to be paid, however.
To provide the links, an extra field has to be added to the home bucket or home record, and an extra field to each synonym.
This effectively reduces the file packing, and may also cause fixed lengths to become variable in length.
The last point could be put right, wasting more space, by adding a potential link field to every record.
This might then be used when necessary, but be left empty in other cases.
If the problem of providing space for link fields can be suitably handled, this method can offer considerable savings.

##### 3 Tagging

One difficulty when processing linked records is that, if a record in the centre of a chain is inadvertently overwritten, the end of the chain is 'lost'.
This can occur when adding records to the file.
The third method of handling synonyms avoids this.
It is called tagging.
The technique used is to tag each synonym individually from the home address.
Each tag will have to hold at least the information: This will mean that the few home addresses or home buckets which have large numbers of synonyms will have to allocate a lot of space for these tags.
An example of the situation where there are five synonyms for a home record is shown in Fig. 6.15.

The tag system uses a little less space than the chaining system, as there is no need for a terminal 'link' field at the end of the chain.
However, all the extra space is required in the home records.
This can make planning and file creation difficult.
If these problems can be overcome, it offers two advantages that chained overflow record handling does not.
Firstly, the file organization is more robust, as the accidental overwriting of a record only affects that record itself and not other members of a chain.
Secondly, it is never necessary to carry out more than two searches to locate a record.
These are:

- 1. Search home record - if record not found pick up address from tag;

- 2. Search the address shown in the tag.

Using the example of a 90 per cent packed file with single-track buckets that can hold ten records: from Table 6.4, 91.4 per cent of records are located on their home tracks.
Thus 8.6 per cent of records will require a full revolution of the home track, then a pick-up of the address required from a tag, then an average of R/2 while the record is located.
The overall time required for the search will be:

If the records are stored on a 25-track cylinder, Table 6.4 indicates that 0.14 per cent of records will overflow from the cylinder, i.e. will not be held in a 250-record bucket.
Although the tags will point to the required record addresses directly, accessing or retrieving these synonyms requires a head movement of at least one cylinder.
Assume that the time to move from one cylinder to the next is the same as the rotation time of the device, which applies for some disk devices.
This will mean an increase in the average access time of 0.0014R.
Thus the total average access time is:

#### Comparing the techniques in practice

It might appear that chaining or tagging would always be preferable to the simpler system of storing records in the next available position.
In practice they do not always turn out so much better, for a number of reasons.
These include the following:

- 1 When records are stored in the next available position (i.e. using consecutive spill), no extra space is required for chain or tag fields.

- 2 Manufacturers' software is usually available for a SEARCH ON KEY operation throughout a whole cylinder.
The search for a required record can start on the home track and continue until the record is located.
There need be no holdup due to consecutive spill storage, however short.
By comparison, following a chain or tag involves reading the link field, finding the key in it, picking up the address and searching for it.
This will be carried out at primary storage speeds, but will still take time, often due to lost device revolutions.
A home track and a track holding synonyms will appear as shown in Fig. 6. 16.

Examining chained records first, tracks with spare space for the storage of synonyms often have room for a number of records, as is clear from Fig. 6. 14.
Tracks that have overflowed during the original file load will not have any synonyms from other tracks present on them, which explains the likely track formats shown in Fig. 6.16.
In some cases members of the chain may directly follow each other on a track holding synonyms.
This could cause the loss of a whole revolution for each member of the chain, because the processing of the link field might take long enough to miss the start of the next record.
This would happen as shown in Fig. 6.17.

The tagged records case is straightforward.
The tag is picked up at the end of a track and the synonym will also, on average, be at or near the end of a track, not in the middle.
For this reason the time required to pick up the tagged record may be rather more than R/2.
This depends on the manufacturers' software.
Sometimes the start of a track has to be sensed before processing of the data stored on it can begin.
This will lead to delays.
In some systems, tag or chain link fields are stored at the start of a track, which will reduce delays caused for this reason.

Lum et al.
investigated the performance of a number of large files, and the author has analysed their results further.
Fig. 6.18 shows a plot of Lum [UNK] et al.'s figures on the basis of average accesses per retrieval; it appears from the curves that consecutive spill is only useful for larger bucket sizes, but the figures are misleading, as the chained overflow was to a separate file area, necessitating head movement.
Table 6.6 shows the very different results obtained when the actual time required for each retrieval, including head movements, is used to calculate break-even points, rather than average accesses per retrieval.

Although most of the work reported in the literature has examined chaining to a separate overflow area, this is not the most effective way of using chaining.
If records are stored in the next available position in the prime data area - the consecutive spill method - but a link field is provided from the home record or from the last synonym, this avoids unnecessary head movements and cuts down the search time required for the consecutive spill techniques.
Table 6.7 compares the additional times added to an average record seek due to consecutive spill (for files using mid-square and division randomizing techniques), chained overflow in a separate area and chained overflow in the prime data area.

The results tabulated here show that, for low packing densities, the most effective technique is generally chained overflow.
At higher packing densities a separate overflow area may be useful for small bucket sizes, while chained overflow in the prime data area remains best for large bucket sizes.

#### Choosing an overflow technique

Tagging is superior to chaining whenever it is feasible (see Appendix 6 for an analysis).
Very large numbers of synonyms for even a few home addresses can make it impractical, however.
The distribution of records produced by a given algorithm should be checked to see that this will not occur.
If it is unavoidable, chaining should be employed (assuming, of course, that the packing density is too high, and bucket size too small, to make consecutive spill attractive).

In general, consecutive spill should be considered for low packing densities and/or very large bucket sizes.
In the intermediate range of these factors, chaining or tagging records stored in the prime file area is the most efficient solution, while at packing densities in excess of unity a separate overflow area will be required.
Although many writers recommend it, it is seldom worth using such a separate overflow area when the packing density is below unity.
The packing density referred to here is measured in terms of the total number of records, both in the prime and overflow areas, divided by the prime data storage capacity only.

### Reducing the effect of synonyms on access times

The analysis of the last section has shown that synonyms will slow up direct access to records on average.
The average figure means little in this case, however.
Access to home records only requires a single seek and search, just as in self-indexing files.
This is increased for any synonym by at least half a revolution of the device.
There are at least as many home records as synonyms in all circumstances (Table 6.5 shows that, even with 100 per cent packing and randomizing to individual record positions, 50 per cent of records are home records; with a two-pass load 63 per cent are home records).
If all records are accessed equally frequently, the effect of any synonyms will be directly proportional to the figures in Table 6.4.
However, this is a very unusual state of affairs.
Normally, some records are accessed more frequently than others, and this tendency can be used to decrease average access time.
The potential improvement in performance and ways of achieving that improvement after a two-pass load are discussed below.

#### Patterns of record access

A rule-of-thumb often used for updating is that '20 per cent of the records give rise to 80 per cent of the transactions'.
It is certainly true that, in most applications, some records are processed far more frequently than others, and a number of commonly occurring distributions of update frequency are examined below.

- 1 The 80/20 arrangement.
Assume that 20 per cent of the records are equally frequently accessed and give rise to 80 per cent of the total transactions.
The remaining 80 per cent of the records are also equal in update frequency, but account in total for only 20 per cent of transactions.

- 2 A smooth curve of accesses in which some records are updated more regularly than others.
The case shown in Fig. 6.20 is taken as an example of a very frequently met distribution (it is probable that the original 80/20 rule-of-thumb is based on a similar curve).

- 3 A random distribution.
In this case a few records are updated very frequently, a few very seldom, and most records are updated more or less an average amount; the distribution is shown in Fig. 6.21.

This is not meant to be a comprehensive list of possible situations; the intention is to show how to tackle any distribution that occurs in practice.
A limitation must be mentioned here.
It is not possible to improve on equal access synonym handling in two cases.
The first is when all records are equally likely to be accessed, i.e. there is no difference in access frequency to exploit.
The second is when there is no permanent pattern.
If a record that is updated or accessed frequently in one time period is likely not to be referenced at all in the next, any analysis breaks down and the equal access assumption is the best guide for design decisions.
Usually there will be some random variation of this sort superposed on a relatively constant overall pattern.
In examining the effect of the patterns defined above, random influences will be ignored.

Each of the three cases will be examined for 90 per cent packed files, randomized to individual record positions and to a bucket that can hold ten records.

1 The 80/20 case When 20 per cent of the records generate 80 per cent of the accesses to a file, and the file is loaded in a random order, the percentage of accesses to synonyms will be the same as the percentage of synonyms; if the file is 90 per cent packed and randomized to individual record storage positions, accesses to synonyms will be 34.063 per cent of all accesses.

If the 20 per cent of records that are most accessed are loaded first, the situation is quite different.
As the file will be 90 per cent packed when it is fully loaded, 20 per cent of the records will occupy 18 per cent of the available storage addresses.
This 'mini' file will have 8.483 per cent of synonyms, so that the 80 per cent of accesses made to these records will be split in the proportion of 91.517 home accesses to 8.483 synonym accesses.

When the whole file has been loaded, it will contain 34.063 per cent of synonyms.
However, as the first fifth of the file (20 per cent) only contained 8.483 per cent of synonyms, the four-fifths of the file loaded later must have a higher average number of synonyms than 34.063 to bring the overall average to that figure.
Let that higher number be y.
Then: Hence, the four fifths of the file loaded later contains 40.458 per cent of synonyms, and 59.542 per cent of home records; the 20 per cent of all accesses to the file that are to these records will therefore be split in this proportion.
The total accesses to home and synonym records will thus be as follows:

By loading in access frequency order, the accesses to synonym records - and these are the records that slow up the average retrieval times of the file - have been cut from 34.063 per cent to 14.878 per cent.
This reduces the effect of the synonyms to a figure that could have been achieved by choosing an initial packing density of just over 33 per cent for the file - but this file is 90 per cent packed.

Fig. 6. 19 shows the improvement that can be achieved in 80/20 type files - those in which 80 per cent of the accesses are to 20 per cent of the records - for buckets holding one, two, three and four records over a wide range of [UNK] packing densities, and Table 6.8 provides figures for a number of bucket sizes and packing densities.

These curves and figures apply only to the 80/20 case.
A general expression to assess the potential improvement that access frequency loading can provide for any case in which A per cent of records account for B per cent of accesses is derived below.
It should be made clear both that (A + B) does not need to add up to 100 - it is an unfortunate chance that the 80/20 or 90/10 'rules' are so well known - and that access frequency loading will only be of benefit when A is less than B. If A were greater than B, meaning that the less active records were loaded first, file access times would be poorer than those of randomly loaded files!

The following symbols will be use in the derivation:

- A is used for the per cent of records loaded first.

- B is used for the per cent of accesses made to A (in total).

- α is used for packing density.

- r is used for bucket capacity:

- S is used for synonym per cent.

Suffices of S are equations that will be evaluated in any given case to give a packing density, followed by r to indicate bucket size, so that the correct synonym percentage can be calculated or looked up.

The percentage of synonyms when A per cent of the file has been loaded is [UNK]

As these records have given rise to B per cent of accesses, the percentage of references to synonyms from these records will be [UNK]

After the remaining records have been loaded, the percentage of synonyms in the whole file will be [UNK].
Of these: had been loaded previously so: have arisen from (100 - A) per cent of the records, and the percentage of synonyms in these later records is: These records will give rise to (100 - B) per cent of the total accesses to the file.
Thus the percentage of references to synonyms from these later loaded records will be: This simplifies to: Combining equations (6. 19) and (6.20), the total accesses to synonyms will now be: For the case in which A = B this equation simplifies to [UNK], as would be expected.

As [UNK], which is approximately true for large values of r, the value of equation (6.20) tends to [UNK] This compares with the value [UNK] if records are stored in random order.
Division of equation (6.22) by [UNK] to show the improvement expected after access frequency loading, yields (100 - B) / (100 - A), i.e. the general equation of which the value ⅓ for the 80/20 case is an example.

When A per cent of records that give rise to B per cent of accesses is loaded first, the improvement obtained tends to (100 - B) / (100 - A) as [UNK].

Table 6.8 shows the percentage of accesses to synonyms to be expected for various bucket sizes, in the 80/20 case.

Many situations cannot be handled on the basis of 'A per cent of records give rise to B per cent of accesses'.
For this reason two other common situations are analysed here.

2 A smooth access curve Fig. 6.20 shows a histogram of records divided into nine groups of equal numbers.
The most active group accounts for 43 per cent of accesses, the least active for 1 per cent.
It is no longer enough to divide the records into two groups, and the analysis has been carried out on the nine separate groups of records responsible for 10 per cent, 20 per cent, 30 per cent..., 90 per cent packing.

As the calculations required in this case are complex, they have been set out in Appendix 8.
The results show that a 90 per cent packed file of this type loaded in access frequency order into single record buckets will achieve a [UNK] reduction from 34.06 down to 16.63 per cent references to synonyms.
If instead the file is loaded into ten-record buckets, the reduction is from 8.59 per cent down to 1.36 per cent.

3 A random distribution If the records are very variable in their number of accesses, but this variation is distributed about a mean value, a curve such as that in Fig. 6.21 occurs.

There is an average number of accesses during a specified period of about sixty-five.
However, a small group of records have been accessed over 120 times, and another small group less than ten times.
To analyse this, the [UNK] frequency curve in Fig. 6.22 (case 3) is constructed relating the percentage of accesses to the file to the percentage of records loaded at any cumulative percentage of records loaded, using the methods shown in Appendix 8.

From the case 3 curve we can decide on the percentage of accesses corresponding to the 10-90 per cent packing points, i.e. 11.1 per cent, 22.2 per cent,... of records.
This can be used to calculate the required information; it turns out that the improvements that can be achieved by access frequency loading are to reduce accesses to synonyms from 34.06 per cent to 28.4 per cent for single - record buckets, and from 8.59 per cent to 4.90 per cent for ten-record buckets.

#### Assessment of possible improvement

The cumulative frequency curves for all three cases analysed earlier are shown in Fig. 6.22.
The more to the left of and above the dashed straight line a curve is, the more potential exists for improvement.
This can be seen by comparing the three cases discussed above with each other, and with the data for the 90/10 case, that has been included for comparison.

If in doubt as to the possible use of this technique, the user should collect enough data to plot a curve of this type.
A visual check will indicate whether improvement can be expected, and will give some indication of its magnitude.
In general terms, however, if there is a consistent access frequency pattern, this type of load will be of benefit.
Even in the third case analysed above, the use of an access frequency load is equivalent to reducing the packing density of the file by nearly 20 per cent, or doubling the bucket size.
This improvement can be achieved by collecting and using access data as explained on page 399.

#### Additions to access frequency loaded files

Additions to a file set up by loading in access frequency order will have a disproportionate effect on file access time; this is because they will be of at least average activity and often more, as new records tend to be very active, but are loaded into a densely packed file.
A high proportion of them will be synonyms - if the file is 85 per cent packed, for example, 17 in every 20 would be expected to be synonyms - and this will lead to rapid deterioration of the file access speed.

The key figure here is the number of seeks per access.
This will rise markedly as additions are made, and should be monitored frequently.
The deterioration to be expected has been analysed by the author, and results for the 80/20 case are given here.
Tables 6.9 (a) and (b) shows the result of access frequency loading up to 20 per cent, 30 per cent, 40 per cent, 50 per cent, 60 per cent, 70 per cent, 80 per cent and 90 per cent packing, followed by additions of records of average activity until the file is 100 per cent loaded.
The results are tabulated for ten-record buckets and single-record positions, and the rapid deterioration in both cases is very clear.

Fig. 6.23 shows the results of additions of average access frequency to an access frequency loaded file.
The dashed curves trace the results of a full access frequency load to 100 per cent packing, while the unbroken curves show the effect of adding records of average activity from the packing densities set into each curve.
In reality, as pointed out above, these curves are likely to represent a 'best' case, as additions to a file are usually new customers, products, personnel, etc. and tend to be highly active, while they also have a high probability of being synonyms.

Fig. 6.24 superposes the deterioration of access frequency loaded 90/10 files as a result of loading additional records in random order, on to an 80/20 file loaded in the same way.
The dashed and dotted curves do not intersect, which makes it clear that the rate of deterioration caused by adding records of average activity to an access frequency loaded file is only dependent on the starting point of the random load, and not on the particular file access situation, such as 90/10, 85/25, etc.

The situation has been explored in detail by the author, and Figs 6.25 and 6.26 are taken from that paper.
They provide the file designer with reference charts for buckets of size one and ten records, and can be used to predict the rates of deterioration of any access frequency loaded file using the given bucket sizes.
The unbroken curves show the improvements due to loading files with asymmetries in access frequency of 60/40, 70/30, 80/20, 90/10 and, for single-record buckets, 99/5.
These are provided for convenience, but the designer can use the charts from any point, and the slope of the broken lines indicates the rate of deterioration to be expected.
Similar curves for buckets holding 2, 3, 4 and 5 records are given in Appendix 1.

The figures against the broken lines correspond to the packing percentages from which a 90/10 case file has received random additions.
The broken curve shows the percentages of access to synonyms as more random additions are made, demonstrating how rapid the degradation is.

In this section we have seen that it is usually possible to reduce the number of accesses to synonyms by loading first the records most frequently accessed.
In cases where a small number of records is accessed very [UNK] frequently, the saving is marked, and may even be dramatic.
When a file is first set up it may not be possible to load in most frequently accessed order.
The savings that can be made usually justify the collection of statistics during the life of the file, and some ways of arranging this are described in the next section.

### 6.7 Practical considerations in setting up direct files

#### Preparing a device for a direct file

Self-indexed files will need little or no prior formatting of the direct access device on which they are to be stored.
It is essential to ensure that every storage position has been initialized, or at least to remove any data remaining from previous uses of the device.
In every other respect the file load will be a normal - and sequential - operation, except that some positions may be left vacant to retain the address/key relationship.

When files are randomly organized using an algorithm, the device must first be initialized to remove all prior data.
If this were not done, data from previous files might still be present in addresses to which records were not allocated.
If the records are to be stored in full track buckets, no formatting is required as the track address is available at all times.
However, if the records are to be stored in individual address positions, the addresses and record storage positions have to be created before the file is loaded.
This applies both for single-record positions and for buckets that are only part of a track in size.

Some manufacturers provide pre-formatted buckets of various sizes on a track.
In this case the user only needs to specify the bucket size required from the alternatives provided, as the formatting and addressing have already been carried out by the manufacturer.
However, it is then often necessary to read a whole bucket into primary storage at a time; it is not possible to search the bucket and read in only the required record, but this does not apply if a device such as ICL's CAFS-ISP is available to speed up the search.
Some manufacturers provide a capacity record at the start of a track, used to indicate whether space remains on the track during loading.
If this is not provided, the user will need to set up an equivalent record.

The load process will be:

- 1 Decide on the bucket size required.

- 2 Initialize the file area on the direct access device.

- 3 Pre-format the file area by setting up dummy records of individual record or bucket size, to provide all the addresses within the range that the address algorithm can generate.

- 4 Load the file.

#### File statistics

In order to get the best possible performance from a direct file, information is required.
Run times will give an indication that reorganization is due; access data will allow more efficient processing; service times will indicate the effect of user demand or the need for file reorganization; a log of the number of sequential processing runs required may point to the use of ancillary files or a different file organization technique.
We shall look at each of these in turn.

##### Run times

The basic criterion for the need to reorganize a direct file is that the number of seeks per access has risen appreciably.
When a direct file is being processed on its own, the run times for the file will point to this.
A predetermined figure should be set, and when this is reached the file should be reorganized.
This situation may come about in several ways.
First, the file may be growing.
If new records are added faster than old records are deleted, the packing of the file will get higher; as we saw earlier in the chapter, this will cause more synonyms.
Second, the randomizing algorithm may be becoming less useful due to some pattern in new record keys.
Third, many of the new records will have become synonyms; if they are relatively frequently accessed this may cause a marked increase in run times.
Van der Pool described what he called the 'ageing' process in direct files, pointing out that performance degrades over time due to additions, even if the packing density does not change.

Usually a direct file will be one of a number of files being processed at any time.
In this case the manufacturer's operating system may be used to keep track of the file run-time.
It is helpful to keep a count of references to home and synonym records.
This can be held in main storage during processing and be printed out on the log or stored in a file label area at the end of the run.
A figure for the ratio of seeks required per access should be specified on the basis of the design criteria used, and the file should be reorganized when this figure is exceeded.

##### Access data

It was shown on page 195 that knowing how frequently a record is accessed can lead to reduced seek times.
Usually we do not have this information when a file is set up.
There are two ways in which it can be provided for in later reorganizations of the file.
The first is to have a count field in each record, and increment it each time the record is accessed.
This has the advantage that records can be sorted into descending count order for loading during reorganization.

When records are being updated during the run, and so have to be written back on to the device after they have been read into main storage, this method involves no loss of time.
However, if records are only being referred to, the position is different.
A half-revolution would be lost for every record, just to update the count field.
In this case a second method of gathering access data is preferable.
It is to set up an ancillary file with the records in sequential key order and each record consisting only of a count field.
This file will be very small and, if indexed, it will usually match the access speed of a larger direct file because it can be held on a single cylinder of disk, with its index in main storage.

When the master file is to be reorganized, this ancillary file will be sorted into descending count order, and the records are read from the old direct file and loaded on to the new in this order.
The resulting master file will be in access frequency order.

Access data is only useful when records remain relatively constant in their activity.
This often happens, as large customers will always remain more 'active' than small customers, and some lines of stock are consistently required more frequently than others.
In other cases it is not true; for example, a flight will be available in an airline booking system long before it takes place.
At first, bookings will be few, then they will increase, and after the flight date the record will vanish.
Statistics of overall popularity of flights will help in planning, but the profile of interest in any one flight will vary with time.

However, some flights will naturally be more likely to be accessed than others.
A Boeing 747 flight between London and New York will always be a candidate for a home position.
A DC9 or BAC 111 cannot hold so many passengers and would tend to be loaded later.
Naturally, if a small aircraft is overbooked consistently, it might rate early loading.
In that case, it would also be likely to merit a larger aircraft.

In some cases no clear pattern emerges.
Then it may not be possible to load records in any predetermined order, and lower packing densities and changes in bucket size or type of algorithm may be needed to give an acceptable performance.

##### Service times

The access times considered in this chapter have been simply the time taken to position the device access mechanism to read or write a selected record.
In practice this is not complete, since two additional times need to be considered in order to obtain the true picture.

The first of these is the data transfer time.
This depends mainly on the size of the record and the operating speeds of the direct access device in question.
For example if the records took up half a track on a device with a rotation time of 25 ms (2400 rpm) then the data transfer would take about 12.5 ms.

The second is the time taken from the moment a record is requested by the program to the time when accessing and transfer takes place, known as wait time or queue time.
This may be zero, though in multi-programming or multi-tasking it is likely to be finite.
For example, if the direct file were being used by an on-line system there could be several concurrent terminal tasks at any one time using the file, and queues would then develop.
Indeed, some operating systems are geared to handling queues by offering the user a choice of queuing algorithm.

If the accesses on a file are completely random, it is often sensible to sort the accesses into cylinder address sequence and minimize individual seek times.
Input or output requests to a file are queued by the operating system and then sorted into sequence before any operations commence.
Updating of a direct file by sorting a batch of update records into their physical order after using the algorithm, and so avoiding the typical random sequence of seeks, can provide rapid 'sequential' batch updating.
This has been discussed by Nijssen.

##### Type of processing

Some files may be predominantly processed directly, but occasionally be processed sequentially.
If a file is self-indexed, this presents no problem.
If it has been randomized, then the process has to be reversed.
A list of keys in sequential order is fed into the program and the keys are transformed into addresses in the usual way.
Every synonym will need to be accessed, so no benefit will be derived from the order in which the records were loaded.

This may mean that a file which operates well under normal conditions, i.e. many home records being accessed but few synonyms, may take a relatively long time to process sequentially.
In such a case it can pay to set up an ancillary file when the file is loaded.
This will be a sequential or indexed-sequential file, in key order, with the actual device address of each record as the data.
This actual address will be identical with the key as transformed by the algorithm for home records, but will be different for synonyms, as the ancillary file used will allow all the records to be reached in a single seek, as if the file were self-indexed.

The use of such a file will eliminate extra searching for synonyms and may save a fair bit of time.
It will need to be updated whenever the direct file is updated if the file is very volatile, and this may require the two files to be on-line together.
If there are relatively few additions it may be updated in batch mode later.
This latter case will favour the use of a sequential magnetic tape file.
The former will tend to require an indexed sequential file on a direct access device.

#### Additions and deletions

Precautions have to be taken to avoid the possibility of excessively long search times or of failure to retrieve records held in a direct file.
When a file has been newly loaded, a search for any record will allow it to be retrieved whether it is a home or a synonym record.
Additions or deletions can change this situation.
An addition may nut he able to take up its home address, because it is already occupied by a synonym from some other address.
Deletion of a home record may mean that, even though the home position is now free, a number of other records that originally randomized to that address are held as synonyms.
Either of these cases may give the appearance that no home record exists for this address, and this situation will thus cause a 'no record found' error to be given, even though the desired record is in the file.

Thus, if the consecutive-spill method of handling synonyms has been used, a search may still be necessary even if no home record is detected when the home position is searched.
The precautions that should be taken to avoid this situation were set out in the section on consecutive spill, page 186.
If the chaining method is used, the lack of a home record will lead to the inability to retrieve any record further along the chain.
Only the tagging method of handling synonyms is unaffected.

To avoid these problems, addition and deletion algorithms will have to ensure that at least one home record remains in any bucket to which any records randomize.
When a record is added, this will involve storing it in its home address unless a home record is already in that address; a synonym from some other address would have to be moved to make way for it.
When a home record is deleted, any synonym that is stored elsewhere, or the first if there are more than one, should be placed in the home address to take the place of the original home record.
This is particularly important if records

This system, which is discussed in detail by Montgomery and Wallace leads to a fairly high number of accesses required to retrieve records from a well-aged file, i.e. one that has had a large number of additions or deletions since it was last loaded.
A stricter file housekeeping discipline, requiring that every home record possible is stored in home addresses, was analysed theoretically by Johnson.
This requires that when a record is added to the file it is stored in its home bucket if any record that is a synonym is at present in the home bucket, and that if space becomes available in a bucket, any synonym that randomizes to the bucket in which space is now available is moved into the home bucket.

The predictions made by Johnson were tested by simulation studies, which showed that even for a 100 per cent packed file, if the discipline he recommended is adhered to, the average number of accesses can be kept down to 1.5 per retrieval, and for larger bucket sizes this is reduced to around 1.25.
Despite the extra work involved in moving records about to ensure that all possible records are held in their home addresses, compared with the less restrictive requirement of at least one home record discussed earlier, this stricter file housekeeping pays off when retrievals outnumber additions and deletions.
This is the usual case, but if it turns out that a particular file is very volatile the less restrictive system should be used.

#### The most appropriate bucket size

The optimum bucket size to minimize the time taken by operations carried out on a file depends on the nature of the operation.
When retrievals and updating predominate, which is the usual situation, the optimum bucket size is as small as possible.
This means a single sector for sector-oriented devices, or one record per bucket in systems that allow the user to choose any bucket size within the capacity of the device.
This does not invalidate the earlier comment that a full-track bucket is advantageous, so long as records are randomized to a full track but stored in single-record format on the track.

If additions and deletions are more numerous than retrievals and updates, it turns out that the larger the proportion of additions, the larger the bucket size that provides the minimum number of accesses per reference to the file.
This is a result of the very much larger number of accesses required to find spare space for an addition, in comparison with those required to locate a record already in the file.
(This only applies for files that are relatively fully loaded; a 50 per cent packed file would require approximately equal numbers of accesses for addition and reference.)
However, even if additions make up most of the processing carried out on the file, it appears that bucket sizes small in comparison with a full track give optimal results.
The full-track bucket, but single-record storage, remains a good option in this case.

#### Conclusion

Direct files have been used less than might be expected in data processing.
There is certainly a security problem, in that arranging for security and integrity of data is more complex by comparison with sequential files and this, coupled with their poor performance for sequential applications, makes it obvious why they are not used if a sequential file is appropriate.
It is equally true that they are not as suitable for a truly mixed sequential-direct application as indexed sequential files.
However, for enquiry systems with no sequential requirement, or when that requirement is minimal, a well-designed direct file will outperform a well-designed indexed-sequential file, often very substantially.

The probable reason that indexed sequential files are so often used when direct files would perform better is the ready availability of software.
Direct files require extensive design work, because every file and every algorithm will differ slightly from every other.
This means that manufacturers' software can only provide the more basic requirements such as GET and PUT macros and record-formatting software.
Randomizing algorithms are sometimes provided, but it is generally wise for the user to allocate and test them for each file on an individual basis.
This chapter has shown the steps that can be taken to ensure that a direct file is optimized, and if the file designer follows the rules laid down here, good results should be obtained in almost any situation.
The choice between indexed sequential and direct files is examined in Chapter 9, and security of direct files in Chapter 10.

#### Revision questions

- 1 What is meant by self-indexing files?
Explain the advantages and drawbacks of organizing a file in this way, illustrating your answer with appropriate figures.

- 2 What relationships between key and address allow a self-indexing file to be created?

- 3 Explain the functions of a randomizing algorithm.
How do synonyms arise?
Can they be avoided in a randomized file?

- 4 What methods of randomizing are you aware of?
Describe and discuss each method you name.

- 5 Calculate the number of synonyms expected when

- - 5 15 records are randomized to 180 addresses

- - 5 150 records are randomized to 180 addresses

- - 5 1500 records are randomized to 1800 addresses

- - 5 15 000 records are randomized to 18 000 addresses.

- 5 Use (a) the binomial theorem, (b) the Poisson distribution, (c) a one-pass load.
Comment on the results you obtain.

- 6 Discuss the difference between one-pass and two-pass loading.
Derive equations for the synonyms created in each case for single-record buckets.

- 7 What methods of storing synonyms are in common use?
Describe how they operate, and explain their advantages and disadvantages.
When would you use each method?

- 8 What is meant by access frequency loading?
Explain how and why it improves some files but not others.
Outline the data required to apply it, and the way that data can he obtained.

- 9 Compare the benefits of random and access frequency loading in a file that is 93 per cent packed, fourteen records to a bucket, and for which 21 per cent of the records account for 82 per cent of the accesses.
How does the file degrade as a result of continued random additions to 100 per cent loading?

- 10 Describe the way in which a file area is prepared to receive a direct file.
How does this compare with the precautions needed for other file organizations?

- 11 Use the following keys to test the effectiveness of using the remainder after division as a randomizing algorithm; divide by 37, 41, 43, and 101, and comment on the results you obtain.
[UNK] Can you suggest any other method of allocation of records to addresses that might reduce both wasted space and numbers of synonyms?
What might he the disadvantage of such a method if the file were larger?

- 12 Explain why you might expect division to perform better than a 'perfect' randomizing algorithm, and by how much.
How is this affected by the ratio of key range to address range?

- 13 Why do you think that direct file organization is less used than some other file organization techniques?
When would you strongly recommend it?

## INDEXED SEQUENTIAL FILES

### 7.1 Introduction

Sequential processing of data files makes up a large proportion of data processing.
However, there is often a need to refer to sequential files just to answer one or relatively few enquiries.
Such a need could be met by processing the whole file sequentially and looking for the records required, but this would be very inefficient.
If the file is large the query may take some time to answer; meanwhile the computer is occupied processing unwanted records rather than doing useful work.

A second technique that greatly improves the speed of searching a sequential file is to use a logarithmic search.
This method has been described in Chapter 5 on sequential files (see p. 119).
It is very useful for a few enquiries but cannot handle a large number, as a series of storage device movements is involved in each search.
Although technically possible on magnetic tape, logarithmic searches are too slow to be economic, so they are normally only considered for direct access devices.
When the number of enquiries gets too large for a logarithmic search, or even some form of interpolation search, an indexing technique can be used to retrieve records more quickly.

The simplest form of index is one that holds the address of every record.
This is called full indexing and provides a very rapid means of locating any given record.
If the main file is large this index too will be large and there will be problems due to its size.
For this reason one or more indexes may be used in a hierarchy, with the lowest-level index pointing to records while higher-level indices point to the index next below them.
Because of the way in which direct access devices operate, it is not normally necessary or desirable for the lowest-level index to point to every record.
Usually one record per track (IBM) or bucket (ICL) has an entry in the index.
This is sometimes called partial indexing.

A sequential data file that is indexed is called an indexed sequential file.
The facilities provided by this type of file usually include:

- 1 Rapid direct retrieval of records by the use of indexes;

- 2 Addition of records and subsequent sequential processing of them by the provision of overflow areas;

- 3 Deletion of records;

- 4 Statistics on the state of the file, giving warning when reorganization is necessary.

Properly used, such a file provides an excellent compromise between the extremes of sequential processing with very rare enquiries that is best handled by sequential files, and direct processing with very infrequent sequential processing, for which direct files are most suitable.
It is not as efficient as either in their own fields, but performs very much better than they can in a situation where a significant enquiry facility is necessary and where the data is frequently processed sequentially.
The precautions needed to ensure that such a file performs satisfactorily are discussed in the main body of this chapter.

### 7.2 File structure

An indexed sequential file generally has the following components.

- 1 A data storage area: this may include some unused space to allow for additions embedded in the data.
It may also incorporate the lowest-level index elements.

- 2 A separate index or indexes: any enquiry will reference this index first; it will direct the enquiry to the part of the data file in which the desired record is stored.

- 3 An optional separate overflow area: the decision as to whether such an overflow area is required, and how best to allow for it, is considered later in this chapter.

These parts of the file are interrelated as shown in Fig. 7.1.

### 7.3 Indexes

#### General principles of indexing

It was stated above that full indexing - knowing the position of a record on a track - is seldom useful, because it does not usually speed up the search for that record.
The read-write head reaches any track at a time which is 'random' in the sense that it is not possible to tell which part of the track will be reached first.
This means that, even if a given address is known, it will be reached no more quickly than if only the track on which the record is stored is known.
This may not always hold good.
It is a result of the physical make-up of present access devices.
The main case in which full indexing is useful is that in which individual records take up a whole track (in IBM terminology) or sufficient buckets or sectors (eight, fifteen or twenty-five in ICL 2900 series terms, depending on the disk in question) to fill a track completely.
The search time can be overlapped by using rotational position sensing, however (see Chapter 2), and in this case the 'wasted' time can be used by some other operation or program.
In this case, knowing the address of the individual record may be useful.

As most of the considerations discussed below do not depend on whether indexing is full or partial, the reader should assume from now on that partial indexing is being discussed.
Exceptions will be pointed out as they arise.

All the common direct access devices, whether disk, semiconductor 'disk' or mass storage device, have a track concept that is important in deciding on the best arrangement of indexes.
It is not possible to control the part of an index track that is read first.
This means that, on average, half a revolution of the device is necessary before the desired entry is found.
If the software writers arranged that the start of the track has to be detected before the search begins, this becomes a full revolution; this is made up of half a track to locate the start, and half a track for the search.
When the desired entry is not on that track, these search figures become a full revolution and one-and-a-half revolutions respectively before it is clear that the record is not on the track, and the search must continue on a further track.

In designing a hierarchy of indexes, these figures are very useful.
The following calculations assume that indexes are stored on a direct access device.

Let I 1 and I 2 both be higher-level indexes, and of these let index I 1 be the higher-level index, pointing to index I 2.
Then the time to locate an address in I 2 will be: I 1 will only be created when it is quicker to search I 1 and then the track to [UNK] which it points in I 2, than to carry out an average length search of I 2.
Assume first that I 2 is one track or less in extent.
In this case a search will take R/2 on average, when the time of rotation of the device is R. Each additional track will add a further R/2 to this.
In the case where the start of the first index track searched has to be located before the search begins, a single-track index will require an average search time of R, but each additional track will again only add R/2.
Total sequential search times for these cases are shown in Fig. 7.2.

When a higher-level index is first added, it can be expected to be less than one track in size.
A search will therefore take the minimum time shown in Fig. 7.2.
The higher-level index will point directly to the required track of the lower-level index, so this will also require the minimum search time.
The break-even point is therefore two tracks if there is no requirement to seek the start of the track, or three tracks if there is.
This shows that as soon as some part of a further track (over and above two or three respectively) is necessary for I 2, a higher-level index I 1 should be created.
This process is repeated each time the highest-level index existing at that time requires a third or fourth track to be added.

The above discussion is based on a sequential search for index I 1.
An alternative is to search using the logarithmic technique.
This is not significant for less than three tracks, as it is effectively the same as a sequential search for one or two tracks.
In the three-track case it is possible to search the centre track first.
This must be a complete search to ensure that if the desired record is on the track it is found.
If the record is not on the centre track the first or last track will be searched, depending on a comparison of the key being looked for with the highest key on the track.
This will take R (or 3R/2 if the start of the track has to be detected first) for the centre track, and R/2 for the other track searched.

There is a ⅓ chance that the desired record is on the centre track, and this brings the average search time to (7/6) R (or (10/6) R where the track start has to be located).
These figures are similar to those for sequential searching, although the lower one is slightly better.

The logarithmic technique is not normally used because it requires an extra search for every power-of-two increase in the number of records, while a higher-level index only needs to be built when an index has reached three or four tracks in size.
This means that an extra search will be added only for every additional (2n + 1) or (3n + 1) records, where n is the number of records per track.
This can never be inferior to a logarithmic search (as n cannot be less than one) and is usually far superior.
The effect is shown in Fig. 7.2 for several values of n.
A number of types of index are in common use, and three of the most important are reviewed below.

#### Types of index

Balanced tree indexing Indexes are said to be of order e when there are e records per index entry, and of height h, where there are h levels of the index.
A tree index is one in which the top level of the index, which is the one consulted first in a search for a record, points to lower levels of the index.
This top level of the tree is often described as the root index of the tree, while the lower-level index items are equivalent to the branches of the tree, and the records are often called leaves or nodes.
A balanced tree is one in which any record can be retrieved in a number of steps s or s - 1, that is the path length to the record varies by no more than one step.

The balanced tree index shown in Fig. 7.3 (a) is made up of a series of index levels, each pointing to the level below it.
The records and the index entries are grouped into twos, so e = 2 and this is described as a tree of order 2 and height 4.

When a record is added it is necessary to use an overflow area, as the data areas are already full.
The added records have to be indexed, which requires a second index entry for each 'track' of the data file.
By track here, is meant e records.
The arrangement of the file after a number of additions is shown in Fig. 7.3 (b).
This type of index is used in the Indexed Sequential Access Method (ISAM) that has been available on IBM mainframe computer [UNK] systems since the late sixties, and is now available on some microcomputers.

The balanced tree index allows for deletions without difficulty, because records are tagged but not removed, so that no data manipulation is required.
In some systems, tagged records are removed if they are pushed into overflow; this depends on decisions taken by the software writers.
However, allowing for additions by providing areas that are logically extensions of the prime data tracks, rather than just physically, has made it necessary to double the size of the lowest-level index, with separate entries for records on the prime data and overflow tracks.

Direct-link balanced trees A second indexing technique, that treats additions as part of the prime data track, is the direct-link balanced tree.
This method of indexing was used on the IBM 1400 series computers - the control sequential method - and is at present in use with ICL's 2900 series.

A direct-link balanced tree index would also look just as in Fig. 7.3 (a) before additions.
However, after additions it would appear as in Fig. 7.4.

This technique is most effective for very volatile files, as the additions change the keys in indexes but do not cause alteration of prime data tracks.
This means that additions are made quickly, but sequential retrievals suffer.
McDonnell and Montgomery have shown that this technique is as good as the other balanced tree method for direct retrieval.
Both methods suffer from the problem that performance of the file degrades as additions are made, and in consequence they both require that the file should be reorganized at regular intervals.
In order to combat this problem, a number of other indexing methods have been developed.

B-trees Bayer, McCreight and Kaufman proposed the B-tree.
In this type of index, there are always more pointers than index items:.
The order of the B-tree is said to be one more than the maximum number of keys per index block.
A modified form of B-tree is used in IBM's VSAM files, to be discussed later in the chapter.
Indirectly, B-trees are also used in IBM's DB/2 relational database system.

Using the same data as before, a B-tree has been set up.
Here, e = 2, so the order is 3.
This is very low, and would never be used in practice, but it allows an example to be shown in a compact diagram.
The minimum number of keys per block has to be e/2, which in this case is one (1).
The keys given in the index entries do not have to be actual keys.
Usually, they are intermediate values to allow for later additions.

Fig. 7.5 (a) shows the same set of keys as in Fig. 7.3 (a), but stored in a B-tree.
Note that they are now in groups nf 1 or 2.

The number of index levels here is the same as in Fig. 7.3 (a) - that is, the height is again 4 - but there is much more room for additions.
The way in which additions are handled is shown in Fig. 7.5 (b); the same additions have been made, but have resulted in index and data block splitting, so that no records are in 'overflow'.
This prime data/index structure can continue to propagate itself as needed.
However, it takes much longer to add records that cause splitting, so the addition versus update-only figures are very important in assessing the efficiency of a B-tree.
A volatile file with relatively little processing might be better handled by a balanced tree index.
VSAM uses a modified form of B-tree, so that the number of keys and pointers is the same, and index entries are greater than or equal to the keys pointed to rather than taking some intermediate value.

The additions to this B-tree have had no effect on the index entries on the left-hand side of the tree, but have led to several changes to the right-hand index entries.
In order to examine this further, let us look at another case.
Fig. 7.6 shows an example of a B-tree of order 5.
In this case the maximum number of keys per block is four (e), and the minimum is 2 (e/2).
Note that the top level index may have as few as one.

Choice of index technique It is clear that the changes to the indexes caused by even a very few additions mean a great deal of reading and writing of data into the index areas on disk.
This is a definite weakness of the B-tree.
It is counterbalanced by the ability of the structure to accept very large numbers of additions - given sufficient space, the structure can grow in an unlimited fashion.
We therefore have a choice between index types that is affected by the use to which the file is put.
In Table 7.1 the three methods are compared, scoring 1 for the best of the three, 2 for the second, and 3 for the worst.

Bradley has discussed index design and optimization in some detail.
Montgomery describes the nary tree method of indexing, and compares it with hashing of keys (discussed later in the chapter, see p. 230).
Rathmann, in a paper particularly concerned with optical disks, compares the balanced tree method with the trie index technique, as did Severance.
A trie index is particularly useful when keys are of varying sizes, and the path of a search at any point of the tree depends on a part of the key rather than its full value.
As most available file organization techniques use the methods discussed earlier, rather than nary trees or trie indexes, they will not be discussed further here, but a full description of tries is given by Knuth.

#### Index position

The start of any direct search, and the first step in any sequential run, is a search of the higher-level indexes.
The process, for direct reference, is as follows:

- Seek the highest-level index (an average head movement)

- Search the high-level indexes (a variable search time)

- Seek the data cylinder (an average head movement)

- Search the low-level index (a single track search time)

- Search the prime data track (a single track search time)

- Search the overflow area (a variable search time).

As this is time-consuming, particularly in the case of direct reference, the file designer will aim to minimize it.
The first high-level index set up by the software is called the cylinder index in ISAM files, or the seek area index in some ICL 2900 series systems.
This index has an entry for each data cylinder of the file indicating the highest key on the cylinder.
Ideally, the file designer will aim to reduce the time taken to reference this index; however, when it exceeds a certain threshold value described earlier, a master index, which has one entry for each track of the cylinder index, can be created to reduce the total search time as described above.
IBM systems usually provide the software to create up to five higher-level indexes automatically in this way if the user specifies MSTIND = YES.
If two or more higher-level indexes exist, each of them may be handled using a different one of the techniques described below aimed at reducing index search time, depending on their size.

##### 1 To hold all or part of the index in main storage

This will avoid the need for a head movement to the index and can yield very marked savings.
If the entire index is in main storage, the correct cylinder to search is located in well under a millisecond.
This compares with head movement times that are usually orders of magnitude greater, and the direct access throughput is often roughly doubled if this technique is used.

Unless the file is small or main storage is very large, the cylinder index size may exceed the space available for it.
In this case IBM software allows the user to store an exact sub-multiple of the index in main storage, i.e. one half, one third, etc.
When this applies, the average seek time will be reduced to a half, two thirds, etc., of average head movement time, as the information will be available in main storage - so saving a seek - in an equivalent proportion of cases.

If, because of the size of the cylinder index, only a higher-level index than the cylinder index can be held in main storage, a 20-50 per cent improvement over the performance of the file when the master index is stored on disk can still be achieved.

##### 2 To hold the higher-level indexes on fast devices

Head movement times for fixed-head disks or semiconductor 'disks' are much shorter on average than those of standard disks.
It is very good practice to store high-level indexes on these devices, so that every direct reference is reduced by the difference in timing.
When the device is dedicated to this file the benefits can be very marked, since the index cylinder on the fast device is available without head movement at all times; if IBM 3340, 3350 or similar devices that offer some fixed-head capacity are available, these indexes can be held in the fixed-head area.

If the file is held on a mass storage device, location of higher-level indexes on a disk will make a very significant contribution to reducing run times.

##### 3 Storage on a separate device

If no faster device is available it is often beneficial to use a separate device of the same sort.
This can be most effective if this device can be dedicated to the file, but is still useful in normal multi-programming; there is certain to be constant arm movement if the file and its high-level indexes are stored on the same device, while this is less likely if they are on separate devices.

##### 4 positioning on a device that also holds the data

When no separate device is available, the optimal position for the cylinder index should be determined.
This has been investigated in great detail elsewhere, and the guidelines may be summarized as follows:

- a) If nothing is known about the distribution of hits in the file, the cylinder index should be placed in the centre of the file area.
In a multi-pack file this will be the centre of one of the packs that is completely dedicated to the file.

- b) If, in a multi-pack file, the only information about hits is the relative number per pack or area, the index should be placed in the centre of the pack or area with the lowest hit density.

- c) If the hit density across a file area or areas is known, the index should be placed in the centre of the highest peak of hits on the least active pack used by the file.

The objective of these guidelines is to place the cylinder index on the file cylinder that is of lowest possible activity, in such a position that the majority of head movements away from the index will be short.
This allows movement back to the index to be rapid.

Past practice has often been to allocate the cylinder index to a cylinder preceding or following the file area.
This is never the best solution; as pointed out above, the centre of the file is the logical position if nothing is known about hit pattern.

Fig. 7.7 summarizes the rules for placement of the cylinder index if it is to be situated in the main file area.

#### Alternative indexing techniques

There have been a number of suggestions for alternatives to the lowest-level index of indexed sequential files.
Ghosh and Senko put forward an interpolation search in place of the track or lowest-level index, and showed that for normal key distributions it would improve the direct retrieval performance of IS files.
In addition, this measure gives a potentially better packing density than conventional indexing techniques.

Mullin suggested the use of hashing, rather than indexing, for the lowest-level index.
As he makes clear, this is only of benefit when the average number of records that has overflowed from a track is two or more.
This limits the possible uses of such a technique to very active files that the user does not wish to reorganize frequently.

### 7.4 Additions

Most indexed sequential file software allows for additions to be made to the file without reorganizing it.
The provision of space for additions is an optional feature.
If no additions are expected, ii is not necessary to leave space for that purpose.
When additions are expected, two techniques are used to store those additions so that they are available for both sequential and direct access.
The first is embedded overflow.
In this case, space is left unused in the main data area when the file is created, and additions are located on the same cylinder (IBM) or seek area (ICL) that they would have occupied if they had been part of the file when it was created.
In this way the record can be found when necessary without movement of the access heads.
Although this allows fast retrieval of records, it can lead to very low packing density of data because there may be many additions in one area and few in others.
To allow for many additions to every cylinder, when only one cylinder has a large number of additions, is wasteful of space.
This is discussed in more detail below.

The second commonly used technique is to provide an independent or global overflow area which is used to store records added to any part of the file.
This is a very efficient way of handling additions, because all the available space can be used before there is any need to provide extra overflow space.
However, it means that references to added records will require movement of the access heads, which wastes a great deal of time.

As one overflow technique saves time but wastes space, while the other saves space but is slow, many users choose a compromise.
A reasonably-sized embedded overflow area is provided on each cylinder, while a small independent overflow area is used to store additions that overflow from their home cylinder.
Variations in numbers of additions from one cylinder to another are to be expected.
This method ensures that the file designer is not forced to provide very large embedded overflow areas on every cylinder, when only a few cylinders require them.

The distribution of additions to a file guides the designer in allocating overflow areas.
Before the appropriate decision can be made, the pattern of additions to the file has to be determined.
Sometimes this can he predicted or measured, but on other occasions there may be no prior information for the designer to work on.
A number of typical cases are discussed below.

No additions expected This can arise when, for example, a file contains records of policyholders under a policy no longer offered.
The number of policyholders cannot grow, and in this case the designer would not allocate any overflow areas.
This provides a file that is well packed; however, if conditions change later the file needs to he respecified.

Equal numbers of additions to each area This is a very unusual case.
The designer must know that additions will be equal.
It might arise if one additional record were added to each group of consecutive records; for example, a group of stores might begin to open on a Saturday, and require an extra record for each store to record transactions.
The superficially similar case in which there is an equal probability of additions to any area is covered below.
If the designer is satisfied that equal additions to every cylinder are going to occur, then it is possible to provide only embedded overflow areas.
This will allow rapid retrieval from the file as no extra head movements will be caused by additions.

The designer has to decide on the size of the embedded overflow areas.
Very often, if it is known that additions will be made precisely evenly throughout the file, it will also be known when they will be made.
An example would be when an extra record is added for each project in a company every day.
If this information is not available the designer will have to estimate it.
The intention will be to plan how frequently the file will require reorganization to merge additions and remove deleted records.
After this has been done several times, the actual frequency of reorganization can be compared with that expected, and the future reorganization schedule will be based on the results.

All additions concentrated in a few areas This can occur when, for example, recruitment campaigns for customers have taken place in a limited area, or a competitor has gone out of business.
In these cases, if customer numbers are based on areas, additions will be in groups.
It is unusual for this to be the normal form of additions.
If the designer is faced with it, the requirement for embedded overflow areas will be minimal or nil; the main provision must be a large independent overflow area.
As this will lead to slow retrieval of added records, more frequent reorganization will be required than in any other case.
If the times at which additions are expected can be predicted, it may be wise to hold additions in an ancillary file until each 'burst' of activity is over and then to reorganize the main file to include them.
Additions equally probable anywhere This is both the most usual case and the assumption the designer should work on if no information is available.
It is not the same as equal numbers of additions to each area, since there will naturally be variations from cylinder to cylinder in the number of additions just because those additions are random.
The Poisson distribution used to predict synonym behaviour in direct files is the appropriate mathematical tool to use here (note that if the number of embedded overflow areas is small the binomial distribution should be used instead).

Assume that l records are to be added to S embedded overflow areas.
Then the probability p (x) that x records will be added to a given embedded overflow area is given by the expression: An overflow area will be able to hold some number of records n.
The probability that this area will be able to hold all the records added to it will thus be:

To demonstrate what this means in practice, assume that, on average, four records are to be added to each embedded overflow area, and that these overflow areas can hold a maximum of five records.

From equation (7. 1), the percentage of embedded overflow areas that will have 0, 1,... n additions is given in Table 7.2.

These figures are plotted in Fig. 7.8, where the shaded section shows the percentage of areas from which at least one record will overflow into the independent overflow area.
This turns out to be about 21.5 per cent of embedded overflow areas.
The percentage of added records that cannot be held in these embedded overflow areas is about 10.26 per cent.
This difference is due to the fact that only one-sixth of the records added to the 'six additions' figure will overflow, two-sevenths of the 'seven additions', three-eighths of the 'eight additions', and so on.

Table 7.3 shows the percentage of all additions that will be held in independent overflow for various combinations of embedded overflow area size and number of additions.
This has similar values to those given in Table 6.4.
The reason is that the addition of records to direct access files is mathematically similar to the random addition of records to overflow areas.
The derivations given here are due to the author and were published in the first edition, but Larson has also carried out similar work independently.

Cases of equal numbers of additions to each area and all additions concentrated in a few areas are depicted schematically in Fig. 7.9.
This shows files with a twenty-cylinder prime data area, and a two-cylinder independent overflow area.
Each prime data cylinder contains ten tracks.
A track can hold up to five records.
One track in each cylinder is set aside as an embedded overflow area.
The files have each had eighty records added.
The assumptions made are:

- a) equal numbers of additions have been made to every cylinder;

- b) additions of twenty, twenty-four and thirty-six records have been made to cylinders five, ten and fifteen.

- c) additions have been made as they occur, in an entirely chance sequence.

As this is a small file, it is useful to check how accurately the Poisson distribution approximates to the more strictly accurate binomial distribution.
Using equations (6.6) - (6.9), the figures obtained are shown in Table 7.4.
The correspondence between the two sets of figures appears to be good.
A check on this using the chi-squared significance test (see Moroney or any standard statistical text for further details) shows that there is no significant [UNK] [UNK] [UNK] [UNK] difference between the two.
This means that any real set of figures obtained by adding records to a file would be expected, due to normal random variations, to show larger discrepancies from the calculated figures.
Thus the Poisson distribution can safely be used instead of the binomial for files of this size.

These three examples show the wide range of conditions that will have to be handled in providing far additions.
Whenever possible, the file designer will have data available on the pattern of additions to a given file.
When no data is provided, or if the only information available is an average number of additions, it should be assumed that additions are equally probable anywhere.
As experience is gained in using the file, any original assumptions about additions should be checked.
Manufacturers' software often provides information about overflow areas that can assist in this; the use of this information is discussed in a later section.

### 7.5 Addition techniques

The way in which additions to an indexed file are made can affect both sequential and direct access to the file.
There are two commonly used techniques.
In the first the record that is added is inserted into its correct position in the file, and the record at the end of the track to which it was added drops off into overflow.
In the second, the added record is placed in overflow, linked from the record before it in sequence, and back to the record following it.

#### Record insertion

The principle is as shown in Fig. 7.10.
The advantage of this technique is that, in subsequent processing, the whole prime data track can be handled [UNK] sequentially by the software, and overflow records are picked up only when the prime track has been processed.
The disadvantage is that, on average, half the records on the track need to be shunted up (in this example records 113, 1 14 and 116 have been moved), and the overflow area will also require updating.
Both of these functions can be carried out quickly and efficiently in main storage, and it is important to use the manufacturers' software and allocate space to allow this to happen.
If half the records on a track have to be moved one at a time, and a device revolution is required for each movement, additions can take a great deal of time.
This would be the situation if the programmer had not allocated sufficient working storage to the file.

The IBM indexed sequential file management system ISAM works on the insertion principle.
The cylinder index, a track index and a data cylinder are shown in Fig. 7.11 (a) as they are set up.
The file consists of four cylinders, 004) 3, and cylinder 01 is illustrated.
Each cylinder index entry gives the address of the cylinder it refers to, and the highest key on the cylinder.
In the case shown this is 341.
This will remain the highest key on the cylinder.
If a record with the key 342 is added, it will be stored on the first track of cylinder 02.
The same principle applies to the highest key on any track; as the highest key on track 06 was 298 when the file was created, a record with the key 299 belongs logically to track 07, whether it is stored on that track already or has not yet been added.

The form of balanced tree index used in ISAM operates as follows.
There are two track index entries for each track.
The functions of these entries are given in Fig. 7.12.
The normal entry links the highest key at present on the prime data track with the address of the track.
It allows a program to check what records are at present physically on that track.
The overflow entry links the highest key on the logical track, which comprises both the prime (physical) and overflow parts of it, and the address of the first record in the chain of overflow records for that track.
A program can check from this what [UNK] [UNK] records are at present logically on that track.
'Logical' here means those records that are processed as if they were on the track.

The effect of additions no processing times is discussed under the sections on sequential and direct access to indirect sequential files (see pp. 251 and 261).
The way in which additions occur, and the changes to index and link entries, are shown in Fig. 7.11.

The field shown as COCR in the track index stands for cylinder overflow control record.
This is used to store information about the address of the last overflow record on the cylinder, the number of bytes of overflow space still remaining and additional data required if the file contains variable-length records.

When records are added to a file organized in this way, there is an advantage to be gained by planning the additions procedure.
Additions should be sorted into descending order.
As the last record added is the first in the overflow chain, it is helpful if this physical order is also the logical order of the record keys.
Coyle has pointed out that significant savings can be made in ISAM file timings by using this technique.

#### Record linking

This method operates as shown in Fig. 7.13.
The advantage of the method is that records on the prime data track do not have to be moved; a link field has to be inserted in record 111, however.
The disadvantage for sequential [UNK] processing is that there will be several rotations during the processing of a track with overflow.
for direct processing the track index does not make it clear which records are in overflow and which in the prime data area; this prevents the first overflow record being retrieved as quickly as is achieved in the two-entry index system - at least while it is the only overflow record.
However, the index itself takes up less space.

IBM s control sequential file organization, used with the 1400 series computers, added link fields to the records shown above as 111 and 112.
This was the organization that preceded the indexed sequential file management system.
The smaller machines in ICL's 2900 series provide an eleven-bit link field that points back to the home bucket if the record is stored in overflow.
This field is present in all records, whether they are in overflow or in a home bucket.
However, it is only used if the record is in overflow.
Otherwise all the bits are set to zero.
If a record is stored in overflow, a tag is placed in the home bucket, pointing to the overflow storage position.
This is made up of a twenty-four-bit field containing the overflow address plus control information, followed by the record key, which can be up to sixty-four characters in length.
The details are shown in fig. 7.14.

It is usually somewhat easier to insert link fields to handle overflow - particularly when they are already available in the records - than to move up all the records on a track to accommodate a record in its correct sequence.
However, the extra speed of processing will repay the time taken to move these records if the file is frequently processed sequentially.
If the file is mainly processed directly, the link method may be more efficient.
In most cases, however, the user will have no choice in the matter.
It is usually a case of accepting the method used by the manufacturer whose software is being employed.

#### Addition techniques compared in practice

Montgomery and Hubbard have compared the performance after additions of IBM's ISAM and ICL's 1900 series indexed sequential software, the files being held on a 2314 and its ICL equivalent, an EDS 30.

They looked at:

- 1. random retrieval;

- 2. random insertion;

- 3. sequential processing;

for buckets holding two, six and fourteen records.

Random processing Random retrieval gave very variable results for ICL files.
Buckets containing two and six 500-character records required retrieval times of 60 - 70 ms per record, while for fourteen-record buckets this increased to 120 - 140 ms.
IBM files, on the other hand, yielded retrieval times of 75 - 95 ms and the effect of bucket capacity was small.
The fraction of the file in overflow did not markedly affect performance until it reached 30 per cent of the total file; the only exception was the ICL fourteen-record bucket file, which began to perform worse as soon as additions were made.

Random insertions were found to be variable in their effect on timing.
IBM files performed better the larger the bucket capacity, while ICL files performed better the smaller the bucket capacity; very roughly, the six-record buckets were equivalent, while IBM two-record buckets performed as badly as the ICL fourteen-record buckets.
The ICL two-record buckets required about 130 ms per insertion, and the IBM files showed little variation due to the fraction of the file in overflow, but ICL files improved as additions were made, up to 10 per cent, and degraded after this.

Sequential processing The sequential retrieval times for both file structures were identical before additions, but IBM files outperformed ICL in every case after additions.
This was most marked for large bucket sizes; IBM fourteen-record bucket files gave average retrieval times increased from 40 ms to 55 ms as a result of 40 per cent of the file being stored in overflow.
Average retrieval times fur ICL files, however, increased from 40 ms to 150 ms due to the same number of additions.

Comment on these comparisons These findings are generally in accord with the considerations on the two types of balanced tree discussed earlier.
However, it should be noted that additions to IBM files did not take a great deal longer than to ICL files, while random retrievals from IBM files were not markedly more rapid.
The authors point out that record size is an important factor which was not varied in the work quoted, and it would not be safe to draw far-reaching conclusions from a limited investigation of this sort.
Further work may clarify the differences between these two methods of handling overflow records over a wider range of conditions.

### 7.6 Data format

#### Individual records

Manufacturers' software usually provides for two formats, as discussed in Chapter 3 (see p. 57).
Because it is necessary for indexed sequential software to build indexes, insert records, etc., the keys of records must be available to the software.
For this reason the separate count, key and data format is usually required, i.e. [UNK]

The software that handles index building and additions can operate on the keys separately, while the size of the gap between key and data allows the data record to be transferred into main storage if it turns out to be the required record after examination of the key by the control unit.
A SEARCH ON KEY, for example, will compare every record key with the search key value, but will only read in the data record or records that satisfy the search conditions.
These are generally:

- KEY EQUAL

- KEY HIGH OR EQUAL

- KEY LOW OR EQUAL

In the case of unblocked records, the most likely condition would be KEY EQUAL, as a particular record would be searched for.

It is usual for the file to be arranged in ascending key sequence, and for the file creation software to expect input to the file to be physically in this order (on initial creation) or logically in this order (when a file with overflow records is reorganized).
In principle, a file could be arranged in descending order, but most manufacturers' software checks that the order is ascending and, if it is not, halts until the input order is corrected.

#### Blocked records

Searching for a record in blocked format is complicated by the fact that only one key can be placed in front of the block.
This is usually the key of the last record in the block, as is shown in Fig. 7.15.

In the example shown in Fig. 7.15 (a), record 112 is in the second block.
If we were searching for this record, a comparison with the 'key' of the first block would be low, and of the second, high.
Thus a HIGH OR EQUAL comparison condition will be used to search a blocked file looking for a given record.
In this case the whole block will have to be moved into main storage, and the desired record will be retrieved by the use of a de-blocking algorithm.
If the ISAM method is in use, the effect of adding a new record to [UNK] a block of records is to cause the block to be re-built, incorporating the new record and pushing the last record of the last block on the track off into overflow.
If record 113 were an addition to the file in fig. 7.15 (a), the new structure would be as in fig. 7.15 (b).
Record 119 goes into the next block, if that is on this track, or otherwise into overflow.
Note that overflow records arise singly, however the prime data area is formatted, and that they are usually stored singly in indexed sequential files (but see discussion of VSAM on p. 266).

The process described is that used in IBM systems.
ICL does not provide a separate key format in its 2900 series buckets.
Instead, home records are located using the bucket index and overflow records via the home bucket and a tag.

#### Variable-length records

In many cases variable-length records are not provided for by manufacturers' software.
It is possible to pad out all records to the length of the largest and handle them as fixed-length.
This wastes space, but the user will not be able to avoid such a shortcoming in manufacturers' software by any other technique.

Often the solution is to move to a different operating system.
The smaller IBM operating systems do not support variable-length records for indexed sequential files, but the larger ones do.
There are obvious additional tasks to be carried out, such as de-blocking, overflow calculations and efficient packing of the file storage areas that make this limitation understandable.
Even if an installation finds it convenient to use one of the smaller operating systems for much of its work, it may he possible to switch to an operating system that provides the extra facility to handle variable-length records, just for those files that need it.

#### Overflow records

It was mentioned above that overflow records arise singly.
In addition, an embedded overflow area will usually contain varying numbers of records from several tracks.
This leads to overflow records usually being stored in unblocked format, even if the records in the prime data area are blocked.
There is some advantage in treating the whole embedded overflow area as a single large blocked record, and manufacturers' software often does transfer the whole track into main storage when an addition is to be made; this allows for the addition itself, creation of link fields, changes of index, etc.
However, handling the whole track as a single block would prevent rapid transfer of individual records from the embedded overflow area during direct access reference, which is the reason this method is often not adopted (but see the section on software packages, p. 264).

#### Key size

On a 3330, the space taken up by the track index will be at least 57 per cent of track zero if all but one track of the device is allocated to data storage (the remaining track is assumed to be reserved for overflow records).
If keys are greater than 155 bytes in length, the track index will exceed one full track in extent, and maximum length keys of 256 bytes will cause the cylinder index to take up as much as 28 per cent of the second track on the cylinder as well.
Equivalent figures for the 3350 are even higher: the minimum track index size for a full cylinder file with no embedded overflow areas is 85 per cent of track zero, while maximum key sizes could expand this to almost one and two-thirds of a track.
The influence of key size is shown in Fig. 7.16.

#### 7.7 File packing

The prime data area of an indexed sequential file is less densely packed than the data area of a sequential file.
There are three reasons for this.
They are as follows:

- 1 The records or blocks of records take up more space, because they are in the CKD format with separate keys.
The effect of this depends on record or block size, but can be calculated using the methods given in Chapter 4 on blocking and buffering (see p. 75).
(Note that in some cases sequential files also use this format.
This point would then not apply.)

- 2 The track index will take up part or all of the first track on each cylinder.
The system-defined parts of this are standard in size, but the record key length depends on the user.
A typical value might be eight bytes, leading to an index size of rather more than half a track (the number of entries in the index depends on the number of tracks or buckets, while the size of the track depends on the device).
If the user decided on very large keys - and IBM [UNK] allows up to 256 bytes, for example - the track index might take up more than a single track.
This is one reason to choose a fairly short key for indexed sequential use.
A further reason is the size of the higher indexes; they, too, will be very much affected by the key size.

- 3 If embedded or cylinder overflow areas are provided they will take up one or more tracks of every cylinder.
The file designer will try to keep these areas as small as possible to produce a well-packed file.
However, the considerations given earlier on overflow area size and the need to allow for a relatively long period between reorganizations will guide the designer to a reasonable compromise.
If a great deal of direct on-line storage is available, the balance will be tilted towards a larger provision of overflow space.
If direct on-line storage is limited, it may be worth accepting more frequent reorganizations as the price for cutting down overflow space.
ICL 2900 series software allows the user to specify the packing of home buckets that is desired when the file is created.
This can be used to replace or supplement a cylinder overflow area; it is a form of distributed free space that is more evenly available through the file than a cylinder overflow area.

- 3 These three points will lead in most cases to something between 80 per cent and 90 per cent of the space in the prime data cylinders being used to store records.
The best that can be achieved is 95 - 98 per cent packing if keys are small and no overflow is expected.
There are, however, two further file structural areas that may reduce data packing.

- 4 The cylinder index and any higher-level indexes: it is unlikely that any but the largest files will require more than one cylinder for these indexes, although a complete cylinder has often to be set aside for them, as is required by some manufacturers' software.
If this applies, small indexed sequential files bear a heavy burden compared with larger files.
The probable penalty in packing density for a large file is of the order of 0.5 to 1 per cent, while for small files it can be very much more - 50 per cent in the most extreme case, when the file takes up only one data cylinder.

- 5 The independent overflow area uses additional space, although in most cases this will not be excessive as the increase in time caused by continual head movements to the independent overflow area from the prime data area and back will soon show up in run times.
The usual loss in packing density is again of the order of 0.5 per cent to 1 per cent, but as with the high-level indexes, there will be a proportionately heavy overhead for small files if the software requires a complete cylinder to be used for independent overflow.

- 5 Apart from the points discussed above, which are due to the structure of the file, two more considerations will influence the space required by the file.

- 6 Blocking of records: the demand for records in CKD format is more wasteful the smaller the record size.
One way to use direct access storage more efficiently is to block effectively.
This will depend on space being available to handle larger blocks in main storage; it was considered in more detail in Chapter 4 (see p. 75).

- 7 The use of variable-length records is sometimes unavoidable, but always leads to waste.
It may appear as padding to a fixed size due to software limitations or it may be wasted space at the end of tracks and overflow areas because the record that should have gone there was too large.
To this must be added the extra time and space demanded in main storage for relatively complex blocking - deblocking routines.
The designer of an indexed sequential file will try to avoid using variable-length records; when they are necessary the discussion in Chapter 3 (see p. 67) should be helpful.

Coyle has shown that it pays to leave some distributed free space within a file.
As pointed out above, ICL allows the user to specify the packing density in buckets, but IBM does not.
Dummy records can be provided to take the place of this space, by placing them where additions are expected, or in a pre-determined pattern throughout the file.
This solution (used by Coyle) led to marked improvement in ISAM file performance.
The packing density is not usually critical, but the additional space used does have an effect on file timing, which will be examined later.

Indexed sequential files can be processed either sequentially or directly.
As handling of the file is very different in these two cases, we shall examine them separately.

### 7.8 Sequential processing

The user may wish to start at the beginning of the file, or at any other point.
using IBM terminology, the SETL macro can be employed to indicate a starting point in the file and the ESETL macro to set a finishing point.
When the processing program issues a GET macro the routine shown in Fig. 7.17 is initiated.
The user is not directly aware of the steps shown but they will result in both 'housekeeping' processing time and input-output operations.
The [UNK] sequence has been simplified for convenience, but it shows the essential stages in sequential retrieval.
We shall refer to it in examining the various operations that can be carried out sequentially.

#### Retrieval before additions

All records will be in their correct places and the file will be physically as well as logically in sequence.
The cylinder index (and any higher indexes) will only be referenced once at the start of the run.
Head movement to the first data cylinder will be dependent on the size and position of the file.
All further head movements will be from the current cylinder to the next and so will be of minimum duration - 3 to 10 ms for modern disks.
For semiconductor 'disks' or fixed-head disks all that is involved is electronic switching, which takes negligible time.
The length of a sequential retrieval run will be slower than an equivalent run using a sequentially organized file for the following reasons:

##### 1 Reference to the cylinder index and any higher indexes

This is not likely to take longer than 100 ms and average times are much lower, e.g. 30 ms average head movement for the IBM 3330, 25 ms for the 3350 and 16 ms for the 3380, followed by a search of the index.
Thus the addition to a given run time will not be significant.

##### 2 Reference to the track index

There will be a rotational delay of half a revolution on average before the required track index entries are found.
This will be repeated for every track on the cylinder, so it will cause a sizeable addition to run times.

##### 3 Increased file size

The track index will take up part of the first track of each cylinder.
Overflow areas, even if empty, will take additional space.
This will mean that the data requires more direct access storage space than a sequential file.
Timing will be increased by:

- a) extra cylinder-to-cylinder head movements;

- b) an increased number of data tracks, each of which will require index entries and so will add to the time required for rotational delays described in 2 above.

As we are examining the case of sequential retrieval before additions, the items given above do not include overflow retrieval.
However, there is more housekeeping activity in handling an indexed sequential file than the corresponding sequentially organized file.
This will add to CPU usage, and the greater software module size will mean that more space is required in main storage.

The two file organizations are fully compared in Chapter 8 (see p. 300).

#### The effect of additions

We shall examine random additions to a file; as the principles involved do not change if the additions are grouped or regular in pattern, the methods used can be adapted to suit those cases.
Table 7.5 shows the percentage of tracks with 0,1,2,... additional records as a result of additions made randomly to a file.
These figures only hold accurately for large files - 100 or more tracks in extent - although they will act as a guide even for very small files.
Fig. 7.18 displays the results pictorially.
Note that Table 7.5 only applies to the given number of records per track while Fig. 7.18 is more general.

The impact of additions depends on the additions technique used.

##### 1 Record insertion

This is the standard balanced tree type of index, described on page 223.
If a single record has been inserted, the last record logically on the track will now be held in overflow.
The average wait before this is located would be half a revolution if the whole overflow track were full.
Usually this is not the case so the average wait will be less than half a revolution.
For timing purposes it is best to assume a wait of half a revolution, bearing in mind that this is usually an overestimate.

The duration of this wait may often lead to the overflow record being processed more rapidly than prime data track records because processing [UNK] time will often be low enough to allow this record to be processed as soon as it is located.
Records on the prime data track, as has been explained earlier, may each cause a full revolution to be lost if they cannot be processed during the time the inter-record gap is traversed.

When there are two or more overflow records on a track, the first overflow record in logical sequence, i.e. the last to go into overflow, will require half a revolution on average to locate it.
This is usually an underestimate as the first logical overflow record is always the last from that track physically and tends to be located near the end of the overflow track.

Each later overflow record will require nearly a full revolution.
Fig. 7. 19 shows the situation on an overflow track.

In this case an overflow chain of three records has been established from the prime track.
The logical and physical sequence of these records is inverted, and the wait-time spiral (WAIT 1 +WAIT 2+WAIT 3) shows that it will take more than two revolutions of the disk to access the three records.
WAIT 1 cannot be overlapped, except with separate functions of this or some other program.
WAIT 2 and WAIT 3 will be overlapped with the [UNK] processing of records 1 and 2, while the processing time for record 3 has to be added to the minimum delay of the three WAITS.
The estimate of three revolutions for three overflow records will thus be fairly accurate in this case.
As n overflow records will require (n - 1) full revolutions, to which the seek and processing times for the last record have to be added, this estimate will get more accurate the more records there are in the overflow chain.
These timings will hold so long as wait times exceed processing times, which is often true.
When this does not hold, additional full revolutions will be added to the total time because the next record to be processed will be missed, and a further revolution or revolutions will be required before it is available once more.

##### 2 Record linking

This technique is used in the direct-link balanced tree.
If the overflow record is held on the same cylinder as the prime data there will be an average wait of half a revolution to refer to the overflow record.
If processing time is negligible there will be an additional half a revolution to return to the next prime track record, and the total time to locate and process the overflow record will be precisely one revolution.
The longer the overflow record processing time, the more frequently will this not be completed before the next prime-track record is available.
This will mean that an additional revolution is lost, so the total time incurred per overflow record will exceed one revolution on average.
The range of processing times that will allow processing to be completed in a single revolution is shown in Fig. 7.20.
Note that, as the time available to process the prime record increases, that available to process the overflow record decreases proportionally.

If the minimum figure - a loss of one revolution per overflow record - is assumed as an average, it will certainly not be an overestimate.
For long processing times this will be too low a figure, but it will then be part of run times markedly higher as a result of overall long processing times and it is probable that overflow records will not cause much extra delay.

##### 3 Comparison of the two techniques

Experimental and simulation work carried out by Montgomery and his co-workers has shown that the sequential retrieval time for records increases as more of the file is held in overflow.
This is less marked for smaller numbers of records per block and some trials have shown an improvement for blocks of only two records.
McDonnell and Montgomery found that higher overflow percentages than 10-25 per cent led to increased retrieval times for all block sizes.

Random insertions to balanced tree files that use two index entries per track took rather less time as the overflow percentage in the file built up.
This was more marked for larger blocks than smaller ones.
In comparison, the time required to make random insertions to direct-linked balanced tree files did not change with overflow percentage.
This is to be expected, bearing in mind the way in which insertion is handled.

#### The effect of hit rate

One of the great strengths of indexed sequential files is that skip-sequential processing is made easy.
When the hit rate - the percentage of records that has to be processed - is low, records, whole tracks and even cylinders may be skipped without reading them if they are not required.
Although a sequential file using a record storage format in which keys are separate from data can also skip records, every key has to be checked so every track has to be traversed, whether any records on it are required or not.
An indexed file can allow more marked savings to be made, as only the index entries need to be read, and these show which tracks and cylinders can be skipped.

The effect of hit rate depends also on the pattern of hits.
Analysis of this is mathematically similar to that of patterns of overflow record occurrences, and the following cases will be considered:

- 1. random;

- 2. even;

- 3. grouped;

- 4. grouped superposed on random.

##### 1 Random update pattern

When hit rates are low, the probability that two adjacent records will both require updating is also low.
This implies that there is a good chance the processing of the first record will be complete by the time that the second record is located, so that skip-sequential processing win provide benefits.
Whether such benefits are available depends both on average hit rate and on processing time.

The results of a series of experiments have shown that the pattern obtained is very similar to those given for sequential disk files in Fig. 5.8 (d).
Thus the relationship between hit rate and overall run time is roughly equivalent to hit rate, but stepped in characteristic disk fashion.
As hit rate reduces, more and more benefit is obtained from skip-sequential processing.
This is examined in detail in Chapter 9. pages 300-307.

##### 2 Even update pattern

When every second, third,... nth record is updated, conditions are ideal for rapid skip-sequential runs.
A constant period is available during seeks to process the records already in main storage, and if every record requires the same processing time this will lead to very predictable run timings.
These will increase stepwise in that, up to some limiting time, processing will be entirely overlapped with seeking.
Beyond this threshold processing time there will be a loss of one revolution for every one, two,... b records, depending on the number of 1 - O buffers, b, that is in use.

A precisely even update pattern is not usual, so the designer is unlikely to be able to rely on such an occurrence in deciding on file timings.
However, in the few cases where it does occur, this type of update pattern makes timing calculations relatively easy.

##### 3 Grouped updates

This pattern occurs frequently due to factors such as the way in which meter readings for, say, electricity supply are made from house to house, i.e. not at random, or the effects of localized advertising campaigns on a larger file in which many unaffected records are stored.

The effect of grouped updates is to cause parts of the file to require few, if any, updates so records are being skipped, and other areas in which all - or most - records are updated, and thus there will be lost revolutions because processing times exceed inter-record gap times.
If skip-sequential processing is correctly used, whole areas of the file can be skipped, producing an improvement in run time similar to that achieved by sectioning a sequential file on magnetic tape (see Chapter 5 for details, p. 112).
In group update areas, if every record in the group has to be processed there will be extra revolutions for every record, every second record,... every bth record, depending on buffering arrangements, where b is the number of buffers as before.
For all normal record updating a loss of this magnitude can be expected, but it would not apply if the processing involved is trivial because then the records can be processed at reading - that is, rotation - speeds.

In summary, the areas in which there are few updates can be skipped very quickly.
Grouped update areas will take an overall time related to individual record processing time, buffer arrangement, update density, i.e. hit rate, and device rotation time.
Although this is complex to analyse, the average times are easily checked in any given case.
The file designer can measure the results of applying groups of updates to the file and make timing estimates based on the results of these tests.

##### 4 Grouped updates with additional random updates

This case also often occurs in practice due to the results of cases such as grouped meter readings from customers who were at home when the meter reader called, combined with customers' own readings carried out because they were out when the meter reader called, and a number of special checks that are carried out at a different time.

Timings can be handled by considering the two separate situations and combining their effects.
The skip-sequential processing of sparsely updated file areas cannot now be regarded as straightforward.
Every cylinder, and quite probably most tracks, will have one or more records that require updating.
However, the likelihood is that processing and seeking will be entirely overlapped so this will not hold up the overall run very seriously.

In the grouped update areas there will be little or no effect, as the hit rate is already high.
Additional transactions from the 'background' random distribution will only make it more unlikely that seeking and processing can be overlapped.
This will reduce the variability of timings due to chance variations in overlap, and so make it possible to calculate run timings more accurately.

#### The effect of blocking

The blocking of records in general has been dealt with in Chapter 4 (see pp. 71 - 98).
The main significance of blocking here is that, even if a low percentage of records is hit in a run, blocking them together will increase this figure.
Again, the increase is not directly proportional to the blocking factor.
The results of any given blocking factor on hit rate can be calculated from Table 4.5 and Fig. 4.6.
For example, if a file has an individual record hit rate [UNK] of 1 per cent and the hits are randomly distributed, the results of varying the blocking factor are as shown in Table 7.6.

The reason for the need to read more records is that as the blocks get larger there is an ever-increasing likelihood of at least one update being required from amongst the records in the block.
Concentration of updates in a particular area - case 3 above - reduces the number of blocks that have to be read and in the most extreme case, where all or none of the records in a block require updating, the percentage of records that need to be read would not change due to blocking.

At the other extreme, very even updating patterns would mean that most blocks or even every block required to be read and such a pattern would therefore make skip-sequential processing pointless.

The main impact of blocking on the speed of skip-sequential processing is usually counter-productive, although it often achieves more in space-saving and rapid data transfer than is lost in increased block activity.
Blocking will not usually increase the probability of having to read data from a given track, except insofar as it allows more records to be stored on that track.
It will, however, mean that a larger quantity of data has to be transferred into main storage for each update operation, even if only one record in the block is required.
Overall, a larger blocking factor will not markedly change the balance of choice between skip-sequential processing of sequentially and indexed sequentially organized files.

### 7.9 Direct processing

The overall set of operations that take place when an indexed sequential file is directly processed is shown in Fig. 7.21.
This sequence occurs whenever a reference is made to the file, and it is helpful to examine each stage of the process:

Reference to the cylinder and higher-level indexes This will involve a head movement in most cases.
If the file is small, the cylinder index may be partly or entirely held in main storage, as explained earlier in this chapter (see p. 228).
Otherwise it should be stored on the most rapidly accessible device available.

Reference to the track index This will take between three-quarters of a revolution and a full revolution as the start of the index will need to be located before it can be searched.
This will take R/2 on average, followed by half the index - which is usually slightly over half a track in extent - before the required entry is located.

Reference to the appropriate data track The timing here depends on whether the record in question is stored on a prime or an overflow track.

#### 1 Prime track storage

If the record required is available on the prime data track it should be located, on average, in half a revolution.
When the start of the track has to be detected, this will be modified; the track index start will have been found - taking a time R/2 - and the index entry will have been located, read and processed during a single revolution (in most cases).
Thus the overall time to read the track index and locate the data record will be: These calculations will apply to files in which all the data records are held in sequence on the prime data track, as for example in IBM systems.
Retrieval of records in files handled using linked overflow will not be so straightforward.
Depending on the software and the linkages provided it is probable that overflow records will have to be retrieved and checked as they are encountered.
This will add at least one revolution for every overflow record and will mean that the time to locate a data record, after the data track has been located, will be: where there is an average of m overflow records per track.

The additional times caused by linkage handling can be avoided if the link held on the prime data track contains the record key, and if the software can detect whether the required record is in overflow quickly enough to avoid missing the start of the next record.

#### 2 Storage on an overflow track

The effects here can be analysed in three stages.
They are:

- a) first overflow records from a track;

- b) further overflow records from tracks on a cylinder stored in the cylinder overflow area;

- c) records stored in an independent overflow area on some other cylinder.

First overflow records do not add any additional time if the index has two entries per track, and if the index items point to the first record in the overflow chain.
The software will recognize the key concerned, and the prime data track will be bypassed.
In the linked overflow case, however, each overflow represents a break in the search.
Thus the link would be expected to occur on average after R/2, and the overflow record would also take an average of R/2tn locate (or R if the start of the overflow track has to be found before the record search can begin).
Depending on the software, further overflow records may take no additional time - if it is not necessary to follow all chains - or the average time per overflow record may be nR/2, where there are n overflow records per track and every overflow chain has to be followed during a record search.

Overflow records other than the first will cause a time lapse of at least (n - 1) R (see page 254 for details).

Overflow records held on a separate cylinder will require a head movement to the overflow cylinder.
An estimate of their number is given in Table 7.3 for the case where additions are random.
There will be little difference between embedded (that is, on the cylinder) and independent overflow methods when additions are random, and independent overflow will prove to be very wasteful of time.
As explained earlier, it is therefore important to avoid the use of independent overflow areas except as a safety precaution; the one exception to this is when updates are grouped in a few areas.

The effect of overflow records on the average seek times for directly processed records has been investigated by Montgomery and Hubbard and the author.
This work has shown the gradual deterioration of performance as random additions are made to a file, and the marked acceleration of this process as records are allocated to independent overflow.

#### Factors involved in design

##### 1 Blocking

Unlike its impact on sequential retrieval, the result of blocking on direct retrieval is not marked.
The record search process is not usually lengthened at all, so only the increased data transfer time needs to be considered.
This is generally of the order of a millisecond or so at most.

##### 2 Batching and sorting input

Sequential processing of an indexed sequential file avoids many access head movements and minimizes those that are unavoidable.
As an example, if there are 200 enquiries made to a file and the file is stored on a disk with 200 cylinders, a completely random distribution of these enquiries would lead to:

- 126 cylinders with one or more active records in them;

- 74 inactive cylinders.

Handling these enquiries directly would involve 200 average head movements, about 200 × 30 ms for a 3330, giving a total of 6 seconds.

By comparison, batching and sorting the enquiries would lead to 126 head movements, most of which would be an absolute minimum of 10 ms and none of which would be much longer than 15 ms.
In addition, about seventy-four cylinders could be skipped so there would be around 126 × 10 ms required for head movements.
This gives a time of about 1.3 seconds for head movements, rather less than a quarter of the earlier figure.
The difference grows as numbers increase; with anything over 1000 enquiries all the cylinders would be likely to be referenced, thus giving a time of 20 × 10 ms or 2 seconds for the batched and sorted input, and 2000 × 30 ms or 60 seconds for the unsorted input.

These figures do not allow for two important aspects of the situation.
The first is that sorting itself takes time.
This is relatively short, but there is also an operating time involved, and for safety a one-minute or five-minute overhead has been added to the actual sort times given in Fig. 7.22.
These [UNK] compare batching and sorting times with direct reference, for a file that takes up the whole of a 2314 disk.

The second consideration is that batching implies holding up the first enquiries to be received.
For a true enquiry such a delay is probably not possible, but in cases where the input is directly processed for convenience alone it should always be considered.
In the many instances where updates arise in a batch' mode, as for example incoming mail, there is seldom any good reason to process directly, as the overall level of service will be improved by batching and sorting.
The few quickly-processed updates that are handled first, if direct processing is adopted, are more than counterbalanced by the shorter overall run time and thus better average service performance achieved by batching and sorting.

The file designer will find it worthwhile to examine every direct processing application of an indexed sequential file critically.
When batches are large, overall throughput will be much improved if any runs can be converted to batched and sorted operations.
The break-even points between the two modes of processing can be seen clearly in Fig. 7.22; for numbers of records for which a sequential curve is above each straight line that represents the time required to process a record directly, direct processing is faster.
After the curve is below any given line, batches of that size or greater should be processed by batching and sorting when that is possible.

### 7.10 The impact of software on indexed sequential files

#### Manufacturers' software

Generally, manufacturers provide software to format, load, update and reference indexed sequential files.
Statistics on the number of embedded overflow areas that are full, how much space remains in the independent overflow area, how many non-first overflow records are being directly referenced, etc., are usually available.
These are of considerable assistance to the file designer, and should be examined at the end of each run, at least while operating data for a file is still limited.

The options available to the user will also allow definition of blocking factor, overflow technique and size of overflow areas.
As all of these may have default options, it is important that the designer should make positive decisions about them and ensure that the file does reflect the design intended for it.

Some other helpful features may be available but not made clear.
For example, handling of overflow is facilitated in IBM systems if the designer allocates sufficient buffer space (usually this means defining more than two I-O buffers).

A number of manufacturers provide a filestore facility that handles the storage of data files in a way that uses backing storage efficiently but does not allow the user any opportunity to optimize file performance.
Although ease of use is important, this approach to file design is not desirable unless the manufacturer's software also optimizes, which is seldom possible.

On occasions manufacturers' software is not highly efficient for a given application, and software houses have taken advantage of this to provide alternative packages.
The shortcomings focussed on by alternative suppliers a

- 1 Large user keys increase index size;

- 2 Records are unblocked in the overflow areas, which wastes space;

- 3 Separate software modules are required to handle direct and sequential retrieval, using a great deal of space in main storage;

- 4 Overflow records add markedly to run times;

- 5 When high hit rate files are processed, many revolutions are lost due to processing not being complete when the next record is located.

Some of the software that is available to exploit these conditions is discussed below.

#### Software packages

The COMTEN AMIGOS software allows the user to replace two separate IBM modules, one for sequential and the other for direct reference to an indexed sequential file, by a single module that requires less space and performs the same functions; this is particularly helpful if a single run updates sequentially but allows enquiries during the runs.
On the other hand, the dual-function module is larger than either of the single-function modules it replaces, so it offers no benefit for single-function runs.

The AMIGOS package includes two other functions that improve space utilization and processing speed.
As a standard, each track is divided into just THREE data blocks, so arranged that they are read in the order 1,3,2 as shown in Fig. 7.23.
This allows a reasonable time for processing, and results in fewer lost revolutions than is normally possible.
However, it doubles the minimum run time, and so will not help in some cases.
The second change is that records are also blocked in overflow.
Although this will mean a slightly increased retrieval time (of the order of 5 - 8 ms depending on the device) it is claimed that the space saving more than offsets this overhead.

Universal Software Inc. offer a PSAM package that achieves improvement by splitting additions between blocks in the prime data area - i.e. providing distributed free space - rather than defining separate overflow areas.
This provides more rapid access to established files, and less-frequent reorganizations.
Freshly reorganized files are identical in performance, whether organized using PSAM or IBM's ISAM.
It is also claimed to reduce space usage.

Examples like these make it appear that the performance of manufacturers' software can always be bettered.
Coyle showed that it was possible to improve the speed of an ISAM file by more than four times by using the [UNK] optimization options available in IBM's software.
The steps he took are shown in Fig. 7.24.
In the case he quotes it was decided not to use alternative software, and other users should ensure that they have already exhausted the possibilities of improving the performance of their present software before they turn to other sources.

The manufacturers have incorporated some of the ideas introduced by software houses into their own offerings, and the facilities provided by IBM's VSAM illustrate this process.
VSAM is of interest to us, partly because the indexing technique used, which has been described in detail by Wagner, is a modified B-tree.

#### IBM's VSAM (Virtual Sequential Access Method)

This file organization technique is a development of ISAM that incorporates many of the concepts used in the software obtainable from independent suppliers.
The method is only available for use with virtual storage systems, and offers access to records in three ways.
These are:

- 1 Reference by record key;,

- 2 Reference by address relative to the start of the file using the relative byte address (RBA for short);

- 3 Reference by relative record number (fixed-length records only).

Of these, 1 (referring to the record by its key) can be compared to ISAM in operation, so the similarities and differences are examined here.
A key-sequenced file or data set is created, with its associated indexes, as a cluster.
For our purposes the cluster is an indexed file.

Data storage is divided into control intervals which are continuous areas of storage of a size that is not necessarily related to the physical make-up of the device on which the data is stored.
This is shown in Fig. 7.25.
A control interval is the unit of data moved between virtual and backing storage.
In a sense it is equivalent to a track in an ISAM file, in that there is one index entry per control interval.

A group of control intervals makes up a control area.
The whole of a control area is referenced by the entries in a single index record, and in a sense this is equivalent to a cylinder in ISAM terms.
The index relates key values to the relative byte address locations of the data record.

Indexes are arranged as follows.
All the higher indexes are collectively called the index set, and they are divided into index records containing a number of pointers.
One of these pointers indicates the next index record at this level, and is used to move sequentially through the file.
The other pointers indicate the location of a number of index records at a lower level.
The lowest level of index records makes up the sequence set, and in this case the pointers are to control intervals; the total number of control intervals indexed by one index record makes up a control area.
The structure of a key-sequenced VSAM file is shown Fig. 7.26.

Additions to the file are catered for by the provision of distributed free space.
This can be allocated by allowing a number of control intervals to remain entirely empty, by leaving space at the end of every control interval that contains data records, or by a combination of both techniques.
As all the space available in a control area is allocated when the file is set up, VSAM provides the equivalent of a cylinder overflow area in ISAM and a proportion of free space in data storage areas, just as was done in ICL 1900 series software.
Records added to a file are blocked in the same way as the original data and not unblocked as in ISAM.
VSAM does not leave deleted records in the data area, as does ISAM.
Instead, the area occupied by the record or part of a record that has been deleted is added to the distributed free space available.
Within the control interval the remaining records are moved towards the start of the control interval, which requires their RBAs to be altered and avoids fragmentation of the free space in the control interval.

When records are inserted, the RBAs of any following records will be increased as a result of their movement in the control interval.
If there is not sufficient space for the inserted records in the control interval, a control interval split takes place under VSAM control.
This uses any free control intervals in the control area rather than the free space in other control intervals containing data.
The consequence of this is that the records may not be physically in sequence after a control interval split, although they will be handled in sequence by the indexes.

If there is insufficient room in the control area to handle all additions, a control area split takes place under VSAM control.
Approximately half the control intervals in the old control area are moved to the new control area, which is made available either as a result of decisions taken when the file was defined or by extending the file as required.
The new control area is likely to be physically remote from the original site of the data.
Although VSAM will handle it sequentially, the situation is similar to that of providing an independent overflow area in ISAM and should be avoided whenever possible.
Splits in control intervals and control areas are shown in fig. 7.27.

VSAM provides the possibility of holding alternate indexes, so the user can reference a file using a number of different keys.
The index set defined first is known as the prime index, to distinguish it from the alternate indexes.
Alternate indexes are updated when records are added or deleted, if UPGRADE is specified in the alternate index definition.
Alternate keys can be duplicated, unlike primary keys, so that a department code could be an alternate key and allow searches to be carried out to select personnel from a particular department.
Keys in all VSAM indexes are compressed, only the distinguishing parts of the keys being stored, in order to reduce the size of index entries.
These facilities make VSAM more similar to database software than most of the file organization techniques that have been examined so far - in fact, many of the database systems available for mini- and micro-computers provide only this multiple index facility.
VSAM itself is used to handle the tables in IBM's DB2 relational database software.

VSAM can be optimized by careful design, applying the same principles that have been described earlier.
The designer should look at the following factors:

- 1 The relation of data areas and index position to the physical characteristics of the device.
The portability of a VSAM file from one device to another, and from operation under one OS/VS system to another, or from DOS/VS to OS/VS is helpful, as it allows for rapid conversion when different [UNK] disks are installed.
However, for optimum performance the size of control intervals and control areas should be so arranged that a sequence set record will be stored on the same cylinder as the control area it indexes.
This means that movement from, say, a 3330 to a 3350 will require the definition of new control area sizes unless the number of control areas on a cylinder is already 2n on the 3330.
There will then be 3n control areas per cylinder on the 3350 and no loss of performance will result from the transfer.
The way the conversion operates is shown in Figure 7.25.

- 2 The size and number of the buffers provided by the user for VSAM directly determines the number of higher index records held in virtual storage (as against backing storage).
Hence, buffers should be both as large as possible and related in size to index record size.

- 3 Distribution of free space - the ability to define empty control intervals where they are required - means that careful planning with a knowledge of the likely distribution of additions will reduce the need for control area splits, and possibly of control interval splits.
This will improve performance.
Further details of VSAM are available in IBM publications.

- 4 The size of blocks used to hold data.
Although the user may imagine that any block size will be acceptable, VSAM only uses blocks of size 512b or 2048b, where b can take any value in the range 1-16; this means that VSAM will round up any intermediate value to the next available block size, so wasting the difference between the two values.
Choice of block size is therefore important if wasted space is to be avoided.

#### Conclusion

Wright has described both ISAM and VSAM files as applied to bubble memory, taking account of the particular design requirements imposed by bubble memory.
He also provides a very detailed description of the medium.
Jalics has compared the performance of IBM's ISAM on a PC AT, a 370/158 and a 3081; contrary to expectations, the micro comes very well out of this trial, due to its use of an improved balanced tree index structure.

Indexed files are easily created as a result of the provision of software by manufacturers.
Improvements are offered by many software houses; the designer will generally find that it pays to explore all possible optimization techniques for the manufacturers' software before examining alternatives.
In some cases, however, the design philosophy of another supplier will meet the user's needs more precisely.
A full examination of the application will lead to an informed choice, and optimum performance.

#### Revision questions

- 1 Describe the main areas of an indexed sequential file.
Indicate which of them are essential and which are used only when required.

- 2 Why is a hierarchy of indexes used in IS files rather than a single large index?
What effect does the size of the record key have on index size?

- 3 Explain the effect of index positioning on file performance and set out the rules for positioning in various circumstances.

- 4 What overflow areas are provided in these files?
Explain and justify the options you would take up in the case of: even additions; random additions;, grouped additions; no additions.

- 5 How are records inserted into IS files?
Describe and comment on two or more techniques, and the way they affect:

- a) - 5 record addition;

- b) - 5 subsequent record retrieval.

- 6 Explain how blocking of records affects skip-sequential processing.

- 7 Outline the sequence of events during direct retrieval of a record from an IS file.
Give times for each step, and hence or otherwise comment on methods of optimizing direct retrieval.

- 8 How would you decide whether input to a file should be processed directly or batched and sorted?
Give worked examples to justify your conclusions.

- 9 Why do some software houses offer 'improved' indexed sequential file organization software?
How valid are their claims?

- 10 Describe IBM's VSAM software, explaining how it operates and how it can be optimized.

- 11 What is a balanced tree?
Describe two versions of balanced tree indexing and their associated files, commenting on the strengths and weaknesses of each method.

- 12 Describe a B-tree.
Explain the advantages this type of tree has over balanced trees, and compare and contrast their performance over as full a range of applications as possible.

## FILE ORGANIZATION FOR MULTIPLE-KEY PROCESSING

### 8.1 Introduction

Much of data processing involves retrieving records that refer to a given customer, stock item or member of staff.
In each of these cases a single key is all that is required to reference the record.
However, in retrieving documents from a database holding the contents of a library, or when a request is based on meeting several different criteria, the situation is quite different.
There are no longer any single 'keys' that uniquely define the document or documents wanted by the user.
Generally, a combination of words or phrases is used as descriptors that can be combined to select the desired record.
For example, a business in the United States may wish to assign an engineer to work in Japan for some months.
The personnel file might be examined to list all the employees who meet the following criteria:

- Speaks Japanese AND

- Graduate Engineer AND

- Single

The personnel department would make the final choice, from the list produced by this enquiry.
If the resulting list were too large, further descriptors could be added to reduce it.
If it were too small, the 'single' restriction might be removed; if the whole family also needed to be sent to Japan this would add to the assignment costs, which might be an acceptable price to pay in order to send the right person.

Multiple-key applications present different problems from those associated with the single-key files discussed so far.
For smaller files, magnetic tape is the obvious storage medium - an example is the International Food Information Service described by Larbey.
Small files that demand multiple-key handling are usually stored on magnetic tape and processed sequentially.
A file arranged as in Fig. 8.1 has considerable advantages for the retrieval of records that meet some request based on a number of separate criteria which are often called record attributes or descriptors.

Each record (such as a title, a summary or a full text) is characterized by the descriptors D1, D2, etc.
Records 1 and 2 have a common descriptor D3, records 2 and 3 share D6, while records 1 and 3 have D1 in common.
Record 4 has no shared descriptors with the other three records, although it may have with later records.

The file organization techniques used for multiple-key processing are discussed in this chapter, but chained and tree structures used in database systems are not.

#### 8.2 File types

Two main file types are used in multiple-key retrieval.
These are serial, which was described briefly above, and inverted.
There are variations of each technique, and they are considered below.

#### Serial files

The straightforward method of handling the examination of multiple keys is to hold all the keys in the record, as in Fig. 8.1.
A further example of this is shown in Table 8.1; each personnel record holds a number of fields, any one of which may be used as a key.

A specific request might require a count of all the grade 2 employees in the systems department.
This could be answered by scanning the whole file record by record, examining each to see whether it met the specified requirements.
After all the records have been scanned a list of two names - Mason and Vince - would be provided.

In the case of a personnel file, the list is likely to be sorted into an order that depends on some major key - in this case, usually alphabetic order or personnel number.
If the file were made up of documents, books or papers the overall classification would probably be based on subject, and the order within subject might well be accession date.
In these library databases the major key is often an accession number.
In either case, the order does not affect the amount of searching to be done and in this sense the file is serial, although it will probably be in sequential order with respect to the major key.

This type of file has to be scanned completely before a single query can be answered.
Each record is examined in turn, and its descriptors are compared with those of the search request (which might be like that for a graduate engineer with other attributes shown above).
Because only one record is examined at a time, it is possible to test the descriptors against very complex Boolean conditions, expressed in terms of the descriptors desired by the user, to obtain a match.
The work areas required in main storage are relatively small as only one record is being examined at any one time.
However, as the data file increases in size, the time taken to search through [UNK] the data increases in proportion.
At between 20 000 and 60 000 records, the search time becomes so slow that it no longer allows a reasonable number of requests to be handled in a working day.
The point at which this happens depends on a number of factors such as complexity of requests in terms of Boolean conditions, speed of access of the medium in use, and size of data file.

A number of steps can be taken to speed up processing, each depending on some different method of handling the search.
The first of these is the bit-pattern index, in which all the alternative descriptors for each record are given values of 1 if the attribute is present and 0 if it is not.
The data in Table 8.1 has been organized into bit-pattern format in Table 8.2.

In cases such as that of a personnel file, for which the number of attributes is relatively low and the same for each record, a bit-pattern index can be a compact way of storing information about the file.
However, it is not very useful for a bibliographic file in which there may be thousands of potential attributes for each record, only a very few of which are non-zero.
The storage of this sort of data causes the difficulty that the compact format is counterbalanced by the redundant information.

Bit-pattern indexes will be examined in more detail later; however, in some circumstances a more rapid reference technique than that provided by a serial file is required.
For this purpose, inverted files have been developed.

#### Inverted files

When records are to be selected on the basis of the state of one or more attributes, a serial search concentrates on the records, examining each in turn to see if it meets the specified conditions of the search.
In fact, what is known from these specified conditions is the attributes required.
A search of the records having a given attribute, to see which of them also has a second, third,... etc. in the required list, will eliminate all the records that are not wanted.
This is achieved by inverting the file, i.e. by providing lists of records or record references possessing each one of the various attributes in turn.
The resulting set of lists - which are, in effect, indexes - is shown in Fig. 8.2 for the same records in a data file that have already been shown in Fig.8.1.

A further example is shown in Table 8.3, which is an inverted version of the data set out in Tables 8.1 and 8.2.
Given that a male in the operations department is required who is able to speak Italian, the male list is scanned first.
This provides seven records.
When the operations condition is added, only records 94 and 122 meet the double condition.
Adding the need to speak Italian eliminates record 94, leaving only a single employee from this small part of the personnel file, with personnel number 122, who meets all the three conditions.

A file in which all the attributes are inverted, i.e. have indexes provided so that a direct search can be made on any attribute, is known as fully inverted.

A file in which only a number of selected attributes have indexes provided is known as partially inverted.

In the case of a fully inverted file the designer has the option of holding very little information in the master file itself, and assembling records from their constituent parts as they are referenced.
In practice many designers prefer to hold the complete record in the master file, as this avoids the problem of assembling information about attributes possessed by the record but not specifically referenced in the request.
To take the example of record 122, grade and branch were not included in the request for a male from operations department who can speak Italian.
This information would not be automatically collected from the request, but is essential in order to describe the person fully, and the retrieval process has to ensure that it is provided.

A master file record in a partially inverted file will always be required to hold at least the data on fields that are not inverted.
The most usual arrangement is to have inverted lists of each descriptor, with a list of the major record keys and addresses or, if each record has a separate address, addresses only, for each of the records to which that descriptor applies.
The master file contains the complete record.
Keeping the index record size down is helpful because if the inverted indexes are small they can be held in main storage, and so cut search times down to a minimum.

Inverted files should not be confused with the alternate indexes available in many indexed file systems such as VSAM or ICL's 2900 series equivalent.
Each such index can be used to give limited partial inversion, i.e. of one descriptor at a time, but they are generally provided and employed to allow the file to be accessed in ways other than by the major key, rather than to carry out an elimination of master file records not meeting some search criterion.
An example would be to use department code as an alternate key to provide personnel listings by department from a personnel file arranged in some other order, such as alphabetic.

When an inverted organization is employed, a number of limitations may follow.
First, the file may not be able to support such complicated search conditions as a serial file, because the size of work area required to process a request is now much larger; instead of dealing with one record at a time, the system now deals with all relevant records at once.
This speeds request handling but greatly increases the work area size needed, particularly if a very widely used descriptor is the first to be cited in the retrieval request.

Second, addition of records to the file is no longer a matter of adding to the end of the file.
Each descriptor record throughout the file that applies to this new record has to be updated, so the process is relatively slow.
Third, the space requirements for such a file are considerably greater than those for a serial file.
Spiegel and Miller investigated IBM's STAIRS/AQUARIUS system (Storage and Information Retrieval System/A Query and Retrieval Interactive Utility System).
The system uses four main files: a dictionary, a text data set, a text index data set, and an inverted file of all descriptors used in the database.
These files are indexed by the use of BDAM (Basic Direct Access Method) and in a typical database of just over 2 Gbytes, which they found was the average size of those they examined, the number of characters in the files comprising the database was as follows:

- TEXT 864 000 000

- TEXT INDEX 83 000 000

- INVERTED 781 000 000

- DICTIONARY 442 000 000

It is clear that the basic text file has been increased by around 150 per cent in order to provide the retrieval capabilities offered by the package.
This is typical, and should he borne in mind before abandoning single-key reference, which usually involves an overhead of only 5 - 20 per cent in providing the facilities offered by indexed sequential or direct organizations.

The system described by Spiegel and Miller could handle up to one thousand queries per hour, but many of them were relatively straightforward.
Larbey described a tape-based system in which the text file contained a maximum of 1400 items, each of 4300 characters or less - six megabytes at most.
This system provided SDI (Selective Dissemination of Information) on current data only to eighty scientists who used a set of thirty-eight separate query profiles.
Each profile was made up of a combination of descriptors and Boolean conditions, and averaged twenty-six distinct search terms.
Production of the complete SDI output took 12 minutes, or just under 200 queries an hour.

A further file storage technique is sometimes useful in handling information retrieval applications.
This is the multilist.

#### Multilist files

In this type of file there are the same sets of indexes as are required for an inverted file.
However, in this case only the first reference to any descriptor appears in an index, while all further linkages are made from record to record (rather as in a chain of synonyms in a direct file).
The arrangement of the same data that has been shown in Figs. 8.1 and 8.2, but now held as a multilist, is shown in Fig. 8.3.

Cardenas compared inverted files with multilists, showing that their space requirements are usually very similar, and that the speed of access provided by each file organization is dependent on the structure of the data.
In particular, multilists provide rapid access when the file has many different descriptors that apply to only a few records, as in this case each chain will be short.
Cardenas also commented that '... the manner in which secondary indexes or dictionaries and associated lists are managed, may have under-estimated impacts.'
Much of this book is aimed at ensuring that file designers know how to minimize the impact of such indexes or dictionaries on space used and time wasted in file processing.

McDonell provided a useful analysis of what is involved in addition, deletion or modification of records, so far as the maintenance and use of associative key lists is concerned; he defined an associative key list as 'a list for each indexed key which joins together all the main file records containing that key'.
He also compared multilists with inverted files, and showed that inverted files have an advantage when the indexes have to be altered frequently.
As the performance of the two is relatively similar and inverted files are more widely used in their own right, most of this chapter deals with serial and inverted files.

### 8.3 Record reference

For small numbers of records, serial files have significant advantages.
The first is that, because each record is dealt with singly, the main storage work area space requirements are very low.
This allows relatively complex Boolean conditions to be built up and tested, such as: in the programming department AND able to speak French BUT NOT if in grade 3 UNLESS from North branch.
In the example in Table 8. 1 the only person corresponding to this request is Duncan.
In this case the BUT NOT condition was not fulfilled, but would in any case have been overridden by the UNLESS.

This example is not in itself very complex.
However, it indicates how very complicated multiple conditions can be built up in the creation of user profiles for information retrieval systems.
This is because in searching a very large library collection it is essential to attempt to ensure that the user gets just those references that are required.
A profile that provides far too many irrelevant references is of little use; such lists normally find their way into a wastepaper basket because the user sees that they are full of irrelevant material and is not prepared to search through them hoping to find some relevant references.
On the other hand a profile that fails to provide the user with required material is equally useless, however brief it may be.
This second problem is more dangerous than the first because the user may not realize that information is missing.

Information retrieval systems include the concepts of relevance - the proportion of retrieved material that is relevant - and recall - the proportion of relevant material that is retrieved.
These are dealt with in some detail elsewhere, but the reader who wishes to study the matter in depth should consult specialist references.

As the numbers of records increase, the problem of waiting for a reply to a query until the whole of a serial file has been searched increases in proportion, and eventually this delay becomes unacceptable.
As mentioned earlier, one possible answer is to use a bit-pattern index of the sort shown in Table 8.2.
When the number of attributes is low, this allows very economical storage of the data about a particular record.
A single bit represents each possible attribute.
If it is set to one, the record in question has this attribute.
If it is set to zero, the record does not.

Searching such an index is very rapid.
For simple cases an equal compare is all that is needed.
However, this means that every attribute has to be specified.
In an earlier example it was shown that a large proportion of requests only require some attributes to be present or absent.
In these cases a Boolean AND condition can be set up.
For instance, a request for a male in operations department who can speak Italian can be tested by comparing each of the bit-pattern index entries in Table 8.3 against a mask of: The Boolean condition will be an AND, which will only return a true indication if all these bits are on.

A bit-pattern index can extend the use of serial files when the number of attributes is limited, but a break-even point will occur somewhere between 20 000 and 100000 records, depending on record size, number of possible attributes and the complexity of Boolean conditions required.
In bibliographic applications the number of possible attributes may be many thousands.
In this case the only possible solution when retrieval times become too long is to turn to an inverted file or a multilist.
An inverted file is the usual choice, but when there are many attributes, each of which is used by relatively few records, it will be worth considering multilist files.

It was pointed out earlier that one difficulty in using inverted files is the need to deal with all the records possessing a given attribute at the same time, so that a great deal of working space is required in main storage.
This is reduced if there are many possible attributes because each attribute index list will tend to be shorter.
Thus, the more suitable the application is for bit-pattern index handling (small numbers of possible attributes), the less suitable it is for inverted file handling.

The number of nested Boolean conditions that can be handled by an inverted file is generally less than the number a serial file can handle.
In addition, the conditions OUT OF, specifying any n conditions out of a larger number, and BETWEEN.
setting upper and lower limits to the value of an attribute, are difficult to achieve.
These conditions can be very useful in setting up a user search profile, which is one reason that information retrieval systems often use a serial file for new accessions, which are matched against user profiles intended to inform users of the latest accessions in their subject field.
This is linked to a complete file of the bibliographic collection held in inverted form.
All the records in the serial file are transferred to the inverted file at intervals, generally when the size of the serial file is beginning to make reference to it relatively slow.
The reasons for keeping down the number of updates to an inverted file are discussed below, and the form of a dual serial-inverted file system is shown in Fig. 8.4.
Such a system has been discussed further by the author.

### 8.4 Additions and alterations

Serial files can handle additions without difficulty.
In very simple cases the new record is added to the end of the file.
Even if the master file is held in a sorted order there will be no particular difficulty, as these files are usually stored on magnetic tapes.
All that is required is to create a new file, although this can be time-consuming.

Inverted files require quite different treatment.
Ideally, the indexes should be held in main storage.
They will certainly need to be on a direct access device.
Addition of a new record will mean that a number of indexes will have to be updated, one for each attribute possessed by the new record.
Thus, even if space is left within and at the end of each index, updating will involve the shifting and shuffling of a number of records or the use of pointers and links to the new records.

The contrast between these two is a further reason for the popularity of dual systems.
It is easier to handle the file in serial form until sufficient new records are available to justify the time and effort involved in an update of the inverted file.

### 8.5 Storage requirements

Serial files can be held in one coherent file.
This is very convenient for the user as it requires the minimum of handling.
An inverted file, however, has to be held in a number of related indexes, and is thus far more 'bitty'.
In, the typical overhead of indexes and related files leads to a final size of about two and a half times the size of the corresponding serial file.
However, there can very occasionally be a space-saving in the use of an inverted file as is shown in the discussion below, due to Revell.

Suppose a file contains N fixed-length records and each record is comprised of a key of k characters and n data items of average size a characters.
If this file is fully inverted, the resultant file will contain as many records as there are unique descriptor values - say V. The inverted file will be made up of variable-length records.
For each descriptor value, the rest of the record will be a list of the keys of the original file records which possess that specific value.

If the average number of keys in the inverted file records is A then: since the total number of terms in both the original and inverted files must be equal.

The size of the original file is: and the size of the inverted file is:

It is therefore advantageous, purely from a size point of view, to use an inverted file when: or [UNK]

For applications of size such that equation (8 1) approximates to:

Additionally, if n is large the expression simplifies further to:

Thus, the decision as to whether a file takes up more space in serial or inverted form depends on the ratio of the size of the key and the data items.
Note that this is of limited use as it implies that the data is held only in the index or in the main file.
The more usual arrangement is that the inverted indexes are an addition to the main file, as explained earlier.
For this reason it is not often possible to achieve a reduction in space requirement by using an inverted file.

#### Conclusion

Serial or inverted files specifically designed for the retrieval of records on the basis of the values of multiple keys are a useful tool for the file designer.
Generally the file itself, and the associated processing programs, will have to be written by the user if high standards of optimization are required.
However, the alternate index facility of VSAM and similar software can sometimes be used to build the indexes required.

Salton has reviewed the methods of handling information retrieval, while a number of authors have described specific techniques that offer advantages in particular situations.
Ramamohanarao et al.
described a mixed hashing/descriptor-based method of retrieval; Nievergelt et al.
presented a 'grid' file that performs particularly well when the number of search attributes is ten or less, and offers a high data storage utilization, good growth characteristics and efficient processing of range queries; Stanfill and Kahle explain the principles of a parallel free-text search on a particular parallel computer, and claim a retrieval speed of 2 - 3 minutes for Boolean queries of 25 and 20000 terms respectively when the database in question takes up 15 Gbytes of storage space.
Their method of searching does not depend on pre-determined descriptors.

Many database systems use the inverted technique, and the convenience of having the software provided by such systems will often outweigh its relative inefficiency.
'Tuning' of the database software may also be possible using manufacturer-supplied options to achieve results more in line with those attainable by programs written in-house.
In order to obtain optimum results, however, there is no substitute for a carefully user-designed and written system.

#### Revision questions

- 1 Give an example of an application that might require multiple-key processing.

- 2 What are the main file types used in multiple-key retrieval?
Describe the make-up of each type and use the same set of data to show the different data structures required in each file type.

- 3 Use your own data to show how records are retrieved from each of the types of file you have described.

- 4 When would a bit-pattern index be useful and when not?
Explain and justify your answer.

- 5 When would you use a serial file for information retrieval?
At what point would you switch to an inverted file?
Explain the factors that influence this break-even point.

- 6 What are the advantages and drawbacks of inverted files?
When might you be forced to use an inverted file, even if it is not very efficient?

- 7 How and why would a dual system including both inverted and serial files be used?

- 8 Describe a multilist file.
When might such a file be preferred to an inverted file for multiple-key processing?

- 9 Discuss the space requirements of serial, inverted and multilist files, making clear the assumptions on which you are working.

- 10 Show how software that allows alternate indexes to be created can be used to set up an inverted file system

