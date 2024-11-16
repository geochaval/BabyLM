# Lectures on electromagnetic theory

## 1. Maxwell's equations

> One of the chief peculiarities of this treatise is the doctrine which asserts, that the true electric current on which the electromagnetic phenomena depend, is not the same thing as the current of conduction, but that the time variation of the electric displacement must be taken into account in estimating the total movement of electricity.

ALL the problems we shall be concerned with may be solved by calling upon one or more of the following equations: [UNK].

Where do the above equations come from?
They are contained (though not quite in the same form and not in the same system of units) in Chapter IX of Maxwell's Treatise on electricity and magnetism published in 1873.

Are we to conclude that electromagnetic theory has made no advance in the course of a century?
That conclusion would essentially be correct.
Our technique of solving the above equations has improved, and of course we are in a much better position now to evaluate the material constants, but fundamentally electromagnetic theory stands now as it stood a century ago.
As far as the interrelationship of electromagnetic quantities is concerned Maxwell knew as much as we do today.
He did not actually suggest communication between continents with the aid of geostationary satellites, but if he was taken now to a satellite ground-station he would not be numbed with astonishment.
If we would give him half an hour to get over the shock of his resurrection he would quietly sit down with a piece of paper (the back of a bigger envelope, I suppose) and would work out the relevant design formulae.

The lack of advance on our part should not be attributed to the idleness of a century, much rather to the genius of Maxwell.
The moment he conceived the idea of the displacement current, a new era started in the history of mankind.
Events of similar importance did not occur often.
Newton's Principia and Einstein's first paper on relativity would qualify, and perhaps two or three more learned papers, but that's about all.
If we assume that our kind of beings will still be around a few millennia hence, I feel certain that the nineteenth century will mainly be remembered as the century when Maxwell formulated his equations.

What was so extraordinary about Maxwell's contribution?
It was the first (and may be the best) example of reaching a synthesis on the basis of experimental evidence, mathematical intuition, and prophetic insight.
The term [UNK] (1.1) had no experimental basis at the time.
By adding this new term to the known equations he managed to describe all macroscopic electromagnetic phenomena.
And when relativity came, Newton's equations were found wanting but not Maxwell's; they needed no relativistic correction.

I could go on for a long time in praise of Maxwell.
Unfortunately we have little time for digressions however entertaining they might be.
But before we get down to the equations I must say a few words in defence of the approach I choose.
I know it must be hard for anyone to accept a set of equations without going through the usual routine of presenting the relevant experimental justifications.
It might seem a little unreasonable at first sight but believe me this is a possible approach, and under the circumstances it may very well be the best approach.
You are already familiar with the mathematical operations curl, div, and grad (I prefer using them in vector-operator form), and you need no introduction to the concepts of electricity.
You have heard about electric charge, current, magnetic field, etc.
All the eqns (1.1) - (1.7) do is go give a number of relationships between these quantities.
So if some of them are known, you can use the equations to work out some of the others.

The notation is fairly standard but still I should better say what is what: H, magnetic field strength; E, electric field strength; D, electric flux density; B, magnetic flux density; J, current density; p, charge density; F, force, q, charge; v, velocity of moving charge; u, permeability; e, permittivity.
The two latter quantities are constants depending on the material under study.
Using the subscript zero to denote their values in free space, they come to [UNK].

The rest of the course will be concerned with the various solutions of eqns (1.1) - (1.7).
Isn't this boring for an engineer?
Shouldn't this be done by mathematicians or by computer programmers?
Not for the time being.
Perhaps one day computers will be big enough and numerical analysts clever enough so that the engineer will only have to pose the problem, but not yet, and not, I think, for some time to come.

In the large majority of cases a straightforward mathematical solution is just out of the question.
So one has to use that delicate substance known as physical intuition.
How can one acquire physical intuition?
There is no easy way.
One has to start with a simple physical configuration, solve the corresponding mathematical problem, then solve a similar problem and then another problem, and then a little more difficult problem, and soon.
The first breakthrough comes when one can predict a solution without actually doing the mathematics.

In order to have a unified view of the subject we have started with Maxwell's equations.
It means a new approach but not a radical departure.
The subject is still the same.
You will be able to see that the laws you love and cherish (Coulomb's, Biot-Savart's, Snell's, etc.) all follow from our eqns (1.1) - (1.7).

The order of discussion will follow the traditional one: electrostatics first, followed by steady currents, then we shall move on to slowly varying phenomena, and reach finally the most interesting part, fast-varying phenomena, exhibiting the full beauty of Maxwell's wonderful equations.

## 2. Electrostatics

2.1.
Introduction

STATIC means not varying as a function of time.
So all our quantities p, J, E, B, D, and H will be independent of time.
Is there such a thing as time-independent charge?
Yes, there is.
It means that neither the magnitude nor the position of the charge varies as a function of time.
And similarly we can imagine constant electric and magnetic fields.
Can we talk of time-independent current?
Well, we have to permit the motion of charges to get any current but if the amount of charge crossing a certain cross-section is always the same then the current at that point is independent of time.
On this basis constant currents also belong to the static branch of electricity.
It is, though, usual to distinguish between electrostatics and magnetostatics; in the former case the variables are p, E, and D, whereas in the latter case they are J, H, and B.

We shall now proceed with the equations of electrostatics, which may be obtained from eqns (1.1) - (1.7) by substituting a/at = 0 and assuming that v, J, H, and B are all zero.
We get then [UNK].

We shall introduce now a scalar function by the relationship [UNK].
The physical significance of this new function may be recognized by determining the work performed by carrying a charge from point a to point b: [UNK], where the negative sign is due to the fact that the work is done against the electrical forces.
Substituting eqns (2.4) and (2.5) into eqn (2.6) we get [UNK], where [UNK] and [UNK] are the values of the function [UNK] at the end-points of the path.
We have used here a mathematical theorem stating that the line integral of a gradient depends only on the end-points and not on the connecting path.
The potential at point b may be written with the aid of eqn (2.7) in the form [UNK].
Alternatively, we may choose [UNK], leading to [UNK].

What is the good of introducing [UNK]?
I. Owing to its scalar character it is more easily calculable than the electric field.
Thus very often in practice we determine [UNK] first and E afterwards, 2.
The choice of [UNK] in the form of eqn (2.5) immediately ensures that eqn (2.1) is satisfied: [UNK], so we have less to worry about.

If the potential function is so useful shouldn't we express all our equations in terms of [UNK]?
Yes, in fact this is what other people did in the past.
So let us convert eqn (2.2) as well.
Noting that [UNK], we obtain [UNK], which is known as Poisson's equation.
If p=0, the above equation reduces to [UNK].
This equation is known after another Frenchman as Laplace's equation.

We have not quite finished.
There is one more equation often used in electrostatics that contains charge and not charge density.
We can get it by integrating eqn (2.2) over a volume [UNK].
Using Gauss' theorem for the left-hand side and noting that the volume integral of charge density is just the total amount of charge, eqn (2.14) takes the form [UNK], where S is the closed surface of volume and q is the charge inside.
Eqn (2.15) is known as Gauss's law.

2.2.
Coulomb's law

Having got the equations what shall we do with them?
Let us first try to prove something that you have come across in school, Coulomb's law.
Note the difference.
We shall not postulate Coulomb's law, we are going to derive it.

We shall have to introduce point charges, but let us be a little more general to begin with and assume that the charge is uniformly distributed within a sphere of radius r0.
We shall now apply Gauss' law and take the surface of integration at a radius [UNK].
Notice that everything is spherically symmetric, hence D must be constant on the chosen surface, and the integral comes to [UNK], where D=|D|.

In view of eqns (2.15) and (2.16) [UNK] or, in a vacuum, [UNK].
Interestingly, the electric field does not depend on the actual positions of the charges.
As long as the charge distribution is spherically symmetric, and as long as all the charges are inside the sphere of radius r0 the electric field depends only on r and not on r0.
So we can just as well imagine that all the charge is concentrated at the origin of the coordinate system.

Let us place now another bunch of charge (say q2) into another discrete point a distance r12 away from our first charge that we will now denote by q1.
With the aid of eqn (2.4) we get for the force upon [UNK], and substituting for E from eqn (2.18) we obtain [UNK].
In words: the force between two charges at rest is proportional to the product of the charges and inversely proportional to the square of the distance between them.
The direction of the force is obvious, it can only act in the line connecting the two point charges.
So we have got Coulomb's law.

2.3.
The potential due to charges

The potential due to a point charge may be determined with the aid of eqns (2.8) and (2.18), as follows: [UNK].

The usual convention is to choose the reference point at infinity and choose the corresponding potential (a) = 0, so we get for the potential of a point charge [UNK].

If we have a number of point charges q1, q2..., qn at distances r1, r2..., rn from the point where we wish to evaluate the potential then we can simply add all the potentials, leading to [UNK].

If instead of point charges we have a distributed space charge p (x', y', z') then the sum in eqn (2.23) goes over into an integral: [UNK], where r is now the distance between the elementary charge [UNK] located at point (x', y', z') and the point (x, y, z) where the potential is evaluated.

The formulae look quite reasonable; what you need is a little practice in handling them.
But as I said before the game is not a purely mathematical one; it is a mixture of physics and mathematics, a combination of intuition and technique.
So before we embark upon solving concrete examples let us turn to a graphical illustration of the electric field.

We shall introduce field lines defined by the statement that at each point on the line the tangent is in the direction of the electric field.
The magnitude of the electric field may be represented at the same time by the density of field lines.
The nearer they are to each other the greater is the field.

A particularly simple example is provided by a point charge.
The electric field is always in the radial direction, so the field lines are just straight lines as shown in Fig. 2.2.
According to convention the arrows on the lines point outwards from a positive point charge.

[UNK] Owing to radial symmetry the potential is constant on a spherical surface at a distance r from the point charge.
Some of these equipotential surfaces are shown in Fig. 2.2 with dotted lines.
Notice that the field lines are perpendicular to the equipotential surfaces.
This is of course no coincidence.
The gradient of a scalar function is a vector perpendicular to the [UNK] constant surface and points in the direction of increasing values of [UNK].
Since [UNK] and in the present case q>0, we find that [UNK] decreases with increasing r.
Hence the vector [UNK] points inwards and [UNK] points outwards.
So the whole picture is consistent.

Having completed the calculations for the potential of a point charge, we shall now investigate a more complicated situation.
Yes, you guessed correctly, we are going to investigate the equipotential surfaces and field lines of two point charges.

In view of eqn (2.23) the potential due to two point charges may be written as [UNK], which for the coordinate system of Fig. 2.3 reduces to [UNK].

The equipotential surfaces may now be plotted on the basis of the above equation and then the field lines may be obtained as trajectories orthogonal [UNK] to the equipotentials.
This is simple in principle but extremely messy and tedious if you want to solve it analytically.
The best method nowadays, of course, is to put it on the computer and let the computer plot the lot.
For q2=-q1 the plot in the x, y plane is shown in Fig. 2.4.

If you look at the Figure and study it carefully you will be able to recognize a number of "commonsense" points.
It is common sense once you see the solution but it is unlikely that you would have thought of all of them a priori.
For example,

1.
all the field lines originate on the positive charge and terminate on the negative charge;

2. the potential is zero on the y=0 plane;

3. one of the field lines coincides with part of the y axis connecting the two charges.

4.
The x=0 and y=0 planes are planes of symmetry.

5.
The equipotential lines become more and more similar to circles as they get nearer to either charge.

6.
Just behind the charges the effect of the opposite charge is minimal so the field lines resemble those of an isolated charge.

The better you grasp the salient points (and store them in your memory), the more physical intuition and predictive power you will acquire.
Shouldn't one rely solely on mathematics?
Physical intuition might provide part of the answer, but surely mathematics will always give the complete answer.
This is true for simple problems but, as I have said many times before, as soon as the [UNK] problems become more complicated our mathematical knowledge turns out to be greatly deficient.

In practice you will find that problems may be broadly divided into two classes: (I) problems that have been solved, and (II) problems that are insoluble.
The reasons for belonging into class II may be numerous: you cannot formulate the problem, you cannot solve the resulting equations analytically, the computer you have access to is not big enough, etc., etc.
It all boils down to the fact that the problem needs to be simplified.
You will find that you never solve the original problem.
At best you solve a similar one.
But how can you recognize a "similar" problem?
Which simplifications are admissible without losing the essential characteristics of the problem?
For all that you need intuition.

The electric dipole

One often goes to extremes in order to arrive at a physical configuration that is mathematically soluble by simple means.
This is what we are going to do now and besides assuming that q=q1=-q2 we will also state that the two opposite charges are infinitesimally close to each other.
Is such a situation entirely fictitious?
No, it can occur in practice.
But surely, two charges will never be infinitesimally close to each other.
Of course not, all I mean is that the distance between the charges is very small with respect to some other distance of interest.
For example, the two charges may be of some atomic distance (of the order of 10 -10 m) apart, whereas we are interested in their effect at macroscopic distances; or take the so-called dipole aerial where the assumed separation of charges is small in comparison with the wavelength of oscillation.
We shall return to the latter, time-varying problem in Section 5.16; let us first solve here the static case.

If we are considering distances far away from the origin of Fig. 2.3, i.e. [UNK], using the approximation [UNK] we obtain with which eqn (2.26) reduces to [UNK].

The product qd is called the electric dipole moment, and we shall denote it by pe.
We shall also introduce a vector pe=qd, where d is the vector connecting the two point charges located at [UNK].
By definition the vector points from the negative to the positive charge.
With the aid of this vector we can replace [UNK] by [UNK] where [UNK] is the unit vector in the direction of point P at a radius r.
So we may write eqn (2.30) in the form [UNK].

Yet another alternative form is obtained by using spherical coordinates [UNK] in which [UNK] appears as [UNK].
[UNK] The above form is probably best suited for deriving the components of the electric field.
Using the formulae (A - 11 and 14) for the gradient in spherical coordinates, we get [UNK].

"The potential far away from the charges

If the charges are within a finite volume and we wish to determine the potential at a point P, far away from this volume, the formula we have obtained before (eqn (2.23)) may be simplified.

We shall assume (Fig. 2.6) that the vectors drawn from any point charge to point P are all parallel to the vector r0 drawn from an arbitrarily chosen origin inside (just another way of saying that the point P is far away).
This is a technique often used that leads to a quick and simple answer.
We may then express the individual distances as [UNK], where di is the vector giving the position of charge qi.
With the aid of the above relation we get [UNK], which substituted into eqn (2.23) yields [UNK].
Thus we have a contribution depending on the total charge, and a second term bearing strong resemblance to our dipole formulae.
Since the second term decays as 1/r2, could it ever become important?
Yes, for many charge distributions of practical interest the net charge is zero, so the first term disappears and the second term acquires significance.

For two charges of opposite sign eqn (2.36) reduces to eqn (2.31); we just have the dipole potential previously derived.
For a large number of charges we sum up the contribution of each dipole moment.

Multipoles

Why stop at dipoles?
Could we have higher-order moments as well?
The answer is yes, but the mathematics gets more and more tedious.
A not-too-difficult example is a special sort of quadrupole (two dipoles of equal dipole moment and of opposite directions arranged axially) shown in Fig. 2.7.
Then [UNK] eqn (2.36) would give zero and we need better approximations for ri.
If you are good at expanding functions up to second order you might like to attempt Example 2.5.

2.4 The electric field due to a line charge

Let us take as an example an infinitely long, infinitely thin distribution of charges as shown in Fig. 2.8.
Let us further assume that the charge distribution is uniform and denote the charge per unit length by pl (we are defining thereby a linear charge density of dimension coulomb per metre).
[UNK] Our aim is to determine the electric field.
One possible method is to work out the electric field due to a point charge pi dz located at z and then add the field due to all the other point charges present.
We obtain then for the electric field at the coordinate R, [UNK], where [UNK] is the unit vector in the direction of the r vector.
Owing to symmetry considerations (there is the same infinite amount of charge in the region [UNK] as in the corresponding region [UNK]) the electric field can have no component in the z direction, so we need only to worry about the radial component.
This we may obtain easily from Fig. 2.8 as follows [UNK].
It is preferable to do the integration for θ so we shall rewrite eqn (2.38) with the aid of the relation [UNK] in the form [UNK], which may be integrated between the limits θ=-; π/2; and θ=; π/2; to yield [UNK].
This formula tells us a lot and in simple language too.
The only surviving component of the electric field varies inversely with the distance from the line charge and it is independent of the coordinate.
Remember, for a point charge the electric field varies with the inverse square of the distance, but it is just inverse distance for the line charge.
Why is this worth remembering?
Because the relationships are simple, they will not considerably burden your memory, and at the same time will assist you in building up your intuitive picture.

Take now a finite line charge as shown in Fig. 2.9 (a) and (b) using different scales.
Can you answer the question what is the relative strength of the [UNK] electric field at points N and M in Fig. 2.9 (a) and at points Q and P in Fig. 2.9 (b)?
To be concrete let us take [UNK].
It looks from points N and M as if the linear charge distribution would be very long indeed, perhaps infinitely long.
Thus the electric field distribution may be expected to follow a (distance) -1 law.
Hence En/Em=½.
Looking from points Q and P the linear charge distribution between z=-H and z=H appears more like a point charge concentrated at 0.
Thus the electric field distribution may be expected to follow a (distance) -2 law.
Hence Eq/Ep=¼.
We have now been able to give immediate answers to fairly complicated questions.
How good are the approximations?
Derive the exact formula for the electric field, work out its values at points M, N, P, Q, take the ratios, and see for yourself how good our approximations are.

Let us solve now the same problem by another method.
Instead of calculating the electric field directly from the charge distribution let us first determine the potential and obtain the electric field by differentiation.
This is surely the better method because we won't worry about vectors when doing the integration.
In order to avoid a lot of painful algebra we shall further simplify the problem and work out the potential for [UNK].

The potential of a point charge is given by eqn (2.22), and that of a charge distribution by eqn (2.24).
Whichever we use we end up with the following integration for the potential of an infinite line charge: [UNK].
All we need to do now is to put in the limits, but alas [UNK].
We get the result that the potential at point P is infinitely large.
Have we done something wrong?
No, we have done the same thing as before with the only difference that we calculated the potential instead of the electric field.
Where could the trouble lie?
Surely, in the infinite nature of our line source.
There are no infinitely long line charges in nature.
We have taken an unphysical picture and we get a nonsensical answer.
But why did we get a reasonable result for the electric field?
That was calculated for an infinitely long line charge too.
Well, sometimes you get away with it, sometimes you don't.
Why?
The cause is only known to mathematicians and philosophers constantly engaged in the study of infinity.
What can an ordinary physicist or engineer do?
Well, there are several avenues open.
Number one is to acknowledge the fact that our line charge is not infinitely long, integrate between the limits -H and +H, differentiate to obtain the electric field, and let then H go to infinity.
Then if there is any justice on earth, we shall arrive at eqn (2.41).
The other thing we can do is to retrace our steps leading to eqn (2.22).
We need to go only as far as eqn (2.21).
We may see then that we chose our reference point at infinity.
Perhaps there is the rub.
We may have tampered too much with infinity.
Let us abandon that assumption and see what happens.
Thus we are going to say that (a) = 0 at some other point.
It probably matters little where we choose that point as long as it is not at infinity.
So let us choose it for convenience at z = 0 at a distance R0 from the line charge as shown in Fig. 2.10.
Then the potential at P due to a point charge at z is [UNK], and the potential due to the infinite line charge [UNK].

Our attempts at determining both the electric field strength and the potential have started with considering the effect of a single point charge and have been followed by an integration for obtaining the total effect of the infinitely long line charge.
Is there another, more direct way of determining the electric field?
Well, there is Gauss's law, we haven't tried using that.
If the line charge is infinitely long (so that the field depends on the radius only) we can choose our Gaussian surface as a cylinder wrapped round the line charge (Fig. 2.11).
By relying on circular symmetry we can further claim that the electric field will have only a radial component which means that [UNK], where [UNK] is the azimuth angle in the cylindrical coordinate system.
The application of Gauss's law (eqn (2.15)) leads then to [UNK].
Performing the integration in the z direction for any finite length, we get for the electric field strength [UNK] in agreement with eqn (2.41).

The potential may be obtained from the electric field as [UNK].
It appears that the application of Gauss's law leads much more quickly to the required result.

What is the moral of the story? (i) Tamper with infinity at your own peril, and (ii) Some ways of solving a problem are easier than others.

2.5.
The electric field due to a sheet of charge

We shall now investigate the case when the charge is uniformly distributed over a plane (the x, y plane in Fig. 2.12).
The charge extends to an [UNK] infinitesimal distance in the z direction so we shall call it a surface charge.
To be consistent with our previous notation for a line charge we shall denote it by ps (dimension coulomb m-2).

The only component of the electric field is in the z direction (the others must be zero by symmetry considerations).
If the sheet consists of positive charge the electric field points outwards.
Since the space to the right of the charged sheet looks the same as that to the left, the magnitude of the electric field will be the same at z=a and z=-a.

Learning from our meandering in the previous section we shall start straight away with Gauss's law.
Choosing our surface as the box of Fig.2.13 we get [UNK].
There is no contribution from the side surfaces because the scalar product E.dS vanishes.
The total charge enclosed is [UNK], hence [UNK].
The electric field is a constant everywhere in space but is of different sign on the two sides of the sheet.

Let us put now a sheet of opposite charge a distance d away from the first sheet (fig. 2.14).
Then the electric fields due to the two sheets add in between the sheets [UNK], and cancel outside the sheets [UNK].
The equipotential surfaces are obviously planes.
We get, by integrating eqn (2.54), [UNK].

2.6.
The parallel-plate capacitor

We have so far considered point charges, dipoles, line charges, and sheet charges without enquiring into the problem how such configurations of charges come about.
Indeed if one gives a little thought to the matter it becomes distinctly doubtful that one could ever establish anything even vaguely resembling a sheet of charge.
Like charges repel each other so the charges constituting the sheet will fly apart.
Interestingly, there is a way of realizing sheets of charges.
We just need to apply a voltage between two metal plates.

What happens inside metal plates in response to an applied potential or for that matter what happens to charges inside any material?

There is no escape; I have to say a few words about the properties of materials.
A piece of material contains equal number of positive and negative charges.
If this was not so there would be large forces between various pieces of materials.
To give you a feeling how large these forces could be I quote from Feynman's lectures: "If you were standing at arm's length from someone and each of you had one per cent more electrons than protons, the repelling force would be incredible.
How great?
Enough to lift the Empire State Building?
No!
To lift Mount Everest?
No!
The repulsion would be enough to lift a "weight" equal to that of the entire earth!"
So as I said before a piece of material contains equal numbers of positive and negative charges.
For a class of materials called conductors the internal charge distribution may be looked upon as a cloud of mobile negative particles in the background of immobile positive lattice ions.
When the voltage is applied, there is initially an electric field inside the conductor and the charges start to move under its influence.
So to begin with this is not a static problem at all.
But if we wait patiently for a few picoseconds until the charges rearrange themselves there will be no further motion and the problem belongs to the realm of electrostatics.
But where will the electrons find their equilibrium positions?
How far will they move under the influence of an attractive electric field?
Disregarding the cases when the electric field is very large or the conductor is very hot (beyond the scope of this course) the electrons cannot get farther than the boundary of the conductor.
So there will be an accumulation of electrons on the surface of one of the plates and consequently a deficiency of electrons at the other plate's surface.
Inside the conductor there will be no imbalance of charge.
This is an important thing to remember.
If we apply a constant voltage then, after the elapse of a short time, charge neutrality is re-established in the interior of the conductor but there will be some uncompensated charges in the immediate vicinity of the surfaces.
How close to the surfaces?
It doesn't really matter.
The scales are certainly atomic, so we are entitled to regard these charges at the surfaces as having spread out in two dimensions only.
So the introduction of a surface charge is not unrealistic at all.

Well then, two infinitely large metal plates to which a constant voltage is applied are equivalent to two oppositely charged sheets.
The electric field between the plates is then [UNK], and the potential [UNK].

Consequently the potential difference (i.e. the voltage) between the plates comes to [UNK].

Next let us work out the capacitance per unit surface area.
Recall the definition from circuit theory: the capacitance is the proportionality factor relating the charge stored on one of the plates to the applied voltage, i.e. [UNK].

The total charge per unit surface area is ps, which leads to the following formula for the capacitance per unit surface area: [UNK].

We shall keep now the voltage constant and insert a piece of dielectric between the plates as shown in Fig. 2.15.
What sort of difference will that make?
Since the voltage is the same and the dielectric is homogeneous the electric field is still given by [UNK].
The flux density, on the other hand, will be different on account of the [UNK] relationship.
What about the surface-charge density?
That will also increase by the same factor Er.
In fact the surface-charge density will [UNK] be equal to D. We can easily provide the proof by choosing a Gaussian surface as shown in Fig. 2.15.
The contribution of S- to the integral is now zero (because both E and D are zero inside the conductor) and that of S+ comes to [UNK].
Hence the application of Gauss's law yields [UNK] or [UNK].
So we have proved that the surface-charge density increases by a factor Er.
Why?
This is a problem that rightfully belongs to the subject of the electrical properties of materials, so I cannot say very much about it.

In a perfect dielectric there are no mobile charges but lots of bound charges, positive and negative.
In response to the electric field in which these charges find themselves, the positive and negative charges will slightly separate.
The effect will be some uncompensated charges at the edge of the dielectric (Fig. 2.16) which will draw some further charges of the opposite sign from the interior of the conductor to its surface.
This is the physical mechanism responsible for the increase of surface charge density in the presence of a dielectric.

Haven't we made a mistake?
When working out the total charge within the Gaussian surface (the right-hand side of eqn (2.63 we ignored the [UNK] charge density on the surface of the dielectric.
Surely, we should have taken that into account.
What counts is the net surface-charge density inside our chosen volume and that hasn't increased at all.
All that happened is that the electric field drew some charges to the surface of the dielectric which caused then some additional charges to appear on the surface of the conductor.
So the surface-charge density increased on the surface of the conductor but not the net charge density inside the Gaussian surface.
Have we or have we not made a mistake?
The answer depends on our definition of charge and charge density.
If q in Gauss's law (eqn (2.15)) means free charge then we are all right, then we can ignore the bound charge on the dielectric.
In fact this is the whole point of introducing D. By assigning a relative permittivity to a dielectric material all these problems have been taken care of.
We need to consider the free charges only.

Let's not forget that we are concerned with parallel-plate capacitors and we are interested in determining the capacitance.
Since the insertion of the dielectric increased the surface charge density on the plates by a factor with the voltage remaining unchanged, we may conclude that the capacitance has also increased by the same factor, yielding [UNK].

Next, we shall consider a more complicated problem where the space between the plates is filled by two different dielectrics, as shown in Fig. 2.17.
Introducing subscripts 1 and 2 for denoting our quantities in the two dielectrics, we may write [UNK].
What else do we know?
In each section the relationship (2.62) must still be valid, so that [UNK], and since potential is additive [UNK].

We need one more equation between our variables that can again be provided by Gauss's law.
Using the Gaussian surface shown in Fig. 2.17 and noting that [UNK], we get [UNK].
The right-hand side is zero since there are no free charges inside the Gaussian surface.
Hence [UNK], and, in view of eqn (2.65), [UNK].

With the aid of eqns (2.67) and (2.71) we may now obtain the capacitance per unit area: [UNK], in agreement with the tenets of circuit theory.

2.7.
Two-dimensional problems

We have so far had infinite metal plates and infinite dielectrics.
They were chosen to be infinitely large in order to reduce the problem to a one-dimensional one.
Let us take now the bold step of increasing the number of dimensions by one.
What is the simplest two-dimensional problem involving conductors?
Two concentric circular cylinders (Fig. 2.18) to which a voltage [UNK] is applied and where the medium between the cylinders is a vacuum.
Our aim is first to determine the variation of electric field as a function of radius and then to work out the capacitance per unit length.

As you are getting used to it by now we shall start with Gauss's law.
The Gaussian surface will be a cylinder at radius R as shown in Fig. 2.19.
Owing to a circular symmetry the electric field will have only a radical component, independent of the azimuth angle.
Hence Gauss's law (for unit length of cylinder) takes the form [UNK], yielding [UNK] and [UNK].

From the definition C=q/V we get immediately for the capacitance per unit length: [UNK].

What have we learned from the solution of our first two-dimensional problem involving conductors?
We have found that the electric field varies as 1/R.
There is nothing new in that; we came to the same conclusion earlier when studying the field of a line charge.
We have managed, though, to derive the capacitance of concentric cylinders, a formula used in practical engineering, so we have certainly achieved something.

It would now be easy to go on and work out the field between two concentric spheres.
We shall however resist the temptation.
We would learn little, because by exploiting spherical symmetry we would just have to deal with another pseudo-one-dimensional problem.
It is important of course that the field varies as 1/r2 in that case, and it is also of some use to know the formula for the capacitance of a spherical capacitor but you can work that out yourself if you are interested.

Let us look at a real two-dimensional problem instead.
We shall take two conducting cylinders of radius a (Fig. 2.20) and apply a voltage between them.
How can we find the electric field?
That should be easy.
For calculating the field in point P we need two Gaussian surfaces, namely cylinders R1 and R2, as shown in Fig. 2.20.
Then owing to the charge on one cylinder (per [UNK] unit length of course) [UNK], and owing to the charge on the other cylinder [UNK].
The problem is linear, superposition is permissible, so all we need to do is to add vectorially E1, and E2 and the field at point P is determined.

Unfortunately the method is wrong.
Why?
Gauss's law is valid, and afterwards we did no more than added the field due to the two charges.
This is permissible indeed if the charges are at fixed positions.
In the absence of cylinder 1 the field due to the charge on cylinder 2 is correctly given by eqn (2.79).
But we have used cylindrical symmetry.
We have relied on the fact that the charge distribution on cylinder 1 is uniform.
When we put cylinder 2 there, the circular symmetry is broken.
The negative charge on cylinder 2 will attract the positive charge on cylinder 1 therefore the part of cylinder 1 facing cylinder 2 will have a higher surface-charge density than the opposite side.
Gauss's law is still valid by eqns (2.79) and (2.80) do not follow from it.

How can we find a solution?
Well, in this particular case we can find the solution by attacking another problem: that of two line charges as shown in Fig. 2.21.
The potential for one line charge was given by eqn (2.45).
For two line charges [UNK].
[UNK] The equipotential surfaces are given by the equation [UNK], where k is a constant.
Doing a bit of analytical geometry it turns out that the equipotential surfaces are circular cylinders as shown by dotted lines in Fig. 2.22.
We can now re-state the two-cylinder problem of Fig. 2.20 as presented in Fig. 2.23; we need only relate the parameters a, b, d, and K to each other.
The calculation outlined above yields [UNK], and [UNK].
[UNK] [UNK] [UNK].

Thus the solution for the two-cylinder problem is provided by the solution for the two-line-source problem having the same amount of charge per unit length.

We may now work out the capacitance if we wish.
The potential difference may be obtained as follows [UNK] and the capacitance per unit length [UNK].
If b>a we get [UNK].

Having got so far it might be of interest to work out the variation of surface-charge density on one of the cylinders as a function of [UNK].
In order to obtain the surface-charge density we need to work out D and E on the surface of the cylinder.
It is very simple in principle; we just need to use the gradient relationship between [UNK] and E yielding [UNK].
The quantity of interest is the relative variation of the surface-charge density, i.e. [UNK] which may be obtained (after a fair amount of tedious algebra) in the form [UNK].
The above equation is plotted in Fig. 2.24 for b/a=1.1, 1.5, 3, and 10.
It may be seen that for a low value of b/a the surface-charge density changes considerably around the circumference of the cylinder.
When b/a>1 there is hardly any variation.
So it is clear that our first approach (demonstrated in Fig. 2.20) had no general validity.
But, if b/a>1 the charges on the two cylinders have little effect upon each other, and the approach is permissible.

[UNK] We shall finish off the two-cylinder problem by working out the capacitance when b/a>1 on the basis of eqns (2.79) and (2.80).
On the line connecting the centres of the cylinders E1 and E2 add algebraically so that [UNK] and [UNK], leading to a capacitance in agreement with eqn (2.88).

Having solved the two-cylinder problem we are not much wiser; we still don't know how to tackle a general problem.
There is though one general rule we can set up easily enough.
The electric field must always be perpendicular to the surface of a conductor.
The reason is that otherwise the surface charges would be in motion contrary to the assumption that a static equilibrium exists.
If the electric field is perpendicular to a surface then, owing to the [UNK] relationship, that surface must be an equipotential.
So if we work in terms of the potential the boundary condition may be easily formulated: [UNK] = constant on all conductor surfaces.
A further advantage of using (as I mentioned several times before) is that we get rid of the vectorial nature of the problem.

The mathematical problem is then to solve the differential equation [UNK] in conjunction with the boundary condition that [UNK] constant on all conductor surfaces.

Are there any general methods for solving eqn (2.93)?
There aren't any.
However, if there is no free charge in the space between the conductors, and strictly for two-dimensional problems, there is a method to which the adjective "general" might be attached, a method that provides plenty of answers but not necessarily to the questions asked.

The method is based on the theory of complex variables.
You have heard about complex variables, and I believe you have come across the Cauchy-Riemann relationships.
So you know that if [UNK] is a complex variable and [UNK] is a complex function, then the relationships [UNK] and [UNK] hold.
Differentiating eqn (2.96) with respect to x and eqn (2.97) with respect to y we get [UNK], whereas differentiation in the opposite order leads to [UNK].
Hence both u and v are solutions of Laplace's equation.

This is sheer luck to find a solution so easily.
In fact we are even luckier.
It turns out (though I am not going to prove it here) that the v (x, y) = constant curves are orthogonal trajectories of the u (x, y) = constant curves.
Thus if we identify one of the functions with the potential, the other one will represent the field lines.
It is really as simple as that.
Take any reasonable function of a complex variable and we have the solution of an electrostatic problem.

What is the simplest function we can take?
Probably [UNK].

Take u1 = x1 and u2 = x2 as conductor surfaces (Fig. 2.25) then the y = constant lines will represent the field lines.
This example does not offer [UNK] anything new (we just got the configuration of an infinitely large parallel-plate capacitor), but we can see that the method works.
Let us try as our next example something more difficult like [UNK].

Identifying now v=2xy with the potential and u=x2-y2 with the field lines we get two sets of orthogonal hyperbolas.
Taking for example v = 1 and 2 for the conductor surfaces we have solved an electrostatic problem as may [UNK] be seen in Fig. 2.26.
Would anyone ever have to do anything with infinite conductors shaped like that?
Very unlikely.
But a finite corner is of interest, after all we often have electric fields in metal boxes.
So we can take v = 0 (giving the asymptotes) as one of the conductors and the ensuing picture (Fig. 2.27) does indeed give some intuitive "feel" for the electric field lines in the vicinity of a corner.
The electric field itself may be found from the equations [UNK].

[UNK] If you are fond of mathematical games there are plenty of functions to experiment with.
You can be sure that you will find a solution of Laplace's equation satisfying the boundary conditions, but you will have to find out which problem you have obtained the solution of.

I will not dwell much longer on conformal mapping (this is incidentally the term most often used for describing the method) but will give a few more examples.
Let us place two coplanar conducting plates very close to each other (Fig. 2.28) and apply a potential difference between them.
At some [UNK] distance away from the gap the equipotentials will be planes and the field lines will be circles.
In the immediate vicinity of the gap the situation is more complicated, as shown in Fig. 2.29.
The equipotentials are confocal hyperbolas and the electric lines of force are given by confocal ellipses.

[UNK] Fig. 2.30 shows the field lines and equipotentials for two semi-infinite parallel conducting plates raised to different potentials.
It tells us what happens at the edge of a capacitor and can also give a numerical estimate of the scattered capacitance (by which the capacitance of a real capacitor differs from that worked out on the basis of the infinite-plate model).

[UNK] The foregoing three examples provided further illustrations of the usefulness of complex functions for solving electrostatic problems (for further information on these mappings see, for example, Simonyi (1963)).
For axially symmetric cases the method is unfortunately not applicable.
I shall not be discussing here the methods that are applicable but shall present the solution to one particular problem arising in electron optics, that of two closely spaced conducting cylinders at different potentials (Fig. 2.31).

2.8.
The method of images

This is again a rather specific method suitable for the solution of a limited class of problems in both two and three dimensions.
The simplest way of introducing the method is to present again the field lines and the equipotential surfaces for two equal charges of opposite sign (Fig. 2.4).
Let us now place an infinite conductor plane halfway between the charges as shown in Fig. 2.32.
Since the y = 0 plane was an equipotential surface anyway (the field lines were perpendicular to it), nothing changes.
Hence we have found the solution for a charge in front of an infinite plane.
Working backwards we may now say that the effect of an infinite conducting plane is equivalent to that of a charge of opposite sign placed in the mirror position (the negative charge is the image of the positive charge in the plane).

As an example let us work out the surface-charge density on the surface of the conducting plane due to a positive charge q above it (Fig. 2.33 (a)).
This is a difficult boundary-value problem, but using the method of images we only [UNK] need to determine the electric flux density due to the two point charges.
According to Fig. 2.33 (b) the electric field at a distance r from the charge is given by [UNK] [UNK] [UNK] (the negative sign is due to the fact that the direction of the electric field is opposite to the normal to the plane), and consequently [UNK].

There are various generalizations of the method.
A charge in a corner has three images (Fig. 2.34) but there are as many as five images in a wedge of 60° (Fig. 2.35).
You can now work out for yourself how many images a charge in a wedge of angle [UNK] has (unfortunately n must be an integer).

[UNK] [UNK] The essence of the method is that a conductor may be replaced by a set of charges without any change in the pattern of field lines and equipotentials.
Another example of a mirror charge, this time in a cylinder, is provided by Figs 2.22 and 2.23, redrawn in a more suitable form in Fig. 2.36.
This is an example we have already worked out.
According to our new interpretation the line charge p1 has its mirror charge -p1 at a distance 2d.
It is also possible to define a mirror charge in a conducting sphere and in some purely dielectric configurations but we will not discuss them here.

2.9.
Dielectric boundaries

The conditions for conducting boundaries have been simple enough.
Unfortunately not all boundaries are comprised of conductors; some of them are dielectrics, and even worse we have to consider sometimes imperfect dielectrics that have a finite conductivity.
The proper boundary conditions may be derived in the usual manner with the aid of Gauss's law.

In the general case the boundaries are neither planes nor circles, but this fact does not need to bother us.
If we investigate a small enough part of the boundary between two arbitrary media we can always regard the boundary as a plane surface.
The Gaussian surface may then be chosen in the form of a cylinder, as shown in Fig. 2.37.
If the height of the cylinder dh is approaching zero then the total flux is going through the top and bottom surfaces, i.e. [UNK].

[UNK] Keeping the treatment entirely general we shall permit now the presence of a surface charge (made up of free charges; it is still true that the bound charges of dielectrics do not count), hence, when dh → 0, [UNK], and it follows from the above two equations that [UNK].
This is now entirely general.
It includes as special cases both eqn (2.63) (when Dn2 is zero inside the metal), and eqn (2.72) (when both dielectrics are perfect so that no free charges can reside on the boundary surface).

So far, so good.
We have derived the condition for the normal component of D. What about the tangential component?
We can get that by taking this [UNK] time the line integral of the electric field along both sides of the boundary as shown in Fig. 2.38.
Assuming that dl → 0 and noting that for a closed contour the line integral of the electric field vanishes we get [UNK], i.e., the tangential component of the electric field strength is constant across a boundary.
This means that the electric field will refract at the boundary of two dielectrics, as shown in Fig. 2.39.
The relevant equations are [UNK].
[UNK] Thus unless the incident angle is 90° the field lines will have a break at the boundary of two dielectrics.

An example is shown in Fig. 2.40.
We have a line charge in front of a dielectric that fills half the space.
The field lines, as expected, refract when entering the dielectric (for a mathematical solution in terms of Images, see Clemmow (1973)).

[UNK] Another example demonstrating the same phenomenon may be seen in Fig. 2.41.
A dielectric sphere inserted into a homogeneous electric field in air or a vacuum "attracts" the field lines.
The physical explanation is that the dielectric is capable of carrying a higher flux density.
The mathematical solution is given below in spherical coordinates, r, 0 (the solution is of course independent of the azimuth angle [UNK]): [UNK], from which E and D may be derived (E0 is the electric field strength in the absence of the sphere).
The boundary conditions, eqn (2.107), are satisfied at r = a.
If you are interested you can check them (Example 2.12).

In an isotropic medium (in which the dielectric constant is a scalar not a tensor) the directions of the E and D lines coincide, thus Figs. 2.40 and 2.41 may refer to either.
However if we want to interpret the density of field lines as being proportional to the field strength then both figures must represent D since it is the flux of D that remains constant across a dielectric boundary.

2.10.
Electrostatic energy

Electrostatics is characterized by charges located at certain positions.
If we know the positions of all the charges, we know everything so we should know the energy as well.
There is unfortunately no obvious way of writing an expression for the energy in the simultaneous presence of all the charges.
It is, however, fairly easy to work out the energy as we bring in the charges from infinity one by one.

The first charge is brought in without any opposition.
The energy of one charge alone is zero.
The second charge is brought in in the presence of the first one.
The work done is [UNK].
There are now two charges, q1 and q2, and we bring a third one, q3, from infinity.
The work done is [UNK].
Three charges are probably enough for seeing the general trend so we shall now sum up the two partial energies [UNK], which may also be written in the form [UNK].
It may be recognized that the terms in the brackets represent the potentials due to the other two charges.
It is easy to guess that in the general case one would have, instead, the potential due to all other charges.
Hence the general term is of the form [UNK], where [UNK] is the potential at the point where q1 resides (ignoring the contribution of q1).
The expression for the total energy of n charges is then [UNK].

The transition from discrete to distributed charge can be made as follows: q1 is replaced by [UNK], and the summation by integration, yielding [UNK], where the volume r must contain all the charges.
Thus if the charge distribution is known we should first determine the potential (from eqn (2.24) and then we may use eqn (2.116) for calculating the energy.
This is a perfectly reasonable procedure, but we have to admit that eqn (2.116) is rarely used.
It is usually transformed into another more popular form.

Since [UNK] and by eqn (A.2) [UNK], we may first transform eqn (2.116) into [UNK].
Noting further that [UNK] and applying Gauss's theorem to the first term in the bracket we get [UNK], where S is the closed surface of the volume r.
Now this is another perfectly reasonable formula to use - once the volume is chosen.
Well, let us choose it in the form of a big sphere.
If r the radius of this sphere is big enough then the potential decays as 1/r (cf.
Section 2.4) and the electric field as 1/r2.
Thus the integrand decays as 1 /r3, whereas the surface increases only as r2.
Consequently the surface integral must vanish as r → ∞.

We are now left with the sought-for expression.
Provided the volume integral is over all space the energy is given by [UNK].
This is a simple and physically easily interpretable expression.
Wherever there is electric field, there is energy as well.

So how should you think about electrostatic energy?
You are certainly entitled to think in terms of charges and potentials.
In order to create a charge distribution a certain amount of work has to be done, and that is available to us in the form of electrostatic energy.
But it is better (it is more general) to regard the electric field as the agent with which the energy has been deposited.
One usually says that the energy is stored in the electric field.

Let us work out, as an example, the stored energy of a parallel-plate capacitor.
The electric field strength is given (eqn (2.57)) by E = V/d, hence the stored energy is [UNK], where S0 is the area of the capacitor plates.
Of course, you can derive the above expression from circuit theory, so once more circuit theory and electromagnetic theory give the same answer.
Could we use this stored energy for calculating the magnitude of forces acting, could we get the direction of the forces?
Take the following example from mechanics: a mass m at rest at a height h has a potential energy mgh.
In which direction will it move if its support is taken away?
It will try to reduce the height h in order to minimize its potential energy.

[UNK] While the energy of the capacitor increases that of the battery decreases.
Why?
Because an increase of dC in the capacitance requires an amount of extra charge dq = VdC, which must flow from the battery to the capacitor.
So the loss of energy by the battery is V dq = V2 dC.
Hence the net gain of energy of the system is [UNK], in agreement with eqn (2.124).

So if we consider the capacitor and the battery together the total energy of the system decreases as the capacitance increases.
We obtain the same force between the plates whether the battery is disconnected or not - as we should.

Examples 2

1.
Four point charges of equal magnitude are located at the corners of a square as shown in Fig. 2.42.
Determine the magnitude and direction of the force on each charge.

[UNK] 2.2.
A cloud of charged particles having a total charge q, fills uniformly the volume of a sphere of radius a.
Find the electric field at a distance r from the centre of the cloud both for r<a and r>a.

2.3.
Determine the electric field on the axis of a charged ring of radius a carrying a uniform line charge of p1 coulomb per unit length.

2.4.
A linear line charge of pl coulomb per unit length extends from the origin to z = ∞.
Determine the electric field at an arbitrary point using cylindrical coordinates [UNK].

2.5.
Determine the electric field as a function of r and 0 produced by the axial quadrupole shown in Fig. 2.43.
Assume that r>d.

2.6.
An infinitely long, perfectly conducting cylinder of radius a is placed into a uniform electric field perpendicularly to the direction of the field lines.
The potential function for this case is given as [UNK], where A is a constant and R and [UNK] are polar coordinates centred at the axis of the cylinder.
(i) Show that the resultant electric field satisfies the boundary conditions, (ii) Determine the differential equation of the field lines.

[UNK] 2.7.
Show that the potential function given in Example 6 satisfies Laplace's equation in cylindrical coordinates.

2.8.
Two point charges q and -pq ([UNK]) are placed at the points (0,0,0) and (0,0, d) of a cartesian coordinate system.
Find the zero potential surface.

2.9.
Determine the force upon a point charge placed inside a conducting sphere at a distance a from the centre of the sphere.
(Hint: Find the mirror charge in the sphere based on the calculations of the previous example.)

2.10.
Determine the capacitance per unit length of a two-wire transmission line above a perfectly conducting earth (Fig. 2.44).
Assume that d1, d2>D.

[UNK] 2.11 Derive eqns (2.83) - (2.85).

2.12 Show that eqn (2.110) satisfies the boundary conditions at r = a.

2.13 Two long concentric cylinders of radii a and b are separated by a dielectric of relative permittivity Er.
They are held with their common axis vertical, so as to provide a liquid-level gauge.
If the capacitance of the gauge is C when a fraction a of its length is immersed, find how its sensitivity [UNK] varies with a and with the relative permittivity of the fluid.

2.14.
Find the equipotentials and lines of force represented by the following conformal transformations [UNK].

2.15.
A capacitor made of concentric cylinders has an inner radius a, outer radius b, and length l. it is filled with a dielectric of relative permittivity [UNK].

Derive an expression for the maximum stored energy, W max considering that the dielectric breaks down at a field intensity Eb.
Calculate W max for the case when a = 5mm, b = 10mm, l = 100mm, Eb = 2 × 107 V m-1, Er = 2.25.

2.16.
Find the lateral force on the dielectric slab partially filling the space between two parallel capacitor plates (Fig. 2.45) having a voltage V between them.

[UNK] 2.17.
One plate of a parallel-plate capacitor having an area S is suspended at its centre from a spring of stiffness k.
The other plate is held fixed at a distance d.
What is the minimum voltage to be applied between the plates for pulling them together?

2.18.
A variable capacitor consists of two sets of n interconnected semicircular conducting plates which can be given mutual rotation as shown in Fig. 2.46.
Derive expressions for the torque needed to hold 0 constant under the following conditions: (i) when the plates are connected to a source of constant voltage V; (ii) after the plates have been rotated to their position of maximum capacitance, charged to voltage V, disconnected from the supply and then rotated to a new position.
What limits the maximum voltage that can be achieved by the operations described in (ii)?

## 3. Steady currents

3.1.
The basic equations

IN this chapter we shall be concerned with phenomena in which the main role is played by the current of charged particles.
All our variables can be functions of space but are independent of time.

It is easy to present the relevant equations; we have all of eqns (1.1) - (1.7) but have to substitute a/at = O, yielding [UNK].

There is a difficulty with eqn (3.6).
It is correct for most of the chapter with [UNK] taken as a constant but breaks down for ferromagnetic materials, which will be discussed in Section 3.11.
All the other equations are all right but will not necessarily provide the simplest starting point for solving a given problem.
We shall, therefore, introduce a number of alternative formulations.

First, we could search for some analogue of the potential function which proved so useful in electrostatics.
We found there that by choosing a scalar function in the form [UNK] we could automatically satisfy the other equation for the electric field strength, [UNK].
Can we do the same thing for the magnetic quantities?
No, but we can do a similar thing.
Since it is the equation [UNK] that needs to be satisfied, we should choose the potential as a vector (called, not without logic, the vector potential), defined by the equation [UNK].
Substituting the above equation into eqn (3.1) we get [UNK], or using the vector relation (eqn (A.6)) we obtain the modified form [UNK].
This equation can be further simplified to [UNK] by choosing (in the physicist's jargon this is called choosing the gauge) [UNK].
Can we do that?
One can't usually assign some arbitrary value to the divergence of a vector function.
In the present case, however, we do have some freedom of choice.
The definition of A by eqn (3.8) is not unique.
If we add to A the gradient of a scalar function, the resulting vector A' still gives the same magnetic field because [UNK].
Hence a suitable choice of will ensure that [UNK].
So we are left with eqn (3.11).
If the current density is specified, eqn (3.11) will provide the solution for A from which B can be determined.
How can we find a solution for A?
There is nothing easier.
We only need to remember the differential equation for the scalar potential [UNK] (eqn (2.12)) and its solution in the form of eqn (2.24).
By analogy the general solution of eqn (3.11) is [UNK].
A simple integration will yield A if J is given.
We shall go through a number of examples later.
For the moment let us use the above expression for deriving Biot-Savart's law.

First we shall assume that the current density is confined to a thin wire in which case the integration variable may be changed to [UNK], where S is a vector normal to the cross-section, [UNK] is the area of the cross-section, and dI is an elementary vector along the tangent of the wire.
Noting further that J. S = I and that I must be constant along the wire we may write eqn (3.15) in the modified form [UNK], whence the magnetic field strength is [UNK].
We have to stop here for a moment to sort out the coordinates.
As may be seen in Fig. 3.1 the coordinates of the wire element are x', y', z', whereas the coordinates of the point where we wish to determine the magnetic field are [UNK] set of coordinates.
Thus the curl operates on the coordinates of P but not on those of dl leading to [UNK] where ir is the unit vector in the direction r and we have made use of the vector relation (A3) in the Appendix.
This is Biot-Savart's law derived directly from Maxwell's equations.

Are there any other ways of determining the magnetic field?
Well, one can use eqn (3.1) as it is, but very often one is better off by using its integral form that can be obtained by integrating both sides of eqn (3.1) over a surface [UNK].
By using Stokes' theorem for the left-hand-side and recognizing that the integral of the current density gives the current, the above equation reduces to [UNK], where the line integration is along the curve C enclosing the surface.
The positive sense of the integration path is defined relative to the positive current direction according to the usual right-hand convention.
Equation 3.21) is known as Ampère's law.

We have now a number of equations describing the same thing.
Which equation should we use in a practical case, the equation for the vector potential, Ampère's law, Biot-Savart's law, or attack directly Maxwell's equations?
It's hard to tell.
Experience with practical calculations helps, but even after years of work one usually remains this side of infallibility.
I regret to say that there are no general guidelines available.
If one manages to find the simplest method at the first attempt that can mostly be attributed to good luck.
Can we claim then that the vector potential is as useful as its scalar counterpart in electrostatics?
For computational purposes the answer is an unambiguous no.
It is always laborious to find the components of a vector, so we are not much better off with A than with H or B. It turns out however that A is a more basic quantity of physics than B. Since B is given by the curl of A it is possible that A is finite while its curl is zero.
Interestingly, under these conditions A has an effect on certain quantum-mechanical phenomena.t It would be unfair both to the vector potential and to quantum mechanics to say that none of those formulations have engineering applications (in fact the most sensitive magnetometer built to date is based on that kind of theory), but by and large engineers wouldn't lose much sleep if the use of A were banned with immediate effect.
The vector potential is not a popular variable among engineers, maybe because it is not directly measurable.
There are no instruments capable to measure the magnitude or direction of A.

In my opinion A is a useful thing if used with moderation.
It helped us to derive Biot-Savart's law, it will come handy later in solving certain radiation problems, and it often leads to nice formulae, e.g. for the magnetic flux crossing a surface, defined as [UNK] that may be rewritten in terms of the vector potential as follows: [UNK] where C is the curve enclosing the surface.

We have now collected a good number of formulae which will serve us well in the following sections.

Before going on, just a few words about the classification of steady currents.
It may be roughly divided into two parts: magnetostatics and the rest.
We shall discuss the rest first (Sections 3.2-3.5), and that will give us some idea of the relative significance of electric and magnetic fields.
Sections 3.6-3.16 are concerned with magnetostatics, where electric fields are assumed to be zero and the interrelationship of J, H, and B are studied.

Since we have so many variables, and since in each physical configuration only some of them appear, we will record (just for this chapter) the non-zero variables in each section heading.

3.2.
The defocusing of an electron beam (J, E, D, p, H, B)

We have so far talked about positive and negative charges, about point charges, and distributed charge.
I shall now introduce the concept of an elementary charge, 1.6 × 10 -19 C, carried by an elementary particle called the electron.
This is not a necessity.
It is possible to study electromagnetic theory without ever mentioning the word electron, but since it has become such a household word and is used so often we can just as well make use of it.

In the present section we shall consider a cylindrical electron beam of radius a in which the charge density is uniform (p = Po) and all electrons travel with velocity v.
We are not going to enquire into the details how such beams can be produced (it belongs to the subject of physical electronics); we shall accept the fact that the beam exists and will try to work out the forces on the outermost electrons.

There is now cylindrical symmetry and a net charge per unit length [UNK], yielding for the radial component of the electric field [UNK].

The magnetic field may be obtained from Ampère's law (eqn (3.21)) as follows [UNK], where the line integral is taken over the circle of radius a (Fig. 3.2), I is the total current of the beam and [UNK] is the azimuthal component of the magnetic field in the cylindrical coordinate system specified by [UNK].
From eqn (3.26) we get [UNK].

The electric force on an electron of charge e travelling at the edge of the beam (R = a) is [UNK] it is in the radial direction pointing outwards.
The magnetic force is perpendicular both to the direction of motion (+z axis) and the direction of magnetic field ([UNK] direction).
The vectorial product v X B gives an inward force in the radial direction.
Hence the net force on the electron is [UNK].
Noting that [UNK] and anticipating the relationship [UNK] to be derived in Section 5.7, we get the following formula for the force [UNK], where c is the velocity of light.
It may be seen from the above equation that the magnetic force is negligible in comparison with the electric force unless the velocity of the electron approaches the velocity of light.
Thus the conclusion is that, owing to the repulsive forces between the electrons, a cylindrical electron beam is unstable.
Using a technical term borrowed from electron optics we could say that the electron beam gets defocused.

The other conclusion (as far as it is permissible to generalize from a single example) is more important in principle.
It is concerned with the relative magnitudes of electric and magnetic forces.
Since charged particles rarely travel close to the velocity of light we may conclude that the magnetic forces are by orders of magnitude smaller than the electric forces.
Why is it then that we have no difficulties in practice in observing magnetic fields?
The reason is, of course, that there are two kinds of electric charges and their effect usually cancels, so the small magnetic field has a chance of getting observed.
And that brings us to the ext example.

3.3 Pinch effect (J, H, B)

In contrast to our previous example we shall now investigate a cylindrical beam consisting of two kinds of charge carriers: negative electrons and some positive particles, which I do not wish to be more precise about at the moment.
We shall assume that the two kinds of particles have equal densities and move in opposite directions.
As a result there is no net space charge and hence no electric field.
The currents, on the other hand, do not cancel because they represent opposite charges moving in opposite directions (remember, minus one times minus one is equal to plus one).

The magnetic field strength is given again by eqn (3.27); we only need to substitute for the current In + Ip where the subscripts n and p refer to negative and positive particles respectively.
Hence the magnetic force on the electron at the edge of the beam (at R = a) is [UNK], and on the positive particle is [UNK].
Note that the force is inwards, and in the same direction for both particles.

Let us distinguish two cases.

Both particles are mobile

In that case both of them will move inwards under the effect of magnetic force.
But if the diameter of the beam is reduced, eqns (3.33) and (3.34) tell us that the forces are even larger.
What happens then?
If everything was uniform then the beam diameter would go on decreasing.
In practice however the beam is not uniform and does not possess perfect cylindrical symmetry.
Under these conditions the motion of the particles is fairly complicated, and of course our model is unable to predict the detailed behaviour of the particles.
Nevertheless a few qualitative conclusions may be drawn without doing any further mathematics.
If the cross-section happens to be smaller at a certain place, then the forces are larger there than at the neighbouring cross-sections, so the beam will be further constricted, etc., leading to the so-called sausage instability (Fig. 3.3 (a)).
If the magnetic field happens to be larger at one side than at the other side, then the beam will be deflected towards the weaker field which makes the field even weaker, etc., leading to the so-called kink instability (Fig. 3.3 (b)).

The positive particle is immobile

In practice this means that the positive ions are part of the crystal lattice.
There is then no magnetic force on the ions, only on the electrons.
So the electrons want to move inwards but cannot because the ions hold them back by virtue of their electrostatic attraction.
Naturally, if the ions attract the electrons the converse is true as well, i.e. owing to the magnetic force on the electrons, there is also an inward force upon the ions.
So the whole crystal structure tries to contract or in other words the material is under pressure (see Example 3.2).
In any practical situation this pressure is small and can be neglected when calculating the forces on current-carrying conductors.

3.4.
Flow patterns and Ohm's law (J, E, D)

Up to now we have not enquired into the question of how the current arose.
We just assumed that certain charge carriers moved with certain velocities.
Now we shall say that in a class of materials the current density at any point is proportional to the electric field; in mathematical form [UNK], where [UNK] is the conductivity of the material.
The above equation is spite of its utmost simplicity represents an extremely good guess.
It is valid for nearly all materials up to quite high electric fields.

Will there be a magnetic field?
Yes, of course, whenever there is a current there is a magnetic field as well.
But the effect of the magnetic field upon the motion of the electrons is nearly always negligible (one exception causing the pinch effect is mentioned in the previous section).
Thus we may safely ignore the magnetic field when determining the lines of current flow.
We are then left with only one equation [UNK] or [UNK] or [UNK], depending on our preference.
Eqn (3.38) tells us that there is some analogy (see Example 3.3) with the electrostatic case treated in Chapter 2.
We may, in fact, reinterpret any of the diagrams of Figs (2.25) - (2.31) by assuming that the whole space is filled with a material of conductivity [UNK] and the field lines are now the lines of current flow as well.

Is the analogy perfect?
Not really, because (1) as current flows there is some potential drop in the electrode itself, (2) zero conductivity for part of the space cannot be electrostatically modelled since there are no dielectrics with Er = 0, and (3) when current flows through two materials of different conductivity there is generally a surface charge at the boundary (see Example 3.4).
It is not worth discussing any of these complications because one is rarely called upon to work out lines of current in a conductor.
We shall rather return to a very simple geometrical configuration for deriving Ohm's law.

We shall take a piece of cylindrical material of length l and cross-section S and apply a voltage between the ends.
The electric field is then [UNK], the current density [UNK], and the current [UNK].
From circuit theory [UNK], where R is the resistance of the material.
Comparing eqns (3.41) and (3.42) we get [UNK].
Since [UNK] is by definition the resistivity we get the result you learned in school that the electrical resistance is proportional to the resistivity and the length of the sample and inversely proportional to its cross-section.

A more general definition of resistance valid for varying cross-sections may be easily arrived at, but it is hardly worth the trouble.
The essential thing is that the relation [UNK] is equivalent to Ohm's law.
Risking the dismay of circuit engineers some theoreticians do, in fact, refer to eqn (3.35) as Ohm's law.

3.5.
Electron flow between parallel plates [J, p, E, D)

We shall investigate here just one more physical configuration where in spite of having a finite current the magnetic field may be disregarded.
The new feature will be a spatially varying space-charge density.

Let us take two parallel conducting plates in a vacuum, one of them endowed with the property that it is capable of emitting electrons.
We shall further apply a voltage between the plates so that the electrons emitted by electrode 1 are attracted to electrode 2 (Fig. 3.4).
The aim is to calculate the [UNK] potential distribution between the plates, and the relationship between applied voltage and the magnitude of resulting current.

We can reduce the problem to a one-dimensional one by claiming that the plates are infinitely large.
Alternatively, we may say that the plates are so close to each other (as it would be in a practical diode) that the electron beam hasn't got a chance to spread.
Whichever way we look at it we can disregard with clear conscience both the radial electric field and the magnetic field.
Hence the variables of interest are the current density, the electron velocity, the space-charge density, the longitudinal electric field strength, and the potential [UNK].

We can arbitrarily assign [UNK].
Then [UNK], where V is the potential difference applied.
The electron velocity at the point z may be worked out by the simple consideration that the electron gains kinetic energy at the expense of its potential energy (the same idea as in mechanics).
Hence [UNK].
Assuming now that the electrons are emitted with zero initial velocity, v (0) = 0, we get [UNK].
Note that e is negative and that, for the above equation to apply, [UNK].

The charge density may be obtained from the relationship [UNK], where J is a positive constant.
p must of course be negative because it represents the space-charge density of electrons.

In this example the charges are in motion and the charge density varies from point to point but the density at a given point z is not dependent on time.
Hence we are faced here with an electrostatic problem which may be solved with the aid of Poisson's equation (eqn (2.12)).
Substituting into it the value of p from eqn (3.46) we get [UNK].
This is a reasonable-looking differential equation; I leave the solution to you (Example 3.5).

The main reason for showing this example is not its intrinsic value to applied scientists (the problem of space-charged-limited diodes is no longer in the forefront of interest) but to demonstrate the applicability of Poisson's equation under conditions of steady current flow.

3.6.
The magnetic field due to line currents (J, H, B)

Assume that a current I flows along the z axis from minus infinity to plus infinity (Fig. 3.5 (a)) and find the magnetic field at a distance R from the current.
Owing to axial symmetry the magnetic field must be constant at a radius R, hence the application of Ampère's law yields [UNK], or [UNK].
In fact we have derived this relationship in Section 3.2.
It makes no difference whether the current is distributed within a radius a or concentrated at the axis (only the enclosed current counts).
Could we get the same result by using our formula for the vector potential (eqn (3.17))?
We could, although we would run again into the problem of a diverging integral owing to the limits at infinity.
We spent quite a long time sorting out this problem in the electrostatic case, and we need not repeat the argument here.
Just by analogy with eqn (2.45) we obtain [UNK].
For obtaining B we take the curl of the vector potential in a cylindrical coordinate system [UNK] as follows [UNK].
Recognizing that nothing can change in the [UNK] and z directions ([UNK]), the only non-zero component is provided by [UNK], in agreement with eqn (3.49)

For two line currents flowing in the opposite directions (Fig. 3.5 (b)), we may write Ampère's law twice and add the magnetic fields or add the vector potentials.
In either case we obtain [UNK] where [UNK] and [UNK] are unit vectors in the azimuthal directions from the two line currents respectively.

3.7.
The magnetic field due to a ring current (J, H, B)

The solution for line currents was simple enough.
Unfortunately the determination of the magnetic field for a ring current needs a lot of calculation.

We shall assume that a ring of radius a situated in the z = 0 plane carries a current I (Fig. 3.6) and we wish to determine the magnetic field at the point [UNK] [UNK], i.e. at an arbitrary point in space.
We shall rely on the vector-potential formulation because that appears to be best suited for utilizing the axial symmetry of the chosen geometry.
The vector potential due to any current element is always in the direction of the current element.
Hence if the current is everywhere in the azimuthal direction the vector potential must be in the same direction too.
Thus even before starting any calculations we may immediately say that A will only have an [UNK] component and that will be independent of [UNK].
Taking the coordinates of the current elements dl as [UNK] (Fig. 3.6) and noting that [UNK] we obtain for the desired component of the vector potential [UNK] or [UNK], where the expression for r has been substituted.

Since [UNK] must be independent of [UNK] we can simplify eqn (3.56) by taking [UNK].
The remaining integration is nonetheless difficult, and not expressible in terms of simple functions.
Mathematicians, wisely foreseeing such difficulties, worked out the theory of a number of special functions and tabulated them as well.
In the age of the computer their work is no longer indispensable but is still useful as a sort of short-hand notation.
If you look up the relevant books you will find that eqn (3.56) may be expressed in terms of elliptic integrals.
Having obtained the vector potential the magnetic field may be obtained by the usual differentiation which, incidentally, also leads to elliptic integrals.

There is nothing fearful in elliptic integrals Their definitions are fairly simple, they are nicely tabulated and they have a few interesting interrelations.
All that is easily digestible.
My main reason for not introducing elliptic integrals here (you can though attempt Examples 3.9-3.11 if you wish to have some experience in handling them) is that I do not want to burden your memory with new formulae, and besides, for cases of most practical interest (the field far away from the ring and in the vicinity of the axis) eqn (3.56) may be integrated out, as will be presently seen.

For both cases mentioned above ([UNK] and [UNK]), the following inequality is valid [UNK].
Hence we can expand the denominator of the integrand as follows: [UNK].
Substituting the above approximate relation into eqn (3.56) we can perform the integration, yielding [UNK].

Let us first consider the case when the point of observation is far away from the ring ([UNK]); then the vector potential takes the form [UNK], which may be rewritten in spherical coordinates as [UNK], whence the magnetic field is [UNK].
Noting that [UNK] we get for the components of the magnetic field [UNK].
Can you remember seeing these self-same components somewhere before?
Well, the constants are different but apart from that eqn (2.33), the formula for the electric field of an electric dipole, looks the same.
On the basis of this analogy we may call a ring current a magnetic dipole, or more precisely we should say that sufficiently far away from a ring current the magnetic field appears as if it was created by two closely spaced magnetic charges (which of course do not exist).

There is another less obvious conclusion at which one might arrive by inspecting eqn (3.63).
Notice that the area of the ring [UNK] appears as one of the factors in the constant.
It turns out (though we are not going to prove it here) that the exact shape of the current loop is immaterial (not unreasonable if the loop is far away) and in the general case we only need to replace [UNK] by S, the area of the loop.

Turning now to the case when the point of observation is in the vicinity of the axis, we get for the vector potential [UNK], and for the magnetic field (in cylindrical coordinates this time) [UNK].

3.8.
The magnetic field inside a solenoid (J, H, B)

A solenoid is a tightly wound coil.
Each turn may be regarded equivalent to a ring in which a current I flows.
For calculating the magnetic field we shall take the coordinate system shown in Fig. 3.7, where the z axis coincides with the axis of the solenoid.
At an arbitrary point on the axis [UNK] the [UNK] magnetic field may be obtained by summing the contribution of each turn.
It is actually easier to do the calculation if instead of individual turns we assume that the current is continuously distributed on the surface of the cylinder, and work in terms of [UNK], the current per unit length, obtained by dividing the total current (NI) by the length l of the solenoid, i.e. [UNK].
The current flowing at z in the interval dz is then [UNK], at a distance [UNK] from the point where we wish to determine the magnetic field.
According to eqn (3.65) such a current will create a magnetic field [UNK] and the total magnetic field may be obtained by integrating over the length of the solenoid as follows: [UNK].
Changing the integration variable to the angle [UNK] by the relationship [UNK], we may perform the integration and get at the end [UNK].
If the solenoid is very long (l>a), then [UNK], and [UNK].
This is of course not valid near the ends but if the solenoid is long enough, eqn (3.71) may be regarded valid for most of its length.

Incidentally, eqn (3.71) may be derived much more simply if we make the a priori assumption that the magnetic field is constant inside the solenoid and zero outside.
We may then apply Ampère's law to the path shown in Fig. 3.8 yielding [UNK] It is a bit of a coincidence that eqns (3.71) and (3.72) agree.
The reason is that in the latter approach the magnetic field is overestimated near the ends inside the solenoid, and underestimated outside the solenoid.
The two inaccuracies just about balance each other.

3.9 Further analogies with electrostatics

What happens in the electrostatic case if we fill the whole space by a dielectric?
The electric field remains unchanged and the electric flux density increases by a factor Er.
What happens in the "steady current" case if we fill the whole space by a magnetic material?
The magnetic field remains unchanged and the magnetic flux density increases by a factor [UNK].

Does the analogy still hold when the magnetic material fills only part of the space?
The answer is not quite, because the boundary conditions are not quite the same.
Using the technique (surface and line integrals shrinking to zero) as in Section 2.10 we get the boundary conditions [UNK], where K is a surface current.
Hence in the absence of surface charges and surface currents the analogy still holds.

If we look at the magnetic field in a region in which no currents flow, the analogy is even closer because [UNK] and we can introduce a magnetic scalar potential with the relation [UNK].
A good example is the calculation of the effect of a spherical piece of magnetic material inserted into a homogeneous magnetic field.
The mathematics is exactly the same as in the electrostatic case; we need only to replace E0 by H0 and Er by [UNK] in eqn (2.110) in order to get [UNK].
Hence Fig. 2.41 (p. 47) is a valid representation for magnetic materials as well.
The difference between the two cases is merely quantitative.
The magnetic materials used in practice have a [UNK] several orders of magnitude higher than the Er of practical dielectric materials.
Hence the "attraction" of the field lines is much more pronounced in the magnetic case.
To give a practical example let us put in the middle of our solenoid a magnetic material of high [UNK] as shown in Fig. 3.9.
Now practically all the flux lines are funnelled into the magnetic material so much so that we are entitled to regard both H and B as being zero outside the magnetic material.

3.10.
Magnetic materials

When studying the electromagnetic properties of dielectrics I was very reluctant to get involved with the physics of dielectrics.
Now I am even more reluctant to talk about the physics of magnetic materials.
Not so much because I don't understand the subject (that is no real obstacle to a lecturer), but more because of the time we are likely to consume, even if we keep a respectable distance from quantum mechanics and concentrate solely on phenomenological theories.

It must be admitted that magnetic materials behave most unreasonably.
The relative permeability may turn out to be a tensor; it may take on very high values, say 106 or more, or it may have a value very close to unity, say 1.00002 for a wide range of temperatures, and then on cooling the material another few millidegrees [UNK] may drop to zero.

Why to bother so much about the details, you may ask; couldn't we just say that [UNK] and go on considering further examples?
The trouble is that for the most widely used magnetic material - iron - [UNK] is not a constant.
Not only that its value depends on H, but, even worse, it depends on the previous history of the sample.
So we have to discuss the B-H curves, and I will include a few more things, but you must realize that there is a lot more to it.
By the time we finish with it we shall have just scratched the surface of the subject.

3.11.
The B-H curve of ferromagnetic materials

It is customary to divide all magnetic materials into diamagnetic ([UNK]), paramagnetic ([UNK]), and ferromagnetic ([UNK]) groups.
Paramagnetic materials are unimportant from an engineering point of view, and diamagnetic materials may have a future; the present, however, belongs to the ferromagnetic group, and above all to the most important representative of the group - the various alloys of iron.

In order to obtain the B-H curve let us make the following experiment.
Place a cylindrical iron rod inside a solenoid (as in Fig. 3.9), vary the current and measure the flux density.
We shall assume that, before we switch on the current, H = 0 and B = 0, a natural-enough assumption.
As we increase the current, the magnetic field will increase proportionally (eqn (3.71)) but the flux density will be a nonlinear function of the magnetic field, as shown by the line OP in Fig. 3.10.
The point P is called the saturation point, beyond which [UNK], i.e. the iron has stopped contributing to the flux density; any further increase of H will result in that much increase of B as in a vacuum.
Reducing now the current (and H with it) we shall not retrace the same curve; B will decrease much more slowly and will have a finite value at zero current.
If we now increase the current in the opposite direction B will decrease further reaching zero at R, and negative saturation at S. The other half of the curve STUP displays the same behaviour.
This is no doubt a remarkable curve.
B being so sluggish, it is usually referred to as the hysteresis curve.
Note that the B-H relationship is irreversible everywhere inside the hysteresis curve.
If at an arbitrary point (say V) we decided to decrease the current, B would decrease in a different manner, as shown in Fig. 3.10.

[UNK] As far as engineering applications are concerned the most remarkable feature of the curve is that we can get a flux density even in the absence of all external agents.
This is of course the permanent magnet you have all come across.

How is this possible?
Up to now a current appeared to be absolutely essential for creating a magnetic flux.
The obvious way out of this dilemma is to say that the currents are there - inside the magnetic material.
The detailed mechanism of these currents has kept lots of physicists busy ever since Ampère made the hypothesis, but apparently some more time is needed to find a proper solution.

For permanent magnets a wide hysteresis curve is needed so that demagnetization should not easily occur.
For transformers and rotating machinery a narrow hysteresis curve is preferable because irreversibility leads to losses.

I am afraid this is about as much as I am going to say about magnetic materials apart from a very brief discussion of some pseudomagnetic materials (superconductors) in Sections 3.15 and 3.16.
We shall look at a few examples now in which simple geometries will be considered.

3.12 The magnetic flux density inside a permanent magnet of toroidal shape (B)

In a permanent magnet shaped as a torus we have H = 0.
The only equation to satisfy is [UNK], and that means that all the flux lines must be closed.
Choosing a toroidal shape there are still lots of possible ways for the lines to arrange themselves, but in a good permanent magnet the flux lines will be circles with centres at [UNK] 0, the centre of the toroid (Fig. 3.11 (a)).
We may then claim that B = constant everywhere inside the magnet and zero outside.

3.13.
The magnetic field inside a permanent magnet of toroidal shape containing a gap [H-B)

In the last section we have come to the interesting conclusion that B may alone exist of all our variables but we reached that conclusion on a magnet shape not much used in practice.
If we take the trouble to make a permanent magnet we would like to have access to the magnetic flux so let us look at the more practical case (Fig. 3.11 (b)) when a narrow gap is cut into the magnet.
How will the flux density vary in the gap?
It will be hardly different from B0, the value in the material; in the short space available the flux lines have not got a chance to spread.
We shall therefore take the flux density in the gap to be equal to B0.
The corresponding magnetic field will be [UNK].
What about the value of the magnetic field in the magnet?
It may be obtained from the consideration that in the absence of an external current the line integral of H (taken over the dotted lines in Fig. 3.11 (b)) must vanish, leading to [UNK], where [UNK] is the width of the gap and l is the length of the path in the magnet.
From eqn (3.76) we get the value of the magnetic field inside the magnet as [UNK].

There is still one question we have to ask, Will the magnetic flux density inside the material B0 be the same as Br the value before the gap was cut?
No, not quite.
There are now two relations to satisfy.
B0 is obtained where the straight line [UNK] intersects the B-H hysteresis curve as shown in Fig. 3.12.

3.14.
The magnetic field in a ferromagnetic material of toroidal shape excited by a steady current (J, H, B)

We shall now take a ferromagnetic material that has a very narrow hysteresis loop so that we can assume with good approximation a unique (though of course nonlinear) relationship between B and H. The material is again assumed to be of a toroidal shape but it is now excited by a current I flowing in a coil of N turns (Fig. 3.13 (a)).
We may then apply Ampère's law to the path shown by dotted lines to obtain [UNK], whence [UNK], - a formula we have already met (eqn (3.71)) when discussing an approximate solution for a long solenoid.
The corresponding value of the magnetic flux density is B1 = B (H1) that can be obtained from the B-H curve, as shown in Fig. 3.14.

Next, we shall find the solution when there is a gap of width [UNK] in the material (Fig. 3.13 (b)).
For the same current the magnetic flux density will decrease to B2, its value being the same both in air and in the material.
Denoting the magnetic field in the material by H2i and in air by H20, Ampère's law yields [UNK].
[UNK] Noting further that [UNK], the above equation gives a linear relationship between H2i and B2.
Hence the solution is obtained by the intersection of the straight line [UNK] and the B-H curve.
The graphical construction is shown in Fig. 3.14.
If we wish to produce the same flux density as in the absence of the gap, we need to increase the current.
This is the subject of Example 3.13.

3.15 The perfect diamagnet (H, B, K)

There is a class of materials called type I superconductors which below a certain critical temperature (around the normal boiling-point of liquid helium [UNK]) become both perfect conductors and perfect diamagnets.
This means that B must be zero inside the material.
Thus if we place a piece of such material (say a sphere) into an otherwise constant magnetic flux, the material will expel the flux lines as shown in Fig. 3.15.
How can this happen?
What mechanism is responsible for expelling the magnetic flux?
The appearance of surface currents (which we have previously denoted by K).
As the sphere becomes superconducting, surface currents are set up producing a magnetic flux opposite to that already existing inside the material.

3.16.
The penetration of the magnetic flux into a type I superconductor (J, H, B)

In real life nothing is ever perfect.
A type I superconductor, I confess, is not a perfect diamagnet; it will let in the magnetic flux just a little bit.
How far will the magnetic flux penetrate?
Is there a simple way of describing the decay of the magnetic flux mathematically?
There is.
We can use the following one-dimensional model.

Half of the space (z<0) is a vacuum in which a constant flux density B = B0iy is assumed.
The corresponding vector potential (assuming no variation in the transverse direction [UNK] is [UNK], where A0 and A1 are constants.
The other half of the space (z>0) is filled with a type I superconductor.

The approach I am going to adopt now applies to the present section only and acknowledges the fact that a superconductor is not an "ordinary" magnetic material; it cannot be described by a "magnetic" constant, by assigning to it a certain value for [UNK].
Instead, a new macroscopic constant needs to be introduced.

We shall proceed similarly as in the case of conductors.
We assumed then that the electric field was proportional to the current density.
Now we shall assume that there is a linear relationship between the vector potential and the current density [UNK], where y is the new macroscopic constant.
Substituting eqn (3.84) into (3.11) and retaining the one-dimensional character of the problem, we get the differential equation [UNK], the relevant solution of which (disregarding the exponentially increasing term) is as follows: [UNK], where A2 is another constant.
Hence we get for the magnetic flux density [UNK].

The flux density reduces to 1/e of its value at a distance [UNK], which is called the penetration depth.
A typical value is λ = 60 nm (nm = nanometre), so the material is not very far from being a perfect diamagnet.

3.17.
Forces

Let us first work out the force upon a current element of length ds in the presence of a flux density B. According to eqn (3.7) the force on a point charge q is [UNK].
Assuming now that the magnetic field is constant over S0, the cross-section of the wire, the force upon all charges within the volume element S0ds must be the same.
Hence the total force on the current element is [UNK], and for a whole current loop we get [UNK].

If the magnetic flux density is constant over the whole loop then B may be taken out of the integral sign, and the remaining integration yields zero.
Consequently, there is no net force upon a current loop in a homogeneous magnetic flux.
There is, however, a torque which may be easily calculated for a rectangular loop.
In the specific example of Fig. 3.16 (your guess is correct if you think that the arrangement has something to do with electrical machines) there is a current-carrying loop capable to rotate around the horizontal axis in the magnetic flux (assumed constant) of the permanent magnet.
As may be seen from Fig. 3.16 (b) the forces on sides 1 and 3 balance [UNK] each other, whereas those acting upon sides 2 and 4 produce a torque.
The force on side 2 is [UNK] whence the torque comes to [UNK] where 0 is the angle between the plane of the loop and the vertical direction.

Next we shall work out the force upon a small current loop due to another current loop in the geometry of Fig. 3.17.
Owing to symmetry the magnetic field of loop I has only Hz and HR components.
In the vicinity of the z axis they are given by eqn (3.65).
We shall consider the forces due to each component separately.
The force due to Hz upon the current element in loop 2 is in the radial direction.
Integrating over all current elements the net [UNK] force is obviously zero.
For the other component, HR the force [UNK] is in the negative z direction.
(Remember from school?
"The force between two currents flowing in the same direction is attractive.")
Integration over the circumference yields [UNK].

Examples 3

3.1.
A current with a constant current density J0 flows in the z-direction between the cylinders [UNK].
Determine the magnetic field in the regions [UNK].

3.2.
A cylindrical column of mercury 10mm diameter carries a current of 100 A uniformly distributed over the cross-section.
Calculate the pressure due to the pinch effect, (i) at a radius of 2.5 mm and (ii) at the axis of the conductor.

3.3.
The resistance between a pair of electrodes immersed in an infinite medium of conductivity [UNK] is R. Show that the capacitance between the same pair of electrodes is [UNK] when the medium is changed to a lossless dielectric.
A general proof is required valid for any geometry.

3.4.
Two lossy dielectric materials are joined together as shown in Fig. 3.18. determine the voltages across each material and the surface charge density at the boundary if a voltage V is applied.

3.5.
Solve eqn (3.47) under the condition that the electric field is zero at electrode 1 (z = 0).

3.6.
Derive an expression for the magnetic field H at a point P distant a from the centre line of a long thin conducting strip of width b (Fig. 3.19) which carries a longitudinal current I uniformly distributed across its section.

3.7. (i) Prove that the magnetic field strength H at a point P distance R from the wire of finite length a (Fig. 3.20) is [UNK] [UNK] (ii) Deduce that the field strength at the centre of a square coil of side b, carrying a current I, is [UNK].
(iii) Determine the field strength at the centre of a current carrying loop which has the form of an n-sided regular polygon inscribed in a circle of radius a. (iv) Show that the above result reduces to that of (ii) when n = 4 and to eqn (3.65) (with z = 0) when n → ∞.

3.8.
With the aid of the transformation [UNK] bring eqn (3.55) to the form [UNK], where [UNK].

3.9.
The complete elliptic integrals are defined as follows [UNK].
Express the vector potential of the previous example in terms of elliptic integrals and work out its value when R = a = 0.1 m, I = 1A, z = a /12 (use Tables, e.g. Jahnke-Emde-Losch).

3.10.
When k<1 the complete elliptic integrals may be approximated by [UNK] and [UNK].
Show that the vector potential obtained in Example 3.9 reduces to those of eqns (3.60) and (3.64) under the respective assumptions.

3.11.
It is fairly simple to differentiate the elliptic integrals (see p. 49 of Jahnke-Emde-Losch, for the formulae) so if you have the patience derive the magnetic field from the vector potential of Example 3.9 and determine its value for the data given there.

3.12.
Eqn (3.70) gives the magnetic field on the axis of a solenoid of length I. Is the formula valid outside the solenoid?

3.13.
The magnetization curve of a certain steel is given by [UNK].
An anchor ring of this material has a mean diameter of 255 mm.
It is wound with 160 turns of wire carrying a current of 2.5 A. Calculate the flux density on the mean diameter.
What current is required to produce the same flux density after a gap of 0.5 mm wide has been cut in the ring?
What flux density is produced in the gap by a current of 7.5 A?

3.14.
The electromagnet shown in section in Fig. 3.21 is designed to give radial magnetic flux density B in an annulus of radius a and width [UNK] when energized with constant voltage V. Its coil is wound from copper of conductivity [UNK] and is located in the annular space inside the electromagnet which has the dimensions a, b, c shown in the figure.
The copper can be assumed to be uniformly distributed across the section but it only occupies a fraction [UNK] of the space available; the current density in the copper is to be J.

[UNK] Neglecting flux leakage, and the contribution of the magnetic material to the line integral, calculate the dimension b, the size of the copper wire, and the number of turns in the winding when B = 1 T, a = 20 mm, [UNK] = 1.5 mm, c = 0.1 m, V = 12 V, [UNK] = 5.7x107 Sm-1, [UNK] = 0.65, J =1.5x106 Am-2.
Explain why [UNK] must be less than unity and why the current density must be limited to J. Estimate values for the dimensions h1, h2 so that each section of the steel core shall be subject to approximately the same maximum flux density.

3.15.
From eqn (3.90) and from the Biot-Savart law show that the force between two arbitrary current-carrying loops (Fig. 4.8, p. 100) is [UNK], where [UNK] is a unit vector in the direction between the current elements ds1 and ds2.
(Hint; Use Stokes's theorem.)

## 4. Slowly varying phenomena

4.1.
The basic equations

IT is difficult to say what "slowly" varying is until I give examples of "fast" varying phenomena.
Thus for a proper appreciation of the distinction between "slow" and "fast" you have to wait for electromagnetic waves to be introduced, discussed, and digested.
For immediate use I offer only mathematics, but a little later (Section 4.3) I shall try to show the limitations imposed by the assumption of slow variation.

Mathematically, the definition is easy.
As long as [UNK], i.e. as long as the displacement current is negligible in comparison with the current of charged particles, we are in the "slowly" varying region.
Hence we disregard the displacement current term but have all the rest of eqns (1.1) to 1.7) as follows: [UNK].

There is only one equation we have not considered so far and that is eqn (4.3), which will probably look more familiar in another form.
Integrating eqn (4.3) over a surface and applying Stokes's theorem to the left-hand side, we get [UNK], where the line integral is over the closed contour of the chosen surface.
Using the definition of magnetic flux (eqn (3.22)) the above equation may be written in the form [UNK].

Remember eqn (2.5) [UNK], the definition of the scalar potential in terms of the electric field.
Substituting it into eqn (4.10) would always yield zero, and that is obviously incorrect because the right-hand side may be finite.
Thus the definition of eqn (2.5) is no longer applicable or we should rather say it is no longer sufficient.
We need something else besides the scalar potential for describing correctly a time-varying electric field.
The additional term may be obtained by substituting the vector potential for B in eqn (4.3): [UNK] and rearranging it in the form [UNK].
For the above equation to be satisfied the expression in the bracket must be equal to zero apart from the gradient of a scalar function (remember [UNK].
Thus the general form for the electric field is as follows [UNK].
The gradient of a scalar potential is still there but we have in addition the time derivative of the vector potential.

When studying static electricity there was no need to make any distinction between voltage and potential difference.
For the static case, by definition, [UNK].
For the time-varying case we still define voltage by the relation [UNK], but now it takes the form [UNK].

There is no reason why the line integral of the vector potential between two arbitrary points should be independent of the path.
This must be kept in mind when considering time-varying fields.
It is no longer unambiguous to talk about the voltage between two points.
It will, in general, depend on the path chosen.

For the static case the line integral of the electric field disappears when taken over a closed path.
For the time-varying case [UNK] is, in general, different from zero.
We shall introduce now the notation [UNK], where [UNK] is the so-called electromotive force.
It is rather unfortunate to call it a force because it isn't one.
At the same time one can have sympathy with those who devised the term because it is the tangential force per unit charge integrated over a closed path.
In other words it is the work done by taking a unit charge round a circuit.
The definition, eqn (4.17), though often used, is regrettably not sufficiently general.
When the closed path is in a wire loop and the loop is in motion then a force due to the magnetic field is present as well, giving rise to a finite amount of work in the same manner.
The more general definition will be discussed in Section 4.7.

For the time being we shall use eqn (4.17), which substituted into eqn (4.10) will yield [UNK], a restricted form of Faraday's law (for its general form, see Section 4.7).
This is valid for the case when the flux linking a stationary circuit varies as a function of time.

The dimension of [UNK] is that of voltage, so it is not surprising that many people refer to it as voltage or induced voltage, a usage into which I often lapse myself.
However, when we want to emphasize the ability of [UNK] to put charges into motion, it seems preferable to accord to it its full title, or at least its popular abbreviation in the form of e.m.f.

We have now derived a new law for slowly varying phenomena.
What can we say about the laws derived in the last chapter?
Are Ampère's law and Biot-Savart's law still valid?
And the relationship derived between the current density and the vector potential (eqn (3.15)), is that still valid?
Yes, all of them are still true as a good approximation as long as the inequality (4.1) stands.
A slowly varying current will produce a vector potential (or a magnetic field) varying at the same rate.

4.2.
The electric field due to a varying magnetic field

Let us consider a two-dimensional case where the magnetic field at a given moment is constant within a cylinder of radius a, and is zero outside this cylinder.
We shall further assume a sinusoidal time variation so that [UNK]

The assumed magnetic field is independent both of z and of the azimuth angle [UNK], hence the electric field follows the same pattern; it is independent of z and [UNK] and depends on R only.
Then eqn (4.3) yields the scalar differential equations [UNK].

We find by inspection that the solutions are [UNK].
The constant may be determined from the continuity of the electric field at R = a yielding [UNK].
This is quite interesting.
A time-varying magnetic field creates an electric field as suggested by eqn (4.3), but this is not necessarily a local relationship.
The magnetic field may be confined to a certain part of space but the resulting electric field will pervade all space.

What can we say about the line integral of the electric field?
It follows from eqn (4.9) that it is finite if the path encloses the time-varying flux but zero otherwise.
How does this appear in practice?
What happens if we place a conducting wire into the electric field?
The mobile charges in the wire are not the least concerned about the origin of the electric field.
They react in the same way whether the electric field is due to static charges or to a time-varying magnetic field; under the force qE they rearrange themselves so as to cancel the electric field inside the conducting material as shown in Fig. 4.1 (a).
There will now be an additional electric field (say Ec) due to the presence of these charges.
Note however that [UNK], hence the charges do not interfere with the line integral of the electric field around a closed path.
It is still true that [UNK] whether we regard E as the original field (without the contribution of the charges) or as if Ec were added to the original field.

So what is the voltage we are going to measure?
Let us take an ideal voltmeter (one that draws no current) and measure the voltage across the terminals of the wire.
The voltage measured still depends on the path.
We measure finite voltage if the time-varying flux is enclosed (Fig. 4.1 (b)) and zero voltage if no flux is enclosed (Fig. 4.1 (c)).

What happens if we have N loops (Fig. 4.2 (a)) round the varying flux?
Surely, we will have an induced voltage [UNK] in each one of them.
If we [UNK] connect the loops then the total induced voltage will be the algebraic sum of the individual voltages.
If we make up a helical coil (Fig. 4.2 (b)) the wires are going round always in the same direction so the voltages simply add and we may rewrite eqn (4.13) in the form [UNK], where [UNK] is the flux enclosed by each turn.

Let us go now one step further and consider a resistive wire ring (Fig. 4.3 (a)).
The force on the mobile charges is still qE but now the charges may follow the electric field all the way around the ring.
A current is set up corresponding to the J = oE relationship.
Then [UNK], where R1 is the resistance of the loop.
As may be expected the ohmic voltage drop in the wire will be equal to the induced voltage.

Let us next evaluate the line integral of the electric field over the closed mathematical curve shown in Fig. 4.3 (b).
As long as the total time-varying magnetic flux is enclosed, the line integral [UNK] will remain the same as in the previous example.
Note however that the electric field is different on Sections 1 and 3 and the line integrals on Sections 2 and 4 vanish altogether (because the path is perpendicular to the electric field).

Let us replace now the mathematical curve by thin wire.
What will determine the current flowing in the wire?
The tangential component of the electric field along the wire.
But then we obtain the answer that the current is larger in Section 3 than in Section 1, and no current flows in Sections 2 and 4.
Is that possible?
According to eqn (4.2) that is not possible.
Taking the divergence of both sides of eqn (4.2) we get [UNK], which may be recognized as the continuity equation for an incompressible fluid.
It means in our case (the same that commonsense would suggest) that the current in the loop must everywhere be the same.
It varies of course as a function of time but not as a function of the spatial coordinates.
So J must remain constant, but it can only remain constant if the tangential component of the electric field is constant as well.
Hence charges must appear (see Fig. 4.3 (c)), producing an electric field Ec.
which will counteract the induced electric field Ei so that the resultant electric field E = Ei + Ec is constant everywhere along the wire.

What difference will it make if the wire loop is placed in the magnetic field as shown in Fig. 4.4?
There will be a current produced by the electric field as [UNK] before; the new feature is the appearance of a qv X B force on each charge element.
Since the velocity of the charge carriers is in the azimuthal direction, the force will act radially.
It is the same story again.
The charges cannot leave the wire so they will accumulate at the outer and inner surface of the ring until a radial electric field is produced that will cancel the force due to the magnetic field.

In conclusion, I wish to emphasize that all the charge rearrangements discussed in this section occur very fast, much faster than the period of oscillation of the magnetic field.

Inductance and mutual inductance

We shall start again with a resistive ring but make two modifications.
The externally impressed voltage need not come from a time-varying magnetic field as in the previous section, it may be produced by a signal generator.
Secondly, we shall take into account the voltage induced by the current flowing in the ring.
If you solve the field problem and exercise due care in getting the signs right, you will find that the induced voltage is such as to oppose the voltage that created it.
For this reason it is often called a back e.m.f.

The resulting equation is [UNK].
But according to Faraday's law [UNK], hence [UNK].

We shall now define self-inductance by the relationship [UNK].
Substituting the above definition into eqn (4.32) and changing from [UNK] to d/dt we get [UNK], as known from circuit theory.
Eqn (4.34) is suitable for the measurement of L. We impose a sinusoidal V ext, we know R (from calculations or measurement), we measure I, calculate dI/dt, and then L, being the only unknown, is determined.
Can we calculate L?
Not easily.
Even for such a simple geometry as the ring there are lots of difficulties.
In Section 3.7 we managed to get simple expressions for the magnetic field far away from the ring and in the vicinity of the axis.
But in order to calculate the flux across the ring we need to know either the magnetic field at every point in the interior of the ring or the vector potential along the perimeter of the ring.
Eqn (3.56) is complicated enough and that does not even take account of the finite diameter of the wire.
So the problem is pretty complicated.
Reference books give the answer [UNK], where d is the diameter of the wire.
This looks simple enough but, believe me, a lot of sweat has gone into producing that formula.

Eqn (4.34) is of course true for any closed circuit upon which a time-varying voltage is impressed.
In general, R is the resistance of the circuit and L may be obtained from eqn (4.33), where [UNK] is the flux enclosed by the circuit.

Can one determine the inductance of any of the practical configurations with relative ease?
Yes, there are a few, e.g. a two-wire transmission line which is nothing else but two parallel wires carrying opposite currents.
For two infinite line currents the magnetic field was given by eqn (3.53).
We get the flux per unit length by integrating the flux density over the space between the wires (assumed to be infinitely thin), as follows: [UNK].

Unfortunately, the above integral diverges.
What's wrong?
Obviously the limits: we should not have taken the wires infinitely thin.
These infinities are our best friends and worst enemies.
By taking things infinitely long and infinitely thin and infinitely something else, we can arrive at simple formulae.
When later we want to use those formulae it turns out not infrequently that we have some divergent results.
In the present case the remedy is clear and easy.
We need to assume a finite wire diameter, and we can do that without landing in a sea of further complications.
This is because wires used in practice (e.g. copper) are non-magnetic: we don't need to worry about boundary conditions at all.
The only difference between copper wire and air is that the former carries the current.
There is no reason now for the current density to deviate from uniform distribution over the cross-section, so eqn (3.53) still correctly describes the magnetic field between the wires.
Consequently, the flux per unit length between the wires is [UNK], where a is the radius of the wire.
Is this the total flux?
No, because the magnetic field can penetrate the wires.
The contribution of a single wire may be determined with reference to Fig. 4.5.
At a radius r the amount of current enclosed is (r/a) 2I, hence the magnetic field from Ampère's law is [UNK] yielding for the flux per unit length inside the material [UNK].

If b>a then this internal flux may be neglected giving the often quoted formula for the inductance per unit length of a two-wire transmission line [UNK], but remember there is an internal flux as well (and a corresponding internal inductance), which may not always be negligible.

Next we shall look at a long solenoid filled with a high-permeability magnetic material as shown in Fig. 3.9 (p. 73).
Then the magnetic field inside the material (from eqn (3.72)) is [UNK], uniform across the cross-section (of area S0) of the core.
Hence the magnetic flux produced inside the solenoid is [UNK].

The voltage induced in each turn of the solenoid is [UNK] hence the self-inductance comes to [UNK].

Let us tap now our solenoid at a certain point (Fig. 4.6 (a)) so that [UNK].
We have now two separate solenoids with N1 and N2 turns respectively.
How could we determine their inductances?
Nothing can be simpler, just use eqn (4.43) above and get [UNK].

I am afraid the above formulae are wrong because our new solenoids don't look the same as the old one.
As shown in Figs 4.6 (b) and (c) the new [UNK] solenoids have a core of length l, although the wiring is confined to lengths l1 and l2 respectively.
Since the magnetic material is still endowed with the property of concentrating the field lines in itself, the flux stays constant for the whole length of the core, yielding [UNK].

If the core makes up a closed circuit as shown in Fig. 4.7 (a) then l should be taken as the length along the dotted line and eqn (4.43) is still applicable.

[UNK] In all of our examples so far we could calculate the flux through a simple surface.
but how should we take the surface when there is no magnetic material to guide the field lines and the wire itself is of a complicated shape?
Then even the choice of the surface (having the wire as its boundary) might tax to the limit one's meagre imagination, let alone the calculation of the flux.
The practical answer is "don't calculate the inductance, measure it," but if for some reason you must do the calculation, the best approach may be to abandon the definition of eqn (4.33) in favour of the equivalent energetic definition (see Section 4.12) [UNK].
It might be simpler to find the total energy in space than the flux crossing a given surface.

[UNK] We shall now go over to the definition of mutual inductance with the aid of Fig. 4.8.
The current [UNK] flowing in loop 1 will produce a magnetic flux [UNK] through loop 2 leading to the definition [UNK].
There is a similar definition for M21 and it can be shown (see Example 4.4) that M12 =M21 =M.

If [UNK] is time-varying, the voltage induced in loop 2 is M (dI1, /dt).
The sign of M depends on the convention adopted for the direction of currents in the two loops.
Circuit engineers take the mutual inductance invariably positive and denote the direction of the induced voltage by a dot in the circuit diagram.
A current flowing into the inductance L1 at the dot produces a voltage V2 = M (dI1/dt) as shown in Fig. 4.9.

[UNK] Let us determine now the mutual inductance between two coils wound on the same magnetic core (Fig. 4.7 (b)).
The flux produced by a current in coil 1 is given by eqn (4.42), [UNK], where the subscript 1 referring to coil 1 has been attached to the current and number of turns.

Assuming now that all the flux produced by coil 1 will pass through coil 2 as well, we get for the voltage in coil 2 [UNK], whence [UNK].
It is interesting to note that [UNK].
If some of the flux produced by coil 1 does not pass through coil 2 (see Fig. 4.7 (b)) then [UNK] appearing in eqn (4.50) is smaller leading to a smaller value of mutual inductance.
Thus when some flux "leaks away" eqn (4.52) becomes an inequality: [UNK].

Alternatively, one may introduce a coupling coefficient [UNK] and rewrite eqns (4.52) and (4.53) in the form [UNK].
The above relationship turns out to be true for any two magnetically coupled circuits.
The proof will be provided in Section 4.12.

Next we shall determine the mutual inductance between two concentric rings at a distance h apart (Fig. 3.17, p. 82) under the assumption that the upper ring is small.
We need to find the magnetic flux through ring 2 due to the current in ring 1.
We can use the formulae derived in Section 3.7 for the vector potential and magnetic field in the vicinity of the axis.
With the aid of eqns (3.64) and (3.65) we obtain the magnetic flux in the form [UNK] from the vector potential, and in the form [UNK] from the magnetic field, giving of course identical results.
The mutual inductance is then [UNK].
Note that we have not so far specified the wire thickness of either ring.
For the mutual inductance it is not needed.

Finally, I want to say a few words about the assumption of "slowly varying currents" in connection with the last example.
As you know, any electromagnetic disturbance (any change in anything) propagates with the velocity of light, something we have so far neglected to take into account.
When calculating the mutual inductance we assumed that the magnetic field due to I1 appears instantaneously at the second ring.
In fact it takes time, the maximum time being equal to [UNK], where l is the largest possible distance between any two points in Fig. 3.17.
If the current I1 may be considered constant during the time [UNK] then we are entitled to talk about slow variation.

For sinusoidal current variation the condition is that the period of oscillation T should be much larger than [UNK].
Using the relationships T = 1/f and c = [UNK] (where f and [UNK] are the frequency and wavelength of oscillations) the condition may be written in the alternative form [UNK].
This is clear.
As long as the maximum dimension involved is small in comparison with the wavelength, we are in the slowly varying region.

4.4.
Kinetic inductance

We have defined inductance by eqn (4.33) without discussing its effect upon the current-voltage relationship.
Let me now briefly recall what an inductance does in a circuit.
It delays things.
If we apply a voltage the current will appear after some delay.
If we switch off the voltage the current will disappear after some delay.

Is there anything else in an electrical circuit that behaves that way?
That reminds me meeting an American friend of mine after he completed his grand tour of Europe.
"D'you know," he told me, "that I can ask for the check in seventeen languages?"
"Eighteen," I said, "I bet you forgot to include" bill .""
As the above story shows it is often difficult to think of the obvious.
In order to have a current, charge carriers must be accelerated, and it takes time to accelerate particles of finite mass.
Hence the current will necessarily lag behind the voltage causing its rise.

Let us put now the relations in mathematical form.
We shall write up Newton's equation for the case when the force is provided by an electric field and friction is present [UNK], where k is a constant characterizing friction (to be related presently to more familiar constants).

For a cylindrical piece of conducting material of length l and cross-section S0 [UNK], which substituted into eqn (4.59) leads to [UNK].

We may formally write [UNK], where [UNK] is the kinetic resistance, and [UNK] is the kinetic inductance.

If you think a little about it you will be able to convince yourself that Rk is nothing other than the old familiar resistance (proportional to length; inversely proportional to cross-section) derived in a different manner.
Whether one defines a conductance or introduces a friction term they are just two different ways of expressing the empirical fact that the electrons' velocity does not go on increasing indefinitely in response to a driving electric field.

Does the same apply to the second term?
Is that also a different derivation of the inductance?
No, in deriving eqn (4.61) we have not talked about magnetic fields and induction at all.
The kinetic inductance owes its existence to inertia.

Why is eqn (4.64) so little known?
Because under normal circumstances this kinetic inductance is negligible.
Comparing eqns (4.63) and (4.64) you may see that Lk = Rk/k, and if you determine k from the identity [UNK] you will find for copper that [UNK].
So you can see that the time constant involved is very small.
The kinetic inductance does, however, acquire importance in superconductors, where the resistance disappears altogether.
It may be seen by comparing eqns (4.64) and (4.35) that for a ring made of sufficiently thin wire the kinetic inductance may exceed the ordinary magnetic inductance.
And this may very well occur in practice because superconductors used in integrated circuits can have cross-sections less than 10 -12 m 2.
It may be said in general that the designer of a superconducting circuit needs to worry about the response time and energy of superconducting electrons.

The transformer

Let us return to the configuration of two coils on a magnetic core (Fig. 4.7) and apply a sinusoidal voltage to coil 1 from an ideal voltage generator (having zero internal resistance).
In response to the applied voltage there will be a current producing a flux that will induce voltages both in coils 1 and 2.
If the coils are lossless then the voltage induced in coil 1 must balance the, applied voltage, yielding [UNK].

Assuming for the moment that all the flux is contained within the magnetic core (so that the amount of flux crossing coils 1 and 2 is the same), the open circuit voltage in coil 2 is [UNK], leading to the familiar relationship [UNK].

Under open-circuit conditions there is no current flowing in coil 2.
The current in coil 1 may be obtained from the relationship [UNK].
For an applied voltage of [UNK] we get [UNK].

What happens if we connect a resistance RL across the terminals of coil 2?
A current I2 will flow.
But the total flux should not be affected because it is still related to the applied voltage by eqn (4.66).
Hence an additional current [UNK] will be drawn from the generator so as to satisfy the equation [UNK].

If L1 is sufficiently large so that [UNK] then [UNK] may be taken as the total primary current I1, leading to the relationship [UNK].

Eqns (4.68) and (4.73) are known as the relationships valid for ideal transformers.
They are certainly very useful for an engineer because they relate practical requirements (e.g. how large the voltage should be at the secondary) to design parameters (what the turns ratio should be).

How are transformers represented by circuit engineers?
Well, the circuit representation shown in Fig. 4.9 is perfectly adequate for lossless transformers, but it would not yield the equations for an ideal transformer, not even for the case of perfect coupling, k = 1.
For an ideal transformer we need to introduce a separate notation which we shall choose in the form shown in Fig. 4.10.
The relationship between the two kinds of notations is not an [UNK] obvious one.
It may be shown (using the criterion that they lead to the same set of equations) that by adding the so-called leakage inductances to the ideal transformer the two representations (Fig. 4.11) become equivalent.

[UNK] One may add copper losses (resistive losses in the wires) in a similar manner.
If you want to include iron losses (occurring in the magnetic core due to the periodically change flux) as well, you should better consult a book having a bigger section on transformers.

4.6 Relative motion of conducting wire and magnetic field

Up to now all the wires have been stationary, and the magnetic field has varied as a function of time.
Let us see now what happens when the wires are made to move with uniform velocity.
As our first example we shall take a straight piece of wire moving perpendicularly to the direction of a static magnetic field.
As a consequence there will be a force qv X B acting on the charges in the wire; the mobile charges will be displaced until the arising electric field produces an equal and opposite force.

Let us investigate now the converse problem when the wire is stationary but the equipment producing the magnetic field is moved lock, stock, and barrel with the same velocity in the opposite direction.
One's first impression is (or should be) that only relative motion counts, hence the force upon the charges should be the same.
Formally, we would have the same force if we assumed (as many textbooks do) that a magnetic field moving with a velocity in gives rise to a force [UNK].
This is a way out of the problem but not a way open to us.
We have started by writing down Maxwell's equations and claimed that they will provide the solution to any electromagnetic problem.
We are not entitled to introduce a new force.
According to our equations a magnetic field, whether it moves or not, cannot produce a force on a stationary charge.

What should we do?
Well, perhaps the trouble is that we wrote down Maxwell's equations in a stationary frame of reference.
In order to tackle the present problem we should change to a coordinate system moving with the magnetic field.
This is certainly a possible approach, and one we shall adopt towards the end of the course when discussing relativity, but such a transformation (though convenient) should not be necessary.
Maxwell's equations written in the stationary frame of reference should be perfectly capable of dealing with the problem.
Why is there a doubt at all?
Some doubts may arise by considering the following problem.

Let us postulate the existence of a static magnetic field that is constant over a finite region of space, say [UNK], and assume that this magnetic field is bodily moved in the +x direction with a velocity u.
What will happen to the charges in the stationary wire situated at (say) x = 0?
One may argue that by moving the magnetic field nothing has changed at the position of the wire.
The magnetic field is unchanged and there cannot be an electric field either because a constant magnetic field is unable to produce an electric field.

The above argument is wrong; don't let yourself be misled.
Induction is not a local phenomenon.
Although [UNK], it does not follow that the electric field is also zero at x = 0; the curl of the electric field must be zero but not the electric field itself.
When the magnetic field is moved bodily there will be certain places in space where the magnitude of the magnetic field is changing (shaded areas in Fig. 4.12) as a function of time, and that changing magnetic field can give rise to an electric field at x = 0.
The electric field will then produce just the right force for displacing the electrons by the right amount.

[UNK] Let's attempt to obtain a general solution of this problem.
We shall assume a static magnetic field [UNK] which will vary as [UNK] when moved bodily by a velocity u.
The equation to solve is eqn (4.3) which we shall write here again: [UNK].
By differentiating eqn (4.77) we get [UNK].
But according to eqn (A.7) [UNK] solution of eqn (4.3) may be recognized as being given by [UNK].

We are now entitled to write the force on the charges as [UNK].
If the magnetic field is moved with a velocity -v the force on the charges is the same as if the wire moved with a velocity v, and we have managed to prove all that from Maxwell's equations.

4.7.
Faraday's law

In order to derive the general form of Faraday's law we need to notice that motion of charge along the wire may be caused both by electric and magnetic fields.
Hence for the calculation of e.m.f. in a moving loop we should take both effects into account leading to a definition in terms of the force per unit charge as follows: [UNK].
Making use of eqn (4.79) and of the vector derivative relation [UNK], we get finally [UNK].
This is the general form of Faraday's law where the derivative is now taken in the frame moving with the wire.

4.8.
Flux cutting

Let us take a loop immersed in a magnetic field as shown in Fig. 4.13 (a) and assume that a section of the loop moves a distance dl coming to a position shown in Fig. 4.13 (b) after a time dt.
This elementary piece of wire moving with a velocity dl/dt contributes to the e.m.f. the amount [UNK] which may be rewritten in the form [UNK], where [UNK] is the amount of flux cut by the moving part of the loop.
If several distinct sections of the conducting loop are in motion then the flux cut by each section needs to be summed algebraically (each contribution taken as positive or negative depending whether the motion of that section increases or decreases the flux linkage).

The conclusion is that eqn (4.84) is valid under a new set of conditions.
The change of flux may be interpreted as the amount of flux cut by the moving sections of the loop.

4.9.
Examples on wires moving in a magnetic field

In the following examples we shall use Faraday's law for calculating the e.m.f. in moving loops.

Let us first take a static one-dimensional magnetic vector field pointing in the z direction and varying sinusoidally in the y direction as [UNK], where B0 and k are constants.
Assume that a loop lying in the x, y plane (dimensions shown in Fig. 4.14) moves with a uniform velocity v in the [UNK] direction of the positive y axis.
For simplicity we shall further assume that the length of the loop in the y direction is smaller than the period of the magnetic field, [UNK].
If the rear section of the loop is situated at y = -b/2 at time t = 0, then the positions of the rear and front sections will be [UNK] at time t.
The flux enclosed is then [UNK] and the resulting e.m.f. is [UNK].

For our second example we shall take a magnetic field varying sinusoidally both in space and in time: [UNK].
Assuming the same loop travelling with the same velocity as in the previous example, the flux through the loop varies as [UNK], yielding [UNK].

Let us consider now a somewhat different example where instead of uniform translation the loop rotates in a constant magnetic field.
This may occur in the same physical configuration as that of Fig. 3.16 (p. 81) used for calculating the torque upon a single turn of current-carrying wire.

Assuming that θ = 0 at t = 0 the angular position of the loop is given by [UNK] and the flux across the loop may be obtained as [UNK], whence the e.m.f. is [UNK].

Are you quite happy with this result?
I suppose you are.
A single turn rotating in a constant magnetic field is one of the standard examples of the application of Faraday's law.
The result is used for the design of a.c. generators so it must be all right.
Nevertheless, just a tiny little doubt should lurk somewhere at the back of your mind.
In this example we are not concerned with uniform translation of the loop but with rotation.
The loop is subjected to acceleration; there is a centripetal force acting upon the electrons inside the wire.
The present approach is permissible only under the condition that the centripetal force is negligible in comparison with the ev X B force.

The ratio of the two forces may be expressed as math; where [UNK] is the so-called cyclotron frequency.
Thus effects of the acceleration are negligible as long as [UNK].
In a practical case (say) B = 1 T and the loop rotates at 3000 revolution per minute, yielding [UNK], so we have a safe margin.
Nevertheless, keep in mind that results derived for stationary or uniformly moving bodies will not necessarily apply when the body is accelerated.

The concept of flux cutting could have equally been used in the calculations involving static flux.

In our first example where the magnetic field varies according to eqn (4.87) the flux cut by the front part of the moving loop in a time dt is [UNK], and the amount cut by the rear part is [UNK].
Hence the net flux cut is [UNK], yielding [UNK], in agreement with eqn (4.90).

4.10.
Eddy currents

In this section the effect of an e.m.f. on a solid piece of conducting body is studied.
In response to the e.m.f. a current (an eddy current) flows which will, in general, take very complicated paths.
We shall now take a very simple case when a conducting disc of thickness [UNK], radius b, and of conductivity [UNK] is placed in the magnetic field of eqn (4.19) so that the axes coincide.
For simplicity we shall further assume that b<a that is the disc is completely immersed into the magnetic flux.

In the absence of the disc the electric field is given by eqn (4.22).
Assuming that the magnetic field produced by the currents in the disc is negligible in comparison with the magnetic field postulated, the electric field distribution remains the same and the corresponding current density is given by [UNK].

At a radius R the current flows in the azimuthal direction in a tube of cross-section [UNK] the average power dissipated by this current is [UNK] (cross-section) 2 × (resistance of the tube) [UNK].

The total power dissipated in the disc may then be obtained by integration as follows [UNK].

How could we reduce the eddy-current losses in the disc?
First, we have to choose a low-conductivity material.
Secondly, we could interrupt the currents by insulating various parts of the disc from each other.
These problems do indeed arise whenever the magnetic cores of coils and transformers are made of conducting materials (mostly iron).
Both remedies suggested above are put into practice.
The iron is made into a high-resistivity material by adding silicon, and its cross-section is laminated as shown in Fig. 4.15.

4.11.
Electromotive force produced by rotating disc

We shall now consider the case when the solid conducting bodies are in motion, the simplest example being when a disc is rotated in a constant magnetic field as shown in Fig. 4.16 (a).
There will now be a q (v X B) radial force on the charges resulting in charge separation and in the appearance of an electric field.

Let us complete now the circuit with the aid of wires and brushes (Fig. 4.16 (b)) and insert an ideal voltmeter.
What is the voltage measured?
It is equal numerically to the e.m.f. in the closed circuit.
Since the wires are stationary only the disc contributes to the e.m.f., hence the integration over the closed path reduces to integration along the radius of the disc, yielding [UNK].

Can we work out the e.m.f. with the aid of the concepts of flux linkage or flux cutting?
Not easily.
If we choose the circuit in the form shown in Fig. 4.16 (c) there is neither flux linkage nor flux cutting.
However, if we choose our loop as shown in fig. 4.16 (d), where the boundary moves with the rotating disc, the both flux linkage and flux cutting make sense and lead to the desired result.

Let us now make the problem a little more complicated by assuming that only part of the disc is in an appreciable magnetic field, as shown in Fig. 4.17 (a).
What happens if we rotate the disc.
An e.m.f. will duly appear.
[UNK] Why?
In the region permeated by the magnetic field the charges are subjected to radial forces and as a consequence eddy currents will flow.
The resulting current distribution would be terribly difficult to calculate, but one can make rough guess and claim that it will flow along the dotted lines shown in Fig. 4.17 (b).
Omitting the voltmeter from our circuit, so that a current can How in the resistive wire, it may be seen that some of the current will be forced through the wire hence the device works as a generator.

4.12.
Energy and forces

The force acting on a circuit placed in a magnetic field is given by eqn (3.90).
If we have (say) two circuits then the forces upon each other may be calculated by determining first the magnetic field over all space and then applying eqn (3.90).
An alternative method is to derive first the energy of a circuit (or circuits) and then use the principle of virtual work to find the force.
In this section we shall have a brief look at the latter method.

How can we find the energy of a current-carrying circuit?
The answer may be easily obtained with the aid of circuit theory.
If we start with the initial condition that I = O at t = 0 and at a later time t the current rises to I then the work done on the inductor is [UNK].

The same result may derived from field theory in the following manner.
If a current element I ds is displaced parallel to itself a distance dl in a magnetic flux density B then the work done is [UNK], leading again to [UNK].

For two coupled inductors a similar derivation (either by circuit or by field theory) yields [UNK].
Let us rewrite the above equation in the following form [UNK].
Since the stored energy must always be Positive for any pair of I1 and I2, we may choose [UNK], whence it follows that the condition [UNK] is valid for any two coupled inductors.

Let us take now two rigid loops in which constant currents I1 and I2 flow.
The total stored energy is given by eqn (4.108).
What is the change in energy if we move one of the loops by a distance dx?
The self-inductances will stay constant (because the loops are rigid), but the mutual inductance depends on the distance between the current elements so it will change by an amount dM.
Thus the change in stored energy comes to [UNK], whence one could conclude that [UNK].
This is, of course, wrong as we could have guessed on the basis of our experience with forces acting upon capacitor plates.
We need to include the work done by the sources in keeping the currents constant.
This amounts to [UNK].
Hence [UNK].

As an example let us now work out the forces between two current-carrying rings with the aid of our new formula.
The mutual inductance is given by eqn (4.57).
The force may then be calculated as [UNK], in agreement with eqn (3.93).

Examples 4

4.1.
A circular coil of diameter 20 mm has 100 turns and lies at the centre of a solenoid for which s = 0.3 m, d = O.1 m, and n = 800, the coil and the solenoid being coaxial (s = total length, d = diameter, n = turns per metre).
What is the e.m.f. induced in the open-circuited coil if the solenoid is fed with a current of 3A at 50 Hz?

4.2.
Fig. 4.18 shows the cross-section of a straight transmission line carrying currents [UNK], where w is the angular frequency and I0 is a constant.

Derive a formula for the e.m.f. induced around a loop comprising a length of l of short-circuited cable running parallel with the transmission line.
Assume that d>a and b<a.

Calculate the e.m.f. when I0 = 1000 A, a = 1 m, b = 3 mm, d = 5 m, w = 100 [UNK], l = 1 m.

4.3.
A long, thin-walled, non-magnetic, conducting tube of radius R, wall-thickness [UNK], and conductivity [UNK] is placed with its axis parallel to the direction of a uniform alternating magnetic field [UNK].

Determine the current per unit length flowing in the wall, the magnetic field inside the tube and the average power dissipated per unit length.
Neglect edge effects that is assume no change in the variable along the tube.

4.4.
Show that the mutual inductance between two arbitrary coils may be written in the form (see Fig. 4.8, p. 100) math;.

4.5.
"Eqn (4.57) gives the mutual inductance of two concentric rings a distance h apart from each other.
If a1 and a2 are interchanges the mutual inductance will not remain invariant, defying the M12 = M21 relationship.
What is the cause of this discrepancy?

4.6.
Determine the mutual impedance between the coil and the solenoid of Example 4.1.

4.7.
Eqn (4.57) gives the mutual inductance of two concentric rings a distance h apart from each other.
Assume that ring 1 carries a [UNK] and the resistance and self-inductance of ring 2 are given as L2 and R2.

Show that the mean value of the force F between the two rings (i.e. averaged over the periodic time of the alternating current) is given by [UNK], and say which way it acts.

It is desired to maximize the ratio (F/weight of ring), and for this purpose it is necessary to decide whether for any given geometry it is better to make the ring of copper or of aluminium.
Is it possible to give an answer without having numerical values for anything except the properties of aluminium and copper? [UNK].

4.8.
Assume an axially symmetric radial magnetic flux density in empty space between the radii R1 and R2 which is constant in the vertical direction (z).
Place now a thin wire of radius [UNK] into the magnetic field at a height z so that its plane is perpendicular to the Z-axis, and each element of the wire is subjected to a constant radial flux density Br.
At t = 0 the ring is released with zero initial velocity,

(i) Derive the equation of motion for the ring and show that it is independent of the cross-section of the wire.

(ii) Determine the position and velocity of the ring as a function of time.

(iii) What is the limiting velocity as t → ∞?

(iv) In which case will the ring fall faster, if it is made of copper or of aluminium?

4.9.
A transformer supplied from a 220 V, 50 Hz mains has an iron core in which the peak flux density, 0.66 T, is reached at a magnetic field of 150 A m-1.
The cross-section of the core is 1.5 - 10 -3 m 2 and its volume is 9 × 10 -4 m 3.

Determine the magnetization current and the number of turns in the primary circuit.

4.10.
A rectangular loop moving with a velocity v is shown schematically in Fig. 4.14 (p. 109) and the resulting e.m.f. is given by eqn (4.90).
Assume now that the loop is stationary and the magnetic field (given by eqn (4.87)) moves with the same velocity in the opposite direction.
Determine the e.m.f. by taking the line integral of the electric field around the loop.

4.11.
A rectangular coil is located parallel to a long straight current-carrying wire as shown in Fig. 4.19.
Determine the e.m.f. in the coil when it is rotated with an angular velocity w.

[UNK] 4.12.
Take the same geometrical configuration as in the previous example but assume that the rectangular coil is moving with a constant velocity u in a direction perpendicular to the straight wire.
Determine the e.m.f. in the coil.

4.13.
Find the torque which tends to align the rotor in the arrangement shown in Fig. 4.20 with 0 = 45° and 135°, (i) when the rotor carries no current, and (ii) when it carries a direct current of 2 A. The rotor inductance is 1 H and the stator inductance has maximum and minimum values 1 H and 0.2 H. Assume that periodic inductances vary in a sinusoidal manner and that the coils are perfectly coupled when they are in line.

