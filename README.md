# KmapSimplifier
An algorithm which performs K-Map simplication for Digital Electronics design
#V1
Simplifies the minterm expression for given minterms
Input format:
First line should be integer N , the number of bits in the minterms. Next line should contain 2^N space seperated terms , each being 0 or 1 .
Eg , if we want to simplify ABC + ABC' + AB'C  which is equivalent to m(5,6,7)
input will be
3
 0 0 0 0 0 1 1 1

Efficiency of algorithm is (Nlog(M))**2
where N is the number of 1's in the second line of the input and M is the number of bits
