# Matrices and engineering dynamics

## Foreword: Alan Simpson's tribute to his co-author

My co-author and friend Professor A. R. Collar, C. B. E., LL. D., F. R. S., Emeritus Professor of Aeronautical Engineering in the University of Bristol, distinguished aeronautical scientist and former Vice-Chancellor of that University, died at his home in Bristol on 12th February 1986, just ten days before his 78th birthday, and only a short time before our book was published.

Roderick's eminence as an engineering scientist and scholar is well known.
However, he was also a man of exceptional personal warmth and charm.
He was, in every sense, a gentleman and a gentle man.
Nevertheless, when the occasion demanded it (as it did during the turbulent period in which he became Vice-Chancellor of Bristol University), he showed great courage and firmness - the latter always in the nicest possible way.

Roderick's interests were wide; for example sport (cricket, tennis and football - both varieties), good music (he played the violin), verse (he read extensively and composed, when inspired or provoked, to match an occasion and could recite extensively from memory - particularly W. S. Gilbert), games and puzzles (chess, cribbage, mathematical conundrums and crosswords; he could, at his zenith, do The Times Crossword any day in less than twenty minutes), and art (he was an active member of The Bristol Savages).
He was also president of a local Gilbert and Sullivan society for many years.
He did much hospital work: for several years up to his retirement he had been Chairman of the South West Regional Hospital Management Board and was an active hospital visitor.
His charitable works were extensive.
He had been President of the Bristol Rotary Club, chairman of governors of many schools and colleges (notably R. M. C. S., Shrivenham), and was a Liveryman of the Guild of Air Pilots and Navigators, to mention but a few of his activities.

He was the perfect committee chairman: he loved committee work when it was productive, and it always was when he was in the chair.
Innate within him was the ability to put committee members at their ease, so that they could give of their best, and he could abstract the maximum amount of information.
This ability was evident in his many years of A. R. C.
Committee and Council chairmanship and in his chairmanship of the university committees, culminating in his Vice-Chancellorship.
At one time he was on 25 committees, over and above those within the University, and was chairman of many of these.
At the height of this committee and other administrative work, Roderick often expressed his desire to return to his mathematics and, in particular, to write a sequel to his famous book (with R. A. Frazer and W. J. Duncan) Elementary Matrices.
I had agreed to be co-author, but it was not until seven years after his retirement that work could begin, for only then had his committee activities abated to an extent which allowed the long periods necessary for writing and discussion.

It is appropriate to recall that Elementary Matrices (1938) was printed nine times in U. K., several times in U. S. A., was translated into Russian and Czech, and finally republished in hardback in U. S. A. in 1983.
It was written following a period of pioneering work on the application of matrices to engineering problems, undertaken by Frazer, Duncan and Collar at the N. P. L., Teddington, in the 1930s.
Collar was certainly the junior member of the partnership, but those who know his mathematical style are well able to perceive his many areas of contribution to the book.
In later years, Roderick confided that he had been far from happy with the title, for the book certainly was not "elementary."
Any sequel must be "more elementary" and tailored to the needs of the engineering student.
This is not to be viewed as condescending: Roderick regarded himself as a student of the subject and said so on many occasions during the writing of the new book.

As work began in earnest on the book, I realised that Roderick had lost none of the skills that I, as his research student twenty years before, had regarded with awe.
But writing now was not easy for him: he had begun to suffer with arthritis in the year following his retirement, and had had to give up his violin owing to lack of flexibility of his fingers, and as the condition developed, he found writing more and more difficult.
This did not deter him, as, between 1980 and 1984, he completed over 400 pages of manuscript.
On average, we met for three hours every ten days, constantly revising, exchanging and criticising so that in the end we had both had a hand in everything.
The whole must have been rewritten about five times.
Roderick was always seeking a better way of putting things in order to remove all possible ambiguities and to assist the reader to the maximum extent: if this meant rewriting 100 times he would gladly do it.
He was meticulous, but never pedantic.

Roderick's last, and possibly finest, contributions to this book were the Theorems XII and XV of Chapter 1 which were completed in 1985 shortly after the serious fall which perhaps precipitated the leukaemia from which he failed to recover, despite repeated blood transfusions.
At this stage, the arthritis in his fingers was scarcely bearable and writing extremely painful.
But the exceptional clarity of his thought processes was evidently still totally unimpaired.
We last met on the Sunday before his death.
Although very weak, he was anxious to discuss technical matters, among which were possible revisions to Chapter 6.
He had, a few weeks before, completed an excellent set of autobiographical notes and, characteristically, a sonnet to his wife, Bobbie, on her birthday.

Roderick will be sadly missed in every circle in which he moved, but most of all, of course, by Bobbie, whose devotion and fortitude was his greatest comfort in his final illness, and whose forbearance over many years enabled Roderick to spend such a great amount of their valuable time on the book.

A. S., February 1986.

## INTRODUCTION

In this text, which is aimed at senior undergraduate students of engineering, the subject of matrices is described and developed before being applied to some of the problems of engineering dynamics.
The matrix theory is presented in classical algebraic form with no recourse to the notions and nomenclature of vector space theory.
In this respect, the book is a sequel to the earlier work Elementary Matrices by Frazer, Duncan and Collar, a book which, by presenting problems in a form which could be assimilated by computers, stimulated the growth of the latter.
In the present book, the subject is brought up to date and related to modern computer methods.
The text is punctuated throughout by numerical examples, most usually based on matrices of small order.
The treatment of engineering dynamics is almost invariably linear, although examples of simple non-linear formulations are provided.

Chapter 1 contains definitions of the basic laws of matrix manipulation and of matrix types.
Matrix calculus is introduced via the Sylvester expansion theorem and considerable emphasis is placed on the matrix eigenvalue problem.
A useful collection of theorems and proofs is presented at the end of the chapter: among these is what is thought to be a novel proof of Sylvester's law of degeneracy.
Chapter 2 is concerned with numerical methods: it divides into two major parts, namely methods of reciprocation, triangulation and solution of linear algebraic equations, and methods for the solution of eigenvalue problems.
Both parts address many alternative procedures, all of which are exemplified - most often by using matrices of order 4.

Chapter 3 concerns neighbour systems, a subject of great importance in engineering dynamics.
The Collar-Jahn method, along with several new variants, is presented.
The difficult problems associated with adjacent or confluent eigenvalues are outlined and methods of solution developed and discussed.
The chapter is thought to be the first on this subject in a text of this type.

Fundamental concepts of dynamical systems are introduced in the simplest of terms, in Chapter 4.
Formulations based on the principle of virtual work are given emphasis: conservative and non-conservative actions are carefully delineated and discussed in the context of discrete systems.
The important notion of semi-rigidity is introduced.
The ideas of Chapter 4 are carried forward in Chapter 5 via a proof of Hamilton's principle and the associated proof of the Lagrange equations.
Conservative and non-conservative actions are identified by the form of the matrices appearing as coefficient arrays in the equations of motion.
A general treatment of the linear conservative dynamical system is given, including calculation of natural frequencies and normal modes, and topics such as removal of zero frequency roots.
An outline of structural damping modelling is also given.

Chapter 6 deals in general terms with the solution of sets of linear differential equations with constant coefficients.
The concept of the matrix Laplace transform is introduced.
In the second part of his chapter, the subject of linear stability theory is discussed, leading from the fundamental encirclement theorem of Cauchy, via the criteria of Leonhard and Routh, to the Poincaré-Liapunov method.
An inverse method for the calculation of stability boundaries is also discussed.

Chapter 7 gives an extended treatment of the dynamics problems of continuous linear systems by use of the semi-rigid method in matrix form.
Emphasis is placed on one-dimensional systems, but flat plate problems are also discussed.
Exact formulations based on "dynamic stiffness" or "receptance" are highlighted, and the concept of "finite element" is introduced as a natural extension of the semi-rigid method.
Finally, Chapter 8 deals with the dynamics of composite systems in a manner which owes much to the pioneering work of Kron.
The finite element and dynamic stiffness methods are introduced and exemplified in simple cases.
The importance of the connexion graph is emphasised.
The chapter ends with an extensive discussion of Kron's eigenvalue method followed by proofs of the Wittrick-Williams and Simpson counting algorithms.

The book will be accompanied by a "computational adjunct" in which a number of BASIC programs for use on home computers will be presented.
These programs, which will be available on disc, relate to specific topics covered in the main text and may be used to verify calculations performed therein.
Some of the programs, however, are of the general-purpose type.

## Properties of Matrices

### 1.1 ASSUMPTIONS, CONVENTIONS; TRANSPOSITION AND RELATED DEFINITIONS

In this chapter we shall discuss certain characteristics and properties of matrices which are of particular importance in dynamical studies of systems with multiple degrees of freedom.
We assume the reader to be familiar with the notation of matrices and with the rules of combination: addition, multiplication, etc., and with conformability and non-permutability.
We also assume familiarity with the elementary rules for combination and evaluation of determinants.

In general, matrices are rectangular; but of particular importance are matrices having equal numbers of rows and columns - i.e. square matrices - and those having only a single row or column, which we call vectors; both types are special forms of rectangular matrices.
Normally, we shall use capital bold type, e.g. A, to denote square and rectangular matrices having two or more rows and columns, and lower case bold type, e.g. x, to denote vectors.

If a matrix A has m rows and n columns, i.e. it is of order (m × n), its typical element [UNK] lies at the intersection of the ith row and jth column ([UNK]).
If we form the matrix [UNK] by writing columns for rows in order, the new matrix, of order (n × m) is called the transpose of A and is denoted by [UNK].
For example, [UNK].
The process is clearly one of reflection in the diagonal containing the terms [UNK], which is described as the principal diagonal.
It is of particular importance in square matrices.
The terms [UNK] in A form the superdiagonal and [UNK] the infradiagonal, while for a square matrix of order (n × n) - or more simply, of order n - the elements [UNK], form the secondary diagonal.
An important property of a square matrix is its trace; this is the sum of all the elements in the principal diagonal.

Wherever it saves space, we shall always write a column vector x as [UNK] the braces{} denote that this is to be read as a column.
Since in dynamics, we are usually more often concerned with columns than with rows, we shall write a row vector as the transpose of a column vector, e.g. [UNK].

### 1.2 SYMMETRIC AND SKEW-SYMMETRIC MATRICES

If [UNK], the matrices, which are necessarily square, are termed symmetric; if [UNK], they are said to be skew-symmetric: in this case, since [UNK] = [UNK], the principal diagonal has zero elements.
A square matrix having zeros everywhere except in the principal diagonal is called a diagonal matrix and is clearly symmetric.
The unit matrix I is a diagonal matrix of unit elements; a matrix having all its elements zero is said to be null and is written 0.
It is possible to express any square matrix as the sum of a symmetric and a skew-symmetric matrix; this is shown by the identity [UNK].
The first term is unaltered by transposition; the second changes sign.

### 1.3 REVERSAL OF ORDER ON TRANSPOSITION

If we have a matrix product A = BC, where B is of order (m × r) and C of order (r × n), then A is of order (m × n).
If [UNK], B and C are conformable only in that order.
The typical product element is [UNK].
Transpose B and C; Then [UNK] are of orders (r × m), (n × r) respectively, and are therefore conformable only in the order [UNK].
Moreover [UNK], or [UNK].
Hence transposition of a matrix product requires reversal of the order of the matrices.
By an obvious extension, if A = BCD, then [UNK], and so on.
In view of the formulae (1) and (2) it is clear that these results hold whether or not B, C are conformable both in the order BC and in the order CB, including the case where both are square.

For the unit and null matrices, (1) implies [UNK].

### 1.4. PARTITIONING OF MATRICES

Any matrix may be partitioned, by drawing dotted lines between adjacent columns and adjacent rows, into submatrices.
We do this, notionally, in any matrix multiplication: if we are performing the operation BC = A then we isolate a row of B and a column of C - respectively (1 × n) and (n × 1) submatrices - to produce an element - i.e. a (1 × 1) submatrix of A. Similarly, we could, for example, isolate the first three rows of B and the first four columns of C and multiply these submatrices, of order (3 × n) and (n × 4), to give a (3 × 4) submatrix in the top left corner of A. Again, since [UNK] it makes no different if we divide the range, s, of summation into subranges; each subrange can be summed, and these sums added to give the total.
This is equivalent to vertical partitioning in B with conformable partitioning in C. An example will make this clear.
The product BC = A could be [UNK], where B is (4 × 5), C is (5 × 6) and A is (4 × 6).
Here B has been partitioned between the second and third rows to give, at the top, a (2 × 5) submatrix (ignore the vertical partition for the moment); C between the fourth and fifth columns to give, on the left, a (5 × 4) submatrix.
Multiplied together, these give the (2 × 4) submatrix at the top left in A. The vertical partition in B, after the third column, and the corresponding partition in C, which must be after the third row, merely divide each summation into two parts.
Symbolically, we may write the operation as [UNK], where the elements [UNK] etc are now the above submatrices.
It is important to note the conformability; thus [UNK] is (2 × 2) × (2 × 4) = (2 × 4) also; and [UNK] is also (2 × 4).
It is evident that, though partitioning is largely arbitrary, conformability both in multiplication and in addition is essential.

Partitioning is often of great use, both in analytical manipulation of matrices and in numerical cases, especially when submatrices can be chosen having simple forms, such as a unit or a null submatrix.

### 1.5 SINGULAR MATRICES, DEGENERACY AND RANK

In a square matrix A of order n the array of elements has a determinant [UNK] which is in general nonzero: this implies that the columns (and the rows) are linearly independent, so that there is no nonzero column vector x such that Ax vanishes.
If, however, a vector x does exist for which Ax = 0, this clearly means that any column of A can be expressed as a linear sum of the remaining columns; by the rules for evaluation of determinants this requires [UNK] to be zero.
If two different vectors x exist for which Ax = 0, then not only is zero, but also all the minor determinants of order (n - 1) vanish.

When [UNK], the matrix A is said to be singular.
If only one vector x exists for which Ax = 0, A is said to be simply degenerate, or to have simple degeneracy; if more than one such vector x exists, A has multiple degeneracy.
Complementary to the definition of degeneracy is that of rank: for a square matrix, the sum of the degeneracy and rank is the order of the matrix; thus [UNK] The rank is in fact the order of the largest nonvanishing minor of [UNK], so that rank 0 implies a null matrix.
We shall be much concerned in this text with matrices which are simply degenerate (degeneracy 1) and with matrices in which all columns (and all rows) are proportional to each other; in the latter case all second-order minors vanish, so that the rank is 1.

In general, for a rectangular matrix, the rank is the number of linearly independent rows (and columns).

### 1.6 FACTORISATION OF MATRICES

All matrices can be factorised, usually in a variety of ways.
In the simplest (trivial) case we may write A = AI = IA where I is the conformable unit matrix.
Even I itself can be factorised in a variety of ways; as one example, if J is the square matrix which has units in its secondary diagonal and zeros elsewhere, which we shall call the reversing matrix, then [UNK]; e.g. for order 3 [UNK] so that J is a double factor of I. The ability to factorise a matrix appropriately can often be of great assistance in solving practical problems.

Singular matrices can be factorised as the product of two rectangular matrices - again, in more ways than one - the orders of which are determined by the rank of the matrix.
This may be illustrated by a simple numerical example.
Let [UNK] Inspection shows the third column to be the sum of the first two.
Hence if we partition the matrix appropriately, [UNK] where the submatrix products are written separately.
If now we postmultiply the (3 × 2) submatrix of A by I, we can add the last result to it to recover A as the matrix product [UNK] Finally, a matrix of rank 1 can be expressed as the product of a column and a row in that order - for such a matrix has effectively only one independent column, all the other columns being proportional to it; similarly for the rows.
For example [UNK] In general, any singular matrix of order n and rank r is expressible in an infinite number of ways as the product of two matrices of order (n × r) and (r × n), since r is the number of independent columns (and rows).

### 1.7 ADJUGATE AND RECIPROCAL MATRICES

If [UNK] is a square matrix of order n, and if, in the determinant [UNK], the element [UNK] has the cofactor [UNK] (that is, the value of the determinant obtained from [UNK] by deleting the ith row and jth column, leaving a minor of order (n - 1) which is then multiplied by [UNK], then by the rules for evaluation of determinants [UNK] while [UNK] since the summation in the latter result gives the value of a determinant having two equal rows.
It follows that if the cofactors [UNK] are arranged as a matrix [UNK] of order n, then [UNK] where, to conform with matrix multiplication rules, we must use the transpose of [UNK] to postmultiply A. If instead of a row summation as in (1) we use column summation, we find also [UNK] so that A and [UNK] are permutable.
The matrix [UNK] is called the adjugate of A. If A is singular, so that [UNK] vanishes, then [UNK] In this case, if A is simply degenerate, [UNK] is of rank 1; but if A is multiply degenerate, so that all the cofactors of Aij vanish for all i, j, then [UNK] is null.

These results are examples of Sylvester's law of degeneracy (see Theorem XII of 1.22), viz. the degeneracy of the product of two matrices is at least as great as the degeneracy of either factor, and at most as great as the sum of the degeneracies of the factors.

When [UNK], we may divide [UNK] by [UNK], calling the result R. then AR = I, and R can be described as the reciprocal or the inverse of A. We have already seen that it permutes with A; however, this is readily proved alternatively.
Let [UNK] from the latter, postmultiplying by R1, we have R2AR = R1, and using the former, R2 = R1.
Moreover, the reciprocal is unique; for if AR1 = I and AR2 = I, then A (R1 - R2) = 0, and on premultiplication by R1 we have R1 = R2.

In conformity with usual algebraic notation, the reciprocal of A is written [UNK] so that a separate symbol is unnecessary.
Thus [UNK] expresses the essential property of the reciprocal of A.

Just as with transposition, if a matrix product is inverted the order of the factors must be reversed.
Let A = BCD, where the matrices are all square and non-singular.
By premultiplication or postmultiplication as required, we have successively [UNK]

### 1.8 POWERS OF MATRICES, POLYNOMIALS AND SERIES

We have just established the existence of a negative power of a square non-singular matrix.
In general, any square matrix can be raised to any positive integral power by continued multiplication, in any order, by itself.
Any such powers are evidently permutable; for example [UNK] Similarly, any power of a matrix may itself be raised to a power; for example [UNK] while if A is non-singular [UNK] Evidently, the index laws of ordinary algebra apply.
In particular, [UNK] where A is non-singular; in fact [UNK] applies for all square matrices.

Just as we can have polynomials involving powers of a scalar quantity{gl}, e.g. [UNK] so we can have polynomials of a square matrix A: [UNK] where the [UNK] are scalar multipliers.
Polynomials of matrices are of great importance in a variety of ways.
For example, suppose we can find a set of multipliers pi such that P (A) vanishes.
Then, if [UNK] exists, we may premultiply or postmultiply P (A) by [UNK] to obtain [UNK] as a convenient formula for computing [UNK].

We can also define matrix series; for example the parallel series [UNK] exp A converges in exactly the same way as exp{gl}.
In parallel with the scalar series, exp (-A) is the reciprocal of exp A. If, as in (2) and (3), we have a polynomial or series in a scalar quantity{gl} and the corresponding function in the square matrix A, we may multiply the scalar function by I to obtain the two matrix functions [UNK] Subtraction term by term then gives [UNK] where Q is a function we need not evaluate here.
The matrix [UNK] is of very great importance, not only in studies of the intrinsic properties of A, but also in dynamical and other applications it is called the characteristic matrix of A.

### 1.9 SPECIAL TYPES OF MATRIX

We have already defined symmetric, skew-symmetric, diagonal, unit and null matrices.
We now summarise and extend these definitions.
(1) Symmetric matrix - characterised by A = AT.
(2) Skew-symmetric matrix - characterised by A = - AT.
(3) Diagonal matrix - characterised by [UNK].
We now establish an important property of diagonal matrices.
Let C be any square matrix and D a conformable diagonal matrix with diagonal elements [UNK].
Then postmultiplication of C by D multiplies the columns of C in order by [UNK], etc., while premultiplication of C by D multiplies the rows of C in order by [UNK], etc.
Thus, the typical element of CD is [UNK] while that of DC is [UNK].
It follows that if C and D permute, so that DC = CD, then [UNK] if [UNK].
For a diagonal matrix D having all its diagonal elements different, it follows that C must then also be diagonal.
If D has some equal diagonal elements, then C can possess nonzero off-diagonal elements in a "diagonal submatrix" corresponding to the equal elements of D.

For example, if [UNK] which we write as D = Diag (1,2,3), and [UNK] then if C and D are to permute we must have [UNK] so that d = e = f = g = h = k = 0, leaving C = Diag (a, b, c).
However, if D = Diag (1,2,3) we have that [UNK] so that e = g = h = k = 0 leaving [UNK] which we may write as Block Diag [UNK] where [UNK] Finally, we note that if [UNK] for all i, then [UNK].
This follows from the identity [UNK].
(4) Unit matrix - this is the diagonal matrix with units in the diagonal positions; it is written I. (5) Scalar matrix - this is the diagonal matrix with the same scalar quantity, say [UNK], in the diagonal positions.
Evidently such a matrix may be written [UNK]; multiplication by a scalar matrix therefore implies multiplication by a scalar quantity.
(6) Reversing matrix - this is the square matrix having units in its secondary diagonal and zeros elsewhere; it is written J. Postmultiplication of any matrix C by the conformable J matrix reverses the order of the columns of C while premultiplication by J reverses the order of the rows.
(7) Null matrix - this has zero elements throughout.
(8) Triangular matrices - these are of two types: lower triangular, L, and upper triangular, U. L is characterised by a typical element having the property [UNK] while U is characterised by [UNK].
Thus, for example [UNK] are, respectively, lower and upper triangular matrices.
An obvious and useful property of triangular matrices is that their determinants are simply the products of their diagonal terms.
Thus, in the above example, [UNK] Another useful property of triangular matrices is the ease with which their reciprocals may be calculated.
For example, if R = (Rij) is the reciprocal of a lower triangular matrix L then [UNK] where a, b, c,... must be nonzero; otherwise [UNK] and R does not exist.
The first row of the product gives [UNK] and in view of this, the second row, excluding its first element, gives [UNK] and so on.
Accordingly, R is also lower triangular, and its diagonal elements are [UNK], as is otherwise obvious from consideration of the cofactors of a, b, c,... in L. Hence a computer program to find R needs to calculate only the n (n - 2) /2 elements below the diagonal; and these are found progressively.
For example [UNK] gives, from the first column, [UNK] and from the second column, [UNK] Transposition of the above shows that the reciprocal of an upper triangular matrix U is itself upper triangular, and that its diagonal elements are the reciprocals of those of U.

(9) Persymmetric matrix - this is a square matrix in which the elements in any line parallel to the secondary diagonal are equal.
Thus, if A is persymmetric, it is characterised by the typical element [UNK] and hence has, in general, 2n - 1 independent elements.
For example, the matrix [UNK] is persymmetric. (10) Centrosymmetric and centroskew matrices - a matrix which is symmetric about the centre point of its array is said to be centrosymmetric; thus, if A is centrosymmetric, of order n, it is characterised by [UNK] More simply, if J is the reversing matrix, a centrosymmetric matrix has the property A = JAJ A centroskew matrix is characterised by the equation A = JAJ.
For example, the matrices [UNK] are centrosymmetric, while the matrices [UNK] are centroskew.
Centrosymmetric matrices and centroskew vectors arise in the study of the dynamics of mechanical systems having physical symmetry (e.g. a suspension bridge).

(11) Orthogonal matrices - a square, non-singular matrix A having the property [UNK] is said to be orthogonal.
Orthogonal matrices are of very great importance in dynamics.

For example, the matrix [UNK] is orthogonal, since [UNK] It should be noted that the determinant of the above orthogonal matrix is unity: in general an orthogonal matrix will have [UNK] as its determinant since [UNK] (12) Hermitian and skew-Hermitian matrices - if a matrix, A, has complex elements, it can clearly be written in the form [UNK] where B and C are real matrices and [UNK] is the conjugate of A. If B is symmetric and C is skew-symmetric, A is said to be Hermitian.
Evidently in this case [UNK] If B is skew-symmetric and C is symmetric, A is said to be skew-Hermitian.
Evidently in this case [UNK] For example, the matrix [UNK] is Hermitian, while the matrix [UNK] is skew-Hermitian.

It should be noted that if A is Hermitian, then iA is a skew-Hermitian. (13) The isolating vector ei - this vector is the ith column of the unit matrix; it has a unit in the ith element and zeros elsewhere.
The operation [UNK] isolates the ith row of A, while Aej isolates the jth column.
The combined operation [UNK] gives the isolated element of [UNK] (14) The summing vector [UNK] - this is the vector of which all elements are units.
Evidently [UNK] gives a row which is the sum of all the rows of A and A{gs} sums all the columns of A. Its principal use is in the checking of numerical operations.

The above list is by no means exhaustive, but it covers most of the matrix types which arise in the present text.

### 1.10 VARIABLE MATRICES, LINEAR SUBSTITUTIONS AND ALGEBRAIC EQUATIONS

So far, we have discussed the properties of matrices, and the algebra of matrices, in general terms, and without reference to the nature of the elements: where illustrations have been given we have used arithmetical numbers for elements.
But the elements can of course be variables.
They may, for example, all be functions of time, so that we must write A = A (t); they may be functions of a parameter, typified by [UNK] when the elements are rational integral functions of{gl}, the matrix is called a lambda-matrix; or the elements may themselves (especially for vectors) be independent variables.
Finally, when sets of differential equations are written in matrix form, some of the matrices will be, in effect, operators.
We now proceed to examine some simple cases.

Suppose first that we have a set of variables [UNK] related to a second set [UNK] by an equation of the type y = Ax; such a relation might, for example, connect the coordinates, referred to two different sets of axes, of a point moving in n-space.
Such a relation is called liner substitution.
Apart from its intrinsic importance, it is of interest since the subject of matrices evolved from it.
Cayley took a set of equations such as [UNK] and enclosed each side in brackets, so that two equal columns could be connected by a single equality sign.
He then extracted the vector x and wrote it vertically as a parallel to y, so requiring the row-by-column rule for multiplication.

A second substitution of the same kind, such as z = By.
implies z = By = BAx, so that BA is the matrix converting x into z.

If the values of x are unknown, but y is given (say y = b) then we have a set of linear algebraic equations for x: Ax = b, of which the formal solution is [UNK]: however, various well known methods exist for finding x without computing [UNK] (see 2.5).

As a very simple example of a linear substitution, consider the coordinates of a point P relative to two sets of axes [UNK] mutually inclined at an angle [UNK] Evidently [UNK] elimination of r, [UNK] gives [UNK] and it should be noted that in this case the matrix of transformation is orthogonal.

The formal solution [UNK] (3) assumes that A is non-singular.
Suppose, however, that A has degeneracy s.
Then s of the rows implicit in (3) may be compounded from the remaining n - s rows, and so provide no extra information.
These s rows, including the appropriate elements of b, may thus be discarded.
We are left with n - s rows which may be written in partitioned matrix form as [UNK] where A1 is a non-singular submatrix of A of order (n - s) (some reordering of the elements of x may be necessary to obtain the non-singular minor), [UNK] is of the order [UNK] and c is the reduced vector b; x has been partitioned conformably into n - s elements (y) and s elements (z).
We may write this equation as [UNK] Equation (5) is known as a parametric solution: since we have only n - s independent relations we can determine only n - s unknowns (y) in terms of the remaining s quantities (z), which may be regarded as arbitrary parameters in the problem.

### 1.11 BILINEAR AND QUADRATIC FORMS

Scalar functions often arise which are linear and homogeneous in two sets of variables x1,..., xn and y1,..., ym.
By inspection, it is evident that such a function may be written as [UNK] when x, y are written as columns.
Here A, of order (m × n) is called the matrix of the form.
Suppose we wish to express f in terms of new variables [UNK], where [UNK] then [UNK] so that [UNK] is the matrix of the new form.
We say hat A and [UNK] are connected by an equivalent transformation.

If the elements of x, y are independent variables, we may differentiate with respect to them.
For example, from (1) above, [UNK] is the first element in the column Ax, [UNK] the second, etc., so that [UNK] In this text, we shall be more concerned with quadratic forms, obtained from bilinear forms such as [UNK] when y = x, so that [UNK] where A is now necessarily square.
Moreover, although in the formulation of A the elements Aij and Aji may not be equal, we may note that (see 1.2) [UNK] and on transposition it follows that [UNK] so that A may be replaced by its symmetric equivalent [UNK]; we now assume that A is symmetric.
Then if we form [UNK] we have [UNK] since transposition of the second term repeats the first.
Thus, since [UNK] If we express a quadratic form [UNK] in terms of another set of variables y given by the linear substitution x = By, then [UNK] where [UNK] and we observe that C, like A, is symmetric.
A transformation of type (2), in which A, C need not in general be symmetric, but in which B is square and non-singular, is described as a congruent transformation and is of particular importance in dynamics.

A quadratic form [UNK] and the matrix A within f, are said to be positive definite (pos. def.) if [UNK] for all real, non-null vectors x.
We may construct a table for such definitions (Table 1).
Necessary and sufficient conditions for a quadratic form to be pos. def. are established in Theorem XIII of 1.22.

If a skew-symmetric, transposition shows that [UNK] vanishes.
[UNK]

### 1.12 EQUIVALENT MATRICES AND CANONICAL FORMS

We have just defined the general equivalent transformation, and this leads naturally to the important concept of equivalent matrices.
We approach this by considering the elementary operations which are commonly used in the condensation of determinants.

Let I [UNK] be the unit matrix with its ith and jth rows interchanged.
The new matrix is symmetric, since both its i, jth and j, ith elements are unity; moreover, its determinant is -1, since in moving the jth row to the ith position [UNK] we cross j - i rows; but the original ith row is now the i + 1th and so in taking it to the jth position we cross j - i - 1 rows.
In view of its symmetry [UNK] can equally be obtained by interchange of the ith and jth columns instead of rows.

Let us restrict ourselves to square matrices; then premultiplication of any matrix A by [UNK] has the effect of interchanging the ith and jth rows of A; postmultiplication of A by [UNK] interchanges the ith and jth columns.

Next, let [UNK] be the unit matrix with the addition of an element k in the [UNK] position.
Then premultiplication of A by [UNK] has the effect of adding k times the jth row of A to the ith row; similarly the operation AI (kij) has the effect of adding k times the ith column of A to the jth column.
The determinant of [UNK] is clearly unity.

Finally, let [UNK] be the unit matrix with the element [UNK] substituted for the unit in the i, ith position.
Then I (li) A multiplies the ith row of A by l; A [UNK] multiplies the ith column of A by l.
This operation is evidently an extension of the I [UNK] operation; instead of adding multiples of a different row (or column) to a given row, it adds multiples of the same row; however, it differs in that now the determinant is l.

The reciprocal of I [UNK] is I [UNK] itself, since a double interchange of two rows restores the original matrix; the reciprocal of I [UNK] is also evidently I [UNK] and that of [UNK].
Any product of these various matrices is always non-singular.

Two matrices, A, B are said to be equivalent if one can be derived from the other by any finite number of elementary operations of the types specified above.
Hence, if all the premultiplications and postmultiplications are grouped together to form (non-singular) matrices P and Q respectively, and A, B are equivalent, then B = PAQ and [UNK] Since k, l are arbitrary (except that [UNK]) it follows that there is a infinite number of matrices B equivalent to A. However, there is one matrix which is of especially simple form; it is described as the canonical form of A.

First, let us suppose that A is non-singular.
If A11 = 0 we can bring any non-zero element to the A11 position by the use of I [UNK] we can then reduce this element to unity by the use of I (l), and then reduce all the remaining elements of the first row and the first column to zero using I (k).
We do the same for the submatrix bordered by the first row and column, and so on, so that finally we reach the unit matrix as the canonical form for A. It is to be observed that, since in using elementary operations I (i, j), I (k), I (l) on A we are effectively at each stage multiplying together determinants neither of which vanishes, the reduction of A to I must be possible when A is on-singular.
In passing, we may note that, since PAQ = I, [UNK]

Now suppose A to be singular, of rank r and order n.
This means that all minor determinants of order r + 1 vanish, but at least one minor of order r is not zero.
None of the operations I (i, j), I (k), I (l), in so far as they affect the minors, can make a minor of order r + 1 nonzero, nor make the minor of order r vanish, since they merely condense these minors.
We may therefore use the processes above as for a non-singular matrix; we achieve a series of units in the positions[UNK]; the other elements in the matrix are all zero.
The canonical form of A is thus [UNK] where I is of order r.
If B = PAQ, where P, Q are non-singular but otherwise arbitrary, then the canonical forms for P, Q are the unit matrix.
It follows that P, Q can be constructed from I by elementary operations; accordingly, if any such product, provided only that P, Q are non-singular, A and B are equivalent matrices; and in particular, they will have the same rank.

### 1.13 LAMBDA-MATRICES

We have already defined a lambda-matrix of which the elements are rational integral functions of some parameter [UNK] Such matrices arise in many problems of mechanics.
For example, suppose we have a pair of simultaneous differential equations [UNK] where the coefficients [UNK] are constants.
We can write these as [UNK] where the column matrices are all functions of time.
An alternative symbolic formulation would be [UNK] where D = d/dt and the square matrix is now an operator on x.
Finally, if we are seeking the complementary function of the equations, we write x proportional to exp [UNK] and obtain [UNK] as the equations determining [UNK] and the ratio [UNK] In abbreviated form this can be written [UNK].
The equation determining [UNK] is obtained from the vanishing of the determinant of the lambda-matrix; it is evidently a quartic in [UNK] and each of the four roots will have its own associated vector x.
While it is often convenient to deal with equations such as (2) in the way indicated, it is also often useful to transform them into first-order equations.
This may be done in various ways, but one simple and useful device is to adopt two auxiliary variables: [UNK] and to write the equations in the form [UNK] Then if we now write [UNK] and [UNK] proportional to exp [UNK] and again seek the complementary function, the four equations may be written, with a little rearrangement, [UNK] This equation can clearly be written in partitioned form as [UNK] or [UNK] where [UNK] The quartic determinantal equation obtained from this first-order set of equations may be seen by inspection to be identical with that obtained from the quadratic formulation.

A matrix of the form M + [UNK] is called a matrix pencil (see 2.9, 2.10).

### 1.14 ADJUGATE LAMBDA-MATRICES

If A [UNK] is a lambda-matrix, its elements are rational integral functions of{gl} and so also, therefore, are the cofactors{ga} of the elements of A: hence the adjugate, [UNK] of A is also a lambda-matrix, and [UNK] We shall denote the determinant [UNK] by [UNK].
The reciprocal of A, however, being [UNK] divided by [UNK] is not a lambda-matrix, unless it should happen that [UNK] is independent of [UNK].

### 1.15 EQUIVALENT LAMBDA-MATRICES

If we have an equivalent transformation [UNK] where P, Q may be constructed by any of the elementary operations defined in 2.12, then B and A are equivalent.
It should be noted that the determinants of P, Q must be non-vanishing constants, though [UNK] may appear in them.
This implies that in an operation I (k) we may see I (),; but [UNK] will not appear in I (l) operations, except in a self-cancelling form, e.g. we could use I (l) with [UNK] in the ith place, following with I (l) with [UNK] in the jith place, so that the product of the two steps has unit determinant.
I (i, j) is, of course, independent of [UNK].

Using elementary operations of this kind, we may construct a canonical form of lambda-matrices, which is diagonal, the elements in the diagonal being functions of [UNK].
The canonical form is not unique; the best-known form is that due to Smith (see Ref. (1)).

If C (); is the canonical form, since C{ ([UNK]) = PA () Q; we have [UNK] and since [UNK] are non-vanishing constants, we have that [UNK] and [UNK] differ only by a scalar multiplier.
Hence the roots of [UNK] are identical with those of [UNK].

### 1.16 THE CHARACTERISTIC MATRIX AND ITS EIGENVALUES

Suppose we have a linear substitution Ax = y in which it is required that y be a scalar multiple of x, say x[UNK].
Then x [UNK] - Ax = (I [UNK] - A) x = 0.
Then the square lambda-matrix (I [UNK] - A), which is the characteristic matrix of A (see 1.8), must be singular; i.e. the determinant [UNK] if x is not to vanish.
This important equation is called the characteristic equation.
If A (which is necessarily square) is of order n, then clearly the characteristic equation may be written [UNK] The n roots of this equation, say [UNK] are called eigenvalues.
In what follows, we shall now regard 1[UNK],..., n [UNK] as all different.

An alternative formulation of the characteristic function is evidently [UNK] and it is to be observed that the two formulations imply, inter alia, [UNK] and [UNK] where Theorems II and III of 1.22 have been used.
Let us write [UNK] then from (4), [UNK] so that if we regard 1 [UNK] as typical of all the roots, [UNK] since all the roots differ.
Now by the usual rule for differentiation of determinants, [UNK] is linear and homogeneous in the first minors of{gd} ([UNK]).
Since, typically, [UNK] it follows that not all the first minors of [UNK] vanish, so that it is simply degenerate.
For the same reason [UNK], the adjugate, is not null, and so has unit rank, as shown below.

Since [UNK] vanishes but at least one first minor does not, there must be n - 1 independent columns, the remaining column being expressible uniquely in terms of the independent columns.
This means that there will be a vector x1, called an eigenvector, such that [UNK] and x1 is uniquely determined, apart from an arbitrary scalar multiplier; that is, the ratios of the elements of x1 to each other are uniquely determined.
Similarly, apart from a scalar multiplier, there will be a unique row vector [UNK] such that [UNK] It is readily shown that the adjugate [UNK] is proportional to the unit rank product [UNK].
For suppose [UNK]; then [UNK] Postmultiply this by any column p such that the scalar product [UNK]; then [UNK] Since the vector x1 is unique to a scalar multiplier, we may identify [UNK] with x1 and similarly [UNK] with [UNK].

If we revert to the original problem, the solution of Ax = x[UNK], we now see that there are just n eigenvalues s [UNK] and that correspondingly there are just n vectors xs; i.e. we have n equations [UNK] We can combine them all into the single equation [UNK] or more briefly AX = X [UNK] where X is ow the square matrix made up of the n column vectors xs, and [UNK] is the diagonal matrix of the eigenvalues; and our problem is now to find the matrices X and [UNK] for the given A.

We may not one further point.
Let d be an arbitrary diagonal matrix; then it will permute with the diagonal matrix [UNK] Postmultiply (7) by d; then [UNK] showing that Xd is a solution of (7).
This expresses the fact that the columns of X are each arbitrary to a scalar multiplier, since in Xd, x1 is multiplied by the scalar d1 and so on.

If (7) is premultiplied by A, we have A (AX) = (AX) [UNK] and AX is apparently an alternative solution for X. But since AX = X{gd} it is X postmultiplied by a diagonal matrix, as before, except that here the diagonal matrix is not arbitrary.

The matrix equation [UNK] arises perhaps most commonly in the study of the natural frequencies and modes of vibration of an undamped mechanical system having n degrees of freedom.
The matrix A derives from the mechanical properties (mass and stiffness) of the system; s [UNK] then determines the square of a natural frequency, and xs the corresponding mode of distortion.
However, the amplitude is not determined; xs is arbitrary to a scalar multiplier.
In this sense an arbitrary multiplier ds can be regarded as an amplitude.

Because of its importance in vibration problems, the matrix X, which is the array of the individual eigenvectors xs, is usually spoken of as the modal matrix, even when the problem from which it derives is not a dynamical one.
Similarly{gd} in vibration problems is a diagonal matrix of squares of natural frequencies and thus defines the frequency spectrum of the system; accordingly it is referred to generally as the spectral matrix.

We may readily show that the matrix X is non-singular. for if it is not, let us first suppose it to be simply degenerate.
Then there will be a vector p, unique apart from a scalar factor, such that Xp = 0.
But in that case premultiplication by A gives 0 = AXp = Xp [UNK] so that p [UNK] provides a relation different from p between the columns of X, which is impossible.
Similarly, if X were doubly degenerate we could have only two vectors p satisfying Xp = 0, but each of these would give rise to other different vectors p[UNK].
Hence X is non-singular.

We may accordingly write (7) as [UNK] and A, [UNK] are equivalent matrices.
If [UNK], then B is said to be derived from A by a similar transformation.
This type of transformation is of great importance.
For example, if [UNK] then [UNK] where [UNK] is the diagonal matrix of the squares of the eigenvalues.
Similarly [UNK] and more generally [UNK] where P (A) is any polynomial in the matrix A. We now revert briefly to Equations (2) and (3) in order to define the companion matrix C of [UNK] ([UNK]).
This is [UNK] Condensation of [UNK] shows that [UNK] so that the eigenvalues of A and C are the same.
We shall give an example of the utility of (10) later (2.9).

### 1.17 THE CAYLEY-HAMILTON THEOREM

This important theorem states that any square matrix A satisfies its own characteristic equation.

First, suppose as above that the eigenvalues are all distinct; then in view of (1.16.9) we may write the polynomial [UNK] (A) as [UNK] Now the diagonal matrix [UNK] has for diagonal elements [UNK] all of which vanish; i.e. [UNK] is null.
Hence [UNK] (A) = 0, which is the Cayley-Hamilton theorem.

The equation is true even when the eigenvalues are not all different.
For we know that in general [UNK] where [UNK] is the adjugate of (I [UNK] - A).
Since both [UNK] and{gd} ([UNK]) I are lambda-matrices, we amy write them as polynomials in [UNK] with matrix coefficients; let us write the equation as [UNK] Then on multiplying out and identifying coefficients of [UNK], we have [UNK] Premultiply the first of these relations by [UNK], the second by [UNK], etc. and add: the result is [UNK] (A) = 0.

Equations (1.16.3) and (1.16.4) show that the characteristic equation may be written in the alternative forms [UNK] It follows that the Cayley-Hamilton theorem [UNK] can be written in the alternative form, in which for consistency each factor has been multiplied by -1, [UNK] It will be observed that, with eigenvalues all different, each of these matrices has degeneracy 1, the product of all n factors having degeneracy n: i.e. it is null; this is an illustration of Sylvester's law of degeneracy (Theorem XII of 1.22).

Since [UNK] (A) vanishes, so also do [UNK], etc. it follows that any power n or more of A, or any polynomial degree of n or more in A, can be expressed as a polynomial in A of degree n - 1.
Furthermore, if A is non-singular, [UNK] may be expressed as a polynomial of degree n - 1 in A, and therefore also [UNK] and higher negative powers.

Examples of the utility of this theorem will appear later.

### 1.18 SYLVESTER'S EXPANSION THEOREM

We revert to Equation (1.16.9) and write [UNK], to conform with the notation for the adjugate of X. Then [UNK] Now P (A) is the diagonal matrix of which the diagonal elements are [UNK] in succession.
Once again we here assume the eigenvalues s [UNK] to be all different.
We now write [UNK] so that each square matrix is null except for a unit in the appropriate diagonal position.
In terms of the isolating vector ei this may be written [UNK] and if P (A) is expanded in this way, the first term, which is typical will be [UNK] The square matrices on the right of these equations are all of unit rank; we may write the last as [UNK] where x1 is the first column of X, and [UNK] the first row of [UNK].
We thus establish Sylvester's theorem for the expansion of P (A), viz. [UNK] where [UNK] The unit rank matrices [UNK] which are known as the constituent matrices of A, have interesting and important properties.
Thus: (i) As has been noted earlier, in 1.16 [UNK] is proportional to [UNK], where [UNK] is the adjugate of (I [UNK] - A).
(ii) We defined [UNK] as [UNK], hence [UNK] This equation requires, for all the rows [UNK] and columns [UNK] [UNK] Hence [UNK] since the inner product (scalar) is unit.
Hence in general [UNK] On account of this property, [UNK] is said to be idempotent. (iii) We have also [UNK] since the inner product vanishes.
(iv) If in Sylvester's expansion we put P (A), which is a arbitrary polynomial, equal to I, so that [UNK], then [UNK] As a simple example of the consistency of the theorem, let us write Sylvester's expansion for A as [UNK] Let us square both sides; then [UNK] and on account of the properties above [UNK] in accordance with Sylvester's theorem.

### 1.19 ORTHOGONALITY AND BI-ORTHOGONALITY OF THE MODAL MATRIX

We consider first the eigenvalues (supposed all different) and modal matrix of a symmetric matrix A. then by (1.16.7) AX = X [UNK] and on premultiplication [UNK] Transpose this; then since [UNK] we obtain [UNK] Comparison of (1) and (2) shows that [UNK] so that [UNK] permutes with [UNK], a diagonal matrix with all its diagonal elements different.
Hence (see 1.9) [UNK] must also be diagonal and it then follows that [UNK] is also diagonal.
Now we have seen that we can use Xd in place of X, where d is an arbitrary diagonal matrix; and it therefore follows that [UNK] is also diagonal.
Now the ith diagonal element of this product is [UNK] and we may clearly choose di to make this element unity.
If this is done for all i, and we write Xn for Xd, then [UNK] so that the modal matrix Xn, chosen in this way, is orthogonal and we say that Xn is the normalised for of the modal matrix.

Next consider the more general case when A is not symmetric, but is expressed as the product of two symmetric factors.
Such factorisation is always possible, in a number of ways; for example, since AX = XA then [UNK] so that A has been factorised into two symmetric matrices; however, this particular factorisation presupposes a knowledge of X and [UNK].
Suppose instead that we can write A as [UNK] where B, C are symmetric; then we have [UNK] or BX = CX[UNK].
Dynamical problems frequently arise in this form directly.
Now as before, if we premultiply by [UNK] and transpose, since [UNK] and [UNK] [UNK] so that [UNK] permutes with [UNK] and is thus diagonal, whence it follows that [UNK] is diagonal also.

Clearly we cannot normalise X in this case to make both [UNK] and [UNK] unit matrices; we say therefore that in this case X is bi-orthogonal or has a generalised orthogonal form.
We may pursue the matter a little further, however.
If as previously we write Xd for X, where d is an arbitrary diagonal matrix, then we obtain [UNK] as diagonal matrices.
Now the ith diagonal element of [UNK] [UNK] where the bracketed term is the quadratic form obtained from C with the ith eigenvector xi.
This quadratic form is not, as previously, a sum of squares; but provided it is not zero we could choose di to make the element unity, when we should have (with X for Xd) [UNK] On account of the properties established here, it is usual to say that the modes of a system are orthogonal to each other.

### 1.20 CANONICAL FORMS OBTAINED BY SIMILAR TRANSFORMATION

We consider a matrix A, which for the moment we regard as having distinct eigenvalues.
We have seen (1.12) that by elementary operations we can perform an equivalent transformation C = PAQ and C has a special canonical form, either the unit matrix or containing a diagonal unit submatrix.
Let us now impose the restriction that whenever we perform an elementary postmultiplying operation to make up Q, we premultiply by the inverse operation to make up P, so that [UNK].
In this case, we cannot reduce C to a diagonal matrix of units, since evidently [UNK].
However, a simple and powerful canonical form is obtainable.

The matrix A has the characteristic matrix (I [UNK] - A).
If this is premultiplied by [UNK] and postmultiplied by Q, then [UNK] so that A and [UNK] have the same eigenvalues.
In particular, if we identify Q with the modal matrix X, then [UNK] by (1.16.8).
Hence, as is otherwise obvious from the derivation of (1.16.8), the eigenvalues of A are given directly by [UNK], etc.
In this case, therefore, we may regard [UNK] as the simple canonical form for a matrix having distinct eigenvalues.

Note that if [UNK] and [UNK] then [UNK] so that, if X is the modal matrix of A, QX is the modal matrix of B.

The great majority of mechanical problems give rise to matrices having distinct eigenvalues; however, problems involving equal eigenvalues are by no means unknown.
For example, a rigid body may have some of its motions constrained by springs, but two (or more) unconstrained; it will then have two (or more) equal zero frequencies.

The canonical form obtained by a similar transformation of a matrix having equal eigenvalues, when reduced to its simplest form, has the eigenvalues in the principal diagonal, with equal eigenvalues in groups; elsewhere the matrix is null except that there may be units in the superdiagonal.
Thus, for example, a matrix of order 6 having three equal eigenvalues{ga}, two equal eigenvalues{gb}, and an unrepeated eigenvalue{gg}, would have as its canonical form [UNK] where each x may be zero or unity; it occurs only within the submatrices containing groups of equal eigenvalues.
C is sometimes called the Jordan canonical form and a submatrix such as [UNK] is known as a Jordan block.
If in C a unit occurs at a position x, it cannot be removed by a similar transformation.
This is readily proved as follows.

Suppose we wish to remove the unit from the superdiagonal in the matrix [UNK] by means of a similar transformation; we can write the most general transformation matrix as [UNK] Then [UNK] and if both off-diagonal elements are to vanish, then [UNK] Provided [UNK] we may satisfy (4) and [UNK]: for example, if we choose [UNK].
Then [UNK] However, if [UNK] then the only solution of (4) is c = d = 0 when ad - bc vanishes, so that [UNK] does not exist.
Hence, if a unit exists (it may not) in the superdiagonal element adjacent to two equal eigenvalues, it cannot be removed by a similar transformation.

The reason for the existence or absence of a unit in the superdiagonal is easy to see.
Suppose C in (3) is derived by a similar transformation from a matrix A, to which it is therefore equivalent.
Then if I-A [UNK] is simply degenerate when [UNK] ={ga} so also is I [UNK] - C. There must in consequence be two units in the top two places of the superdiagonal, for without them I [UNK] - C would have three null rows and three null columns, and so be triply degenerate.
With two units present, only the first column and third row are null, so that I [UNK] - C is simply degenerate as required.
Evidently the introduction of a unit reduces the degeneracy of I [UNK] - C by unity.

It is clear from the derivation of the canonical form that it is conventional, but not necessary, to put equal eigenvalues in groups, and to put units in the superdiagonal.
In a practical case, we might find an intermediate form for the matrix C of (3) to be (we shall discuss the meaning of x and y) [UNK] Now suppose [UNK], and therefore [UNK] to be simply degenerate when [UNK] Then [UNK] must also be simply degenerate.
This requires that either x or y is nonzero, the other being zero; only so does the matrix have only one null column and row.
Suppose x is zero, so that the second row and fifth column are null.
Then y must not vanish.
Now, by further operations of type I (i, j) we can bring the two roots into adjacent places in the diagonal, when -y will move to the infradiagonal and a zero, replacing x, will appear in the superdiagonal.
A similar transformation of the submatrix then gives [UNK] so that, so far as [UNK] is concerned, we have arrived at the conventional canonical form.

The conventional form is generally convenient; it is useful to have equal eigenvalues in groups and to the use superdiagonal; but in particular cases it may be well to use a nonzero quantity other than a unit in the superdiagonal.
For example, if the eigenvalues are numerically small, a unit could dominate the spectral matrix; or if they are very large, a unit could be of the order of the errors in the computation.
It would then be better to choose a quantity of the order of magnitude of the repeated eigenvalue, or even the eigenvalue itself, provided this is not zero.

### 1.21 SOME REMARKS ON EQUAL EIGENVALUES

We have already remarked that the case of equal or confluent eigenvalues is not common in practical dynamical problems; however, when it occurs, it can cause difficulties.
We shall not attempt to deal with the full problem of multiple equal eigenvalues; it will be sufficient in general to consider the case of two equal roots 1 [UNK] = 2 [UNK] as typical.
Extension to more complicated cases is not difficult (a) Extension of the Cayley-Hamilton theorem In 1.17 we showed that a matrix A satisfies its own characteristic equation, i.e. [UNK] irrespective of the nature of the eigenvalues.
Now when [UNK], the characteristic matrix (I [UNK] - A) may be simply or doubly degenerate, according to the nature of its canonical form [UNK] If it is simply degenerate (i.e. its canonical form includes a unit in the superdiagonal) then [UNK] (A) = 0 is in fact the vanishing polynomial in A of lowest degree.
But if it is doubly degenerate, there is a reduced characteristic equation [UNK] being one degree lower than [UNK].

Consider the equation [UNK] where [UNK] is the adjugate of ([UNK] if for [UNK] ([UNK] is doubly degenerate [UNK] is null, since all first minors of (I [UNK] - A) vanish.
Accordingly, [UNK] must have the factor ([UNK] - [UNK] in each element, while [UNK] ([UNK]) has two such factors.
If we cancel one factor from both sides, we can write [UNK] and then, as before, we can prove that [UNK].
An alternative expression is evidently [UNK] where the first factor is doubly degenerate; the remainder are simply degenerate, giving as before a total degeneracy n.
But if the first factor is simply degenerate, it must appear twice.

We may illustrate this with a simple numerical case.
Let [UNK] Put [UNK] = 2 and [UNK] in the characteristic matrix [UNK] then [UNK] since by inspection it is doubly degenerate.
Also [UNK] which is simply degenerate; the sum of the columns vanishes, but first minors do not.
By inspection [UNK] satisfying the reduced characteristic equation.
However, when we put [UNK] [UNK] in the characteristic matrix [UNK], we obtain [UNK] both of which are simply degenerate; it is readily checked that [UNK] which satisfies the full characteristic equation.

If a reduced characteristic equation exists, so that [UNK], then [UNK]... also vanish; and, as in 1.1, we may now express powers of A or polynomials in A as polynomials in A of degree one less than that of [UNK].
(b) Nature of modal matrix We now turn to the confluent form of Equation (1.16.7), viz. AX = XA, and we shall deal with this by using the example of the numerical matrices A and B above.
By inspection of (3) we can see that a column vector xi postmultiplying (2I - A) to give a null result must be such that [UNK] vanishes; two obvious vectors achieving this are{1,2,4) and{1,0, - 1}.
Also if (I - A) is postmultiplied by{1,1,1} it vanishes.
Hence we may write (8) as [UNK] so that, in this case (two equal roots and double degeneracy of the characteristic matrix), the form of (8) is unaltered.
However, it should be noted that, while the first two columns of X are arbitrary to a scalar multiplier, they are also obviously arbitrary to any linear combination; i.e. we may postmultiply the equation by a matrix [UNK] in which [UNK] and [UNK] are arbitrary except that D must be non-singular.
The leading second-order submatrix of D corresponds to the scalar submatrix in A and therefore permutes with it, so that as before [UNK] and XD is a solution of (8).

Now consider the matrix B, which yields two equal eigenvalues but simple degeneracy.
Since 2I - B and I - B are both simply degenerate we can find only one vector for each to satisfy [UNK]; they are respectively (see (6)) {1,2,4} and{1.1.1}.
No other vector (apart from scalar multiplies) satisfies the equation.
It follows that we cannot make up a square matrix X of eigenvectors to satisfy (8); for this reason the matrix B is said to be defective.
However, we may note that{1.2.4} and{1.1.1} are the first and third columns of the modal matrix X appropriate to A. If we try this X for B we find that we obtain L or [UNK] where [UNK] is now the diagonal matrix of the eigenvalues with the addition of a unit in the top superdiagonal place.
Evidently A is the canonical form of A, and [UNK] that of the defective matrix B. In this latter case, a postmultiplying non-singular matrix analogous to (9) which will permute with [UNK] is [UNK] where [UNK] and [UNK] are otherwise arbitrary.
Then [UNK] satisfies (10).

We may note that, for both the matrices A and B, [UNK] we may therefore construct the canonical forms directly from [UNK] We now revert to (10); if for convenience we denote the columns of X by [UNK] respectively, then as we have said above, only x1 and x3 are eigenvectors; they make [UNK] and [UNK] vanish, and are each unique to a scalar multiplier.
We now examine the origins of [UNK], which in relation to B we call an auxiliary vector.
In (10) we find [UNK] Premultiplication of this by (2I - B) yields [UNK] Accordingly, postmultiplication by the auxiliary vector [UNK] annihilates [UNK], in fact, since [UNK] is doubly degenerate, there will be two linearly independent postmultiplying vectors which annihilate it, separately or in linear combinations.
We can, and indeed must, choose x1 as one of these, for sine [UNK] vanishes, so evidently does [UNK]; and then [UNK] is the other.

We might have anticipated this result from Equations (5) and (7).
I (5) the doubly degenerate matrix (2I -A) is annihilated by two linearly independent eigenvectors and the simply degenerate (I - A) by the third.
In (7), [UNK] is doubly degenerate and so corresponds with (2I - A); however, in this case one eigenvector and one auxiliary vector emerge.

It is now clear that, to make up X, we require (i) an eigenvector x1 satisfying [UNK] (ii) an auxiliary vector [UNK] satisfying [UNK] (iii) an eigenvector x3 satisfying [UNK] In the numerical example (10), [UNK] and postmultiplication by x1 ={1,2,4} makes both vanish; postmultiplication by [UNK] ={1,0, -1} annihilates the second but not the first; the product yields - x1.

There is one further point of importance: [UNK] is not unique, but contains an arbitrary element.
As we have seen, [UNK] is satisfied by two linearly independent vectors (in our example, {1,2,4} and{1,0, -1} and therefore by any linear combinations of them.
One is chosen to be x1, satisfying (2I - B) x = 0; the other [UNK], is another arbitrary combination.
However, it must satisfy [UNK] so that if x1 is multiplied by a scalar d1 so also is [UNK]; which is why (11) contains equal elements [UNK].
But the equation is also satisfied by [UNK] so that in our example [UNK] with [UNK] arbitrary.
This result is evidently generally true.

As a dynamical example, perhaps the commonest practical problem leading to a double eigenvalue with simple degeneracy is that of critical damping.
For example, the equation of motion of a mass constrained by a spring and dashpot is, in the well-known standard form, [UNK] Here we shall consider [UNK] as fixed and [UNK] as a variable (in practice, a variable spring stiffness) and for convenience we shall write [UNK] for [UNK]; this [UNK] is a variable parameter, which may be positive or negative: in the latter case, the motion is a damped oscillation.

If x is proportional to expt[UNK], we have to satisfy [UNK] and for [UNK] we therefore have two different roots: either two real roots or a conjugate complex pair.
However, for [UNK] (the critical damping case) the two roots coalesce into a repeated (real) root, [UNK] = [UNK]

If we write v for x, the equation of motion may be written as the first-order pair [UNK] or, when{x, v} is proportional to expt[UNK], [UNK] This requires [UNK] Giving of course the eigenvalues [UNK] for each of which [UNK] is simply degenerate.
In the critical case, when{ge} vanishes, we have two equal eigenvalues -{gm}, but I [UNK] - B (0) is still simply degenerate; thus [UNK] and so the column [UNK] makes this vanish.
Squaring it, we obtain a null matrix, so that [UNK] is satisfied by two linearly independent arbitrary columns.
As we have seen, one of them must be [UNK] the most general form of the other is [UNK].
Choosing [UNK] we find Equation (13) to be, in this case, [UNK] with the spectral matrix (on the right) in the standard canonical form for a defective matrix.

There is a further interpretation of this which is of great importance.
With [UNK] general, we may write the eigenvectors corresponding to [UNK], [UNK] respectively; hence the operation [UNK] and [UNK] is converted to the standard canonical form for matrices with distinct eigenvalues.
However, this similar transformation fails when [UNK]: the two columns of X (O) become identical, so that its reciprocal becomes infinite.

However, if we postmultiply [UNK] by a matrix which in effect sums and differences the columns, thus: [UNK] then a similar transformation [UNK] yields [UNK] as follows: [UNK] i.e. a quasi-canonical form: it is to be remembered that the standard canonical forms are conventional, but not unique.
The two matrices [UNK] and [UNK] are both equivalent to [UNK] and to each other; they are each derived from [UNK] by a similar transformation.
But the first is possible only for [UNK], while the second becomes a canonical form appropriate to a defective matrix only for [UNK]

This example shows that the auxiliary vector{0,1} is in effect the differential with respect to [UNK] of the two confluent vectors [UNK] and [UNK].

#### (c) Extension of Sylvester's expansion

We come finally to the confluent form of Sylvester's expansion for any polynomial, and again we use the matrices A and B as exemplifying the general case; however, for greater generality we shall write the repeated roots as [UNK] the unrepeated root as [UNK] and shall replace the unit in the superdiagonal of [UNK] by r.
Them, treating A first, we have as in 1.18 [UNK] The expansion can then proceed as before, and we obtain [UNK] where [UNK] are unit rank matrices.

The case of B, involving a double root with simple degeneracy, is a little more complicated.
In succession, we find [UNK] Now P ([UNK] is the polynomial in [UNK] [UNK] which on differentiation gives [UNK] We can evidently construct corresponding polynomials in the matrices B and [UNK], and in view of (13) they will be connected by [UNK] in (17), the first column of X is proportion to [UNK].
Using (15), we may expand [UNK] in the form [UNK] Accordingly, if we now proceed (exactly as in 1.18) to premultiply (17) by X and postmultiply by [UNK] ([UNK]; the first row of [UNK] is proportional to r) we obtain [UNK] Comparison with (14) shows that we have now added a new term [UNK], which derives from the element r in the superdiagonal of the canonical form.
This also is a square matrix of unit rank, and z12 evidently has the properties [UNK] In fact, the above equations, and the properties of the matrices [UNK] discussed in 1.18, are all contained in the general result [UNK] on evaluation of the inner products.

Equation (18) is the confluent form of Sylvester's expansion for the case of two equal eigenvalues which give only simple degeneracy to the characteristic matrix.
As an example of its consistency, if we put P (B) = I, giving [UNK] then as before [UNK] while if P (B) = B, then [UNK] If we multiply (21) and (22) the result repeats (22) in view of the properties of zii and (19) above; squaring (22) yields [UNK] in accordance with (18).

As an indication of Sylvester's expansion for more complicated cases, suppose we have [UNK] Then if we evaluate [UNK], it is readily found that the expansion in this case will be [UNK] Further extensions follow this pattern.

##### Example 1

We use B as defined in (2) together with [UNK] where, in order to obtain r = 2 in [UNK], the first column of X in (10) has been halved, and the first row of YT in (12) has been doubled.
These matrices satisfy [UNK].

Suppose we wish to calculate B-1.
Then in (18) we put [UNK] with [UNK] Then [UNK] The reader is invited to check that this is correct.

### 1.22 SOME MISCELLANEOUS THEOREMS

We append here some useful theorems and definitions: Theorem 1 - The reciprocal of the transpose of a matrix A is equal to the transpose of the reciprocal of A. For [UNK]; transpose to get [UNK].
Postmultiply by the reciprocal of AT, and [UNK].
We shall write [UNK].
Corollary If A is symmetric, so also is A-1.
Example 1 If [UNK] Also [UNK] Theorem II - The trace of a matrix, which is the sum of the elements in the principal diagonal, equals the sum of the eigenvalues.

If the determinant [UNK] of order n is expanded in the usual way, the first product is [UNK] times its cofactor, which is similar to [UNK] but of order - 1.
All other products are evidently of degree n - 2 in [UNK] at most.
By progressive expansion of the diagonal minors it therefore appears that the two leading terms in the full expansion are [UNK] Now if we write the determinant as [UNK] the leading terms are [UNK] Hence [UNK] Example II Let [UNK] and on expansion [UNK] Then [UNK] Theorem III - The product of the eigenvalues of A is [UNK].
In [UNK] put [UNK].
Then [UNK].
Hence if an eigenvalue of A is zero, A is singular; and conversely if [UNK], then one or more eigenvalues are zero.
Example III If A is the matrix in Example II, then [UNK] Theorem IV - If a scalar [UNK] is added to each principal diagonal element of A, the eigenvalues of A are each increased by [UNK].
This is immediately obvious from the identity [UNK] The sum of the eigenvalues, and tr A, are each increased by [UNK] Example IV Let us add -3 to each diagonal element of the matrix A in Examples II and III; we obtain [UNK] and [UNK].
Hence, compared with Example I, the eigenvalues have each been reduced by [UNK] and [UNK].
Theorem V - Any matrix can be expressed as the product of two symmetric matrices.

The case in which A is non-defective has already been treated in 1.19, so that here we must consider the defective case.
We write [UNK] Suppose we have a Jordan block or blocks such as [UNK] in [UNK].
If this is premultiplied and postmultiplied by the reversing matrix Js, then [UNK].
Now let K be the unit matrix, except that wherever a block [UNK] occurs in [UNK], the corresponding Is is replaced by Js in K. Then [UNK] We now revert to (1), postmultiply by [UNK] and use (2): [UNK] on use of the transpose of (1).
Now (3) shows that AXKXT equals its own transpose and so is symmetric, says S1.
Also XKXT is symmetric, says S2.
Thus [UNK] is expressible as the product of two symmetric matrices.
If we put [UNK] and hence K = I, the two factors in (4) reduce to those given in 1.19.

This establishes that such factorisation is always possible.
A general numerical procedure, not involving X, [UNK], is given later in 2.10.3.
Example V (a) Non-defective matrix - let A be as defined in (1.21.1).
Then [UNK] assumes the numerical values [UNK] In this case [UNK] and [UNK] The reader may check that [UNK].
(b) Defective matrix - we use B as defined in (1.21.2).
Then [UNK] takes the numerical values [UNK] X being the same as in case (a).
Also if [UNK] then [UNK] while [UNK] and again the reader may check that the product of the symmetric matrices [UNK].
Theorem VI - AT can be obtained from A by a similar transformation.
This has been proved incidentally above; (3) may be written [UNK] Example VI We use the matrix B of Example V (b) above.
Then [UNK] Theorem VII - If A is any matrix of order (n × p) and B any matrix of order (p × n) where [UNK], then the eigenvalues of AB are those of BA plus n - p zeros.

Consider the matrix product [UNK] where the matrices are square and of order N = n + p, appropriately partitioned.
If we take determinants and note that [UNK] we have [UNK] In reverse order, we find [UNK] so that [UNK] and hence

It follows that the zeros of [UNK] also make [UNK] vanish and that [UNK] must also have n - p roots [UNK] = 0.
This last is otherwise obvious; A has only p columns, so that AB, of order (n × n), has at most p linearly independent columns; i.e. it is of rank p at most, and so must have at least n - p zero eigenvalues.

If A and B are square, and one at least (say B) is non-singular, this result may be obtained very simply from the identity.
[UNK]

#### Corollary

If A, B an C are matrices of order n × p, p × q and q × n respectively, the nonzero eigenvalues of ABC (n × n), CAB (q × q) and BCA (p × p) are identical.

(N. B. if n = p = q, this corollary applies only to the products ABC, CAB and BCA and not to BAC, etc.; i.e cyclic permutation only is permitted.)

#### Example VII

(a) [UNK] Here, [UNK] The reader will verify that AB is of rank 1 with spectral and modal matrices [UNK] while BA is of rank 2 with [UNK] The eigenvalues of AB and BA are thus 0, 0 and -7.
It will be noted that trBA = tr AB = -7 and that Theorem VII applies regardless of the fact that rank [UNK] rank BA. (b) [UNK] Here [UNK] each product being of unit rank.
The reader will verify that the spectral and modal matrices are (i) For ABC: [UNK] (ii) For CAB: [UNK] (iii) For BCA: [UNK] The non-zero eigenvalue, 47, is common to all products, as indicated by Theorem VII.
Theorem VIII - If, in the eigenvalue problem [UNK] the matrices B, C are both real and symmetric, and if further C is pos. def. and B non-neg. def., then all eigenvalues are real, finite and non-negative.

In (8) write [UNK]; multiply out and separate real and imaginary parts.
Two real equations result: [UNK] If these equations are respectively premultiplied by [UNK] and subtracted, then since B, C are symmetric, the left-hand side vanishes, and [UNK] Since x is not null and C is pos. def., the bracketed term is positive; hence{go}= 0 and [UNK] is real.
Equation (8) is now [UNK] and since the bracketed term is real, so also is x.
Finally, [UNK] and with the given conditions [UNK] is therefore real, finite, and non-negative.
I B, C are both pos. def., [UNK] is real, finite, an positive.

#### Corollaries

(i) The eigenvalues of a real, symmetric matrix A are all real and finite, and the eigenvectors are real.
This follows from the theorem by putting B = A, C = I. (ii) The eigenvalues of a Hermitian matrix are all real.
The relevant equation may be written [UNK] which yields the two real equations [UNK] Premultiply the first by qT and the second by pT.
Since B is symmetric, the left-hand sides are equal, an since C is skew-symmetric, its quadratic form vanishes (by transposition [UNK]).
Subtraction of the two equations therefore yields [UNK] (iii) The non-zero eigenvalues of a skew-Hermitian matrix are all imaginary.
Here we premultiply the first of Equations (10) by [UNK] and the second by [UNK].
Now, since B is skew-symmetric it disappears from the equations, while C is now symmetric, so that the right-hand sides are equal and opposite.
Addition then gives [UNK] Theorem IX - If a matrix A and its inverse A-1 are known, then if a unit rank matrix is added to A, the inverse of the new matrix may be written down.

Let us write the unit rank matrix as [UNK] Then [UNK] Hence [UNK] To prove this, we merely multiply out the product [UNK] which gives I. Equation (11) is an example of the "modification formula" generally ascribed to Householder (3).
(Householder's formula relates to the more general case where a matrix of rank [UNK] is added to A. The additional, modifying, matrix may be written CRT with C of order (n × p) and RT of order (p × n).
Then with [UNK] an analogy with Equation (11).
The reader might verify this useful formula in which it is evident that the inverse of a matrix of order n is obtained in terms of that of a matrix of smaller order).
Examples of the use of this theorem are given in 2.2.3.
Theorem X - If A is real and symmetric, it cannot be defective.
For suppose it is; let us write its spectral matrix [UNK] with a Jordan block [UNK] as the leading submatrix of order 2 (it can be part of a larger block); x1 is the corresponding eigenvector and [UNK] the auxiliary vector.
Then from the first two columns of [UNK] we have [UNK] on transposition, since A is symmetric; and [UNK] Premultiply (13) by [UNK]; then in view of (12) [UNK] In corollary (i) of Theorem VII we have shown that if A is real and symmetric, x is real; hence in (14) [UNK] and p vanishes; similarly for all other superdiagonal elements.
Hence A is not defective.

#### Corollaries

(i) If A is not symmetric, but can be written as the product [UNK], where B, C are real ad symmetric, and in addition C is pos. def., then A cannot be defective.

In this case, (12) becomes successively [UNK] and (13) yields [UNK] Hence as before, [UNK] We have proved in Theorem VIII that with these conditions, X is real; hence (15) implies p = 0, and as before, A is not defective.

Provided only that A is real, it is always possible to find real symmetric matrices B, C satisfying CA = B (see 2.10.3).
Accordingly, if A is defective, so that [UNK], (15) requires that [UNK] must vanish.
(ii) A defective matrix cannot be similarly transformed into a real symmetric matrix.

For suppose we have a Jordan block as in the theorem, with [UNK], and we apply the most general transformation; we obtain [UNK] This cannot be real and symmetric: it requires c = d = 0, which violates the condition [UNK].

#### Example X

We now illustrate Equation (15).
(a) No-defective matrix - we choose the matrix defined in (1.21.1), and write it here as A1.
Then with [UNK], one possible numerical expression is [UNK] Here B, C are real and symmetric, and C is pos. def.; A1 has two equal eigenvalues, 2, and two eigenvectors{1,2,4} and{1,0, -1}.
These give [UNK].
With p - 0 these satisfy (15).
(b) Defective matrix - we use the matrix defined in (1.21.2), writing it here as [UNK].
A possible choice for C, B now yields [UNK] As in (a), [UNK] has two equal eigenvalues, 2, but here possesses only the one eigenvector, {1,2,4}.
With this vector [UNK].
This permits [UNK] in (15).
Theorem XI - The eigenvalues and vectors of a complex matrix may be obtained by treating a related real matrix.

Suppose [UNK] where [UNK] are all complex.
There will be a conjugate relation [UNK] Write A = B + iC, with B, C real; then [UNK] These equations are contained, twice, in the single equation [UNK] Hence the real matrix [UNK] has the eigenvalues [UNK] of (16), and the corresponding eigenvectors [UNK]

#### Example XI

Let [UNK] Then the numerical form of (12) is [UNK] so that the eigenvalues and vectors of A are 1 - i, {-1,2 + i} and 2 + 3i, {-1,1 -i}.
In the alternative form the system matrix, modal matrix and spectral matrix of (17) are, respectively, [UNK] and the reader is invited to check that these matrices satisfy (17).
Theorem XII - Sylvester's Law of Degeneracy: the degeneracy of the product of two square matrices is at least as great as the degeneracy of either factor, and at most as great as the sum of the degeneracies of the factors, or the order of the matrices, whichever is less.

We consider the product C = AB, where A, B have degeneracies p, q respectively.
Without loss of generality we may take [UNK]; for, since the rank of a matrix is unaltered by transposition, we may consider the product either as C = AB or CT = BTAT, with the matrix of greater degeneracy on the right.

We also recall the result proved in 1.12: if a matrix of rank r is multiplied by a non-singular matrix, the product has rank r.
This is because the non-singular matrix may be regarded as made up of elementary operations, and these cannot change the rank of a non-vanishing minor of order r.
This is a special case of Sylvester's law: the degeneracy is at least n - r and at most n - r; i.e. it is n - r.

We now turn to the general case, and approach it by means of a simple example.
Let A, B be standard canonical forms, with n - p, n - q consecutive units in the respective diagonals, beginning at top left, and with zeros elsewhere.
Since [UNK], only the first n - q units in A are multiplied by units in B, ie.e. the product is identical with B and is of degeneracy q.
Now move the units in A one place down the diagonal.
The leading element in the product now vanishes, i.e. the degeneracy is now q + 1.
Proceeding in this way, we finally have all the units in A at the lower end of the diagonal, with p zeros at the top, so that the degeneracy of the product is now p + q (or, if [UNK], the product is null).
This example not only illustrates Sylvester's law; it also makes the important point that the degeneracy of the product depends on the relative positions of the units, and therefore of the linearly independent columns, in the two factors.

Now let A, B be general, and let the equivalent transformations which give them canonical form be PAQ, RBS, where P, Q, R, S are non-singular.
Then we may write [UNK] and D has the same degeneracy as C. The matrix [UNK] will in general be fully populated; if it is appropriately partitioned, we may write (18) as [UNK] To be conformable with the first and last matrices in the triple product, [UNK] must have - p rows and n - q columns.
The final matrix then shows that D has p null rows and q null columns; since [UNK], D has degeneracy q at least.
This establishes the first part of the theorem.

Whether or not D has greater degeneracy than q clearly depends on the number of linearly independent columns in [UNK] To examine this question, consider the submatrix [UNK] The n - p rows of this submatrix, being part of [UNK], a on-singular matrix, are necessarily linearly independent.
In consequence, [UNK] must have just n - p linearly independent columns, making up a non-vanishing minor of order n - p; the other p columns are either linear combinations of some or all of the columns of the minor, or null (a special combination with all coefficients zero).
First, suppose [UNK].
Now [UNK] has n - q columns, the minor n - p columns: separately, a total of 2n - (p + q).
But [UNK] has only n columns; hence [UNK] and the minor have at least n - (p + q) common columns, i.e. [UNK] has at least n - (p + q) linearly independent columns.
The remaining p columns of [UNK] may themselves be columns of the minor, or may be linear combinations of some or all of the columns of the minor, or may be linear combinations of the n - (p + q) common columns, or may be null.
At the extremes, all columns of [UNK] or n - (p + q) columns of{ga} will be linearly independent, giving D degeneracies of q and p + q respectively; any intermediate degeneracy is clearly possible.
Finally, suppose [UNK].
Then, as before, at one extreme, [UNK] can contain n - q columns of the minor, which are linearly independent; at the other extreme, the minor could be wholly contained in [UNK] and [UNK] could be null, when D has degeneracy [UNK].
This establishes the second part of Sylvester's theorem.

#### Examples XII

Although in a numerical case we can find the degeneracy of AB by evaluating and studying C, it is instructive to examine (18) in numerical cases.
We give two examples (i) Let [UNK] Here A is of degeneracy 1, B and C each of degeneracy 2.
Now by building up P and Q by elementary operations (see 1.12) we obtain [UNK] giving the canonical form for A. Similarly, for B we obtain [UNK] Inverting Q and R, we find [UNK] Hence D is given by [UNK] and D is of degeneracy 2.
Note that here the submatrix [UNK] is [UNK] and we can take the first two columns as linearly independent; the third is obtained by subtracting half the first from the second.
(ii) If we transfer the last column of A to the first position, we have a new matrix A; with B unchanged we then have [UNK] A is again of degeneracy 1, B of degeneracy 2; but here C is of degeneracy 3.
We leave it to the reader to follow the steps of Example (i), merely noting that, in the present example, [UNK] is [UNK] with a null column in the first position.
Theorem XIII - a necessary and sufficient condition that a real symmetric matrix A shall be positive definite is that all its leading discriminants shall be positive.

If [UNK] is the real symmetric matrix of a quadratic form [UNK], then the determinant [UNK] is called the discriminant of the form.
The leading minor discriminant of order 1 is [UNK] of order 2 is [UNK], and so on.
Thus if A is to be pos. def., the theorem requires that [UNK], all i.
The vector x is real and non-null but otherwise arbitrary.

First, we put x = e1. then [UNK] reduced to [UNK], which must be positive if f is pos. def.
Next, put [UNK] Now f reduces to [UNK] which, with [UNK] requires also that [UNK].
We might proceed in this way, but a different approach is simpler.
In the full expansion of f, collect together all the terms involving x1; they may be written as a perfect square, so that [UNK] where B is a quadratic form involving [UNK],..., xn only.
Now we collect all terms involving [UNK] and write them as a perfect square, and so on, so that ultimately we can write the form as [UNK] where in fact [UNK] and [UNK] while y is related to x by the triangular substitution (see (20)) [UNK] and [UNK].
Hence f = [UNK], so that [UNK], and [UNK] Now put xn = 0.
Then f may now be written as the quadratic form of which the matrix is the leading minor of A of order b - 1, and we may deduce, corresponding to (22), [UNK] Now, by putting [UNK] we establish a similar result for [UNK] and so on, so that finally we establish that [UNK] From (21) it is clear that a necessary and sufficient condition that f shall be positive is that Di shall be positive, all i.
It then follows from (23) that all the discriminants [UNK] must also be positive; this also is both necessary and sufficient.
This theorem was first established by Sylvester.

Theorem XIV - If two matrices A, B permute, then provided at least one is non-defective, they share the same modal matrix.

Let [UNK] where C is the canonical spectral matrix [UNK] of A, and X is the modal matrix of A: X is not unique; if we have any matrix Y which permutes with C, then from (24) AXY = XCY = XYC so that we can write the modal matrix of A alternatively as XY.
Now write [UNK] so that D is a similar transform of B. Then it follows from AB = BA, on use of (24) and (26), that CD = DC.
We now consider three cases.
(a) The eigenvalues of A are all different.
Thus A is non-defective, and C is diagonal, all the diagonal elements being different.
In this case (see 1.9 (3)), D must also be diagonal; (26) then shows that D is the spectral matrix of B, which thus shares the modal matrix X with A. Note that D can have equal elements (including zeros) in its diagonal.
(b) A is non-defective, but has some repeated eigenvalues.
Thus C is diagonal; we assume it to be in standard canonical form, i.e. it has equal eigenvalues grouped together: this only requires the columns of X to be written in appropriate order.
Suppose, for example, that C has m eigenvalues{ga}, in a submatrix of order m in the leading diagonal place: there may be similar submatrices down the diagonal.
Thus C possesses a scalar submatrix [UNK] in the leading position; Equation (28) (see 1.9 (3) again) now permits D to have a corresponding submatrix, also of order m, arbitrarily populated: thus D will have a block diagonal form.
Now in this case D can be reduced to a standard canonical form E by a similar transformation [UNK] where Y has precisely the same block diagonal form as D; in effect, each diagonal block is resolved into its own canonical form.
But in this case, Y will, like D, permute with C; thus from (25) the modal matrix of A may be written XY, while (26) and (29) require [UNK] so that B shares the modal matrix XY with A. Note that here, E need not be diagonal, so that B can be defective; but non-zero elements in the superdiagonal of E can only occur in a submatrix corresponding to a scalar submatrix in C.

This establishes the theorem as stated.
(c) For completeness, we look briefly at the case where A is defective.
Suppose, for example, that C has the leading submatrix [UNK] then the most general submatrix of D which will permute with C1 is [UNK] where d, e, f are arbitrary.
Thus D1 is in general not of standard canonical form; to make it so we must at least remove f.
Now while, we can find a submatrix Y1 such that [UNK] where E1 is of standard canonical form, Y1 is not of the general form D1 and so will not permute with C1.
In this case, A has the modal matrix X, B the modal matrix XY.
Of course, it is possible for B to be such that f = 0, when D1 is in standard canonical form: A and B then share the modal matrix X, though both are defective.
The obvious (trivial) example of this is that of a defective matrix permuting with itself.
But in general, if A and B are both defective, they do not have a common modal matrix.

In the light of the above, it is clear that two matrices having the same modal matrix do not necessarily permute; they will do so only if their spectral matrices permute.

#### Corollaries

(i) If A, B permute, so do powers of A, B. For example [UNK] (ii) If A, B permute, and the eigenvalues of A are all different, then B can be expressed as a polynomial in A.

As in case (a) above, here [UNK] where C, D are both diagonal.
Now consider the general polynomial [UNK] We can identify P (C) with D; this requires [UNK] where 1[UNK],..., n [UNK] are the diagonal elements of C, and d1,..., dn those of D. The square matrix in (30) is known as an alternant: its reciprocal is discussed in Ref (P1).
Equation (30) defines the coefficients [UNK] such that [UNK] which establishes the corollary.
It is capable of extension, but we shall not pursue the matter here.
There is a considerable literature concerning permutable matrices, see, for example, Turnbull an Aitken (4).

#### Theorem XV - Sylvester's "Law of Inertia"

Let a real symmetric matrix A be rendered diagonal by a congruent transformation [UNK], where B is, of course, non-singular.
Then the numbers of positive, zero, and negative elements in the diagonal of [UNK] are invariant with B.

The number of matrices B which diagonalise A in this manner is indefinitely large: to prove the theorem we need only show that it holds for any two.
Our first choice is B = X, where X is the orthogonal modal matrix of A (being symmetrical, A cannot be defective: see Theorem X) so that [UNK], the spectral matrix of A. Our other choice is [UNK], where L is the lower triangular matrix having units in its diagonal and its other elements so chosen that LA is upper triangular, when [UNK], a diagonal matrix.
It is a simple exercise, which we leave to the reader, to show that the process of triangulation of A by LA without row interchanges gives the elements [UNK] discussed in Theorem XIII, where the [UNK] are the principal discriminants of A and [UNK]: and example (for a non-symmetric matrix) is given in [UNK]

We first note that if A is of rank r, then so are [UNK]; for since [UNK], B, may be regarded as made of elementary operations [UNK] which cannot change the rank of a matrix.
Thus both [UNK] and D will have n - r zeros in their diagonals, which establishes part of the theorem.
To prove the remainder, we suppose the theorem does not hold; let [UNK] have p positive and r - p negative elements in addition to its n - r zeros, and D have q positive and r - q negative elements.
Then [UNK] where, since we have introduced the negative signs, all non-zero i [UNK] and [UNK] are positive numbers.

We begin by supposing p = q + s, where s is a positive number, so that [UNK]; and we examine the general quadratic form [UNK].
If [UNK] then [UNK] These two expressions are equal for all x; subtraction yields [UNK] Let us seek a vector x such that [UNK] Now from (31), [UNK]; thus the first part of (33) provides n - p relations of the form [UNK], and the second part, q similar relations: a total of n - p + q = n - s relations.
But x has n elements, so that we can find only n - s of its elements in terms of the remaining s (see [UNK] an example is given in 2.5) which are arbitrary.
Thus a vector x satisfying (33) has s arbitrary elements.

Now substitute (33) into (32); the RHS vanishes, and so, therefore, does the LHS.
With all [UNK] [UNK] positive this implies, inter alia [UNK] This, taken together with (33), gives y = 0 which in view of (31) gives x = 0.
We thus have two results; x has s arbitrary elements, and x is null: these can only be reconciled if s = 0, when q = p.

If we now take [UNK], a similar argument leads to the same result q = p.
Since the argument does not depend on the nature of X and L, the result is generally true, and the theorem established.

The invariant p is known as the index of positiveness, or simply the index, of A and its quadratic form.
Examples XV (a) Let [UNK] then its orthogonal matrix X is [UNK] which yields [UNK] We build up L as the product [UNK], where L1 annihilates the last three elements of the first column of A, L2 the last two elements of the second column, and L3 the last element of the third column; then [UNK] Then [UNK] and the diagonal elements of LA are those of D = [UNK] We see that both [UNK] and D have two positive and two negative elements.

It may be noted that [UNK].
(b) Let us add 2 to each diagonal element of A, to give [UNK].
then we know (Theorem IV) that [UNK].
We leave it to the reader to construct the corresponding Lo; and to show that [UNK] Thus both [UNK] and [UNK] have two positive, one zero, and one negative element.
Since Ao is singular, so is [UNK] which is shown by the null row.
2

## SOME NUMERICAL METHODS

### 2.1 INTRODUCTION

In this chapter we shall discuss some numerical methods for solving problems formulated in terms of matrices.
However, it must be stressed at the outset that we can do no more here than to indicate the basic principles involved, and give illustrations of a few of the almost innumerable variants of basic methods that exist.
Quot homines, tot sententiae: almost every worker in the field has his pet variation, which suits him ad his computer better than any other.
For a wider discussion, readers are referred to texts such as Bodewig (5) and Wilkinson (6).

Most of the numerical problems which arise in matrix studies (particularly those which derive from dynamical systems) lead ultimately to one or both of two basic processes: (a) the inversion of a numerical matrix; (b) the evaluation of its eigenvalues and vectors.

It will be convenient to deal with these under separate headings.
The methods themselves also divide into two broad categories: (a) direct methods, in which the solution requires is reached in a finite, predictable number of operations; (b) indirect methods, in which the solution is usually obtained by successive approximation procedures, when the number of operations is determined by the rate of convergence.

### I: RECIPROCATION; LINEAR ALGEBRAIC EQUATIONS

#### 2.2 DIRECT METHOD FOR MATRIX INVERSION

Under this heading we give three methods which are all very different in principle.
Each has variants; for each there are circumstances which favour its use.

#### 2.2.1. Pivotal condensation

This method is the simplest, and probably the most universally used.

Suppose we have a square matrix A = [UNK] of order n for which we require to find the reciprocal R: then AR = I.
Now it is possible to write down a sequence of matrices [UNK] Mr (r is usually n or n + 1, depending on the variant employed) which when used as a chain to premultiply A, condense it to the unit matrix, so that [UNK] which evidently implies [UNK] The numerical procedure is to operate successively on 91); given A we can write down M1 and we evaluate [UNK] so that (1) becomes [UNK] Knowing B we can now write down [UNK] and form [UNK] and so on, until R is obtained.
As we shall see, in practice it is not necessary to write down the matrices [UNK] merely perform simple operations with the rows of A and I in (1), which is all the matrices [UNK] do.

For ease of exposition, let us suppose n = 4.
Consider the matrix product, corresponding to (3)

[UNK] In writing down [UNK] we have first arbitrarily selected a non-zero element [UNK] of A as a pivot (underlined) for this first step in the operation.
[UNK] is then obtained from the unit matrix by replacing its second column (corresponding to the subscript 2 of [UNK] by the third column of A divided through by [UNK] with negative signs for the off-diagonal elements.
The third column of B is then null except for a unit in the position corresponding to [UNK]

The product makes it clear that all we are doing, in fact, is to operate with the rows of A in a manner similar to that often used in the condensation of determinants.
Thus row 1 of B is now 1 of A minus [UNK] times row 2 of A; row 2 of B is row 2 of A divided throughout by 3[UNK]; row 3 of B is row 3 of A minus [UNK] times row 2 of A; and so on.

Having obtained B, we now select a pivotal element in it for the next step; the selection is arbitrary except that the element must be nonzero and must not be in the second row, which contains the unit.
For example [UNK] in which [UNK] has been chosen as the pivotal element.
We now choose a pivotal element in C, excluding rows 2 and 3 containing the units.
Note that [UNK] and [UNK] cannot both be zero, or A would be singular and R would not exist; similarly for [UNK] We choose a nonzero element from these four -say [UNK] and then [UNK] The last step is not arbitrary: we must exclude the first three rows (containing units), so that the only choice for pivot in the next step is D44, which cannot be zero.
We write down [UNK], evaluate E = [UNK] obtaining a matrix which if the rows are rearranged by premultiplication by an obvious matrix [UNK], becomes the unit matrix.

As we have said, in practice we do not need to write down M1 etc.
When we use [UNK] as a premultiplier of (1) we combine the rows of I in exactly the same ways as those of A. We can therefore write the two arrays side by side and operate on rows of 2n elements.
For example, to summarise what has been done above (we refer to row i as [UNK]) we use Table 1.
[UNK] When the left-hand array has been condensed to I, the right hand array is R. This method has a number of variants.
First, it is possible to operate with columns, using postmultiplying matrices Mi; but this is really only transposition of operations on rows.
The variants derive mainly from the choice of pivot.
In the so-called optimal pivoting method, one chooses the element of largest modulus from among those available.
In a second variant, one chooses the element of largest modulus in each column in turn; in a third, the diagonal elements are chosen in order; and in a fourth, the diagonal elements of largest modulus are chosen in turn.
The third has the advantage that no final rearrangement of rows is required; on the other hand, it fails if a pivot becomes zero, or even very small.
The third variant is usually described as "diagonal pivoting without row interchange," the fourth as "diagonal pivoting with pivotal strategy."

It is to be observed that the determinant of A is readily found from the condensation procedure.
The determinant of [UNK] is [UNK], etc.
It follows that the determinant of A is [UNK], i.e. the product of the pivotal elements chosen, multiplied by the determinant of [UNK], which rearranges the rows, and so has the value [UNK], according as to whether the number of interchanges is even or odd.

##### Example 1

We exemplify these procedures using the matrix [UNK] This matrix, in fact, has the determinant 100; since its elements are integers, the elements of the reciprocal will be terminating decimals.
In the intermediate steps, however, the numbers are incommensurable: for brevity of exposition we give four decimal places only, though of course a computer will normally employ a much greater number.

##### (i) Optimal pivoting

In Table 2, the last array on the right is the required reciprocal.
Note that, in the rearrangement of the last step, we crossed three rows in bringing [UNK] to the top; then the new second row [UNK] crossed two rows in going to the bottom.
Since the total number of crossings, 5 is odd, [UNK] has the determinant -1; accordingly [UNK] [UNK] [UNK] Coincidentally, this example also illustrates he second variant: it is adventitious that the largest element among those available occurs in the first, second, third and fourth column in succession.
There is thus no difference in the working.
However, in the optimum method a computer is required to scan all elements available, i.e. [UNK] in successive steps, while in the second variant only m, (n - 1),..., 1 need scanning.
In this example, therefore, the second variant has the advantage; in a matrix of large order, the scanning process can take considerable computer time.
No scanning is needed in the third variant, where the diagonal elements are prescribed.

##### (ii) Diagonal pivoting

We now treat the same matrix by the third variant (see Table 3).
For this example, this variant presents no difficulty.
Also [UNK] as before.
The student is invited to effect this reciprocation by means of the fourth variant, in which the largest diagonal element available is chosen as the pivot at each stage; it begins with the bottom right-hand element.

##### 2.2.2 The method of submatrices

This method has nothing in common with the pivotal method, but has great advantages in certain circumstances.
(a) Suppose we have a computer which will accommodate a matrix of order m, but we require to reciprocate a larger matrix A of order n where [UNK].
(b) Suppose we have a matrix B of which we know the reciprocal [UNK]; B is now bordered, so that it becomes a submatrix of a larger matrix A, and we require A-1.
The method of submatrices is particularly useful in solving both these problems.

Let A be partitioned in the form [UNK] Here A is of order n, B of order m, E of order n - m; C and D are in general rectangular.
Let the reciprocal of A be similarly partitioned: [UNK] Then the equations [UNK] provide relations from which, in general, [UNK] [UNK], may be explicitly found.
Various formulae are possible, but the most advantageous from the computational standpoint appear to be the following.
Write [UNK] Then [UNK] as may be checked by evaluating [UNK] It is to be noted that, although these formulae involve a number of multiplications, only two reciprocations, B-1 (of order m) and [UNK] (of order n - m) are involved.

##### Problem (a)

It is clear that the formulae just established provide a method of solution for problem (a) since [UNK] and the computer can reciprocate both B and [UNK] and perform the required multiplications.

##### Example 1

Although it is very small, we may use the matrix A of Equation (2.2.1.4) to illustrate the principles involved.
We shall here partition it into four square submatrices, each of order 2.
In this simple illustrative case we avoid decimals.
Thus [UNK] [UNK] We are now able to evaluate the remaining submatrices of the reciprocal as [UNK] Accordingly, the reciprocal is [UNK] in agreement with the result found earlier.

##### Problem (b)

It is also clear that Equations (3) and (4) provide a solution for this problem.
We are given [UNK] and we border B as in (1) and apply our solution to obtain [UNK] The working is then exactly as in the example just given.

The formulae are, however, rendered much simpler if we have only line bordering, i.e. C is a column, D a row, and E a scalar.
Then X is a column, Y a raw, and [UNK] a scalar.

It follows that we can provide the answer to a third problem, (c): the successive evaluation of the reciprocals of the leading minors of a matrix A until [UNK] is achieved.

##### Example 2

Again, we choose the matrix A of Equation (2.2.1.4): (i) The leading minor of order 1, b1, is the element 6: reciprocal 1/6. (ii) Using (i), we apply the formulae (3), (4) to find the reciprocal of the leading minor of order 2, viz: [UNK] Here [UNK] and we deduce [UNK] (iii) We now use this result to examine the third order minor [UNK] Then [UNK] similarly, [UNK] Also [UNK] Note that, in Equations (4) which we now evaluate, [UNK] is a matrix of rank 1.
We find [UNK] (iv) Using [UNK], we proceed to obtain the reciprocal of [UNK].
We leave this step to the reader, but observe that [UNK]

Since an element in the reciprocal of a matrix M is defined as the ratio of the cofactor of the corresponding element in M to the determinant [UNK], it follows that, for example, [UNK] and hence [UNK] In this example, therefore, [UNK]

##### 2.2.3 Column (or row) building

This method makes use of Theorem IX of [UNK] which states that if we have a square matrix Ao of order n, and know [UNK], then by a simple calculation we can find the reciprocal [UNK] of a new matrix [UNK], where [UNK] is a unit rank matrix, also of order n, [UNK] being an arbitrary column and row respectively.

A second application of the theorem enables us to find [UNK], where [UNK] and so on, until we find [UNK], where [UNK] In this present context, suppose we have a matrix A of order n and require to find its reciprocal.
Then it is possible, using (1), so to choose, [UNK], etc. that Ao is transformed into A, when a last simple calculation gives [UNK] The method has many variants: we can build A column by column, or row by row, or column and row simultaneously.
We give here what seems to be the simplest approach.

We choose [UNK] (or possibly a scalar matrix [UNK]).
Then, if [UNK] is the isolating row vector, we form [UNK] Here [UNK] is the first column of A except that the leading element [UNK] is diminished by 1; thus the first column of [UNK] is identical with that of A, while the (n - 1) remaining columns are those of I. By Theorem IX of 1.22 [UNK] Next we evaluate (this step is not quite so simple) [UNK] so that [UNK] Here [UNK] is the second column of A but with the second element reduced by 1; [UNK] and [UNK] is the second element of [UNK] Further steps follow this pattern and are obvious.
We may, however, observe that (4) may be written [UNK] i.e. as the sum of [UNK] and a rank 1 matrix of which the rows are proportional to the second row of [UNK].

##### Example 1

We choose the same numerical matrix as before (Equation (2.2.1.4)), viz: [UNK] so that [UNK] [UNK]

##### 2.2.4 Triangulation

We have already seen, in [UNK] that reciprocation of a triangular matrix can be achieved by a simple process of back-substitution.
Accordingly, if we first reduce a matrix A to triangular form we can then proceed to determine its reciprocal.

The usual reduction to triangular form is by a pivotal condensation similar to that described in 2.2.1, except that we only remove elements below the diagonal.
We may best illustrate this with out usual example (see Table 1).
What we have done is to keep [UNK] but use it to eliminate the leading elements of [UNK] and so on, reducing the number of rows by 1 at each step.
We have now, in effect, achieved the equation [UNK] [UNK] This has been obtained by triangulation without row interchange.

If we now proceed to the process of back-substitution, this is in effect operating again with rows, and all it does is to compete the process which was done continuously in the pivotal condensation of 2.2.1.
There is thus no advantage at all in he intermediate triangulation step.
However, much attention has been given in the literature to inversion of triangular matrices by methods other than back-substitution, particularly iterative methods.
We illustrate below one direct method.

Triangulation has many important uses.
When we reduce a matrix A to triangular form, we write it as [UNK].

We may first note that the product of the diagonal elements of the leading matrix in (1) is evidently [UNK].
If we divide each row through by its diagonal element, (1) becomes [UNK] The leading matrix here is of the form I + C, where C is null except for the elements above the diagonal.
Now, provided [UNK] as r increases, [UNK] as may be checked by premultiplication by I + C. In this example [UNK] and on use of (3) we obtain from a single multiplication [UNK] Premultiplication of (2) by (4) yields finally [UNK] in agreement with results given earlier.

##### 2.3 ITERATIVE METHODS

These methods are well suited to computers and often have the advantage that, should an error occur, at worst it lengthens the computations a little.

##### 2.3.1 Improvement of an approximate reciprocal

This is an important topic; it often happens that an approximate reciprocal of a matrix A is known: perhaps from a rough calculation, or one in which an error has been made, or even that belonging to a neighbour matrix of A. Refinement of this approximate reciprocal is then required.

The usual procedure is as follows.
Let R be the exact reciprocal and [UNK] the approximation.
Write [UNK] Then [UNK] Premultiply by [UNK] then since [UNK] [UNK] Thus [UNK] is a new approximation to R, and we may repeat the cycle as required to obtain R, subject to convergence of the method.
The conditions for this are readily established.
From (2) we find.
[UNK] and further steps give [UNK] and so on.
Thus, provided [UNK] as r increases, the method will converge very rapidly.
This will normally be the case of R1 is a reasonably good approximation, when the elements of [UNK] will be small.

At each step the method requires the multiplication of two matrices such as AR1, the subtraction of the result from 2I, and then the second multiplication, e.g. [UNK] to obtain the next approximation.
An alternative procedure which achieves the same result but is more convenient computationally is the following.
Write [UNK] Then [UNK] Inversion of this and premultiplication of the result by R1 gives, provided [UNK] as r increases.
[UNK] It is readily checked, in view of (3) et seq., that he product of the first two terms in (5) is R2, of the first three is R3, and so on.
The number of matrix multiplications in this procedure is the same as before; but the squaring of [UNK] etc. is usually relatively easy since they become rapidly smaller in practice.
Indeed, if, for example in (5), [UNK] and higher powers are sensibly null to the order of accuracy required, we can write [UNK] saving one multiplication.

In practice, since the numbers in [UNK] and I become progressively and rapidly more disparate, it is better to deal with them separately; i.e. the operations in (5) are carried on as follows; we are given A and R1: (i) evaluate [UNK] (ii) evaluation [UNK]... until to the order of accuracy required a power of E1 is sensibly null.
(ii) evaluate [UNK] and add R 1 to get R 2, (iv) evaluate [UNK] and add [UNK] to get [UNK], (v) evaluate [UNK] and add [UNK] to get [UNK], and so on.
Normally, very few steps are needed.

##### Example 1

Suppose we are given [UNK] Then A is the matrix of our previous examples, and R1 an approximate reciprocal, given to three places of decimals.
It is required to find the reciprocal R of A, correct to six places of decimals.
Then [UNK] where the figures are exact.
[UNK] is thus exact to six decimal places, viz: [UNK] but [UNK] would require 12 decimal places.
We retain only eight: [UNK] an to this order of accuracy [UNK] is null.
Hence [UNK] Since [UNK] is null, we can apply (6), when [UNK] where we have retained eight decimal places.
Finally, to six decimal places [UNK]

##### 2.3.1 General Iteration

The most general iteration procedure appears to be the following.
We require to solve RA = I for R. Write the known matrix A as A = B - C, where B is a matrix having a known (or easily found) reciprocal.
Then the problem can be written [UNK] where we have written [UNK] There are various iterative methods for solving (2).
For example, we may write it as [UNK] and use the regression formula [UNK] so that, for example, if Ro = 0, we should obtain [UNK] and so on.
Evidently, these are successive steps in the solution of (2), which is valid of [UNK] as r increases.
[UNK] A rather more rapid method is to write (5) as [UNK] For the simple reciprocation of a matrix A these methods hardly compete with pivotal condensation; however, they do have a place in the parallel problem of solution of linear algebraic equations.
It must be stressed, however, that the choice of B must be such at [UNK] has eigenvalues with moduli all less than unity; Sylvester's expansion then shows that [UNK] as r increases.
There are certain physical problems yielding matrices for which this can be guaranteed; but in general some trial and error is involved.

It should be noted that (2) can be written alternatively as [UNK] leading to [UNK] It is important to observe that this general iteration procedure is really exactly the same as the method given in 2.3.1 for improvement of an approximate reciprocal.
The first of Equations (4) shows that [UNK] is an approximate reciprocal, and then Equations (2.3.1.5) and (6) are the same, provided E1 and E are the same.
Now, if B-1 is the same as R1, [UNK] so that the methods are effectively the same.
This result shows that, although in (1) no restriction is placed on B, it must in practice be a reasonable approximation to [UNK] if the method is to converge.

##### Example 1

We illustrate Equation (6) here.
Let [UNK] Here we have chosen B as the lower triangular portion of A, and C is of course B - A. We are given that [UNK] To four places of decimals we now find [UNK] and to this order of accuracy, [UNK] is null.
Then, successively (note that these are not the steps of (4)).
[UNK] and [UNK] is in fact the exact reciprocal of A.

##### 2.3.3 Special iteration procedures

In Equation (2.3.2.1) the only restriction placed on B was that it should have a known or easily-found reciprocal.
We now discuss two particular choices for B.

##### (a) Seidel iteration.

Here B is chosen to be the lower triangular part of A, including the diagonal, with all superdiagonal elements null.
B is then reciprocated as in 1.9 (8) an the methods of the last paragraph applied.
The example given there is in fact an illustration of Seidel iteration.

##### (b) Simple or diagonal iteration.

Here B is chosen to be the diagonal matrix of the diagonal elements of A. Its reciprocal can therefore be written down.
It is mostly used when A is a "sparse" matrix, with elements dominated by the diagonal; B-1 is then a reasonable approximation to R. If this is not the case, the method may not converge, or do so very slowly.
For example, if we take the matrix A of the last example, an choose [UNK] then [UNK] This matrix has two real eigenvalues, 0.319 and 0.597, and a pair of complex eigenvalues of modulus 0.999.
The powers of E therefore converge very slowly indeed.
A better illustration follows.

##### Example 1

Let [UNK] Then, if we retain eight decimal places [UNK] Hence, if [UNK] and so on, we find as successive approximations to [UNK] correct to six decimal places, [UNK]

#### 2.4. SPECIAL TYPES OF MATRIX

Certain matrices have properties which make reciprocation rather easier than would otherwise be the case.
We give a few examples.

##### 2.4.1 Symmetric matrices

The reciprocal R of a symmetric matrix is itself symmetric.
For if A is symmetric and we transpose AR = I to get [UNK] then evidently [UNK] (see also 1.22, Theorem I, Corollary).
[UNK] It follows that we do not need to compute all the [UNK] elements of R; n (n + 1) /2 elements, comprised in the diagonal and below, are all that are required.

##### Example 1

We give in Table 1 a scheme for pivotal condensation of the matrix just examined in Example 2.3.3.1.
For convenience, the reciprocal has been multiplied by 103; we work to six decimal places on the left, three on the right.

If the last four rows of Table 1 are taken in reverse order, the required reciprocal is obtained.
It is to be noted that the starred numbers in Table 1 do not need to be calculated, though it is convenient to write them down.
Provided that appropriate proportions of [UNK] are subtracted from [UNK] as they stand to give zeros in the first column, the array of numbers on the left in [UNK] can be written down; when the rest of [UNK] is found, the third element of [UNK] can be inserted, and so on.
Also, when [UNK] is reached, this gives the last row of R and hence also the last column, so that the eighth elements in [UNK] can be written down, and so on.
However, in practice, the programming required to avoid these calculations could be more time-consuming than the straight pivotal condensation, when the symmetry of the final result gives a check on the calculations.
The procedure in Table 1 also exemplifies triangulation without row interchange.

The product of the underlines elements in the table gives [UNK].

##### 2.4.2 Positive definite (symmetric) matrix

The method to be described is usually attributed to Choleski.

It is a simple matter, which we leave to the reader, to show that if A is real, symmetric and positive definite, then it can be written as the product BTB where B is real and triangular.
Then if [UNK] and since B is triangular, [UNK] is readily found.
We give a simple example.

##### Example 1

Let [UNK] The leading element gives [UNK] (use of - 10 makes no difference).
Then ab = 30, b = 3; ac = 10, c = 1; ad = -10, d = -1.
Next [UNK] and so on.

In this way it is quickly established that [UNK] Inversion of B as in 1.9 (8) then yields [UNK] and then [UNK] It may be of interest to note that if x ={p, q, r, s} is any vector of real numbers, not all zero, then the quadratic form [UNK] may be written (see also 1.22, Theorem XIII) [UNK] where [UNK] so that, where the second term does not involve p, the third p, q, and the fourth p, q, r, [UNK] and is always positive under the conditions given.

If A is not pos. def., the elements of B are in general complex.

##### 2.4.3 Persymmetric matrix

The reciprocal of a persymmetric matrix is not in general also persymmetric; e.g. [UNK] A persymmetric matrix can be treated as symmetric for the purpose of reciprocation, but otherwise it is not special.

##### 2.4.4 Centrosymmetric matrix

We shall consider here only matrices of even order; the odd-order case is quite straightforward, but is algebraically more complicated.

A centrosymmetric matrix A is characterise by A = JAJ, where J is the reversing matrix.
Inversion of this gives [UNK] since J2 = I; the reciprocal of A is therefore also centrosymmetric, as are the integral powers of A. If A is of order 2m, it can be partitioned into four submatrices, each of order m, thus [UNK] other representations are possible, but this appears to be the most convenient.
If (2) is premultiplied and postmultiplied by [UNK] the result is A as required.

We can write the reciprocal of A as [UNK] and then the product of (2) and (3) yields (twice) [UNK] These may be solved if either P or Q is non-singular; we assume P-1 exists, and we write R for P-1Q.
Then from (4) we obtain [UNK] The reciprocation of A may thus be effected through two reciprocations of order m, instead of the much more laborious single reciprocation of order 2m.

##### Example 1

Consider [UNK] Then, in the above nomenclature [UNK] Accordingly, [UNK] A caution must be added: the method is not always viable.
Thus, for example, [UNK] but this result cannot be obtained by use of (4) since by inspection the submatrices of order 2 are all singular.

#### 2.5 LINEAR ALGEBRAIC EQUATIONS

A set of linear algebraic equations (often called simultaneous equations) has the form Ax = p.
Here A is, in general, a rectangular matrix of order m × n with given elements, p is a given column of m elements, and x a column of n unknowns; it is required to find x.

Suppose first that [UNK].
Then we have more equations than unknowns.
If (1) is soluble, there must be n independent equations; if these are written first, we can partition (1) in the form [UNK] where B is square and non-singular.
Then [UNK] If s does not satisfy (2) the set of equations is inconsistent, and (1) does not have a valid solution.
If, however, the equations are consistent, then the solution (2) for x uses only n of them; the remainder are superfluous.

Now let[UNK].
In this case, we have fewer equations than unknowns; we now partition (1) in the form (B, C) {y, z}= p, where B is square, of order m, and y is a column of m quantities.
We now obtain the partial solution for x [UNK] in which we determine m of the unknowns x in terms of B, C, p and the remaining m - n unknowns z.
This is the parametric solution of 1.10.

##### Example 1

[UNK] Consider as partitioned, the solution is (see (2)) [UNK] and [UNK] so that the equations are consistent; if they are taken any two at a time, the three cases all yield the same answer.
However, had the last element in p been other than 4, the three pairs of equations would have given three different answers.

##### Example 2

[UNK].
Here, a simple example is [UNK] which yields [UNK] In Examples 1 and 2 the main numerical problem is the solution of BX = r, By = p - Cz, where B is square.
We now confine our attention to the case where A is square and non-singular; this is obviously germane to the above solutions.

##### 2.5.1 Direct Method

Our problem is to solve Ax = p, for x; here A is a given square and non-singular matrix of order n, p is a given column of n quantities, and x a column of n unknowns.
Formally, the solution is obvious: x = A-1p.
We can therefore obtain our solution by inverting, using any of the methods of 2.2, 2.3, and postmultiplying the inverse by p.
In some problems we require to obtain x for each of a set of values for p; e.g. the elements of p may be functions of an independent variable, and we require x for each of a number of values of the variable.
If this number is high - in particular if it exceeds n - then labour is saved by inverting A and using (2).
If, on the other hand, the number is small, labour is saved as follows.

We use the approach of 2.2.1; but instead of operating on (2.2.1.1) with the matrices Mi, we operate directly on (1).
Evidently, we then progressively approach the solution (2).
The computations, by simple operations on rows, are effected in exactly the same way.
Indeed, reciprocation is really only the solution of a particular set of linear algebraic equations, in which the vectors p are successively [UNK] For a single set, in pace of e1 we use the single vector p.

##### Example 1

Suppose we require to solve [UNK] The square matrix used here is that employed for the Examples of 2.2; we choose diagonal pivoting without row interchange.
The working of the left-hand array is thus identical with that of Example 2.2.2.1.
See Table 1.
The last four figures in the right-hand array are given correct to three decimal places and are in fact the exact solution.

##### 2.5.2 Iterative methods

We exemplify the general iteration procedure of 2.3.2; we write B - C for A, where the reciprocal of B is known or easily obtained.
Then Equation (2.5.1.1) can be written [UNK] so that, if F is written for B-1C, the solution is given by [UNK] say.
As before, this may be developed in either of two ways, provided [UNK] as r increases: x = q + Fx, suggesting the regression formula [UNK] or [UNK] Though the computations may be different, these two formulae are equivalent; for if xo = 0 the regression formula gives [UNK] and so on.
We illustrate (3) below.

##### Example 1

It is required to solve [UNK] The square matrix has been used in Example 2.3.2.1.
We again choose B to be A except that the elements to the right of the principal diagonal are all zero: then, as before [UNK] [UNK] Note that here F = B-1C: in the previous example, E = CB-1.
We now construct the iteration table (see Table 1), beginning with x1 = q and applying (3).
Since, in view of the fact that F has two null columns, the first two elements of x are always multiplied by zeros, it is not necessary to compute them until the iterations are complete.
At the beginning of the iteration, we have retained only two decimal places: later three, then four, until to this order of accuracy the iteration repeats.
Finally, the first two elements are computed, when the last column (here x10) is the solution required.

It may be observed that equations of the form x = q + Fx arise naturally in some dynamical or quasi-static problems, e.g. the distortion of a structure under applied load, when the load is varied by the distortion.

##### 2.5.3 Choleski's method for positive definite matrices

Let us now suppose that in 2.5.1 A is pos. def.
Then as in 2.4.2 we can write A as [UNK] where B is triangular.
The equations for solution are now [UNK] Write y for Bx; then (1) can be solved in two steps: [UNK] and then Bx = y for x.

It may be noted that a set of equations Ax = p, where A is general, may be cast in the above form by premultiplication by AT: [UNK] However, this does not appear to offer any computational advantage.
Resolution of [UNK] into [UNK] implies A = CB where C is an orthogonal matrix, so that [UNK].
Again, however, this does not appear to offer any worthwhile computational short-cut.

##### Example 1

Suppose we wish to solve [UNK] As in 2.4.2, we can quickly resolve the square matrix into [UNK] A self-explanatory scheme for computation is shown in Table 1.
Here BT, p are written at the head of the left-hand array; by obvious row combinations we find y at the bottom.
This and B are inserted at the top of the right-hand array, when again obvious row combinations give the required solution at the bottom right: in summary [UNK]

#### 2.5.4 Least squares

In 2.5 we noted that if we have more equations than unknowns, the equations must be consistent, or a unique solution does not exist.
Nevertheless, especially in experimental work, cases often arise where the number of equations exceeds the number of unknowns.
For example, suppose we have a measurable quantity f which we have reason to suppose is a polynomial function of an independent variable t: [UNK] and we wish to find the m coefficients [UNK].
Measurement of f at each of m values of t would provide m equations for the m unknowns; however, since f is measured and so is inexact, it may be thought better to measure f at n values of t, where [UNK] in order to minimise the effects of experimental error.
How do we proceed to find optimum values of the coefficients [UNK]?

The "least squares" solution of this problem is due to Gauss.
Let the n equation in m unknowns [UNK] be written Ax -p = e, where A is of the order (n × m), x is the column of m unknowns [UNK], p is the column of n measures values of f, and e is a column of n errors.
We are given A and p; e will vary with x.
Gauss' proposition is that x will have its optimum value when the sum of the squares of the errors, ie.e [UNK] is a minimum.
Now [UNK] and for this to be a minimum, its differential with respect to x (see 1.11) must vanish; i.e. [UNK] which is our original set of Equations (2) with e = 0, premultiplied by AT; it gives m equations for the m unknowns.

##### Example 1

Suppose we expect the relation (1) to be [UNK] and suppose further that we have the following experimental table: [UNK] Then in view of (5) our equations for solutions may be written [UNK] Before we proceed to the least squares solution, let us see what results would be obtained if we solved these equations three at a time, with e taken to be zero for each set of three.
We should get [UNK] These are all very different.
Moreover, if we adopted the first solution and applied it throughout, e would become (the first three elements have been assumed zero) [UNK] which is clearly quite unacceptable for the later measurements.
However, if we premultiply (6) by AT as in (4) we get [UNK] and the solution, by inspection, is x ={1, -2,1}, i.e. [UNK] If we now return to (6) and use this solution, we find [UNK] which compares very favourably with the result given earlier.

##### 2.5.5 Least squares: weighted errors

In the basic Gaussian method just described, it has been tacitly assumed that all errors are equally likely.
The method is readily adapted, however, to cases where some weighting of errors is desirable: it is merely a case of premultiplying (2.5.4.2) by an appropriate diagonal matrix.

##### Example 1

Suppose we wish to put a straight line [UNK] through the following set of experimental points: [UNK] Suppose further that, in view of the experimental method, we may expect errors in f to be proportional to t.

Let us first examine the straight Gaussian solution.
The equations can clearly be written [UNK] Premultiplication by AT yields [UNK] so that the optimum lime, if all errors are equally likely, is f = 0.57t + 1.80.
However, we are given that errors are likely to be proportional to t.
To make them equally likely, we must multiply the first of Equations (1), at t = 1, by 6; the second, at t = 2, by 3; the third, at t = 3, by 2, etc; i.e. we premultiply (1) by Diag (6,3,2,1,5,1,2,1).
The result is [UNK] and premultiplication of this by [UNK] yields [UNK] to two decimal places.
Hence in this case, the optimum line is f = 0.50t + 2.01.
For comparison, the errors e in the two solutions (2) and (3) are (the lines intersect at t =3) [UNK] and it is clear that in the second case the errors increase markedly with t, as required.

### II: EIGENVALUES AND VECTORS

#### 2.6 THE CHARACTERISTIC EQUATION

The n eigenvalues of a square matrix A = (Aij) of order n are given (see 1.16) by the roots of the characteristic equation [UNK] which, in expanded form, can be written [UNK] In theory, therefore, the calculation of the eigenvalues of A is straightforward: we form the characteristic determinant in (1), expand it to the form (2), and solve this by any suitable means to obtain [UNK].
Having obtained the eigenvalues, can readily find the corresponding eigenvectors.
If r [UNK] is a known eigenvalue (which we assume here to be unrepeated) and [UNK] the corresponding column and row eigenvectors respectively, then [UNK] Since [UNK] are each arbitrary to a scalar multiplier, we can in each vector make a suitable element unity; then Equations (3) provide in each case n linear algebraic equations for the (n - 1) unknown elements: one equation is superfluous, or can be used as a check.
For example, if we make the last element of [UNK] unity, and partition ([UNK]) to isolate its last column and row, we can write (3) as [UNK] which give [UNK] Equations (5) can be solved by any of the methods of 2.5 (the second would be transposed to [UNK], and then [UNK] Unfortunately, so far as the expansion of (1) to (2) is concerned, theory and practice are at odds.
With [UNK] general, the labour involved in the expansion is quite prohibitive even for small values of n, and indirect methods are always used in practice.
We describe two such methods below; first, however, we observe that, in (2), we can readily obtain the two coefficients p1, pn, since (see 1.22, Theorem II, III) [UNK] The evaluation of a numerical determinant, even of high order, is very quickly accomplished on any modern computer by reduction to triangular form; thus we can find p1 and pn without difficulty.
It remains, however, to find p2, p3,..., pn-1.

##### 2.6.1 Location method

In Equation (2.6.1) we arbitrarily assign (n - 2) different values to [UNK] (other than [UNK] = 0, which we have in effect used to determine pn) and then evaluate the (numerical) determinant for each of these.
We then obtain n - 2 linear algebraic equations for the n - 2 unknowns pi.
A caution should be added: most the arbitrary values of [UNK] should preferably lie among the zeros of [UNK] ([UNK]; otherwise inordinately high accuracy may be needed.
At this stage, the zeros of [UNK] ([UNK]) are now known, but their approximate locations may often be inferred from their sum and product as given by (2.6.6) and (2.6.7).

##### Example 1

Let [UNK] The sum of the eigenvalues is thus [UNK] and their product 3906.25 (=p4).
Their arithmetic mean is thus about 11 an the fourth root of [UNK] about 8.
These suggest that we might use [UNK] = 20, [UNK] = 10 in (2.6.1); we have already used [UNK] = 0 to obtain [UNK].
It is readily found, by condensing the numerical determinants, [UNK] Now we know that [UNK] or [UNK] Insertion of [UNK] = 20, [UNK] = 10 in (3) together with the numerical values of [UNK] (gl}) from (2) yields the two equations [UNK] which give p2 = 606.25, p3 = 2812.5.
Hence [UNK] on factorisation.
The eigenvalues of A are thus 25, 12.5, 5, 2.5.

We illustrate the calculation of the eigenvector [UNK] corresponding to the eigenvalue 12.5.
Then [UNK] giving [UNK] of which the solution is (any method from 2.5 may be used) [UNK] and it is readily checked that these also satisfy the fourth equation.

##### 2.6.2 Iteration method

In view of the Cayley-Hamilton theorem, A satisfies its own characteristic equation; i.e. [UNK] Postmultiply this by any arbitrary column co and write [UNK].
Then a computer will rapidly evaluate the successive products [UNK] and so on.
Accordingly (1) yields [UNK] This provided n linear algebraic equations for the n unknowns pi.
As before, we can find [UNK] independently if we so wish.

It must be added, however, that this method is not suitable when n is large.
As we shall see later, the columns ci usually tend to proportionality as i increases, so that Equations (2) become increasingly ill-conditioned; also the numbers involved can assume widely different magnitudes.

##### Example 1

We use the matrix A of (2.6.1.1) with co = e4.
It is found that successive columns ci are then [UNK] Accordingly, (2) can be written [UNK] in agreement with (2.6.1.4).
With the particular choice of co, p4 enters into the last equation only.
Accordingly, if we calculate p1, p4 from the trace and determinant of A, we can discard the last equation and substitute for p1 in the remainder, when (3) reduces to [UNK] Any two of these (consistent) equations give p2, p3 their values in (4).

#### 2.7 POWER METHODS

The most commonly used device for finding the eigenvalues and vectors of a matrix A is the power method, or one of its many variants, in which A is effectively raised to a high power.
We illustrate some aspects of the basic principle.

##### 2.7.1 A dominant eigenvalue

Sylvester's expansion for A is (see 1.18), in its simplest form, [UNK] and in view of the properties of the constituent matrices [UNK], [UNK] Since the order of the terms on the right is immaterial, there is no loss of generality i supposing1 [UNK] to be the eigenvalue of greatest modulus.
If for the moment we assume it to be real and unrepeated, then all other eigenvalues have smaller moduli.
Thus if r is increased sufficiently, say to a value s, the first term on the right of (2) dominates the rest, which become relatively insignificant.
Then, in the limit, [UNK] By use of (3) we thus find both 1 [UNK] and [UNK].
We could in theory find them from As only, since [UNK], but there is a practical difficulty.
Unless the modulus of 1 [UNK] is close to unity, the numbers appearing in Ar (r large) are either inordinately large or small; in practice therefore it is usual to find not Ar but a matrix proportional to it: at each stage in the power evaluation, a homologous element is reduced to unity.

##### Example 1

Let A be the matrix in Equation (2.6.1.1).
Then, if we reduce the bottom right-hand element to unity, we have [UNK] We now evaluate B2 and divide through by the bottom right-hand element to obtain [UNK] Evaluation of F2/2.4997 repeats F except for occasional small differences in the fourth decimal place.
Now, if we round off to three decimal places, we find that F can be written as the unit rank matrix, proportional to [UNK] [UNK] If we now revert to A and postmultiply by [UNK] [UNK] Thus, 1 [UNK] = 25.
Also, the inner product [UNK] is [UNK] so that normalising to make [UNK] unity: Note that [UNK] so that A has been raised fairly rapidly to a high power.
An alternative.
There is, however, an alternative device which is in practice more commonly used; this is repeated premultiplication by A of an arbitrary column [UNK] as in 2.6.2.
We successively evaluate [UNK] etc.
If we postmultiply (2) by co and write [UNK] (ki is of course a scalar) we obtain [UNK] Accordingly, provided that co is not such that k1 ([UNK]) vanishes, the first term on the right dominates the rest as r increases, until in the limit when r = s [UNK]

##### Example 2

We exemplify this using the same matrix A as above; also, we adopt the device of reducing at each stage a homologous element (in this case the bottom element) to unity, beginning with co = e4.
The first step is [UNK] Proceeding in this way, we find successive columns as in Table 1.
Also given are the dividing factors at each step.

Since c16 repeats c15, they give x1; also the dividing factor 25 is 1[UNK].
To complete the solution, we now require to find [UNK]; this could be done by repeating the iterative procedure, evaluating [UNK], where [UNK] is an arbitrary row, or more usually, by the device given in (2.6.4), viz: [UNK] giving [UNK] We leave it to the reader to show that in this example, (7) leads to [UNK] or to a scalar multiple of it.
We normalise [UNK] in the usual way.

We may note in passing that (as they should) the columns [UNK] and [UNK] of Table 1 agree with the last columns of B, C, D, E, F (subject to rounding-off errors in the last place of decimals).
This leads naturally to a comparison of the two methods.
There are two reasons why the second method is commonly used.
First, if an error (even of rounding-off only) is made during the successive squaring process, it is multiplied by itself [UNK] subsequently, an persists through the calculations; in the second method, if an error is made in calculating ci, this only amounts to choosing a new arbitrary column, an at worst may prolong the calculations.
But, mainly, the first method usually involves more work than the second.

It is difficult to quantify "work" exactly, but if the number of individual multiplications is taken as a guide, then, if A is of order n, each of the n2 elements of [UNK] involves n multiplications: i.e. n3 in all.
If r squaring processes are needed, we perform rn3 multiplications, yielding [UNK], r must be an integer.
In the column process, each step involves n2 multiplications; hence, to reach the same accuracy, between [UNK] and [UNK] multiplications are needed.
Now, provided the eigenvalues are reasonably separated, column iterations usually number between 15 and 50.
Suppose, in a particular case, 25 are required.
Then the "work" is measured as [UNK] From Table 2, r must be 5, with the work measure for squaring 5n3.
The ratio is n/5; so if [UNK] the work involved in squaring is greater.
If, say, n is 100, the work is 20 times greater.
[UNK]

##### 2.7.2 Subdominant eigenvalues: deflation

Again, for the moment we assume the eigenvalues of A to be real and unrepeated; and we assume that in (2.7.1.1) they appear in descending order of modulus.
If, as in 2.7.1 we have found [UNK], then Equation (2.7.1.1) can be written [UNK] The known matrix on the left now has all the eigenvalues and vectors of A except the first set, and it can be treated as in 2.7.1.
The process of reducing A in this way is known as "deflation."
Evidently the eigenvalue 1 [UNK] has been replaced by zero, so that A1 is singular.

Having evaluated A1, we can again apply column iteration.
However, we need not begin with an arbitrary column; we can readily find an appropriate column to begin with, which avoids many iteration steps.
An example will make this clear.

##### Example 1

We continue Example 2.7.1.1.
The iterations have shown that 1 [UNK] = 25, while x1 is proportional to{1,2,3,5} and [UNK] to (1,7,5,4).
Normalising these, we find [UNK] Note that [UNK] vanishes when premultiplied by [UNK].

We now revert to the iterations for 1 [UNK] an observe that, for example, c9 of Table 2.7.1.1 is mostly composed of x1.
The remainder will clearly be mostly [UNK].
Since x1 is orthogonal to [UNK], the part of c9 due to x1 will disappear when it is premultiplied by A1 (see 1))).
Thus we find [UNK] and dividing by the last element, we find as a starting column co for iteration with A1 [UNK] The iterations give us successive columns as in Table 1.
Column c9 repeats c8, so that 2 [UNK] = 12.5 and [UNK] is proportional to{-0.5, = -0.5,0,1}.
As before, we now find that [UNK] is proportional to (-1, -2,0,1).
Normalising, we find [UNK] We proceed to the third eigenvalue; we further deflate A by subtracting the unit rank matrix (3) from A1: [UNK] Note that [UNK] = 7.5, while [UNK] is in fact doubly degenerate; it vanishes when premultiplied by [UNK] or [UNK].

As before, we choose a column from Table 1 - say c3 ={-0.4978, -0.4992, -0.0015,1} - and apply it as a postmultiplier to [UNK].
The result is a column proportional to{0.981, 0.0095, - 1.0095, 1}.
We leave it to the reader to show that this leads rapidly to 3 [UNK] = 5 with x3 proportional to{1,0, - 1,1} an that [UNK] is then found to be proportional to (27, -11, -15.8).

We normalise this to obtain [UNK] an now further deflate A to obtain A3; in this case, as will be seen, no iteration is required to obtain a solution: [UNK] In obtaining the last form of (5) we have noted (a) that [UNK]; since the other three eigenvalues have been replaced by zeros, 4 [UNK] = 2.5; (b) A3 is, by inspection, of unit rank an so, with 4 [UNK] extracted, can be written in the form (5).
This completes the solution.
With the four terms of the Sylvester expansion now given numerically in (2), (3), (4) and (5), the whole solution can be expressed compendiously as [UNK]

##### 2.7.3 Subdominant eigenvalues: sweeping

Although the delation procedure discussed in 2.7.2 is the most straightforward possible method, other devices are often useful and sometimes preferable.
We now discuss "sweeping," which takes two forms.

##### (i) First method

Instead of operating with a deflated matrix, we operate on the original matrix A (or a part of it) with a column vector from which all contributions from x1 have been "swept" away.
This is valuable, for example, when (as is often the case in dynamical problems) A is sparse.
Deflation destroys this characteristic; the sweeping method under discussion does not.

With r = 0, Equation (2.7.1.5) becomes [UNK] Hence if we choose co to make k1 zero, it will contain no contribution from x1, and, as r increases sufficiently to a value s, (2.7.1.5) will tend to [UNK] The condition [UNK] means that we can express one element of co in terms of the remaining n - 1.
In theory, if co is chosen in this way, the iterations will in due course yield (2) without further attention.
In practice, rounding-off errors soon produces inaccuracies which re-introduce small proportions of x1, which tend to grow relatively rapidly.
It is therefore best to apply the criterion [UNK] at each step; i.e. to calculate one element of cr from this criterion when the others have been found.
This means that we can ignore one row of A; we exemplify this below.

As before, we need not be completely arbitrary i our choice of co (though it must satisfy [UNK]) from (1), a column free of x1 is [UNK] with co arbitrary.
But we can with advantage choose co to be a column in the previous iteration to find1 [UNK] etc.: this will contain mostly x1, some [UNK], but little else; then [UNK] eliminates the contribution from x1.

##### Example 1

We use the same example as before, restating for convenience what we have already found.
[UNK] Note that [UNK] have been normalised to give [UNK].
Now any postmultiplying column say{a, b, c, 1}, must satisfy [UNK] In performing our iterations, therefore, we may ignore completely the first row of A; we use the last three rows to find the corresponding elements in a column, and then apply (3) to find the top element.

For our initial column co, we again choose the column c9 from Table 2.7.1.1, in the iteration to find 1 [UNK] etc.; thus for our present purpose [UNK] Then [UNK] and [UNK] As it should, this column vanishes when premultiplied by [UNK].
We divide throughout by the last element to obtain as our new starting column [UNK] then the iterations, using (3) at each step, begin [UNK] We postmultiply A (ignoring its top row) by the column (4) to get the column of three numbers on the right; divide by the last element to get the bottom three elements in the next column, and find the top element from (3).
In this way, we obtain the successive columns and dividing factors in Table 1.

Thus we find [UNK].
As before, knowing 2[UNK], we find [UNK] is proportional to (-1, -2,0,1).
Normalising: [UNK] The same principle serves for the third root.
If cr ={a, b, c, 1} then [UNK] and [UNK] must both vanish; we find [UNK] If we select c3 from Table 1 as our new co, it already excludes x1, so that [UNK] will also exclude [UNK].
This is [UNK] If this is written{0.9333,0.0333, - 1.0333,1}, it satisfies (6).
We now iterate on A, but ignore the first two rows: [UNK] We leave it to the reader to show that this converges quickly to 3 [UNK] = 5, x3 ={1,0, -1,1}.
In the usual way, [UNK] is found to be proportional to{27, -11, -15.8}.
Normalising: [UNK] As before, no iteration is needed for the completion of the solution.
If we choose the last column above (which excludes x1 and [UNK]) as a new co, then a column which also excludes x3 is [UNK] Since x1, [UNK], x3 are excluded, this column is proportional to x4.
Premultiplication by a row of A gives 4 [UNK] = 2.5; completion of the solution is straightforward.

##### (ii) Second method

Instead of sweeping our iterated columns at each step, we can do it one for all with the aid of a "sweeping matrix."
In view of (3) we may write [UNK] If (8) is used as postmultiplier of A, it is clear that A is deflated by the sweeping matrix in (8) to [UNK] (note that A1 here differs from the deflated form A1 of 2.7.2).
If A is of simple form (e.g. sparse) this characteristic may be partly or wholly destroyed in forming A1; on the other hand, A1 has a column of zeros, and thus its own simplicity.
This means also that the umber of the head of a column iteration is always multiplied by zero, an so need not be calculated till the final step.
We are thus effectively operating with the third-order submatrix of A1 when its first row and column are omitted.
As before, we may find a suitable initial column such as (4).
We then perform the iteration, omitting the first element of (4): [UNK] The numbers produced in this way reproduced exactly those of the last three elements in the columns of Table 1, as well as the dividing factors; they are of course exactly the same calculations, but with the matrices associated differently.
At the conclusion, the top element of the final column is found by use of the first row of A1.

We must emphasise, however, that the row vectors A1 are not [UNK], [UNK].
Hence, when 2 [UNK] has been found, we revert to A itself to find [UNK].

For the next root, we use another sweeping matrix based on the second part of (5): [UNK] If this square matrix is used to postmultiply A1 we find [UNK] We now iterate on the submatrix [UNK] to determine the last two elements of x3; we leave the completion of the solution to the reader.,

##### 2.7.4 Shifting and inverse iteration

Theorem IV of 1.22 noted that, in view of the identity [UNK] addition of a quantity{ge} to each of the diagonal elements of A implies the addition of{ge} to each of the eigenvalues of A. We note here, additionally, that the constituent matrices zii of A are unaltered by such a change.
Sylvester's expansion gives (see 1.18) [UNK] whence [UNK] The device of adding{ge} in this way is known as "shifting," and has a variety of uses.
For example, with hindsight, we know that the eigenvalues of A in (2.6.1.1) are 25, 12.5, 5 and 2.5. the rapidity of convergence of the initial power solution depends principally on the relative separation of the eigenvalues 25 and 12.5, i.e. 2:1.
If we reduce all eigenvalues by 7.5, they become 17.5, 5, - 2.5, - 5 and the relative separation is 31/2:1 which yields much quicker convergence.
Note that this is the optimum: the second and fourth eigenvalues now have equal moduli.
To select the optimum requires accurate knowledge of the eigenvalues, which at the outset of a calculation is of course not available; but if one has a general idea of the disposition of the eigenvalues, shifting can save much time.

The principle use of shifting, however, lies in inverse iteration.
Suppose, for example, that the matrix A is the system matrix of a vibrating mechanical system, and suppose further that this system is excited by a forcing vibration of frequency corresponding to [UNK] = [UNK].
It is desired to determine the eigenvalue (and its vectors) nearest to [UNK] in order to study the response.

To approach this problem, we first note that Sylvester's expansion for negative powers of a matrix B gives [UNK] It follows that the eigenvalue of B with the smallest modulus now becomes the eigenvalue of B-1 with largest modulus.
Hence, to solve our problem, we first evaluate B = A - [UNK] the eigenvalue of A nearest to [UNK] now becomes the eigenvalue of B nearest zero, i.e. of smallest modulus.
(Note that A, B and B-1 all have the same constituent matrices zii.)
We therefore invert B and iterate on B-1 as usual to obtain our solution.

##### Example 1

Once more we choose the matrix A defined in (2.6.1.1) and used in previous examples.
We also let [UNK] = 5.5.
Then [UNK] If we invert this, e.g. by the methods of 2.2, we obtain [UNK] We postmultiply this by an arbitrary column co: here we choose co = e1 and iterate as usual.
The successive columns are given in Table 1.

The iterations converge rapidly to x ={1,0, - 1,1} with the eigenvalue of B-1 equal to -2.
Hence the eigenvalue of B is - 0.5 an of A is 5.5 - 0.5 = 5, in accordance with results obtained earlier for 3 [UNK] and x3.

Note that, since the eigenvalues of A are in fact 25, 12.5, 5, 2.5, those of B are 19.5, 7, - 0.5, - 8, and of B-1 therefore 0.0513, 0.1429, - 2, - 0.124.
The relative separation of the two roots of largest moduli is here 14:1.

Clearly, the method is not restricted to mechanical systems: by its means we can study the eigenvalues and vectors of any matrix A which lie near any given value o [UNK] of [UNK].
[UNK]

##### 2.7.5 Confluent eigenvalues

So far, we have restricted our attention to unrepeated real roots of the characteristic equation belonging to a matrix A; we now consider the case of two equal real roots.
Multiple roots are in practice very rate (except perhaps for mechanical systems moving freely in space, when multiple zero roots can occur: but these have a special simplicity).
The treatment for two roots is readily extended to the multiple case if required: even for two roots, however, we require to examine two cases (see 1.21).
We assume the roots to have dominant moduli, any roots of greater modulus having been removed by deflation etc.

##### (i) Characteristic matrix doubly degenerate

When a repeated eigenvalue 1 [UNK] makes the characteristic matrix doubly degenerate, we know (see (1.21.14)) that the Sylvester expansion of the system matrix A is [UNK] It follows that we can use the power method to find 1[UNK]; postmultiplication by co gives in the limit, when r is sufficiently large, say s, [UNK] We thus find 1 [UNK] without difficulty; but the determination of z11 + z22 requires further consideration.
Now [UNK] and [UNK] is thus, in general a linear combination of 1, [UNK].
At this point, the iteration has given no indication that a double root is involved; however, this becomes apparent when we seek the row vector corresponding to cs: for all first minors of 1I [UNK] - A vanish and we cannot find a unique row vector.

To proceed, it is simplest to generalise (2.6.4) by partitioning off the last two rows and columns of 1I [UNK] - A, thus: [UNK] Here [UNK] [UNK] is a square submatrix of order [UNK] of order 2; [UNK] has two columns and [UNK] has two rows.
Then [UNK] These algebraic equations are solved for [UNK]; we now have two independent columns [UNK] which annihilate 1I [UNK] - A when used as postmultipliers; and correspondingly for the rows [UNK].
We now normalise them; we evaluate [UNK] Then m is a square matrix of order 2 and, for example, [UNK] are normalised rows and columns.
Finally [UNK] Note that only the sum [UNK] is unique.
If they are individually expressed as [UNK] and [UNK] then their sum can be written [UNK] where M is an arbitrary non-singular matrix of order 2.
This replaces x1, [UNK] with two different linear combinations (x1, [UNK]) M of them, with corresponding changes for [UNK].

It will be observed that in this approach we have not used cs (which we have already found); its introduction would spoil the simplicity of (2).
When x1, [UNK] have been found, it is possible to check that cs is a linear combination of them.,

##### Example 1

Consider the matrix [UNK] It is assumed that at this stage we have no knowledge of its eigenvalues.
If we choose [UNK] and iterate in the usual way, we find quite quickly that [UNK] Normally, we would choose [UNK] However, if we attempt to use (2.6.4) to find [UNK], it at once emerges that all first minors of 1I- [UNK] A vanish, indicating that 1 [UNK] = 12.5 is a repeated root.
We therefore apply (2) with [UNK] This gives for the solution of (2) [UNK] Since the columns and rows are arbitrary to a scalar multiplier, we may now write [UNK] (for simplicity of exposition we have multiplied the first column on the right by 3).
The product of the numerical matrices in (8), in that order, is (see (3)) [UNK] If we premultiply [UNK] we ca finally write [UNK] These enable us to choose, if they are required, [UNK] but, following (5), we could equally well use any two different linear combinations o x1, [UNK], represented by (x1, [UNK]) M provided these are associated with. [UNK], /div4.

##### (ii) Characteristic matrix simply degenerate

This case is rather more difficult: the difficulty derives from the appearance of a unit in the superdiagonal of the spectral matrix of the given matrix A. For simplicity of exposition we assume here that A is of order 4: extension to larger matrices is obvious.
We know (see 1.21) that [UNK], [UNK] so that [UNK] on expansion of the triple product.
We know further that, in view of the properties of the constituent matrices zij, [UNK] When [UNK] is absent, this reverts to the simpler case dealt with under (i).
Our task now is, given A, to resolve it numerically into one of the forms (12), i.e. to find 1 [UNK] etc.

Sine, a priori, we do not know the nature of A, we should approach this task as usual by iteration with A on an arbitrary column co.
If we write [UNK] then postmultiplication of (13) by co yields [UNK] When the iterations have proceeded so far, say when r = s, that contributions from 3[UNK], 4 [UNK] are insignificant and may be neglected, then [UNK] Previously, with [UNK] absent, at this stage [UNK] equalled [UNK].
Now, owing to the last term, this is no longer true and successive columns tend to show a near arithmetical progression in their elements.
It is true that, when s is very large [UNK] the columns tend ultimately to x1 (last term in cs dominant), but the number of iterations required is very large.

However, in place of the simple [UNK] we can drive from (15) the relation [UNK] In practice, therefore, if convergence seems very slow, we evaluate three successive columns fully, omitting the reduction of a homologous element to unity, and solve the quadratic [UNK] for at least two homologous elements.
If they have a common root, we test the remaining quadratics to see if they are satisfied by this common root.
If they re, then the root is 1 [UNK] and the iterations have proceeded far enough (r = s) for only terms in 1 [UNK] to remain.
Knowing 1 [UNK] we use (15) to evaluate [UNK] giving us a column proportional to x1.

Knowing 1[UNK], we now form the matrix 1I [UNK] - A; if we put r = 0,1 in (13), multiply the first by 1 [UNK] and then subtract the second: [UNK] Premultiplication of this by [UNK], or postmultiplication by x1, annihilates it; none of the other vectors does so: the matrix is rendered simply degenerate by the presence of z12.
We may, however, use (2.6.4) to find [UNK], we then known 1 [UNK] and [UNK] subject to scalar multipliers.

To find [UNK] we revert to (11), which yield, inter alia, [UNK] or [UNK] Since 1I [UNK] - A is simply degenerate, the last equations provide, in general, n - 1 independent linear equations for [UNK] (and [UNK]).
However, one element in each of these vectors may be assigned arbitrarily.
For, since (1I [UNK] - A) x1 vanishes, the equation for [UNK] is also satisfied by [UNK], where q is arbitrary; so, for example, if we choose a non-zero element in [UNK], the homologous element in [UNK] may be made zero by appropriate choice of 1.
Similar considerations apply for [UNK].
We are thus able to solve (19) for [UNK] and [UNK].
Having done this, we now require to normalise: we evaluate [UNK] and we may then choose our vectors as, for example, [UNK], [UNK] and the pair [UNK] which we now call [UNK].

We have now obtained 1 [UNK] the vectors [UNK] and [UNK], and the auxiliary vectors [UNK] and [UNK]; we are therefore in a position to deflate A (see (12)) by removing all contributions from these quantities.
The solution is then completed in the usual way.

##### Example 2

We require to find the modal and spectral matrices of [UNK] We begin by iterating on co.
If we choose co = e4, then after about 18 steps, four successive columns are [UNK] These show very slow convergence; indeed, the elements show a near-arithmetical progression.
We therefore choose, say, the first of these columns and without reducing the last element to unity, calculate the next two columns: [UNK] We choose, say, the first and last elements of these and solve [UNK] The common root 12.5 also satisfies the middle two quadratics; hence we find 1 [UNK] = 12.5.
We now use (17) and find{2.2875, 4.6875, 7.5, 13.125} - 12.5{0.165, 0.355, 0.57,1}={0.125, 0.25, 0.375, 0.625} and hence [UNK] may be taken as{1,2,3,5}.

Using (21) we now evaluate [UNK] and it may be checked that postmultiplication by [UNK] gives a null product.
We use (22) as in (2.6.4) to find [UNK], we leave the solution to the reader: it is found that [UNK] which when used to premultiply (22), annihilates it.

We now proceed to find the auxiliary vectors.
If we write [UNK] (the first element of [UNK] is nonzero, so that of [UNK] may be taken as zero) then we solve, using the appropriate submatrices (see (19)) [UNK] The solution is [UNK].
A similar calculation yields [UNK].

We must now normalise these.
We evaluate [UNK] Note that here, since the second row and first column of the product are necessarily orthogonal, m is triangular; also in this case it happens that m-1 = m.

Accordingly, we may choose to retain the columns [UNK] and to adopt the rows, orthogonal to [UNK], [UNK], [UNK] We are now able to evaluate [UNK] and [UNK] We can now deflate A (see (21)) to [UNK] Note that trA1 = 7.5; also A1 is doubly degenerate, being annihilated by postmultiplication by both [UNK] and [UNK].

Iteration with A1 on co = e4 produces quite quickly the simple eigenvalue 3 [UNK] = 5 and vector x3 ={1,0, -1,1}.
We then evaluate 5I - A1 and employ (2.6.4) to obtain [UNK].
Normalising this with x3, we obtain [UNK] and we are now able to deflate A further to [UNK] Since [UNK] and [UNK] is the only remaining eigenvalue, [UNK] and [UNK] can be written [UNK] which completes the solution.
The results may be expressed compendiously as [UNK] The numbers are not of course unique.
We could, for example, divide x4 by any factor f provided we multiply [UNK] by f.
However, if for example we divide [UNK] by 10 and multiply [UNK] by 10, we must replace the unit in the superdiagonal of [UNK] by 10.

##### 2.7.6 Conjugate complex eigenvalues and vectors of a real matrix

So far, we have restricted our studies to real eigenvalues.
However, complex eigenvalues and vectors are of frequent occurrence, and require special consideration.

First, if the matrix is real, then its characteristic equation must have real coefficients.
Hence, if it is satisfied by [UNK], then it will also be satisfied by [UNK]; complex eigenvalues of a real matrix therefore occur in conjugate pairs.
In a similar way, if the eigenvector corresponding to [UNK] is [UNK], then the relation [UNK] implies the conjugate relation; hence p - iq is the eigenvector corresponding to the eigenvalue [UNK]

Evidently, the vector in (1) is arbitrary to a scalar complex multiplier, say [UNK] + [UNK] another vector satisfying (1) is thus [UNK] Any arbitrary linear combination of p and q may therefore be taken as the real part of the vector, with a corresponding combination for the imaginary part.

If we expand (1) we obtain successively [UNK] If we eliminate q we find [UNK] The same equation is satisfied by q.
This suggests that the square matrix in it is doubly degenerate and that p, q can each have two arbitrary elements; but this is not so.
When [UNK] p are known, q is uniquely related to p by [UNK] in which [UNK] is not singular.

What is said above gives a background to what follows.
We assume once more than [UNK] have dominant moduli, any eigenvalues of greater moduli having been removed by deflation etc.
Again, a priori, we assume nothing is known of the nature of A, so that the process of finding the dominant eigenvalue and its vector is approached as usual by iterating with A on an arbitrary column co.
Once again, for simplicity, we assume A to be of order 4.

The Sylvester expansion of A gives [UNK] Accordingly, if we perform the usual iteration on co and continue until, with r = s, terms in 3 [UNK] and 4 [UNK] are negligible.
[UNK] where [UNK] is a complex scalar.
Now, as we have seen (p + iq) is arbitrary to a complex scalar multiplier (and p - iq similarly).
We are therefore at liberty to choose [UNK] and then [UNK] Elimination of p, 1 from these three equations yields [UNK] Note that, since [UNK] this is precisely the same as Equation (3); however, in the iteration case, it is only true when the iterations have proceeded sufficiently far for the terms in 3[UNK], 4 [UNK] to disappear, when cs consists only of p.
Now in practice, with a pair of complex eigenvalues, the elements in [UNK] tend to change sign periodically: there is no point in reducing a homologous element to unity, since there is no convergence to a settled form.
When [UNK] behave in this way, conjugate complex eigenvalues must be suspected; and then three consecutive columns must be periodically tested to see whether various pairs of homologous elements give consistent values for [UNK].
When this happens, the iteration has gone far enough, and we can take p = cs, when q is determined from the second of equations (6), which is in fact the same as (4).
We now know{gm}, {go} p and q.

Finding [UNK] is not so straightforward.
Knowing [UNK] we can either (i) Solve [UNK] with one element of [UNK] arbitrarily assigned.
We then have to solve a set of linear algebraic equations with complex coefficients; (ii) Iterate with A postmultiplying an arbitrary row [UNK]; this will lead to [UNK] (and [UNK] again) as for p, q. (iii) Solve the equations which parallel (3) and (4): [UNK] Since [UNK] are known, this, like (ii), involves only real numbers; on the other hand, it requires [UNK], the evaluation of which requires considerable computer time if the order of A is large.
On the whole, since most modern computers can work with complex numbers, (i) seems the most straightforward.

When we have obtained [UNK] we can perform a check, which is in any event needed when the vectors are normalised.
For since [UNK] belong to different eigenvalues, they are orthogonal, and [UNK] so that [UNK] For the process of normalisation, we require to evaluate [UNK] and m is evidently diagonal; in view of the check equations (9) it can be written [UNK] the determinant of which is [UNK], so its reciprocal is readily written down and we can obtain normalised forms of [UNK].
We can now deflate A. Since [UNK] a deflated matrix A1 is [UNK] We can therefore use A1 to obtain the remaining eigenvalues and vectors of A in the usual way.

##### Example 1

Let [UNK] If we use this for iterative premultiplication of an arbitrary column, say the summing vector, successive columns are as show in Table 1.
[UNK] It is apparent from the first that the vector elements are changing sign; so we do not reduce a homologous element to unity (though in general we might periodically remove a power of 10).
If, starting say at c5, we test to see if pairs of homologous elements give consistent values for [UNK], [UNK] in (7), we find this is not so.
However, [UNK] give nearly consistent values; we therefore begin with [UNK] accurately: [UNK] If these three columns are used in (7) then any two pairs of homologous elements give [UNK].
We thus obtain [UNK] Also, we may now choose [UNK] and using the second of Equations (6) we now find [UNK] We now have to find [UNK], and for this we use (8).
One element of [UNK] can be arbitrarily assigned: here we assign the value 1 to the third element and solve [UNK] which, if we omit one column (e.g. the last) from the square matrix, gives [UNK] We omit the details of solution; the answer is [UNK] Note that [UNK] Accordingly, [UNK] and if we postmultiply p + iq as given by (14) and (15) my m-1 we obtain as our normalised p, q, [UNK] We are now able to deflate A. Equation (11) becomes, with A given by (12) and use of (13), (14), (15) and (16), [UNK] A1 is, in fact, doubly degenerate; it is annihilated by both the columns immediately above it.
iteration with A1 on an arbitrary column quickly leads to the result [UNK] Further delation leads at once to [UNK] which completes the solution.

##### 2.7.7 Adjacent eigenvalues: Two eigenvalues with nearly-equal moduli

When two eigenvalues have nearly-equal moduli, it is obvious that very many iterations will be required for a direct solution.
The following device can be helpful in this case.
Suppose the iterations have proceeded so far that only contributions from the two nearly-equal eigenvalues remain.
Then we can write, when a homologous element is not made unity, [UNK] Here a, b, c, d; p, q are the values of a homologous element in the various columns; a, b, c, d are known.
Elimination of p, q, yields two equations which may be solved for 1 [UNK] + 2 [UNK] and 12[UNK] [UNK]: [UNK] Hence, [UNK], [UNK] are readily found.
When they are known, then [UNK] which follow from the first two of Equations (1).
When 1[UNK], 2 [UNK] are very close, both numerator and denominator in (2) tend to be small differences, so that accurate calculation of a, b, c, d is desirable.

In practice, iteration in this case behaves rather like that for a defective matrix (2.7.5), in that convergence is slow and successive columns tend to a quasi-arithmetic progression of the elements.
The occurrence of nearly-equal roots is more common than that of a defective matrix; hence tests to see whether homologous elements yield, in (2), consistent results should be applied first when convergence is slow.
[UNK]

##### Example 1

[UNK] Iteration on a column, beginning with co = e4, yields successive columns as given in Table 1.

At this stage, we make consecutive accurate calculations, to see if we can get consistent values for [UNK]: [UNK] Using the elements of the last line in (2) we obtain [UNK] The elements of the first line give [UNK] The results are consistent, as indeed are the results from the second and third lines.
By inspection (or from the implied quadratic) [UNK] We now evaluate the eigenvectors: [UNK] so that we may take [UNK] I now remains to find the corresponding row vectors and to deflate A for further study; we leave this to the reader.
However, we may note here that [UNK] whence [UNK].

##### 2.7.8 Applicability of power methods

We have seen that the power method can be used to obtain dominant eigenvalues and the associated vectors, and, by deflation, sweeng[UNK], shifting and inverse iteration, can also be used to find all non-dominant eigenvalues and their vectors; the results are obtained seriatim.
This implies that, if one is interested only in a limited number of eigenvalues, the power method is the obvious choice.
For example, suppose we have a mathematical model with n = 100 for study of the vibration characteristics of an aircraft.
The aeroelastic engineer will usually be interested only in the fundamental mode of vibration and a few overtones, say 10 in all; in the usual model this implies the dominant and the 9 immediately subdominant eigenvalues and vectors.
The vibration engineer will be concerned with a band of frequencies near the engine rotational speed, and so will use shifting and inverse iteration.
But in any event, the mathematical model will usually involve the finite element concept which gives accurate values for the lower band of frequencies, but is often quite unrepresentative of the top frequencies.
Evaluation of all frequencies and modes is therefore not normally required.
For such a model, power methods are the obvious choice.

However, if interest attaches to all eigenvalues, and in particular if there is less concern with the associated vectors, other methods may be used.
We now begin a brief study of transformation methods.

#### 2.8 TRANSFORMATION METHODS

In these methods, we apply a succession of similar transformations to a matrix A: [UNK] and so on, until A is transformed into a form giving the eigenvalues directly: it may be a triangular form, or the ultimate canonical form [UNK] (or [UNK] if A is defective).
Since the transformations are similar, all the derived matrices B, C, D,... have the same eigenvalues as A; and if we proceed to the diagonal form, then the chain product X3[UNK] [UNK]... gives the modal matrix X.

##### 2.8.1 Jacobi's method for a real symmetric matrix

In 1.22, Theorems VIII and X, we have shown that a real symmetric matrix has real eigenvalues and that it cannot be defective.
Moreover, its modal matrix is orthogonal; hence [UNK] Jacobi's method is as follows.
We begin by searching the off-diagonal elements of A (since A is symmetrical, we usually use the upper half only) to find the element Auv of greatest modulus.
We then construct the orthogonal matrix [UNK], which is the unit matrix except that the units in the (u, u) and (v, v) positions are each replaced by [UNK] and the zeros in the (u, v) and (v, u) positions by [UNK] and s respectively.
Then [UNK] and we may evaluate [UNK] of which the relevant submatrix is (omitting all other rows and columns) [UNK] which yields [UNK] We now choose{gth} 1 such that Buv vanishes; i.e. [UNK] This fixed{gth} 1.
If than 2{gth} 1 is positive, we take 2{gth} 1 to lie in the first quadrant; if negative, in the fourth, Then{gth} 1 lies between [UNK] = c is positive and [UNK] has the sign of tan 2{gth} 1.

With c, s fixed, we can now evaluate B fully.
Elements other than in the uth, vth columns and rows are unaltered from those in A; at the intersections of the uth, vth columns an rows the new elements are given by (3) (with Buv = 0), while the remaining elements Biu, Biv in the uth, vth columns and rows are [UNK] We may make two deductions.
First, from (3) we have [UNK] and since only these diagonal elements have changed, it follows that [UNK] as it must in a similar transformation.
Next, fro (5), squaring and adding, we have [UNK] and since only the uth, vth columns and rows have changed, we deduce that the sum of the squares of all the off-diagonal elements of B is less than that of A since we have replaced the two elements Auv of A by zeros in B. Thus [UNK] Having evaluated B, we repeat the procedure to find C; we select the element Bpq of largest modulus and find [UNK] from (see 4)) [UNK] we then proceed as before to construct [UNK] and [UNK].
C will have Cpq = 0 and may also have cuv = 0 (if [UNK]); but this situation will not persist.
At some stage, in general, elements formerly made zero will again become nonzero, though usually smaller than before.
Thus Jacobi's method does not terminate in a finite, predictable number of steps; indeed, the umber may be very large.
Nevertheless, following (6) [UNK] and, in an overall sense, the off-diagonal elements therefore become progressively smaller, until eventually we obtain a matrix in which the off-diagonal elements are all vanishingly small: i.e. a diagonal matrix of which the diagonal elements are the eigenvalues.

We give below an example, but must enter the caveat that because of its small order (n = 3) it converges radly[UNK].
At each stage, the sum of the squares of the off-diagonal elements decreases by at least one third.
However, if we had a matrix of order 100, it would have 9900 off-diagonal elements, and we can only say that at each stage the sum of the squares of these elements would decrease by 1/4950 at least; convergence to diagonal form is likely to take very much longer than for a small matrix.

We may add two observations.
The method is viable if Auv is reduced, not to zero, but to some lesser modulus; nevertheless, reduction to zero is obviously best.
Also, the method requires only that A is real and symmetric: its state of definiteness is irrelevant.
In the example below, A has a negative eigenvalue.

#### Example 1

Let [UNK] We select the off-diagonal element of largest modulus (underlined) and evaluate (we record only six decimal places) [UNK] Hence [UNK] and then [UNK] Note that [UNK] also [UNK] thus we have effected a considerable overall reduction.

The second step is to obtain C. For this we select the underlined element in B an evaluate in succession [UNK] and then [UNK] Note that the zero elements in B have become nonzero in C; however, [UNK] is now 2.19132; compare [UNK] above.
Proceeding in this way, after six transformations, we find to the order of accuracy employed [UNK]

##### 2.8.2 The LR and QR methods

We now describe briefly two methods which are applicable to any square matrix A, whether symmetric or not, real or complex, simple or defective, non-singular or singular.
Here, we shall merely state and illustrate the methods; for proofs, readers are referred to Wilkinson (6).
We may note, however, that while a complex matrix A = B + iC (B, C real) may be treated as such, using complex arithmetic, it is more usual to treat its real equivalent [UNK] which (see Theorem XI, 1.22) yields the eigenvalues and vectors of A and its conjugate.

##### 2.8.3 The LR algorithm

It is a straightforward process, readily programmed for a computer, to resolve a matrix A into the product L1R1 where L1 is a lower triangular matrix having units in its diagonal, and R1 is an upper triangular matrix.
For a model, we here take n = 4; it is tycal [UNK] of any order.
Let [UNK] [UNK] Apart from the top row of [UNK] which by inspection is identical with that of A, we have here 12 equations ad 12 unknowns.
From the first column of the product we have [UNK] which determine p, q, r.
The second column yields [UNK] which, with p,.
q, r known, determine in succession 2[UNK], s, t.
The remaining unknowns 3[UNK], x33, n and the last column of R1 are found progressively in the same way.
Note, however, that A11, 2[UNK], x33,... are divisors (vots[UNK]) in this procedure, so that a voting [UNK] strategy may be needed.
Note also that [UNK], so [UNK]; hence, if A is non-singular, the diagonal elements of R1 must all be nonzero.
Indeed, this program is very suitable for the numerical evaluation of determinants.

The [UNK] algorithm resolves A into the product [UNK] as above, and then multiplies the factors in reverse order to obtain a new matrix B. Since [UNK] and then [UNK] is a similar transform of A. B is, in general, a fully populated matrix of which the last column is that of R1 (thus A14 reappears in B) and the last row that of L1 multiplied by x44.
When B is found, it is in turn resolved into the product L2R2 and [UNK] evaluated, and so on.
As the succession of similar transforms proceeds, it is found that (a) the elements below the diagonal become progressively smaller, (b) the diagonal elements tend to the eigenvalues, in descending order or modulus down the diagonal.
When the process is well established, it is found that (with n = 4 as our model) the element [UNK] becomes approximately [UNK] in [UNK].
When this element becomes very small [UNK] tends to decrease by the factor [UNK] and [UNK] by [UNK] and so on.
Accordingly, if the eigenvalues of A are widely spaced, convergence of the [UNK] method is fairly rad[UNK]; if, however, there is a pair or group of nearly-equal eigenvalues, then very many iterations may be required before the end result is achieved.
This is an upper triangular matrix T, of which the diagonal elements are the (real) eigenvalues in descending order of modulus, and which still retains the element A14 in the top right position.

If A has a pair of conjugate complex eigenvalues, then T is not strictly upper triangular: the diagonal includes a block of order 2 such as [UNK] with [UNK] on the diagonal of T and [UNK] below it.
In this case, the solution of [UNK] yields the complex eigenvalues.
the numbers, [UNK] not in general constant under transformation; but if the iterations have proceeded so far that I is in the quasi-triangular form, the trace and determinant of (3) are invariant, so that the complex roots are fixed.

As the LR transformations proceed, the most rad [UNK] convergence is to the smallest eigenvalue in the bottom right-hand corner.
Indeed, if there is a zero eigenvalue, it appears in the first transformation, i.e. in B. It follows that shifting (see 2.7.4) can be used with great advantage to accelerate convergence.
When the element in the bottom right-hand corner has reached a settled value (i.e. the eigenvalue), we can deflate the transform, by omission of its last row and column, before continuing the iterations with a matrix of reduced order., /div4.

##### Example 1

We choose the deflated matrix i (2.7.2.2) as A: [UNK] Since [UNK], the bottom right-hand element of [UNK] vanishes, as it should.
We now evaluate the product in reverse order: [UNK] The reader is invited to check that, if B is resolved as it stands into [UNK] then C = [UNK] will also have its last row null, the zero eigenvalue thus repeating.
We may therefore deflate B, omitting its last row and column and continue the iterations with the leading first minor of B. It is found that, after 22 more iterations, working to six decimal places, [UNK] Thus, the eigenvalues of A are, in descending order of modulus, 12.5, 5.0, 2.5, 0.

The whole operation may in fact be summarised as LT = AL: [UNK] Recovery of the eigenvectors in the LR procedure is not straightforward, especially if deflation has been used.
Since the eigenvalues are known, probably the simplest method is to use (2.6.4).
However, if we have not deflated, then clearly [UNK] leads to (see (5) above) [UNK] We now require to transform T to [UNK].
If TP = PA, then tycally [UNK] [UNK] where PA has been multiplied out.
Identification of the elements on each side, beginning with the superdiagonal, leads to [UNK] giving a, d, f.
The remaining unknowns, b, e, c are found progressively.
With P determined in this way, we have [UNK] so that the modal matrix of A is the product LP.
The reader is invited to evaluate LP, using the numerical values of (5) in (6), and in particular to note that the eigenvector belonging to the zero root is that originally associated with the eigenvalues 25 in (2.7.2.6)

The LR procedure is thus simple and easily programmed.
However, in practice, it normally requires very many iterations before convergence is achieved; moreover, the process of recovering eigenvectors outlined above is apt to be ill-conditioned, and some other procedure is usually to be preferred.

##### 2.8.4 Pre-reduction to upper Hessenberg form

As we have seen, the LR procedure (and the QR method, to be discussed shortly) annihilates the elements of A below the diagonal.
This is, however, usually a very long process; and while it can be accelerated by shifting and deflation, it is in fact better to depopulate A below the diagonal, as far as possible, as an initial step.

An upper Hessenberg matrix has only zeros below its infradiagonal; and it is possible to transform any matrix A to this form by a similar transformation.
This is the best that can be done to depopulate a matrix below its diagonal; if one could remove infradiagonal elements as well, there would be no problem in finding eigenvalues and vectors of a matrix.
We illustrate reduction to upper Hessenberg form with a general matrix of order 4; it is clear that the procedure applies to matrices of any order greater than 2.
We write AK = KH as [UNK] Just as we have done earlier, we can evaluate the n2 unknowns progressively.
The first column of the product gives [UNK] which determine h11, h21, p, q (note that here, also, a voting [UNK] strategy may be needed).
From the second column [UNK] which yield in succession [UNK] and so on.
Thus, by progressive substitution, we arrive at the Hessenberg matrix [UNK]; it possesses the same eigenvalues as A. If we apply the LR or QR algorithms to H, the Hessenberg form is retained at each step; thus, instead of removing all the elements below the diagonal, we have to remove only those in the infradiagonal.
Much computer arithmetic and time is thus saved.
Transformation of A to H therefore greatly improves the LR algorithm; we have introduced it here, however, because for the QR method it is a sine qua non.

We may add here, in passing, that it is possible by simple substitutions to reduce any matrix A to tridiagonal form - populated only in the superdiagonal, diagonal and infradiagonal.
However, for our present purposes this is unnecessary; and in any event it often involves ill-conditioned equations and so lacks accuracy.

##### Example 1

We again choose the matrix A of (2.8.3.4).
The reader is invited to check that, if A is transformed as in (1), then [UNK] If we now treat H as our basic starting matrix A and resolve it into L1R1 then [UNK] As will be seen from [UNK], resolution of an upper Hessenberg matrix requires an upper Hessenberg L1, i.e. a matrix with zero elements everywhere except in the diagonal and infradiagonal.
Both the resolution of A into L1R1 and the subsequent evaluation of [UNK] (B is also of upper Hessenberg form) are thus much simpler than when A is fully populated.

##### 2.8.5 The QR algorithm

We assume that the matrix A is already in upper Hessenberg form.
Then, in parallel with the LR algorithm, we write [UNK] where [UNK], as before, is upper triangular.
However, here we do not resolve A into [UNK] instead, we require that [UNK] shall be a orthogonal matrix: [UNK] Thus [UNK] is our similar transformation of A into B. We then transform B into C: [UNK] and so on, until the transform is eventually an upper triangular matrix having the eigenvalues of A in its diagonal.
It remains to explain how Qi is chosen.
There are various possibilities; the most popular methods are those of Givens and Householder (6).
Here we describe Givens' method; and as before, for simplicity of exposition, we choose n = 4.

Let the matrix, pre-reduced to upper Hessenberg form, be [UNK] Also, let [UNK] where [UNK].
Then if we evaluate [UNK] as a chain, beginning by premultiplying A by the last of the three matrices in (4), and if also we take [UNK] then A is first replaced by a matrix in which the leading element of the infradiagonal vanishes.
The top two rows of A are altered; in particular, 2 [UNK] is replaced by [UNK].
In the next multiplication we take [UNK] and then the second element in the infradiagonal vanishes.
Finally, with A33 now altered to [UNK] we put [UNK] and complete the chain.
The result is the upper triangular matrix R1.
We now have to complete the similar transformation by postmultiplying by Q1; the result, [UNK] is again of upper Hessenberg form.
We now repeat the cycle to obtain [UNK] and so on.
As before, it is found that the infradiagonal elements become smaller at each step until the similar transform of A is ultimately upper triangular (or quasi-triangular if A has complex eigenvalues); i.e. a matrix T given by [UNK] The following point is important.
In our treatment above, B is the product of a chain of seven matrices.
When the multiplications are carried out in the order indicated, the upper Hessenberg form is maintained throughout, If, however, we begin by multiplying the central three matrices, the upper Hessenberg form is lost, with a accompanying loss of simplicity.

It is now apparent why A must be pre-reduced to upper Hessenberg form.
Equation (4) employs one matrix for each nonzero element below the diagonal - three in this case; n - 1 in general.
There are thus 2n - 2 multiplications in each iteration.
But if A were fully populated, the number of multiplications would be n (n - 1).

##### Example 1

The reader is invited to work through this example; we avoid repetitive labour by the use of hindsight.
Consider the matrix defined in (2.7.6.12) and reduce it, as in (2.8.4.1), to upper Hessenberg form.
The result is a new matrix [UNK] We now, with hindsight, use a shift of 0.2; i.e. we work with the matrix A - 0.2I.
Shifts are always used to improve convergence: this particular shift requires only one step.
The matrix is now [UNK] and after the six multiplications implied (see (4)) in [UNK] it becomes [UNK] Thus A - 0.2I has a zero eigenvalue; we recover B by adding 0.2I and can then deflate and consider the reduced matrix [UNK] Once again, to avoid repetitive labour in the example, we use hindsight: we now apply a shift of 0.4 and consider [UNK] We require only one step (four multiplications) to reduce this to [UNK] We now recover [UNK] by adding 0.4I and deflate by omission of the last row and column: [UNK] In any similar transform of [UNK] the trace and determinant are unaltered.
The two eigenvalues of [UNK] are thus determined by [UNK] The required eigenvalues are thus 0.2 (bottom right-hand element of B), 0.4 (bottom right-hand element of [UNK]) and [UNK].

The convergence properties of the QR algorithm are superior to those of LR, particularly when shifts are used and deflation is performed whenever possible.
If complex eigenvalues exist,"double shifts' (see Wilkinson (6)) may be made and two QR steps performed simultaneously to give rapid convergence while all arithmetic is kept real.
The QR method is thus very powerful and of quite general applicability; it is probably the most popular technique on modern main-frame computers for the evaluation of eigenvalues of non-symmetric matrices.
On the other hand, recovery of eigenvectors, though possible, is very difficult and often inaccurate, and some quite different routine (e.g. (2.6.4), when the eigenvalues have been found by QR) is recommended.,

#### 2.9 MATRIX PENCILS

Our discussion of this toc [UNK] is very limited, though we look again at the subject, also briefly, in 2.10.

##### 2.9.1 Eigenvalues and vectors of matrix pencils

Any lambda-matrix of the form C [UNK] - B, which can in general be rectangular, *is described as a matrix pencil (see 1.15).
If C is square, of order n, and non-singular, the pencil is described as regular, since in the polynomial equation obtained by expansion of [UNK] the coefficient [UNK] which does not vanish, so that there are n eigenvalues i [UNK] which satisfy (1).
It is clear that these eigenvalues belong also to the matrix [UNK].
For each root i [UNK] there will be at least one linear relation between the columns of the pencil, so that we may write [UNK] and [UNK] is an eigenvector of the pencil.
The pencil is described as simple if there are n independent vectors [UNK] so that we may write the set compendiously as [UNK] where [UNK] is of simple diagonal form, even through it may include multiple roots.
If, on the other hand, one or more auxiliary vectors are required, so that the spectral matrix takes the form [UNK], then the pencil is defective.

In particular, a pencil is simple if B, C are real and symmetric and if C is pos. def.
This proposition is proved in Corollary 1 of Theorem X of 1.22.
However, it does not follow that if B, C are real and symmetric, the pencil is simple, or its roots real.
The reader is invited to study the two pencils [UNK] Pencil (i) is real and symmetric; it has two equal eigenvalues [UNK] = 1 and the spectral matrix is of elementary Jordan block form; it is defective, with only the single eigenvector{2,1}.
Pencil (ii) also has real, symmetric coefficients; but its eigenvalues are [UNK], with independent vectors{1,1 + 1} and {1,1 -i}.
It is thus simple.
In both (i) and (ii), [UNK] is negative, and so C is not pos. def. (see 1.22, Theorem X).

If B, C are real and symmetric, and if in addition C is pos. def. then as in Theorem VIII of 1.22, the eigenvalues are real and finite and the eigenvectors real.
We ow restrict our attention to simple pencils, where symmetric or not.

In parallel with (2) we have the equation [UNK] and this leads to the counterpart of (3) [UNK] Postmultiply this by X and use (3); then [UNK] For simplicity, let us now suppose all roots i [UNK] to be distinct.
Then [UNK] permutes with a diagonal matrix and is therefore itself diagonal: [UNK] But (see (3)) is arbitrary to a postmultiplying diagonal matrix; we may thus write [UNK] and then from (5) [UNK] In the special case where B, C are symmetric, we may evidently identify Y with X.

So much for the elementary properties of pencils.
We turn ow to their numerical treatment.

First, if we have a simple pencil C [UNK] - B, we may premultiply it by C-1 to obtain I [UNK] - A, A = C-1B; we may then obtain the eigenvalues and vectors of the pencil by applying any of the methods of 2.6-2.8 to A, and often this is the simplest procedure.
However, cases can arise where this is not the best approach.
For example, suppose C to be tridiagonal and B diagonal.
Then C-1 is in general fully populated, and so would be C-1B; the simplicity of the pencil is thus lost in A. The same is true when C, B are sparse.

We now give an example in which C, B are sparse and symmetric.
The reader is invited to study this closely, since it illustrates more than the possible treatment of a pencil.

##### Example 1

Consider the pencil [UNK] here C is tridiagonal and symmetric; B is diagonal.
Also (though this is immaterial for our present purpose) both are centrosymmetric.
The pencil thus has particular simplicity as it stands.
We re required to find the eigenvalues i [UNK] which satisfy [UNK], and the corresponding vectors.

First, if we attempt this evaluating A = C-1B we find [UNK] Thus A is fully populated and is not symmetric (though, as it must, it remains centrosymmetric).
We therefore return to the original form (8).

A possible way of dealing with this is to use the location method (see 2.6.1).
If we write [UNK] then [UNK] (since P is of order 4); we therefore require to assign three arbitrary values to [UNK] and then, by simple triangulation, evaluate [UNK] for each of these.
Since the product of the roots is [UNK], we may choose [UNK] = 2, 1, - 1 as reasonable arbitrary values.
Then we find, using a typical direct triangulation [UNK] while [UNK].
Fortuitously, we have found one of the zeros of[UNK].
Disregarding this for the moment, we write [UNK] and use the above values; we find [UNK] the solution of which is [UNK].
Hence [UNK] or [UNK] To find the zeros of [UNK] ([UNK]) we may, for example, use the companion matrix (see 1.16), which, in this example, is [UNK] the eigenvalues of which are the zeros of (10).
We may find these in the usual way by iteration: we repeatedly premultiply an arbitrary column, say [UNK], by M. Successive columns are then given by Table 1.
We observe that, owing to the particular form of M, we need calculate only the top element of each column, in this table; the remaining elements are those of the previous column, one step down.
In fact, we re only solving the regression formula [UNK] which is equivalent to the iteration with M; this is in effect Bernoulli's method of solution of [UNK] ([UNK]) = 0.
To six places of decimals, we have now found 1 [UNK] - 6.464102.
Hence [UNK] on extraction of the first factor.
If we set up a regression formula (or companion matrix) for the cubic, we find the next factor to be ([UNK] + 1), as we have already noted.
In face [UNK] so that the eigenvalues are [UNK].

We now look briefly at the eigenvectors.
Typically [UNK] which is of course singular.
We treat it by the method of Equation (2.6.4), using the first three rows, to obtain with x4 =1, [UNK] so that we find at once [UNK].
In this way, with the eigenvalues in order of modulus, we find [UNK] A point of interest may be noted: the individual vectors are either centrosymmetric or centroskew, just as a symmetric structure has either symmetric or antisymmetric modes of vibration.

We leave it to the reader to check that (see (3)) [UNK] and also that [UNK] are diagonal.

To complete this discussion, we may observe that the companion matrix, or its equivalent - the regression formula, may be used to find complex roots of a determinantal equation (see 1.7.6).
For example, suppose we find [UNK] Then we may set up the regression formula [UNK] and if we begin with [UNK], we find for successive values of [UNK] [UNK] The periodic change of sign, with no settled ratio, indicates complex roots.
We therefore apply Equation (2.7.6.7) to the last 4 figures in sequences of 3 (we assume contributions from the other roots to be vanishingly small): [UNK] which give us [UNK].
Hence (13) has the factor [UNK]; and we may write [UNK] so that all he factors of (13) are complex.

##### 2.9.2 Deflation of a matrix pencil

The eigenvalues and vectors of a simple pencil (not necessarily symmetric) will satisfy [UNK] Write these as [UNK] then [UNK] are evidently the eigenvectors belonging to the eigenvalue i [UNK] of C-1B.
If we normalise them so that [UNK] then Sylvester expansion of C-1B (see 1.18) is [UNK] so that we may express B in terms of C, etc., as [UNK] Now suppose that we have found [UNK].
Then we are able to evaluate, on the left-hand side, [UNK] and evidently a new pencil, which has all the eigenvalues and vectors of the original pencil except that 1 [UNK] is replaced by 0, is [UNK] This is Lancaster's deflation formula.
We may note two points: (i) since [UNK] has a zero root, must be singular, (ii) it is not necessary to normalise the vectors; we can write B1 generally as [UNK]

##### Example 1

We use the pencil defined in (2.9.1.8) and we assume first that we have found an eigenvalue 1 [UNK] = -1 and the associated eigenvector [UNK].
Since the pencil is symmetric we shall have y = x.
Now, using (2.9.1.8), we have [UNK] Hence, from (5) we find [UNK] which, with B defined as Diag (1,2,2,1) gives [UNK] This matrix is simply singular; indeed, as is indicated by (3), it is annihilated by postmultiplication by [UNK]: in (3), [UNK] is orthogonal to [UNK], i = 2,3,..., n.
Accordingly, the pencil P1 (); has a zero eigenvalue.

The deflation can of course be repeated.
If, using P1 (),; we now find an eigenvalue 2 [UNK] = 0.6 and the associated eigenvector [UNK], then [UNK] and then we may calculate [UNK] which, with B1 given by (6), yields [UNK] By inspection, B2 is doubly degenerate; it is of course annihilated by postmultiplication by [UNK] or [UNK].
A third deflation would produce B3, a unit rank matrix, which in this instance (n = 4) would be the last term in (3).

##### 2.9.3 Iteration with submatrices of vectors

We conclude this section with a description of a method often used in the following circumstances: (a) The problem is formulated as a matrix pencil; if it is of dynamical origin, we re given a non-singular symmetric stiffness matrix C of order n and a corresponding symmetric mass matrix B: the problem is to find certain modes and frequencies satisfying [UNK], x being proportional to exp [UNK] (b) the order n is large, say [UNK] (c) Interest attaches only to a relatively small number, say [UNK], of consecutive frequencies and modes, beginning with the fundamental.

The process is one of iteration with a submatrix of p vectors, where p is a little greater than the number of eigenvalues sought, and involves the solution at each step of an eigenproblem of order p only.

Since B, C derive from a mechanical system and are non-singular, they will be pos. def., and accordingly (see Theorem VIII of 1.22) the system eigenvalues are all real, finite and positive.
if we write [UNK] then the full problem may be written [UNK] where X is the modal matrix, [UNK] the spectral matrix, and A = C-1B the dynamical matrix.
It is assumed that the eigenvalues in [UNK] (and the corresponding eigenvectors in X) are so ordered that [UNK] has the eigenvalues [UNK] in descending order of magnitude down the diagonal, so that 1 [UNK] and the first vector in X define the fundamental frequency and mode.
We are not concerned to solve (1) as a whole.
If it is partitioned in the form [UNK] where Y is of order (n × p) and [UNK] square, of order p, (2) gives [UNK] and only the first of these equations concerns us.
However, we may note that (see 1.19) premultiplication by [UNK] of the first equation in (1), and transposition, shows that [UNK] are both diagonal.
For analytical purposes we may normalise X so that [UNK] which imply, inter alia, [UNK] Having set out some preliminary considerations, we now state the method.
Select a set of starting vectors Yo, arbitrary except that they must be linearly independent; then evaluate the (n × p) matrix [UNK] and use Wo to form the two square matrices of order p [UNK] Now solve the eigenproblem (any suitable method from this chapter may be used) [UNK] for its modal matrix Mo; the spectral matrix Ao which emerges is (see below) a first approximation to Ay.
Then an improved approximation to Y is [UNK] where do is an arbitrary non-singular diagonal matrix which may, for example, be used to make a homologous element in each of the corresponding columns of Y1 and Yo the same; do is useful, but not essential.
This completes one step.
The next step uses Y1 in (6) to give W1 = AY1, and the cycle of operations is repeated until convergence occurs.

We may note some interesting aspects of the method.
(i) If Yo consists of one vector only, so does Wo, and then [UNK] are scalars, s is the modal matrix [UNK].
If we choose [UNK] in (9) then [UNK] and this is the single vector iteration discussed in 2.7.1.
Moreover, the trivial eigenproblem gives a first approximation to 1 [UNK] as the Rayleigh quotient. [UNK] (ii) If Yo happens to be the correct set Y, the method makes this apparent at once, for then in view of (3) [UNK] so that, on use of (5) [UNK] Thus both matrices are diagonal, so that the eigenproblem is again trivial, having the solution [UNK].
Then [UNK] when scaled appropriately, repeats [UNK] showing that both equal Y. (iii) If Yo happens to be a set of linear combinations of the vectors in Y, the correct solution is obtained in one step.
For we may then write [UNK] where P is a square matrix of order p, non-singular since the columns of Yo and of Y, separately, are linearly independent.
Then [UNK] in view of (3).
Thus, on use of (5), [UNK] On premultiplication by [UNK], the eigenproblem (8) reduces to [UNK] which has the solution [UNK] If do is chosen as [UNK] The condition envisaged in (iii) is, in general, unlikely, unless for example a neighbour system (see Chapter 3) supplies a good approximation to Y. In most cases, we must write [UNK] where R, like Yo, is of order (n × p).
In this general case [UNK] in view of (1).
Then the eigenproblem matrices become [UNK] where (4) has been used.
We therefore have to solve for [UNK] [UNK] Knowing Mo, we now use (11) to evaluate [UNK] whence in turn we find [UNK] Since [UNK] is non-singular, we may reduce the eigenproblem based on W1 to [UNK] which we solve for the unknown [UNK].
A third step leads to [UNK] It is clear from (13), (16) and (17) that after r steps we have to solve [UNK] If [UNK] is written as M, (18) in partitioned form is (see (10)) [UNK] or, on expansion, [UNK] Now, since all the eigenvalues in [UNK] are greater than any of those in [UNK], when r is sufficiently large the terms in [UNK] become negligible compared with those in [UNK], when (19) reduces to [UNK] and if s is on-singular, this in turn reduces to [UNK] which has the solution [UNK].
This shows that convergence is complete.

Two things must be noted here.
First, although when r is large, in an overall sense the terms in [UNK] those in [UNK], yet the smallest element in [UNK] is not necessarily much larger than the largest element in [UNK].
As a result calculation of the last two or three eigenvalues in [UNK] may not be very accurate.
It is for this reason that we choose p to be a little greater than the number of eigenvalues sought.
Second, reduction of the eigenproblem to (20) requires s to be non-singular.
Now R has p linearly independent columns, and therefore also p linearly independent rows.
Thus s can be non-singular; but it is not necessarily so, and then Y as given by the method may be deficient.
For example, if the top row of s were null, the first vector in X (the fundamental mode) would be absent in the make-up of Yo, and this absence would persist.
There is no certain way of avoiding this difficulty when Yo is chosen arbitrarily; but in practice it does not often arise.
Although the eigenproblem to be solved at each step is vastly less time-consuming and expensive than direct methods applied to the full system, yet it does take much time.
However, after a few steps v, and [UNK] usually become heavily diagonal, so that Mr tends towards I; this occurs before the vectors Yr have converged.
In these circumstances, use of the Collar-Jahn method, described in Chapter 3; may greatly expedite the solution.
An example of this is given in 3.9.
Further reference to the method is also made in 8.5.

##### Example 1

The small-order example which is all we can give here does not of course do justice to the method, but at least shows how it works.
We begin with an illustration of the situation in (iii) above; the reader is invited to check the arithmetic.
Let [UNK] Then [UNK] Suppose now we are given, or choose, [UNK] It then follows that [UNK] The eigenvalues of [UNK] are thus 10 and 5 and [UNK] The reader should check that these are eigenvectors of A and that they correspond to eigenvalues 10 and 5.
We have thus obtained our solution, in this case, in one step.
It will be found that each column of [UNK] is in fact, a linear combination of the columns of [UNK]

##### Example 2

We use the same A, B, C, as in Example 1, but select as our starting vector submatrix [UNK] In choosing Yo we have selected simple vectors which are clearly linearly independent, and which between them bring all elements in A into operation in the formation of Wo.
We then find [UNK] where the product is quoted to four significant figures.
Its eigenvalues are 9.805, 2.411 and, very approximately (great accuracy is not necessary), [UNK] which yields, again approximately, [UNK] Proceeding in this way, we find at the end of the fifth step [UNK] and in the sixth step this gives [UNK] These are so nearly diagonal that the eigenproblem is trivial; the eigenvalues are 10, 4.9987.
However, we do not obtain convergence until after the 10th step, which gives eigenvalues 10, 5 and [UNK] The second columns should be{1,1,0, -1}.

##### 2.9.4 A variant

We now give a variant of the method of 2.9.3; we do so partly because the variant can save computer time, especially if may iterations are required, but also because it enables us simply to bring out certain features of the method, which lead to possible modifications.

For simplicity, we assume that the eigenvalues sought are all different.
We are given the matrices C and B, both symmetric an pos. def.
We may therefore use Choleski's method (see 2.4.2) to find a lower triangular matrix L such that [UNK], and may then evaluate [UNK], accordingly the equation [UNK] may be written [UNK] and S is symmetric and pos. def.
Now, instead of using the three matrices C, B and A = C-1B as in 2.9.3 we work only with S.

Suppose we now proceed as in 2.9.3: we begin with the submatrix Yo and successively evaluate [UNK] and we then solve for Mo the eigenproblem [UNK] Then a new approximation to Y is [UNK] At this point we may ask: what is the purpose of eigenproblem?
The answer appears if we premultiply and postmultiply Equation (5) by appropriate quantities to give since do permutes with [UNK], [UNK] on use of (6).
Transposition of (7) shows (compare 1.19) that [UNK] permutes with [UNK] and is therefore diagonal, as is [UNK].
The columns of [UNK] are thus mutually orthogonal; this is the purpose of evaluating Mo: its use orthogonalises the columns, an our ultimate objective is the orthogonal set Y.

A second step with Yo in (2) replaced by Y1, leads to the eigenproblem (compare (5)) [UNK] Again we may pause and observe that (8) gives us [UNK] directly; we do not need to find Mo first from (5) and then M1 from (8).
Thus the step (5) is unnecessary.
Then, in its turn, the step (8) is unnecessary; and so on.
Indeed, in theory all that is required is that a sufficient number of direct iterations is made, with the columns orthogonalised as the last step; in practice, however, the numbers would become increasingly ill-conditioned as S is raised to a high power and approximates to a unit rank matrix.
However, it is probably sufficient if the columns are orthogonalised at, say, every fourth iteration.

If we do this, the procedure is as follows.
Begin with Yo and evaluate successively [UNK].
At this stage, evaluate [UNK] and solve the eigenproblem [UNK] for M. Then a new approximation, which has mutually orthogonal columns, is [UNK], with which in place of Yo the cycle is repeated, and so on.

##### Example 1

We use the same matrices B and C as in Example 2.9.3.1. then, if [UNK], [UNK], we find, to four decimal places, [UNK] [UNK] As our starting matrix we choose [UNK] This has mutually orthogonal columns; however, as we shall see later, it is not a good initial choice for the first column.
We ow form [UNK], at each stage making the "11" and "22" elements unity.
We find [UNK] we require [UNK] as it stands.
We now form v, [UNK] as in (9), (10), and solve (11) for M. To sufficient accuracy, we find [UNK] and then a new Yo is, with d chosen appropriately, [UNK] and it may be checked that these two columns are, sufficiently nearly, orthogonal.
We now repeat the cycle.
This time we find [UNK] and [UNK] and again, sufficiently nearly, the columns are orthogonal.
A third cycle leads to the eigenvectors (and eigenvalues) of S: [UNK] We leave it to the reader to establish that the eigenvectors of the original system, given by premultiplication of w by [UNK] may be written [UNK]

#### 2.10 IMPROVEMENT OF THE ACCURACY OF EIGENVALUES AND VECTORS

It frequently happens, both in dynamical problems and in other eigenvalue problems that we have approximate values for one or more eigenvalues (and perhaps vectors) and require to obtain more exact values.
This problem, from another viewpoint, is discussed more fully in Chapter 3.
Here we shall deal only with some simple cases.

##### 2.10.1 Problem formulated as a matrix pencil

For simplicity, let us first discuss the undamped oscillations of a mechanical system having n degrees of freedom, the equations of motion of which have been derived by Lagrangian methods from energy considerations; they will appear, in the usual notation of dynamics, as [UNK] Here x is the column of coordinates; in what follows, we assume the last element x to be non-nodal (if it is not, it can be made so by rewriting the equations in a different order).
Also C, the inertia matrix, will be symmetric and pos. def. and B, the stiffness matrix, also symmetric and non-neg. def; finally, F is a column of applied forcing functions.
In simple harmonic motion, these forces, and x, will be proportional to exp [UNK] and if we then write [UNK] for{go} 2, (1) reduces to the usual formula [UNK].
We observe that, in addition to the given matrices C and B, (2) contains 2n + 1 other quantities, viz. λ, x, and F. Since we have n equations, we can determine any n of these quantities in terms of the remaining n + 1, to which we can ascribe arbitrary values.
Here, we shall

(a) choose λ as an independent variable;

(b) prescribe the value unity for [UNK];

(c) prescribe the value zero for each of the first n -1 functions in F, the last being written f.

Then f and the coordinates [UNK] become functions of λ, and we note that when f vanishes (i.e. all the functions F vanish in (2)), λ will be an eigenvalue and [UNK] the corresponding eigenvector.

We not write, in partitioned form, [UNK], [UNK], and, since the pencil in (2) is symmetric, [UNK], where [UNK] is a square submatrix of K of order n = 1.
Then (2) becomes [UNK], which yields, progressively, [UNK], [UNK].
Since the submatrices in (5) are all functions of λ, (7) and (8) give f and ξ (or x) as functions of λ.

Now suppose we have an approximation [UNK] to an eigenvalue.
Since f is a function of λ which vanishes at the eigenvalues, we may use it in the Newton-Raphson method to obtain an improved approximation [UNK]: [UNK], the zero suffixes indicating that the functions are calculated for [UNK].
Equation (8) is not suitable for differentiation; instead, we obtain another form for f by premultiplying (6) by [UNK]; we obtain [UNK], and since K is symmetric it follows that [UNK], which, with K given by (5), reduces to [UNK].
In a numerical calculation, we use (11) for [UNK] and either (8) or (10) for f.
If we use the latter, we must note that, at [UNK], [UNK], when Equation (9) reduces to [UNK], i.e. the well-known Rayleigh quotient.
In the numerical evaluation of this, we obtain x from (7) with [UNK].
Having obtained [UNK] we can adopt it as a new [UNK] and repeat the cycle of approximation, which is known to be quadratically convergent: i.e. if [UNK] is the true eigenvalue, then for small differences [UNK].

Equation (9), with [UNK] given by (8), is analytically precisely equivalent to (12).
In numerical applications, they may differ, depending on the accuracy with which [UNK] and ξ are evaluated.
Probably (12) is the user to use.

##### Example 1

In Equation (1), let [UNK].
Suppose we are given an approximate eigenvalue [UNK].
We evaluate [UNK], which we have partitioned as in (5).
Then ξ is given by (7) as [UNK], and the reader may check that this yields [UNK].
We give this to four decimal places only: it is not necessary to calculate ξ to great accuracy, but once found, it must be used consistently, and calculations made accurately.

We deduce that for [UNK], the approximate eigenvector is [UNK], and we are able to calculate [UNK], [UNK], whence [UNK].

If we round this off to a new [UNK], we quickly find that [UNK] also, i.e. 40 is an exact eigenvalue; also the corresponding eigenvector becomes [UNK].

If, instead of the Rayleigh quotient, we use (9) directly, we require from (8) [UNK].
Hence (see also (16)) [UNK], in close agreement with (16).

##### Problem formulated in terms of a single matrix

If we premultiply (2.10.1.2) by [UNK] and write [UNK], we obtain the problem in terms of the characteristic matrix of A: [UNK].
Note that here A is, in general, not symmetric; however, it evidently possesses the same eigenvalues as the system (2.10.1.2).

Let us now abandon the connection with a mechanical system, and treat this as a problem involving any given real matrix A, the eigenvalues and vectors for which have to be found.
The treatment is closely similar to that of §2.10.1.

As before, we choose λ as an independent variable, assign the value unity to [UNK] and zeros to the first n -1 elements of G: [UNK]; we also write, remembering that A is not symmetric, [UNK].
Then Equation (2) gives us [UNK], from which we obtain as before [UNK], [UNK].

We now look for the left vector [UNK] corresponding to x as the right vector; in §2.10.1 this was [UNK]: here it is different.
In place of (2) we write [UNK]; by the same argument as before, we set [UNK], [UNK], hence from (4), (9) and (10) [UNK], yielding [UNK], [UNK], and on comparison of (12) with (7) we see that h and g are identical; this is not surprising, since they are evidently similar functions and have the same zeros, i.e. the eigenvalues.

As before, we now employ g in a Newton-Raphson application to improve the accuracy of any given approximate eigenvalue [UNK].
Premultiplication of (5) by [UNK] gives [UNK], and then, differentiating term by term, we have [UNK], which in view of (4) reduces to [UNK].
Accordingly, as before [UNK].
This is the parallel to (2.10.1.12); as before, we can, if we wish, use g as given by (7) for alternative treatment, but we shall not pursue this here.

##### Example 1

In (2), let [UNK].
This matrix is, in fact, obtained from our previous example by evaluating [UNK].
However, we shall treat a different eigenvalue: suppose we are told that there is an eigenvalue in the neighbourhood of [UNK].
We evaluate and partition [UNK].
Then we find at once from (6) and (11) that [UNK], [UNK], and hence, from (15), [UNK].

If we round this off to a new [UNK], and repeat the calculation - we leave it to the reader to check this - we find [UNK]; finally, rounding this off to 20 and repeating again, we find that 20 is an exact eigenvalue and that the corresponding right and left eigenvectors are, respectively, [UNK], [UNK].

##### 2.10.3 Factorisation of A into two symmetric matrices

In Equation (2.10.2.1) we derived A as the product of two given symmetric matrices, [UNK] and B; this was done for convenience in the examples.
For completeness, we interpolate here a brief discussion of the reverse procedure: it was shown in §1.19 and Theorem V of §1.22 that a matrix can always be factorised into two symmetric matrices, but the subject was not pursued there.
Here we obtain the most general solution.

We first continue the discussion of §1.19, and treat the most common case in which A has distinct eigenvalues.
It was shown there that A permutes with [UNK], which is therefore diagonal.
This diagonal matrix, D, is arbitrary, since X is arbitrary to a postmultiplying diagonal matrix.
Write [UNK] where P, Q, R,... are arbitrary.
Now if (see §1.18) we write [UNK], C may now be expressed as [UNK], so that C is expressible as an arbitrary linear sum of the n symmetric unit rank matrices [UNK].

Next consider the case where A has two equal eigenvalues α, but is not defective.
Then A can be written with the (2 × 2) scalar submatrix αI in the leading diagonal position.
This means that D is not necessarily diagonal; corresponding to αI there may be a (2 × 2) block which is arbitrary except that it must be symmetric and non-singular.
This therefore contains three arbitrary quantities, giving n + 1 in all.

Finally, suppose A has two equal eigenvalues α but is defective.
As previously, we note that [UNK] since [UNK] is symmetric.
Accordingly [UNK] with K as defined in Theorem V of §1.22.
Thus [UNK] permutes with [UNK].
This implies that [UNK] is diagonal except for the leading (2 × 2) submatrix.
Now the following submatrices permute (see also §1.21) [UNK], [UNK], where a, b are arbitrary.
The second of these is thus the leading submatrix of [UNK], whence in [UNK] it is [UNK], which is symmetric and contains just two arbitrary quantities; there are thus just n arbitrary quantities in all.

Extension to more complicated cases is not difficult.
However, these studies employ the modal and spectral matrices, and in practice these may not be known.
We can, however, find directly the general solution of [UNK].
Write [UNK], so that C contains n (n + 1) /2 unknown elements, n in the diagonal, viz. p, q, r,..., and n (n -1) /2 elsewhere, viz. a, b, c....
Now the conditions that B is symmetric provide just n (n -1) /2 linear algebraic equations connecting the unknowns, so that we can determine a, b, c,... in terms of p, q, r... which are arbitrary.
The procedure is best illustrated by means of a numerical example: we choose A to be the matrix of (2.10.2.16).
Then [UNK].
Then the condition that [UNK], for example, leads to [UNK], and there are five other such equations.
We set them out thus: [UNK] These are then solved, e.g. by direct operation on rows, when a, b, c,... emerge as quantities linear in p, q, r, s.

To set out the result compactly, we write [UNK], where [UNK]... have zero diagonals except for a unit in the first, second,... place respectively.
In this example, we can write [UNK], where to keep the elements numerically simple, we have extracted the factor 1/3 from [UNK] and [UNK].
This is evidently the most general form of C. Postmultiplication by A yields B in the form [UNK].

When p, q, r, s are assigned numerically, C and B are known and then the factors [UNK] and B of A are found.
We can recover the matrix C (and also B) defined in (2.10.1.13) by assigning to p, q, r, s the values 1, 1.52, 3, 0.92 appearing in the diagonal of C.

The following characteristics of [UNK], [UNK], etc. are to be noted.
First, since each contains zeros in its diagonal, it cannot be pos. def.
Next, the ranks of the matrices do not conform to any simple pattern: [UNK] is of rank 4, [UNK] and [UNK] of rank 3 and [UNK] of rank 2.
Finally, in relation to our main problem, since for the Rayleigh quotient (which gives eigenvalues identical to those of A) [UNK], and since also p, q, r, s are arbitrary, it follows that [UNK], i = 1,2,3,4, though this result is not particularly helpful in practice.

##### 2.10.4 Another method for improvement of eigenvalues

We discuss here the same problem as that in §2.10.2, but vary the treatment.
The eigenvalues are determined by Equation (2.10.2.5) with g = 0, viz. [UNK], where α is the submatrix of A corresponding to [UNK], and [UNK] is the last diagonal element in A. From this we find [UNK], [UNK], and elimination of ξ leads to the equation for λ [UNK].

This equation is not easy to solve numerically as it stands; however, if we are given an approximation [UNK] to an eigenvalue, we write [UNK] for the exact eigenvalue, which therefore satisfies (4), so that we obtain [UNK], which is now an equation for ε Write [UNK] then [UNK].
Thus [UNK], provided ε is sufficiently small.
Insertion in (5) leads to [UNK], or, if [UNK], [UNK], [UNK], etc., [UNK].
Finally, if [UNK] is written [UNK], we obtain the scalar equation [UNK].
Provided the series converges, this may be solved for ε in any suitable way; often a regression procedure, beginning with ε = 0 on the right-hand side to give a new approximation on the left, will solve the equation in two or three steps.

Comparison of (8) with (3) shows that, when ε has been found from (9) [UNK], so that both eigenvalue and vector are found.

##### Example 1

Once again, we use the matrix specified in Equation (2.10.2.16) and we are given that it has an eigenvalue near [UNK].
Then, in (6), with n=4, [UNK].
Also, [UNK]; [UNK]; [UNK];.
Hence, using (7), we obtain [UNK], [UNK], [UNK], [UNK], [UNK], and it is in fact unnecessary to proceed further.
We now evaluate the scalars [UNK]; they become [UNK], [UNK], [UNK], [UNK], [UNK].
Hence Equation (9), for ε, becomes [UNK], and if we collect the linear terms and rationalise: [UNK] and solution of this, by regression or otherwise, gives [UNK]; [UNK].
Also, using (10) with [UNK], we find [UNK] or [UNK].

