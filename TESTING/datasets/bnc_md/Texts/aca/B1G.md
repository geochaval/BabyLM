# Handling geographical information

## Methodology

### The areal interpolation problem: estimating population using remote sensing in a GIS framework

#### Introduction

Data integration is one of the fundamental GIS operations (Burrough 1986).
It involves transformation of data so that they are reported at a comparable geographical scale, projection and set of geographical units.
The need for data integration arises because many of the questions which scientists and social scientists investigate require data from a wide range of sources which are only reported on disparate spatial bases.
Data integration is especially a problem for geographers because information synthesis is at the very heart of the discipline.
The difficulties of integrating data are compounded by the fact that there are few standards governing the way in which geographical data are collected and reported.
Hearnshaw et al. (1989), for example, highlight the problem in the context of Leicestershire, a county in the Midlands of England, and show the difficulties of linking enumeration district (ED), ward, parish and postcode data.
Similarly, Openshaw et al. (1986) report that the data in the Domesday System are available for 25 different and incompatible types of areal unit.

Strategies for integrating data reported at different geographical scales and for different map projections have received considerable attention over the past few decades (Robinson et al.1984; Burrough 1986).
Although there are still a number of problems to be solved, in contrast to the difficulties of comparing data reported for different spatial units, these aspects of data integration are fairly well developed and understood.

In this chapter we concentrate on the problem of integrating geographical data reported for different areal spatial units, one of the most intractable of all data integration problems.
A fuller description of the process of data integration is presented by Flowerdew and Green in Chapter 4.

#### Areal interpolation

There have been a number of published attempts to provide solutions to the cross-area aggregation, or 'areal interpolation' problem (Goodchild and Lam 1980; Lam 1983).
These have been summarized and classified by Flowerdew and Openshaw (1987) and several examples are given in Hearnshaw et al. (1989).
The areal interpolation problem can be defined as the transfer of data from one set (source units or zones) to a second set (target units) of overlapping, non-hierarchical areal units.
Where the source zones nest hierarchically into the target zones, for example UK administrative EDs nest exactly in wards, transfer of data from the source units to the target units is one of simple aggregation.
However, where the units are overlapping and non-hierarchical the problem is more complex and it is this that we investigate here.
The nature of the problem can be illustrated with an example.

A common problem in geographical information systems (GIS), and one which has been known about for many years in the context of choropleth mapping, is that of producing maps from population data aggregated over selected arbitrary areal units.
In the UK, the decennial Census of Population records the number of individual people and households, but almost all population data are reported as various aggregations which ensure that data about individuals cannot be recovered.
Unfortunately, the aggregations are generally chosen for non-statistical reasons and so differ from data set to data set and are often unstable over time.
This makes any comparative analysis of data recorded at different times or using different aggregation units problematical.
The difficulty is particularly important in studies where it is necessary to find the denominator, in order to estimate the incidence of a property as a proportion of some population total.
For example, the numerator might be a count of people in a postcode sector who have, say, a cancer, yet, because the census and health data are reported for different areal units, it is not possible to find the appropriate at-risk population for the denominator and so compute a reliable incidence ratio.
Although this example relates to what have been termed 'imposed' areal units, that have no landscape reality (Unwin 1981), it is increasingly necessary to create aggregations of population over 'natural' areal units such as a soil association or outcrop of a particular rock type.

The solutions to this type of problem utilize either point interpolation or areal interpolation methods (Lam 1983) and these will be examined in turn.

The point interpolation methods essentially use a point, usually the centroid, as a surrogate for the areal units and then apply conventional point interpolation methods.
The crudest of these involves matching the centroids of source and target units by minimum distance nearest neighbour techniques.
A slightly less crude method is to use the centroids to generate a continuous surface by interpolation.
The target zones are then overlain and the interpolated value is transferred into the zones.
However, this technique is particularly unsuitable for population estimation because as Tobler (1979) points out, there is a danger that people can be created or removed.
Martin (1988, 1989) describes a simple algorithm that uses the ED centroids, with a spreading function to allocate people to neighbouring grid squares, which incorporates Tobler's idea.

An intermediate method between the point and areal methods uses point-in-polygon techniques (Burrough 1986) to locate the centroids of the source units in the boundaries of the target units.
Although relatively unsophisticated, this method is reasonably fast and it seems to work satisfactorily where the target units are much larger than the source units

Also in situations where the target units are much larger than the source units, polygon-in-polygon areal interpolation techniques can be used to obtain reasonable estimates by locating the source units within the target units.
A simple decision rule can be used to decide what to do in the case of source units which cross the target unit boundaries.
The most reliable and accurate estimates can normally be obtained using one of the true cross-areal interpolation methods.
Lam (1983) suggests that there are two types of true areal interpolation methods: polygon overlay and pycnophylactic interpolation (Tobler 1979).
These are well known and have been described elsewhere (Lam 1983; Wagner 1989).

The above areal interpolation methods are alike in that, other than the purely spatial information given by the boundaries, areas or centroids of the areal units involved, no extra information is used in interpolation.
In a truly integrated GIS framework (Jackson and Mason 1986) it is almost certain to be the case that other potentially useful information is available.
This additional information can be used for 'intelligent' interpolation.
Flowerdew (1988) developed a theoretically sound and very general statistical approach using Poisson regression which incorporated an additional binary variable.
He predicted the population characteristics of parliamentary constituencies in Lancashire (the target units) from district level data (the source units) using the party affiliation of the constituency's Member of Parliament as a binary variable.

In this chapter, we develop a method similar to Flowerdew's in which we use GIS techniques to enable areal interpolation to be informed by the distribution of land-cover types, as inferred from a classified Landsat Thematic Mapper (TM) image, in both the source (1981 Census wards) and target (National Grid kilometre squares) units.

#### The basic approach

The basic idea is simple.
A suitable satellite image is classified using image-processing techniques to identify the various types of land cover which exist over the entire study area at very fine spatial resolution.
Thus, for each census ward for which a 1981 population total exists, it is possible to determine the number of pixels classified as a certain land-cover type.
It is then feasible to express the known ward populations as a function of these pixel counts.
Provided the model relating population to these land-cover data is reasonably good, the resulting relationship can then be used to estimate populations for any set of imposed or natural areal units that can also be located on the image.

The use of remotely sensed data to inform population mapping is not new.
Previous attempts to estimate entire populations, especially of Third World cities, include studies by Ogrosky (1975), Lo and Welch (1977) and Han (1985).
Similarly, a number of authors have used vertical aerial photography to estimate residential densities across individual cities (see, for example, Collins and El-Beik 1971; Hsu 1971; Clayton and Estes 1980) while others have experimented with the use of satellite imagery (Iisaka and Hegedus 1982).
Convenient summaries of this previous work are to be found in Lo (1986) and Griffiths (1988).

The work described here involves four distinct steps.
First, there is the choice of satellite image and the production of a land-cover map.
Second, there is the overlay on to this map of the 1981 Census ward boundaries and summation of pixels falling into each of the recognized land-cover types.
Third, there is the statistical modelling of the relationship between population and land cover and the validation of the resulting model.
Finally, at the end of the process lies the estimation of the population over some target set of areal units, in our case the kilometre squares of the UK National Grid.

#### Obtaining a land-cover classification

A Landsat TM image of Leicestershire recorded on a cloud-free day in July 1984 constitutes the basic data source.
This area was selected for study because of the authors' familiarity with it, the adequate rural-urban contrast and the availability of a suitable image.
The ground resolution of a TM image is such that a pixel has about a 30 m side, which seems appropriate for the scale of analysis used.
Indeed, it may be that an image of higher spatial resolution, such as one obtained by a SPOT satellite (20/10 m), would prove counterproductive, giving too much local variation in pixel reflectance.
The full seven bands of image data were loaded into an ERDAS (Earth Resources Data Analysis System) software system and ground control point information entered to rectify the image to National Grid coordinates.
This rectified image was then subsetted to give an area covering the 49 wards that make up the districts of Oadby and Wigston, Leicester, and Charnwood in northern Leicestershire (Fig. 5.1).

Since a faithful classification of land cover is an essential component in the proposed scheme, several attempts were made in an effort to obtain a consistent and suitably detailed product.
An unsupervised classification provided an acceptable separation between rural and urban cover, but finer detail was concentrated in agricultural subdivisions at the expense of intra-urban differentiation.

Information on agricultural land use is unimportant to this application, whereas urban detail illustrating housing densities or alternative urban land is highly desirable.
A second classification was made using a supervised approach so that we could capitalize on our local knowledge of the study area.
The supervised approach enabled urban subdivision of dense and less dense housing.
The result was an improvement over the unsupervised product, and yet we still felt that further urban differentiation might be possible.

This led us to undertake a principal components transformation of the seven bands of image data, which gave encouraging results similar to those obtained by Forster (1985a).
As a data compression exercise, the first four components of the transformation reduced the storage requirement by 42 per cent for less than 1 per cent loss in information content.
However, of great significance was the information displayed in the transformed images.
The first principal component, carrying 50 per cent of the original variance, was dominated by land-cover differences in the rural area.
The second component (40 per cent of variance) revealed the urban distribution very clearly with a strong rural/urban differentiation.
The third component, despite carrying only 6 per cent of the original variance, revealed intra-urban differentiation with a clarity unseen in any RGB (red-green-blue (colour)), composite taken from the original bands.
The fourth component (2 per cent of variance) was dominated by the thermal infra-red band, recording thermal characteristics of the surface at poor spatial resolution.
Finally, the remaining three components seemed to consist of uninterpretable noise.

As previously stated, rural land cover was not an important consideration, and so the first component image was discarded, together with the last three, leaving components 2, 3 and 4.
When these components were displayed as an RGB composite they continued to show good urban differentiation, closely matching both our local knowledge of the area and the ground truth data that were collected.
The final attempt at classification involved a supervised classification of principal components, 2, 3 and 4.
This produced the land-cover classification shown for a part of the area in Fig. 5.2.
Other, similar attempts to produce urban cover classification using satellite data are discussed in Jackson et al. (1980), Forster (1983, 1985b), Wheeler (1985), Lam et al. (1987) and Griffiths (1988).
In an interesting variation of the work described here, Quarmby et al. (1988a) outline the use of census data to derive training sets for classifying urban areas into housing types.
Quarmby et al. (1988b) also discuss the use of SPOT data for monitoring urban land-use change in south-east England.

For analytical purposes, the 12 categories of land cover recognized during the classification stage were compressed into five representing:

- 1. Industry and commerce (presumably detected by large single buildings and different building materials);

- 2. Dense residential areas;

- 3. Ordinary residential areas;

- 4. Areas that logically have no population (quarries, woods, water bodies);

- 5. All agricultural land uses.

#### Overlaying census ward boundaries

In the second phase of the work, digitized 1981 Census ward boundaries and population totals were compiled using GIMMS and SASPAC (at Manchester Computer Centre).
These data were transferred into ERDAS and rasterized.
ERDAS GIS functions were used to overlay the ward boundaries on to the classified image and then count the number of pixels of each recognized land-cover type within each ward.
The result was a data matrix giving pixel counts for five land-cover types together with the recorded population for the 49 wards.
These data are summarized in Table 5.1 and Fig. 5.3 is a map of the population density.

#### Towards a statistical model

Table 5.2 shows the matrix of intercorrelations between these six variables.
The ward population, the response variable, has a relatively high positive correlation with the 'industry and commerce', 'dense residential' and 'ordinary [UNK] [UNK] residential' variables and low negative correlations with 'nobody' and 'agriculture'.
There are equally logical intercorrelations between the various land-cover pixel counts which are used as the carrier variables.

Our intention is to express the ward populations as some function of the pixel counts for each land-cover type.
It should be apparent that there is a very large number of possible models that might be used and, indeed, a number of considerations involved in making this choice (see Dunn 1989).
In particular, three such considerations influenced our analysis and selection of carrier variables.

First, there is a conflict between a desire to maximize the fit obtained, by inclusion of as many statistically significant terms as possible, and simple logic which suggests that the correct form of any fitted model should be a linear weighted sum of only those land-cover types that actually contain mostly housing (' dense' and 'resid') without any intercept term.
In such a model the weights themselves will have a direct interpretation as the average population density per Landsat pixel.
Second, although there is no reason to expect any model to be other than linear and additive, there is an argument, presented by Flowerdew (1988), which says that since the response variable compromises count data, the appropriate regression model should combine a Poisson error distribution with an identity link function (see Aitkin et al.1989; 217).
Third, there are a number of criteria for goodness of fit.
Although the usual coefficient of determination or scaled deviance can be used to indicate the global fit of any specified model, it is also important to examine model performance when estimating populations over areal units other than the wards from which the models were derived.
In this study, this was achieved by examining the estimated kilometre square populations together with those which were reported for the same areal units in the 1971 Census of Population.
Three methods were examined in detail using the MINITAB and GLIM packages.

##### A 'Shotgun' model

The overall regression equation, calibrated by ordinary least squares, relating population to the carrier variables is [UNK] Table 5.3 gives further details.
It will be seen that although the overall fit, at 84 per cent is good, only industry, dense residential and ordinary residential have significant regression constants.
The same set of variables used in a model with a Poisson error term gives the model [UNK] which is remarkably similar.

Figure 5.4 shows the standardized residuals for this model.
Four wards are particularly badly fitted.
In the western central area, two rural wards (Charnwood 16 and 17) actually have almost doubled the fitted value.
In the west of Leicester's urban area, Newton ward, with population 20 440, has a fitted value of only 13 495 and is badly fitted by all the models examined.
This is probably due to the large preponderance of low-rise multi-storey council housing.
Finally, there is an over-prediction of the population of [UNK] [UNK] central Leicester itself (The Castle ward), which is another feature shown by all the models.

Although this Shotgun model gives the best fit to the observed ward population data, it is logically flawed in at least two respects.
First, it is evident that the correct form of any model linking population to land cover should not have an intercept constant; if there is no residential cover, then there should be no population.
Second, three of the variables incorporated into it have negative signs, indicating that as the number of pixels of these types increases, so population decreases.
At first sight, this seems reasonable, but when the model is used to estimate populations of any other arbitrary areas there is a possibility that, if there is very little housing, it will predict negative populations.
A further point is that the Shotgun model includes a large number of carrier variables and that it is worth further investigation to see if a more parsimonious model provides a satisfactory relationship.

##### A 'Focused' model

It is thus argued that any statistical model linking pixel counts of land cover to population should be simple, linear, additive and without any intercept constant.
In such a model, the individual coefficients have a direct interpretation as the average density of people in each 30 m square pixel of the specified type.

The ordinary least squares focused model is pop 81 = 9.89 dense + 5.03 resid whereas specification of Poisson errors gives pop 81 = 10.93 dense + 4.82 resid Note that the estimated population densities for a 30 m square pixel for the two types of residential housing identified using the Landsat data seem reasonable and that this model cannot produce negative population estimates.
In the intercept constant form, this greatly simplified model has an R2 of 81.8 per cent.
The reduction to just the two land-cover categories, concerned with housing, loses only 3 per cent explanation when compared with the Shotgun model.
for these re; sons, the Focused model is considered to be superior to the Shotgun model.

Figure 5.5 shows the standardized residuals for the least squares Focused model.
The fit is reasonable over most of the area and, as might be expected, is broadly similar to that given by the Shotgun model.
Again it tends to under-predict values for wards surrounding the centre of Leicester (Humberstone, Aylestone and Newton) and massively over-predicts for The Castle ward which includes the city centre.
Here an actual ward population of 10 149 is predicted to be 18 373.

##### A 'Simple' model

The final model investigated is the simplest of all.
In this the 'dense' and 'residential' variables (equivalent to 'houses') were summed and regressed against population in a simple linear model.
Figure 5.6 shows that the plot of 'houses' against 'population' is remarkably linear, with a correlation coefficient of 0.869.

The ordinary least squares model, with forced zero intercept term, is pop 81 = 5.41 houses or, with Poisson errors: pop 81 = 5.40 houses [UNK] This result implies that each pixel classified as having people living in it, and there are 86 178 of these, will on average contain 5.4 people.
Examined in detail (Fig. 5.7) this simple model repeats the problems of fitting the city wards identified by both the Shotgun and the Focused models, but adds to this a tendency towards relative over-prediction in the rural wards to the north and east of the area.

#### An areal interpolation application

The final step is to use the results of these models to predict the distribution of population over other arbitrary areal units for which pixel land-cover counts can be obtained.
A particularly severe test is to use the results to estimate the population of the area over the kilometre square grid given by the UK Ordnance Survey.
In this, the estimation not only involves a cross-area element, it also embraces a considerable areal disaggregation, from an average ward size of 7.7 km² (range 0.74-38.7 km²) down to the individual kilometre square.

Figures 5.8-5.10 have been produced using UNIRAS to show the predicted 1984 population for the Shotgun, Focused and Simple models outlined above.
All three pick out the major features of the population density variation across northern Leicestershire but, of course, as they stand they are impossible to validate in any direct way.
First, the 1981 Census of Population was not made available for grid squares and, second, our estimates were produced using a 1984 satellite image and 1981 Census ward data.

There are two indirect ways of validating these estimates.
First, they can be compared with the actual distribution of population as reported on a grid square basis by the 1971 Census of Population (Fig. 5.11).
Figures 5.12-5.14 show the differences between the actual population for 1971 and the predicted population for 1984.
Table 5.4 provides a summary of the overall fit in the form of the root mean squares (RMS) of the differences for each map.
All point to precisely the same problems as were identified when evaluating the original model fits.
The average ward population is 9488 (Table 5.1) and so the RMS errors are comparatively small (the range of RMS errors is from 815.13 for the Shotgun ordinary least squares (OLS) to 1035.29 for the Simple Poisson).
There is little difference in the values obtained using OLS [UNK] [UNK] and Poisson regression and the Simple models produce only slightly higher errors.
Figure 5.12 shows the differences given using the Shotgun model which has the lowest RMS value.
Throughout most of the area, the differences are less than 1000.
In fact, only 30 (or 5.3 per cent) grid squares have absolute differences greater than this.
Unfortunately, some urban squares in Leicester and Loughborough have large individual differences which have a total range from -4466 to +6976.
Thirteen years, between the 1971 Census and the 1984 image used, is a long time and has encompassed considerable population change in both magnitude and distribution.
The general tendency of this model to overestimate central city population and underestimate around the urban fringe is consistent with the known pattern of change.
Figure 5.13 shows the same data for the Focused model which, although it has much the same proportion of grid squares with differences in excess of 1000 people, now gives a total range from -4799 to +8339.
Even Fig. 14, for the Simple model, has only 6.5 per cent of squares with absolute differences greater than 1000 but, as might be expected, the range is now from -3506 to +11 204.

A second indirect way of validating the regressions is to produce models relating population to 1981 land cover calibrated using the 1971 populations.
If the general approach is fairly robust, it ought to be that the relationship between population and land cover is fairly stable, so that we would expect the model coefficients to be similar to those obtained from the ward data.
Table 5.5 presents these coefficients, estimated using ordinary least squares, for exactly equivalent models to those reported in section 5.6.
It can be seen that in every case the two sets of coefficients have the same sign and general magnitude.
However, even allowing for the fact that the population and satellite data were collected 13 years apart, the differences are greater than we would have liked.

#### Conclusions and further work

We regard these results as encouraging.
They suggest that it is possible to use satellite remotely sensed data to help inform population mapping by allowing cross-area estimation and some element of areal disaggregation.
Given that the remotely sensed data add a great deal of information to these processes this is hardly surprising, but this general approach is relatively easy to carry out in a GIS environment.
We are currently extending this work in three ways.
We are applying this technique in another part of the East Midlands, as a further test of the utility of this approach.
We are working on other methods of classifying images, including textural classifiers, in order to improve the statistical modelling.
Finally, we are trying to obtain independent 1 km grid square estimates for the 1981 population.

### Error propagation: a Monte Carlo simulation

#### Introduction

The absence of facilities within GIS software for handling the effects of input data uncertainty and possible error propagation by GIS operations creates a question mark over the safe utilization of many aspects of the technology.
The problem arises because it is thought that the positional errors and attribute uncertainties which are characteristic of all spatial databases, may be propagated and amplified by GIS operations and thus adversely affect some or all applications.
These input data uncertainties are attributable to a number of sources ranging from errors in the original cartographic map documents through to the effects of the GIS operations themselves.
Specific types of error in digital map data include: locational uncertainty, measurement errors in digitization, map-scale-dependent accuracy and resolution, and classification and generalization error in both categorical and remotely sensed map data.
For thematic maps the principle cause of error is the original map document and its conversion to digital form.
For remotely sensed data error depends on the accuracy of the sensing device and the pixel classification technology used in image processing.

There is nothing new about the existence of map-related errors.
Error and uncertainty have always been a feature of cartographic information.
Previously, however, the worst effects were largely avoided by a combination of the expertise of the cartographer, who knew about the inherent generalization implicit in analogue maps, while the difficulty of manipulating maps by manual means precluded most forms of analysis likely to be sensitive to the effects of error.
The advent of GIS has significantly changed all this.
The ease of use and flexibility of GIS allow the user to perform operations on map data that were previously impossible on a large scale.
The typical end-user of GIS output will probably care or know little about the cartographic and uncertainty characteristics of the map data being used, while the GIS itself has no procedures for handling the varying accuracy and reliability of the digital map data being processed.
A GIS gives the user complete freedom to combine, overlay and analyse data from many different sources, regardless of scale, accuracy, resolution and quality of the original map documents and without any regard for the accuracy characteristics of the data themselves.
The mixing of geographical information from different map scales and sources is a key aspect of GIS functionality, but it does raise the question as to what effects the combination of different levels of data uncertainty has on both the output maps and on the data derived from spatial query and analysis.
It must be recognized that there are many good reasons for wishing to combine data in these ways, but a major problem arises because GIS packages fail to offer any means of keeping track of the effects of error propagation and how it affects the results.

Despite research into some aspects of the error propagation issue in spatial data processing (e.g. Blakemore 1984; Chrisman 1984; Drummond 1987; Goodchild and Dubuc 1987; Walsh et al.1987), Burrough (1986:103) correctly points out that 'It is remarkable that there have been so few studies on the whole problem of residual variation and how errors arise, or are created and propagated in geographical information processing, and what the effects of these errors might be on the results of studies made.'
This neglect is widely perceived to be a major unresolved problem.
Such is its importance that the National Center for Geographic Information and Analysis (NCGIA) in the USA, has placed this issue first in its list of research priorities (NCGIA 1989).

This chapter is concerned with developing methods able to provide estimates of the confidence regions around GIS map-based outputs by taking into account certain selected sources of uncertainty affecting spatial databases.
A Monte Carlo simulation-based approach is used as a general means of estimating the effects of input data uncertainty on the map outputs after an arbitrary sequence of GIS operations.
The objective is to identify and handle the effects of data uncertainty in a GIS by defining uncertainty envelopes to create 'credibility regions' around the results.
This is considered to be the minimum needed to allow a GIS to function in a mixed data environment.

#### Sources of error in GIS

Error and uncertainty are common features of cartographic information, so it is hardly surprising that these aspects are also present in digital versions of analogue maps.
It follows, therefore, that no map-related spatial data exist which are wholly error-free.
There are many different causes of uncertainty and those which are explicitly due to GIS-based manipulations of geographic information are merely a more recent problem.
However, it is also obvious that the power of GIS has the potential dramatically to increase both the magnitude and importance of errors in spatial databases.

Burrough (1986) identifies three main groups of factors that govern the errors which may be associated with spatial data processing.
These are:

- 1. Obvious sources of error;,

- 2. Errors resulting from natural variations or from ordinal measurements; and

- 3. Errors arising through processing.

Group 1 errors include such sources of age as the data, areal coverage, map scale and density of observations.
Group 2 errors include positional accuracy, attribute uncertainty, and generalization arising from data classification and spatial variations in map quality.
Group 3 errors include those arising through the processing of geographical data, such as numerical computing errors, faulty topological analyses and errors in interpolation.
The three groups represent errors of increasing complexity and difficulty of handling, such that those in groups 2 and 3 require intimate knowledge of the data, their structure and the algorithms used and some means of converting this knowledge into quantitative measures of impact.
It is useful to start by examining some of these sources of error.

##### Digitizing error

Despite the availability of hardware for the automated conversion of geographic data from paper maps to digital form (e.g. optical scanners) much data input to GIS is still done by hand using a digitizing table.
As a result of human and other complicating factors involved, a high level of error is often present in digital map data.
Manual digitizing is consequently recognized as a significant source of map error in GIS (Otawa 1987; Keefer et al.1988).
However, error introduced into digital map databases through the digitizing process is often ignored because the characteristics of digitizing error have not been fully defined and because no practical means of handling input data uncertainty exist within proprietary GIS software.

Sources of error in the digitizing process can be broken down into two main streams: source map error and operational error.
Source map error includes the accumulated error of the map being digitized, while operational error includes those errors propagated during the digitizing process itself.
In looking at the first of these it must be recognized that no map, however detailed or carefully compiled, can perfectly represent the 'ground truth', while in the second instance, the digitizing process merely serves to compound the errors present in the original map (Poiker 1982; Blakemore 1984).
Going back to the source map, the level of detail and accuracy depends very much on the map scale.
Large-scale maps can be topologically very detailed and have complex legends while smaller-scale maps are more generalized.
This scale-related generalization gives rise to both locational errors and attribute uncertainty.

Consider line thickness on paper maps.
All lines on maps, depicting features such as roads, contours and boundaries, are drawn so as to be easily visible to the user.
The thickness of some lines are even emphasized to accentuate their importance (e.g. major roads).
This can be misleading (e.g. a road shown as a line 1 mm thick on a 1: 50000 scale map implies a width of 50 m on the ground - an obvious exaggeration) and as a result leads to difficulties in the digitizing process.
Common sense suggests that the true course of a line on a map is along its mid-point.
However, as the operator traces a line extra errors arise because it is impossible to follow the centre of the line exactly and some displacement of the cursor on either side of the line is inevitable.
Burrough (1986) suggests that the area of the map covered by lines can be assumed to be an area of uncertainty.
In one example he states that a 1: 25 000 scale soil map measuring 400 by 600 mm may have as much as 24 000 mm of drawn lines, covering 24 000 mm² or 10 per cent of the total map area.

Blakemore (1984) attempts to estimate the uncertainty caused by cartographic line thickness and associated digitizer error by adapting an idea forwarded originally by Perkal (1966).
Perkal defined a distance (' epsilon') about a cartographic line as a means of objective generalization.
Blakemore inverted the concept, suggesting that it can be used to indicate an error band about a digitized line.
This can be applied to polygon overlay operations to ascribe descriptive levels of certainty to the resulting map.
A point-in-polygon problem was used as an example which results in five classes of answer depending on the position of the point relative to the digitized boundary and the 'epsilon' distance (Fig. 6.1).
Empirical investigation using UK Department of Industry 1 km square data overlaid on polygon boundaries of north-west England employment office areas revealed that only 60 per cent of the points in the industry database could be positively assigned to an employment office area by being within a polygon and away from the boundary by a distance greater than epsilon.

The accuracy of a digital representation of a line depends not only on the ability of the person using the digitizer to follow the centre of the line on the map exactly but also on the number of points they input to describe the shape of the line (Aldred 1972).
Converting a line on a map into a series of x, y coordinates involves a sampling process.
The number of sample points required accurately to copy a straight line is much less (2) than that required for a curve or complex line feature (>>2).
The relative error associated with digitizing straight lines (e.g. power lines) is considerably less than that associated with digitizing line features made up of complex curves (e.g. coastlines).
Although a number of methods are available for sampling only those vertices which describe the basic shape of the line (e.g. Douglas and Peucker 1973), the difference between digitizing straight lines and complex curves suggests that Blakemore's use of distance 'epsilon' is an over-simplification of reality.
This could be improved by more detailed consideration of the processes of error propagation inherent in digitizing procedures.
Several empirical studies have examined digitizing error by comparing digital data to their source maps (Traylor 1979; Otawa 1987; Keefer et al.1988).
From such studies appropriate models of digitizer error could be formulated.

##### Errors in digital overlay analysis

Much of the functionality of GIS lies with their ability to overlay one or more digital maps for the purposes of Boolean or network analyses.
This kind of map analysis used to be done manually (before the advent of practical GIS) by overlaying transparent map sheets, establishing the required spatial relationships and drawing the new map on a clean top sheet with felt pens (McHarg 1969).
Digital cartography promised a more efficient and flexible way of doing this kind of work.
However, making the step between simple paper overlays and digital overlay proved difficult.
Much research and development was carried out into this problem during the 1970s (e.g. McAlpine and Cook 1971; Goodchild 1978).
Results from this work have, however, created more questions about data quality and error propagation.
These questions need to be answered, at least in part, before GIS can realize their full potential.

McAlpine and Cook (1971) experimented with the polygon overlay problem by overlaying different sized hexagons over a hexagonal grid with random orientation and displacement.
Their results showed a surprisingly large proportion of small, 'sliver' polygons on the output maps.
When applied to a case study, involving the overlay of three maps of Papua New Guinea containing 7, 42 and 101 polygons respectively, the output map was comprised of 304 polygons, of which those less than 3.8 km²; amounted to 38 per cent of the total area.
McAlpine and Cook evaluated these results by classifying the derived polygons by size and boundary complexity.
A 10 per cent random sample of derived polygons was evaluated to determine the measure of agreement between the initial and derived descriptions.
It was found that approximately 30 per cent of the map area was made up of polygons which did not agree with the initial map descriptions.

Goodchild (1978) suggests that the number of derived polygons is more a function of boundary complexity than the actual number of polygons.
When the boundaries of overlaid polygon networks are highly correlated (e.g. as for certain types of administrative areas) serious problems are created through the introduction of large numbers of 'spurious' sliver polygons.
In the case of administrative boundaries, different units present in different maps often share a common boundary (e.g. a river or stretch of coastline).
These common boundaries will have been digitized separated, and so will not, therefore, coincide exactly.
Furthermore, the more accurately common boundaries are digitized in each map and the more coordinates are used, then the larger the number of spurious sliver polygons produced (Goodchild 1978).
Elimination procedures are available in GIS software to remove sliver polygons on the basis of minimum area (e.g. ARC/INFO, ESRI 1987).
It is likely, however, that the resulting common boundary will be moved from its true position by the elimination procedure, thereby introducing further uncertainty into the output map.

An attempt to estimate the cumulative effect of thematic map errors in digital overlay analysis has been made by Newcomer and Szajgin (1984).
Using conditional probability theory they suggest that the accuracy of maps resulting from overlay analysis is determined by the number of map layers, their accuracy and the coincidence of errors at the same position in several map layers.
As a result the accuracy of a composite map from overlay analysis is generally less than the accuracy of the least accurate map layer used (Newcomer and Szajgin 1984).
Newcomer and Szajgin go on to define the lower and upper bounds of accuracy in the output map.
The upper bound is at best equal to the accuracy of the least accurate map layer (when all errors in other layers are coincident in their location), while the lower bound results when the errors in each map layer occur at unique locations.
Other researchers have compared spatial databases with ground truth observations.
for example, Walsh et al. (1987) made an assessment of the error inherent in Landsat data, digital terrain models (DTMs) and digital thematic soil maps by comparing the data from these sources with information collected in the field.
They found that the error ranged from 43 per cent for the soil maps to 83 per cent for the DTMs.
Using the techniques described by Newcomer and Szajgin (1984) Walsh et al. (1987) found that the combination of inherent and operational error ranged from 71 per cent (upper bound) to 83 per cent (lower bound).
The problem is knowing what these results mean in the context of a particular application.

##### Errors associated with vector to raster conversion

There are generally recognized to be two major sources of error when converting vector maps (either paper or digital) into gridded or raster format.
These are coding errors and topological mismatch errors.
The first, and probably most obvious, source of error is associated with the problem of coding those grid cells which contain parts of several different vector polygons each in similar proportions.
How should the grid cell be coded?
This problem arises because each grid cell can only have a single attribute value and because the chosen grid dimensions are too large to resolve the spatial detail required.
One answer is to use a finer grid to achieve finer detail (Walsh et al.1987), but this causes a corresponding increase in the size of the raster database.
The second source of error is the problem of topological mismatch when a polygon map is represented by a grid.
Again this can be reduced by using a finer grid, but problems with the increased amount of data storage required still occur.

#### Methodological outline

In conclusion to their paper Walsh et al. (1987) state that 'additional research in inherent and operational error assessment is warranted.
Research in methods for cartographic display of errors, and the setting of statistical confidence limits of databases, are particularly required' (Walsh et al.1987; 1429).
Expanding on this it is possible to identify five major tasks in the study of error propagation within GIS.
These are:

- 1. The development of mathematical models to represent the uncertainty characteristics of digital map databases;

- 2. The development of procedures for estimating the effects of input data uncertainties and their propagation through GIS;

- 3. The application of these models and techniques to a representative range of case studies to derive empirical estimations of likely error levels in GIS output;

- 4. The development of techniques to utilize output data uncertainty estimates; and

- 5. The incorporation of the technology as standard GIS tools.

Task 1 is of critical importance.
A means of modelling the distribution of errors is needed.
One way of meeting this need is to take some commonly used map data sources (both analogue and digital) and perform numerical experiments on them to investigate the effects of scale and map resolution on data accuracy.
In doing so there are a number of important areas to consider: mathematical modelling of the distribution of positional errors in digital maps derived from source maps of different scales; the level and distribution of error which characterize digital map data; and the types of probability models which best represent these errors.
The long-term aim of this research should be to obtain a reasonable representation of the various errors that exist, although practical considerations would limit the scope and complexity of the representations used.
It should be possible to obtain reasonable error models relating to positional accuracy, classification errors, attribute uncertainty and normal sampling aspects of spatial data.
Such an approach conforms to Chrisman's concept of a total error model as a decomposable set of stochastic processes which operate simultaneously.
As more components of the total error model become available as a result of research then they could be adopted.
As a result, any error-handling and estimation procedures should be sufficiently general as to be able to incorporate any new error model that may emerge at a later date.

Task 2 may be solved by using a Monte Carlo approach.
The generality and flexibility of such a procedure are a very attractive feature of the technology.
Here, a Monte Carlo based simulation procedure for estimating the impact of error in GIS is proposed and developed.
The concept is simple and universal in its applicability.
It does, however, present a number of operational difficulties that require basic research before it can be widely used.

The procedure is to simulate the effects of input data uncertainty by a Monte Carlo approach that is often used in statistics to perform exact significance tests.
Each input data source is assumed to be characterized by an error model that represents reasonable estimates of the levels and nature of the data uncertainty thought to be present.
This allows the map data to be replaced by probability distributions of known form and parameters.
A single simulation is made by generating random numbers from these probability distributions and adding them to the observed geographic coordinates (defining point, line or area features) with these random values.
This process is repeated for each source of data input.
The randomized input map data are then subject to an arbitrary sequence of GIS operations.
The final output results are saved.
The entire process is repeated M times (where M may be up to 100).
Research is required to determine the appropriate value of M.
If the GIS output is merely numeric, then the distribution of M results gives some indication of the effects of input data uncertainty.
If the result is a map, then the total set of output maps can be used to draw confidence intervals or 'credibility regions' which can be overlaid on the deterministic results as a visual indication of the effects of data uncertainty.

For example, suppose a series of map overlays is being used to define suitable locations for a facility.
The certainty of the output map being correct can be estimated using Monte Carlo simulation.
In a vector GIS the set of M different output maps would be rasterized and a count made of the frequency that each cell appears in the final map.
Those cells in locations which are little affected by the sensitivity analyses would accumulate high counts.
They could then be converted back into vector form as polygon data and superimposed on the deterministic results.
There is a useful analogy here with Monte Carlo significance testing which could be used to add a further degree of inferential screening to assessing the descriptive significance of the uncertainty bands in the context of a particular application.

This simulation procedure is totally independent of the error models used and the nature and sequence of the GIS operations employed.
The GIS component can include all manner of map manipulation, evaluation and statistical procedures.
However, there are a number of basic research tasks that need to be resolved before this technique can be widely applied.
These include: defining suitable values for the number of simulations required in a GIS environment rather than a statistical hypothesis-testing one; assessing the utility of kernel estimators as an approximation that may allow smaller numbers of simulations to be used; investigating the possibility of predicting the final output regions without performing large numbers of simulations; and investigating possible hardware solutions to speed up the simulation process.

The Monte Carlo simulation technique offers an effective means of identifying and demonstrating the effects of data uncertainty in a number of case studies drawn from the natural and social sciences.
This is important as a means of drawing end-user attention to the problems of error propagation.
The resulting 'error audits' would also provide a platform for illustrating to vendors the importance of installing error estimators in GIS software.

A practical means of identifying approximate levels of output uncertainty also requires that some basic recommendations are made about how this variability can be retained, used and passed on to subsequent operations and applications using the data.
Some US research groups appear to be tackling part of this problem by tagging databases with error information.
Attention might be better focused on more technical questions such as how this error information may be used in GIS and spatial analysis.
For example, development of spatial retrieval techniques and nearest neighbour analyses which can operate with fuzzy data.
Other issues relate to investigating how this uncertainty information can best be presented to the user.

Finally, the simulation approach and associated error models should be capable of being incorporated into standard GIS software.
The principal problem area concerns the additional amount of computation that may be necessary successfully to implement Monte Carlo based techniques.
It is possible, however, that quick approximations could be devised that would reduce the work-load by a factor of 5, while improvements in hardware over the next few years may well absorb the rest.

#### Monte Carlo simulation methodology

##### Some preliminaries

Although the methodology is of general applicability, it has been developed here using ARC/INFO running under the VMS operating system on a microVAX 2.
Some of the terminology, therefore, relates to the ARC/INFO GIS software (see Table 6.1).

##### The basic sequence of operations

The nature of the simulation methodology is outlined in Fig. 6.2.
The simulation of input data uncertainty involves replacing the deterministic input data values by those from a probability distribution that reflects an appropriate error model.
The GIS operations are then performed and the results saved for evaluation.
The GIS software used in this case study is the widely used ARC/INFO package (ESRI 1987).
The methodology is operationalized in a macro which calls a separate program to perturb the input data without changing the topology.
This is achieved by accessing the binary arc files directly from a FORTRAN program and then replacing the deterministic values by probabilistic ones, checking in the process that the implicit topology is retained.

There are a number of approaches to implementing the methodology in ARC/INFO.
The sequence of events is:

- 1. Perturb the arc data for the coverages, preserving polygon topology;

- 2. Carry out the GIS operations on the perturbed coverage;

- 3. Rasterize the results; Steps 1-3 are repeated 100 times.

- 4. Calculate frequencies for each raster; and

- 5. Map the results for a given probability level.

Steps 1-3 are contained within the macro, written in the ARC/INFO macro-language, AML.
Step 1 is implemented in a separate macro.
Step 4 is implemented in a VAX DCL command procedure.
The results are then [UNK] mapped on a micro, using a Postscript driver (Adobe Systems 1985) of the authors' own devising (step 5).

The first major problem is to access the arc data.
In ARC/INFO, the binary arc/node topology information is kept in one subdirectory, while the tables which access these attributes are stored in another subdirectory.
Initial attempts used the ARC UNGENERATE command to extract the binary data in ASCII character form for input to the FORTRAN perturbation program, followed by a GENERATE and BUILD to re-create the coverage.
There are two disadvantages to this approach; first, it is enormously time consuming and second, the polygon topology of the input coverage is not preserved, so one cannot work back to the initial coverage attributes.

The easiest solution is to access the binary files directly.
All the information is then contained in only one file.
The ARC/INFO programmer's guide (Aronson 1985) give some clues as to what to expect, but the actual file structure can only be determined by inspection.
Fortunately, the VAX command DIR/FULL gives enough information to allow a FORTRAN program to be written which can read the data block by block, and then replace the arc coordinates by randomized values drawn from some appropriate probability distribution.

The complexity of the record structure provides extra problems for coding the perturbation program.
Integer and real data representations are mixed together in the logical records in the data.
The trick is to recognize which are which, and deal with them accordingly.
The header/trailer and topology information must also be preserved exactly, and only the coordinate data perturbed.
finally, the node information can be perturbed only once, which involves creating a node table into which the perturbed nodes are stored as they are read in, and from which they can be retrieved in later references to the same node.

The GIS overlay operations follow next.
In this case, the operations are a series of overlays, designed to remove infeasible areas from the base coverage.
Lastly the polygon data in the output coverage are rasterized and the rasterized coverage stored.
Rasterization is used to provide an easy way of visualizing the uncertainty in the output results.

The object of the final analysis is to create a data set which contains, for each raster, the number of times it is simulated to be inside the areas resulting from the sequence of GIS operations.
There are several ways of achieving this.
The methodology used here is a three-stage operation; first, the binary raster files or single variable files (SVFs) are expanded into character form, compressed (Held 1983), and a row number added; second, the files area is sorted by the row number so that all records with the same row number are contiguous in the file; third, a count is made of all the rasters in each row which are simulated to be inside the required areas.
These frequencies can then be mapped to yield credibility regions corresponding to particular significance levels.

#### A case study

##### Searching for radwaste sites

Openshaw et al. (1989) discuss the use of ARC/INFO to identify feasible sites for radwaste dumps.
The GIS operations constitute little more than a sequence of map overlays in the form of a Boolean search.
This process is re-examined here with particular attention to northern England to reduce the computational resources required.

The object of the overlay exercise is to determine potentially feasible sites for the dumping of waste material from the nuclear industry, in particular, low- and intermediate-level radioactive waste.
This chapter is not itself concerned with the mechanics or politics of the matter, the example chosen is merely a convenient one for purposes of illustrating a very common GIS procedure.
For the dumping of such radioactive matter four criteria need to be considered:

- 1. The waste dump must be on a site with a suitable underlying geology;

- 2. The site must be accessible from the UK rail network;

- 3. The site must not be within a conservation area (that is, a national park, area of outstanding natural beauty, etc....); and

- 4. The site must be away from areas of population concentration.

Four coverages are used in the case study.
The underlying suitable geologies, defined by the British Geological Survey (Chapman et al.1986), were digitized from 1: 625 000 scale maps.
The rail network was digitized from 1: 250 000 maps, and buffered at 3 km.
The national park data were digitized from 1: 250 000 maps.
The population counts those grid squares with a population greater than 490 residents, representing a population density of greater than 4.9 persons/ha.
The coverages are shown in Fig. 6.3 and the error estimates for them are contained in Table 6.2.

The first step involves processing a suitable geology coverage (GEOLOGY).
The ARC/INFO ERASE command (the Boolean equivalent of NOT) is used to remove the constrained areas from the coverage to build up a composite coverage.
The elimination sequence is presented in Fig. 6.4.
Those areas which are outside the rail buffer, RAILBUF, are removed (to give ERASRG), and next the conservation areas, CONSV (to give ERASRGC).
finally, the densely populated areas, POP490, are deleted to give a set of feasible areas for site investigation (ERASRGCP).
The characteristics of each of the coverages are shown in Tables 6.3-6.6, and the ARC command sequence to obtain the final overlay is in Table 6.7.

It is difficult to attempt to determine what are suitable estimates of the error in the map.
ARC/INFO works to a minimum tolerance - the smallest distance between any pair of coordinates - known as the fuzzy tolerance.
As a default, the fuzzy tolerance is 1/50 000 of the width of the base map, in this case, 0.48 mapunit.
As the mapunits are 10 m, the fuzzy tolerance represents 4.8 m on the ground.
The population data arc rather more problematic, since they are generated from the 'centroids' of census enumeration districts (EDs); the boundaries of the census EDs do not conveniently follow a grid, it is assumed they have a similar fuzzy tolerance to the other coverages.
Clearly, the quantization noise which is introduced to the data requires a rather more sophisticated error model.
The case study uses the error estimates in Table 6.2 as a guide to likely levels of uncertainty until further research yields more realistic models.

The simulation is run 100 times.
In each simulation:

- 1. Leftovers from any previous run are removed;

- 2. A copy is taken of each of the unperturbed coverages;

- 3. All nodes and vertices of each coverage are perturbed;

- 4. The file structures are reorganized into a form the ARC i/o routines can deal with.
This step is highly VAX/VMS specific and could probably be replaced by some more universal coding in the perturbation software.

- 5. The overlay sequence takes place; remnants of any previous failures are removed; and

- 6. The output vector coverage is rastered, prior to plotting.

Step 6 introduces a series of problems.
The rasterization process introduces noise.
For the experiments here, a raster size of 1 km (100 mapunits) is used.
[UNK] Given that the fuzzy tolerance is 25 mapunits, then the raster size should be that or less, to remove the quantization noise.
However, reducing the raster size from 100 to 25 mapunits increases the disc space required to store the raster files by a factor of 16 as well as increasing processing times.
ARC/INFO is not well tuned to handle this sort of problem.

##### Simulation results

The error model used here is an obvious over-simplification of reality.
Each vertex in the coverage was perturbed by selecting random numbers from a uniform distribution, with ranges defined in Table 6.2.
Steps were taken to ensure that the nodes were not perturbed more than once, but no checks were made to determine whether the perturbation process caused sliver polygons to be created.
The fuzzy tolerance of 25 mapunits was chosen to try to eliminate these from the final coverage.

The process required 16 140 s of CPU time and 20 h of elapsed time on a lightly loaded microVAX 2, under VMS.
The resulting maps are shown in Fig. 6.5.
There are seven maps, showing 90, 95, 96, 97, 98, 99 and 100 per cent, 'credibility regions'.
The credible region is that which contains the feasible region n or more times out of M; in this case M is 100.
As the 'credibility level' increases, so fewer and fewer areas are included in the map, reflecting [UNK] [UNK] [UNK] the increasing confidence in the map.
More areas are included in the map where the user is willing to be wrong 10 times out of 100, but far fewer in that which they are willing to run the risk of being wrong once in a hundred times; a comparison of the 90 and 99 per cent maps will make this clear (figs 6.5a and f).

There is little difference between the 90, 95, 96 and 97 per cent maps (Figs 6.5a-d), but between the 97 and-98 per cent maps a considerable region in the north-east corner of the map is lost (Figs 6.5d-e).
Between 99 and l00 per cent, virtually all the map (figs 6.5f-g) is lost with the exception of the region in the south-east corner of the map.
The overlay process has been most reliable here.
Comparing this map with the ERASRGCP map from Fig. 6.4 will reveal the effect of trying to take uncertainty in the input data into account explicitly on the resulting map pattern.
There are far fewer areas in the simulated map about which one would risk a definitive statement than in the map from the unsimulated process.

##### Discussion

The main problem with using a Monte Carlo approach is its slowness.
A lightly loaded microVAX 2 can expect to take over 24 h of elapsed time to carry out 100 simulations on a small problem.
Fortunately the process is explicitly parallel and were it to be run on multiprocessor hardware then there could be substantial speed-up.
The simulation process is parallel, since one simulation does not depend on the outcome of a previous one.

The selection of a suitable error model is problematic.
One approach is to carry out experiments with a digitizing table in order to determine empirically an appropriate distribution for digitizing errors.
Synthetic data which are themselves a GIS-derived product may be the most difficult to deal with.
The grid square population data used here are a case in point.
These data had to be estimated from census ED information.
The aggregation process merely allocates to a grid square the populations of the ED whose 'centroid' happens to fall in that grid square.
In the case where two or more EDs fall in the same grid square, then the grid square's population is the sum of those of the individual EDs.
It can also be argued that the error present in this data, given its crudity, would swamp any of the other data.
However, it is only fair to point out that the population distribution is uneven, and any swamping will take place in urban areas.
In the context of radwaste disposal, this is not critical, but for some other operations, it obviously is.

There might be alternatives to using a grid.
Very few 'natural' data come in grid form.
One might buffer the ED centroids, assign populations to the resulting zones, then determine the population densities.
The choice of buffer distance would need to be the subject of some experiment.
The use of Theissen polygons has been suggested, although the statistical properties of processes giving rise to such areas are poor surrogates for digitized ED boundaries.
The varying size of EDs in urban and rural areas, and the discontinuous nature of the population distribution inside the larger rural EDs is also difficult to parametrize.

The selection of a raster size presents some other problems.
The authors used an IBM 4216-010 PagePrinter as an output device.
This is a device which supports PostScript, and which has a specified resolution of 300 pixels/inch, both the vertical and horizontal direction.
In the case study maps, 1 pixel represents a square of size 118 m.
With a l200 dpi printer (such as a phototypesetter), each pixel would represent a square of size 29.5 m.
These set minimum sizes for output.

It should be noted that all the experiments thus far have used vector representations.
It may be easier to implement it in a raster environment, but much would depend on the size of the rasters chosen to represent the areas.
Clearly this is yet another area for further research.

#### Conclusions

This chapter has introduced some of the issues surrounding the propagation of error in GIS and described the preliminary application of a Monte Carlo approach to assessing their effects.
The empirical research carried out here is intended to test the feasibility of this approach, as well as providing some general indications of what the effects might be and of one way by which they can be represented on the final output map.
In so doing it is recognized that many of the questions raised are left open for subsequent investigation and that the results are initial and tentative.

Although conceptually clear, the method is not easy to implement with current hardware.
There is likely to be substantial increases in CPU times, although it might be possible to reduce this by a factor of 5.
However, with faster hardware likely to be on the market in the near future and the possibility of the emergence of parallel GIS machines, there is some justification for believing that extra effort is both worth while and acceptable.
The challenge is to resolve the outstanding questions and perfect the technology as soon as possible.

Perusal of Fig. 6.5 indicates that it does appear to work, and that it offers a pragmatic solution that could probably be developed further into a general-purpose GIS 'error button'.

### User interfaces

#### Introduction

Geographical information systems (GIS) make considerable demands on the user: the wide variety of data types recorded in digital maps, the complex data structures used to organize them and the range of operations available, amount to a formidable obstacle for most users with standard requirements.
As such, the quality of interfaces to GIS has taken on a considerable importance in terms of awareness, training and usage, both to the providers of GIS software and users of GIS alike (Rhind, et al.1989).
However, there are many aspects to the definition of an interface for systems as complex as GIS, and the solutions to this problem are developing extremely rapidly at the time of writing.
Accordingly, this chapter aims to set out the requirements for a fully configured GIS interface, and profiles the development of a new GIS user interface system called UGIX.
This model is also used to define a research agenda for the next 5 years; the reader may judge the accuracy of this analysis by the commercial reality of available systems during the early and mid-1990s.

There is a wide recognition that the problems of poor interfaces are of considerable importance to the development of GIS.
The UK Government Committee of Enquiry chaired by Lord Chorley (DoE 1987) on the Handling of Geographic Information suggested in recommendation 59 that GIS technology projects be promoted since the report noted that the existing interfaces to GIS systems were poor.
The shortcomings of GIS user environments can be divided into two groups:

- 1. Task complexity - the system functions implementing spatial operations are often complex and obscure;

- 2. Poor database view tools - few systems make available database views meaningful to the user.
Accordingly, it is clearly desirable that improved

- interfaces be developed so that the range of spatial operations in a system can be organized into standardized functions or tasks, and so that the spatial database can be visualized.

The quality of GIS user interfaces is also an important factor in the acceptance, uptake and efficiency of the integrated GIS which are currently on the market.
In a recent study by Willis and Nutter (1990) of 136 publicly funded utilities and municipalities in the UK 57 per cent stated that they were inhibited in their GIS developments by 'a lack of staff with the right expertise'.
At a time when there is a national and international shortage of staff skilled in the computer handling of geographical data (Rhind and Mounsey 1989), 'ease of use' is a vital criterion for the selection of an appropriate GIS.
It is generally accepted that a system which is easy to use can help cut recruitment and training costs, and help retain staff.
Organizations which are in the process of implementing GIS strategies also appreciate that the 'ease of use' factor is a key control over how quickly GIS programmes can be implemented, and therefore the speed with which financial targets for paying off capital costs can be met.
It may also be true that 'ease of use' can influence the quality of work done and the effectiveness of a GIS as a decision support system.
To illustrate this in the negative, Beard (1989) for example, showed how 'use error' in GIS was an important but neglected aspect of quality control in GIS.

In summary, the user interface is a vital element of any GIS.
Long ignored as an esoteric aspect of GIS design while GIS development was driven by the need to extend functionality, the user interface is now beginning to attract its due attention.
However, the implementation of a GIS user interface involves considerably more than the improvement of the human-computer interaction (HCI) process.
Since GIS are conceptually complex and involve diverse operations ranging from data modelling to geometric transformations, improving the HCI cannot be a complete solution to the improvements of GIS use.
Consideration also needs to be given to the embedding of knowledge, task definitions and database view manipulations into such interfaces.

A key assumption, therefore, which remains to be tested is whether a GIS user interface should condition GIS use.
While there are many who would argue that a measure of technical knowledge is desirable in those who use a GIS and a protection against the misuse of a powerful tool, it must now be established that maximum 'achievable' use of a software system owes much to the creation of a structured use environment, with logic controls built into the interface.
The user is then free to choose the environment which best matches their use characteristics or which improves their aggregate efficiency measured in time, error or quality terms.

#### Characteristics of a user interface

A user interface, at its most basic, consists simply of a system for communication with the computer.
Since the demise of the punch-card system for entering commands this has normally been undertaken using a keyboard and a screen driven by a cathode ray tube (CRT) or liquid crystal display (LCD), although voice entry of data and touch screens have also been used.
Typical computer operating systems use (and continue to use) 'command line interfaces' where a user enters a syntactically correct command at a prompt in order to give an instruction.
Many computer applications use this kind of interface which is common on all machine ranges and sizes, e.g. MS-DOS for IBM-compatible personal computers.

However, in the last 5 years the command line interface has begun to be replaced by the graphical user interface (GUI).
The GUI is an audio-visual display on the computer screen which presents a screen metaphor for the actions which the computer or program can carry out.
Typically the means of issuing commands using this system has been via a window-icon-mouse-pop-up menu (WIMP) display, where the mouse is used to point at icons or menus in windows (which are subsets of the screen working area).
The options available are indicated to the user by the range of identifiable screen objects (Helander 1988).

Early work on the concept of WIMP user interfaces developed from research on the Smalltalk-80 project at the XeroxPARC in California in the early 1980s (Goldberg and Robson 1983).
Work by Smith et al. (1983) and Sneiderman (1983) developed the concepts behind moving and selecting screen representations, which has become important to all graphics-oriented applications (such as GIS).
The GUI for the Apple Macintosh (first released in 1984) was the first to become widely used and its popularity helped ensure that other GUIs were developed for PC compatibles and UNIX platforms.
This development has defined a new and higher standard for interfaces which has become common in all areas of data processing.

Apple's publication Human Interface Guidelines (Apple Computer 1987) set out the 10 chief characteristics of its own GUI as follows:

- 1. Metaphors from the real world;

- 2. Direct manipulation by the user;,

- 3. See and point (instead of remember and type);

- 4. Consistency;

- 5. WYSIWYG (what you see is what you get);

- 6. User control;

- 7. Feedback and dialogue;

- 8. Forgiveness;

- 9. Perceived stability;

- 10. Aesthetic integrity.

These principles have now been generally adopted across all platforms, although since the Macintosh GUI is embedded in the system architecture most of these characteristics are enforced in Macintosh software design and engineering.
However, this is not generally the case, and a whole variety of GUIs have developed, each adopting a slightly different subset of these principles as guidelines.

The range of GUIs which have now developed are surveyed in Hayes and Baran (1989).
On the basis of the analysis of 12 GUIs they suggest that the GUI is composed of three main components.
Firstly, the windowing system is a set of tools for creating windows and their characteristics - an example of this is X Windows.
The second main component of the GUI is the imaging model which controls the drawing of the screen representations such as fonts and icons; an example of this is Display Postscript.
The third component is the application program interface which acts as an interface to the program operations and controls feedback from the screen representations.
In response to the buoyant demand for GUIs almost all vendors of computer systems now offer such an interface product.
Some GUI components are becoming standard across a variety of vendor platforms; thus, the windowing system X Windows is shared by a number of systems running UNIX.

Several GIS have already begun to use GUIs to make their systems more user friendly using the standard platform interface tools as described above.
One example is AlperRecords from Alper Systems of Cambridge, UK which uses SUN interface tools, and is based on pop-up hierarchical menus.
However, a standard GUI can only translate the command structure into graphical cues and will still be a 'function-oriented' rather than a 'task-oriented' system.
(This means that the user sees 'primitive' spatial operations and not a whole spatial problem which may involve a sequence of primitive operations).
Hence, the use of a GIS with a GUI can only improve user productivity in 'use' factors, for example by increasing the speed of use and reducing errors, and may only help the user with a previously substantial knowledge of GIS.
Thus, due to the sheer complexity of spatial data and the operations available, this can only be a partial solution to the general problem of user interaction with a GIS (Gould 1989).

#### Recent research into GIS user interfaces

Research into the form and content of user interfaces for GIS has accelerated rapidly in the last couple of years.
Initially this work has followed from the general acceptance of the WIMP system as an effective form of human-computer interface.
Within GIS the unique appeal of the GUI has been the desire to improve the ease of use for systems involving complex graphical display and spatial manipulation.
Hence the primary interest has been in:

- 1. The development of new task-oriented interfaces based on standard windowing systems; and

- 2. The creation of standard query formats which are independent of the database structure.

Initial work in the GIS field on user interfaces has concentrated on the screen designs appropriate for spatial data handling.
Thus, Egenhofer and Frank (1988) suggested a way in which the WYSIWYG principle of 'what you see is what you get' could be extended to GIS and outlined the components of their own system which included a study of the selection of objects and areas, legends and query specification.
Subsequent work by Cassel and Parker (1989) carried out tests on the effectiveness of different designs of GUI, focusing especially on the use of icons to represent classes of spatial data.
This work demonstrated some of the special problems which have to be solved to design good GUIs for GIS: thus, an icon of a single pine tree caused some confusion when presented to a forester since he could not identify its species!
This indicates how legends and graphical cues must generalize a complex reality to provide appropriate 'cues for action' (Mark 1989).

Gould (1989), in a review of the HCI literature, also noted the potential to move beyond simple GUIs in interface design and identified three areas of potential improvement.
First, he considered that graphic interaction was presently a limited form of process-response system, and recommended that designers of GIS interfaces look for ways to exploit the sophisticated forms of human visual thinking (Verplank 1988).
Second, he suggested that the interface itself exploit multi-media techniques of sound and video to issue and support commands.
finally, he suggested that interface design ought to concentrate on handling 'fuzzy' queries and parsing 'natural language' concepts.

One recent study of user interfaces by Campari et al. (1990) has employed graphical concepts in the design of GIS operations.
This work, described as a visual language approach to GIS, used a visual programming language to define map operations.
This consisted of a graphic workspace and primitive GIS operations shown as icons which the user selected from a palette and assembled in the workspace.
The whole set of commands encapsulated in the visual procedure was then executed sequentially.

Hence, another key aspect of spatial user interface design is that it must seek both to structure and filter human perception of space and spatial relationships when expressing an operation and passing it to a GIS.
Research into general aspects of the perception of spatial relationships began long before the special problems presented by GIS existed, and is exemplified by the classic work of Gould and White (1974) on 'mental maps'.
In the GIS context such issues are becoming increasingly important as GIS use grows rapidly and reaches a wider audience: this concern has created a new sub-discipline of 'spatial language' research.

Early work on spatial languages was based upon the principles of spatial inference and retrieval, and was not specifically digitally based (McDermott 1980).
Thus, Palmer and Frank (1988) distinguish between the interpretation of a man-made image (whose meaning is to be reconstructed), and a 'natural' image (whose meaning has to be extracted and standardized with belief systems).
Since maps are man-made the chief objective of a spatial language is to guide in the elucidation of the meaning (s) attached.
Palmer and Frank (1988) also identify the key components of a spatial language as a family of spatial objects, the geometry of space (as mapped and perceived) and the mappings of the objects into the space.

The importance of the cognitive structuring of space is expressed by Mark and Frank (1989), who set out the research agenda for the 'Spatial Languages' Research Initiative of the US National Center for Geographic Information and Analysis (NCGIA).
Cognitive aspects of spatial perception place constraints on the definition of a spatial language intended to be used as part of a user dialogue with the computer.
Thus, Mark (1989) suggests that the 'image-schema' can be used to structure perceptions of space and provides examples drawn from Johnson (1987) such as CONTAINER (associated with the preposition 'IN') and PLATFORM (associated with the preposition 'ON').
This consideration can affect the process of data modelling since the cognitive models available define the 'entities thought to be relevant to the task in hand'.
Mark (1989) applies this consideration to the digital line graph, extended (DLG-E) model of cartographic representation used by the US Geological Survey mapping programme and comments that the rules and feature classes adopted do not relate well to an image-schema, and hence will be difficult to generalize.

Similarly, different linguistic traditions structure space in distinct ways (Mark 1988).
Examples of linguistic structuring (with examples in English) include:

- 1. Preposition, e.g. near, between, among;

- 2. Motion, e.g. across;

- 3. Demonstratives, e.g. this, that;

- 4. Viewpoint, e.g. further down the road;

- 5. Distribution of attention, e.g. reference frame such as a field.

Awareness of these characteristics of language can help in the design of a generic spatial language with which a wide variety of users can interact with a spatial database.
A clear objective in this field must surely be the evaluation of the language of groups of users.
However, attempts to translate the Geographical Information Systems Tutor (GISTutor) (Raper and Green 1989) into a number of European languages have encountered two main difficulties: first, the local adoption of English for spatial terms (and therefore concepts?) due to the English lexicon of most commercially available GlS, and second the difficulty of providing for translation of terms with no direct counterpart.

The spatial query language tools which a GIS uses for general interaction with spatial data and for the elucidation of spatial relationships have also been the subject of recent research (Egenhofer 1989).
However, spatial query tools are intrinsically linked to the data model employed: hence the use of multiple spatial data structures has led to the proliferation of query processors.
The result has been that in many GIS spatial queries initiated by the user must be formulated in terms of a software-specific command language.
However, the fact that many new systems use relational database storage for spatial and non-spatial data has led to a wide interest in the adaptation of the structured query language (SQL) for spatially-related query operations in GIS.
Thus, SQL is now seen as one possible means of establishing spatial queries across many different spatial data models and data structures.
Hence, Herring et al. (1988) described the design of SQL extensions to a new object-oriented GIS; Abel (1988) has reported work on the creation of SQL-based spatial extensions to a relational database in the 'Spatial Information in a Relational Open-architecture database management system' (SIRO-DBMS) project; and Ingram and Phillips (1988) have designed spatial extensions to a hybrid GIS data model.

Egenhofer (1989) also reported the test development of a prototype extended SQL (XSQL), adding concepts of spatial relations, spatial operations, graph representation and context.
However, when he tested the system he found that the queries became far too long and complex to parse and execute for user-initiated queries.
This may indicate that user interfaces to query structures cannot yet replicate human processes of spatial reasoning in a reasonable time, or that in software terms it is inefficient to extend SQL, and that an alternative must be found.

Hence the link between the user interface and the spatial query processor is a problem of key importance, and the subject of considerable debate.
Egenhofer (1989), in work on the testing of query processors, suggests that it is not possible to hide the implementation structure of the query at the interface.
However, note that Rhind et al. (1989) suggest that a Universal Geographic Information eXecutive (UGIX) can be created to interface between the user and a wide variety of different systems.
However, the UGIX concept is based on the key assumption that current GIS users are motivated and capable of exercising spatial reasoning.
These users want access to tools to extend the spatial database as well as to make spatial analyses.
This may indicate that a different approach is required for 'public' spatial information systems used by 'spatial professionals'.
These systems may have to be restricted to passive use based on the extraction of information in well-defined forms.
An example of this would be the systems recently installed in Shell petrol stations in the UK developed by Action Information Management which use touch screen technology to view 'road atlas' type maps marked with symbols indicating travel hazards on major routes.

The information content of maps is also an issue for user interfaces.
Thus, Bertin (1983) defined the concept of a 'map-to-see' as 'a clear graphic representation which can be comprehended in a short moment'.
Such an efficient map design should provide the map user with answers to all possible questions related to the map, whatever their type or complexity, in a single moment of perception.
Every other kind of map must be a 'map-to-read' and requires some study; it is implicit in experiments carried out by Kraak (1989) that such maps are not suitable for temporary display on a computer screen.
Kraak also showed that maps illustrating the values of a variable in 2D shaded polygons best formed a 'map-to-see' when they were displayed with the variable visualized in 3D.

The design of help systems and tutors for GIS also presents some significant challenges to the developers of GIS user interfaces.
However, the availability of such systems may be a crucial component of the user interface (Rhind et al.1989).
Difficulties include the need to show complex graphic operations, the explanation of algorithms and file structures, and the application of GIS techniques to decision-making in a variety of application areas.
One example of a solution to this problem is the creation of GISTutor which is described by Raper and Green (1989).

Hence at present three main kinds of problems are encountered in the use of existing systems: first, the generally inappropriate design of GUIs for GIS purposes; second, the specification of the language of interaction for spatial operations and queries; and, third, the limited content and rigid structure of standard help systems.
It is therefore suggested that the design of a user interface must be rooted in the creation of a user environment which integrates the data-modelling process, the availability of spatial operations and queries, and the system of assistance and concept support within the interface.

#### User interface development: a case study of UGIX

In an attempt to define the basis on which a comprehensive GIS user environment could be built Rhind et al. (1989) proposed the Universal Geographic Information eXecutive (UGIX) as a system design.
It contains three main modules viz. (A) containing the screen interfaces, dialogues and spatial command processor; (B) containing a help and information system for a GIS; and (C) an expert system shell or high-level system access module.
The structure of UGIX is illustrated in Fig. 7.1.
This section describes the [UNK] approach taken in the UGIX project, through first and second generation implementations.

The first generation approach to interface design within the UGIX project has been to prototype using Hypercard for the Apple Macintosh, where the Hypercard application (complete with in-built communications software) acts as a client to a host processor 'running the GIS application software.
This approach is similar to the one used by Cowan and Love (1988) to create an interface to the S Carolina Historic Preservation Office GIS database.
Hypercard with its standard set of buttons, scrolling boxes and cards makes use of the GlS less daunting for the less technically aware user.
In addition, with the rich graphics environment available in Hypercard it is possible to show a graphic to illustrate the effect of various options available at any one point.
It is also desirable to display all the commands available to the user at one time, with a pop-up explanation for each option.

Screen design has involved the standardization of button and text field formats as well as card and background layout for different areas of activity such as:.

- 1. Introduction and explanation (using a map guide);

- 2. Map and file selection (using standard Macintosh file selection dialogue);

- 3. Session screens for command processing;

- 4. Help environment (UGIX (B) based on GISTutor II);,

- 5. Library for maps and images generated in the GIS (along with a button to redraw them).

Screen metaphors have been developed for each of these areas to make location in the system a graphical attribute.
Currently this system interface 'shell' is being implemented for the GIS ARC/INFO.
During the second phase of the UGIX project a new interface 'shell' is being developed as part of a generic GIS-independent approach to GIS user interfaces (Raper and Bundock 1991).

The first-generation system known as 'HyperArc' is currently under test with users at 'novice' and 'competent' levels of expertise: in addition to feedback on the use of the system, the aim of the evaluation phase is to define a core area of functionality in common use to help optimize the system structure.
A key consideration for the development of a spatial language interface to GlS is that many different groups of users exist within the spatial data-handling community.
It is recognized within the UGIX design that to some high-level users skilled in the manipulation of spatial data a command line interface to a GIS offers the maximum flexibility and power available.
However, it is considered that during the first stage of the expansion of GIS use the largest group of new users are non-computer-literate professionals who frequently have a highly developed insight into spatial data.
It should therefore be emphasized that the first objective within the UGIX project is to improve access to existing GlS by converting the current function-orientation [UNK] of the native system interface to a task-oriented interface usable by a spatially aware user (see Fig. 7.2 for a taxonomy of interfaces for ARC/INFO at the time of writing in 1990).
The second generation of the UGIX project aims to build on the experience of constructing such task-oriented interfaces to create generic interfaces capable of communication with any GIS.

The basic principle of the UGIX design is that in order to make a GIS easy to use the process of making a database enquiry, plotting a map or carrying out spatial analysis must be broken down into manageable parts, linked by a pathway for the user to follow.
Following such a path and gaining experience with the alternative options is an excellent way to improve a user's end-to-end understanding of the components of spatial data processing.
In order to create this form of interface environment this project is engaged in the definition of a language of spatial interaction to handle a dialogue with a GIS through a system shell.
In the development of this shell it is considered that the selection of options itself should drive the commands presented to the user for action.
Appropriate information needed for a user to make a decision is also retrieved before presenting the command options, for example, maps with the correct specifications (e.g. with topological relations already created, when this is necessary for the operation).
Thus, the structuring of a wide range of task-related paths through a GIS has formed one of the main development objectives in this project.

Another key objective in developing a GIS user interface is to improve the data-handling procedures to support the user's concept of maps as views of spatial data.
Thus, utilities to manage map files are being implemented within HyperArc which use icons to access ARC/INFO data.
Search routines to find maps with particular names, to sort maps by type (e.g. point or polygon based), to access the map tiling system and to select the part of the sheet to view have also been created.
In the first generation of this project the user specifies spatial queries using system implementation concepts which are made comprehensible (and refined through testing).
However, a new query language interface based on SQL is under development for the second generation of UGIX (Raper and Bundock 1991).

#### Conclusions

This chapter has attempted to summarize the recent developments in user interfaces for GIS.
It can be said in conclusion that these developments have become central to the future of the 'GIS revolution' of the late 1980s, since it is now clear that the massive (and desirable) growth of the use of GIS cannot be supported without improvements to the use environment experienced by the user.
It is predicted that such developments will gain common ground in the elaboration of the GUI concept as it has in the computer-aided design world, but will quickly diversify in terms of the actual products which emerge.
Already a variety of vendors are attempting to create user interfaces which go beyond GUIs, but not have appeared at the time of writing in 1990.

Finally, it is important to note that the user interface 'debate' can also be interpreted as another facet of the data-modelling debate in GIS.
User interfaces are not just pretty screen representations: as their use is extended they will come to express the whole nature of the system data model, and will probably become highly specialized as the interfaces move from function-oriented to task-oriented forms.
Hence in the 1990s the user may not gain freedom of interaction with spatial data but become a captive of a particular design and control purpose.
Hence, the challenge for GIS user interface design is to gain credibility for generic forms of interface: it is this form of GIS use that will ensure wider and more informed use of GIS in the years ahead.

#### Acknowledgements

The authors of this chapter acknowledges the help of ESRI in the funding of work leading to the prototyping of the first generation of UGIX.
Apple Computer (UK) have also assisted in this work by providing laboratory Macintosh computers which now form the Apple Mapping Centre at Birkbeck College.

## Potential Applications

### Overview

Given the extent to which geographic information management is applications driven, it is important to consider in some depth the characteristics of some potential application fields.
In the process it will be necessary to examine not only the extent to which geographic issues feature on the policy issues agenda in these fields but also the institutional context which governs decision-making and the extent to which data are available for research and policy analysis purposes.
Questions on data availability are likely to be particularly important where users are heavily dependent on secondary sources.
In situations of this kind provisions governing access and format may exert powerful constraints on the use that can be made of these data.

The first four chapters in this part examine issues relating to geographic information handling in terms of four potential applications fields.
The authors were asked to review the current state of the art in their fields with particular reference to the likely requirements of the future policy issues agenda in terms of the demands that they make on geographic information management.
Authors were also asked to evaluate critically the state of geographic information provision in terms of the needs of users and to consider the impact of user requirements on the development of geographic information handling methodology.
In this way the chapters in this part present a number of perspectives which essentially complement and amplify the discussion in the previous part.
In this case, however, methodological issues are tackled from a largely user standpoint, whereas in the previous part they were viewed as substantive problems in their own right.
In effect the product of the discussion in both parts is a matrix where the methodological issues are listed along one axis and particular applications fields on the other.
Figure 8.1 summarizes the main features of this matrix.

There are important differences between the chapters in this part both in the nature of the demands that they make on geographic information and also in the relative importance that is attached to geographic criteria as against other issues by planners and decision-makers in these fields.
The first three chapters dealing with environmental monitoring, natural and technological hazards and settlements and infrastructure applications make use of a very wide range of geographic information.
A major feature of these applications is the extent to which they involve overlays of a variety of information drawn from different sources on a topographic map base.
for this reason they make particularly heavy demands on current GIS technology both because of the size of the data sets and the diversity of the data structures that are involved.

Brown's chapter on geodemographics discusses an application field where primary data collected for operational purposes are typically evaluated in relation to secondary data derived from sources such as the Census of Population.
The range of data sets involved and the demands that are made on GIS technology in applications of this kind are often more limited than those of previous applications fields.
However, this is offset by the demands that are made on spatial analysis and modelling methodology.

Rhind's chapter on environmental monitoring and prediction discusses the role of geographic information management in promoting sustainable development on a global scale in the context of the issues identified in the Brundtland report.
It points to the impact that the findings of global environmental research are likely to have on most sectors of the UK economy.
This contribution also indicates the wide variety of groups that are involved in monitoring environmental change and draws attention to the role that the European Community is increasingly playing in co-ordinating these efforts.

One of the examples of work in progress discusses research that has been carried out for the European Commission as part of the CORINE Project.
This highlights the challenges for research in a field categorized by a lack of data for some countries, varying definitions and standards in use, and unreasonably high user expectations.
The chapter as a whole draws attention to a number of key methodological issues that are involved in environmental monitoring and prediction.
These include the highly specialized nature of much of the technical analysis, the limited capacity for checking the accuracy of many of the findings of this kind of research and the consequent need for the development of knowledge-based inference machines for extracting useful information from secondary and often proxy data.

In Chapter 10 Gatrell and Vincent consider a wide range of natural and technological hazards including industrial hazards, risk assessment, hazardous waste disposal, emergency planning, natural hazards and environmental epidemiology.
The substantive content of much of this research straddles the social, environmental and mathematical sciences.
To model the dispersal of a plume of toxic gas generated by a chemical explosion and its impact on the surrounding area, for example, an understanding of atmospheric dispersion models, epidemiology and population distribution would be required.

In applications of this kind the authors argue that geographic information management in general and GIS in particular have an important role to play and they give a number of examples from research in progress to illustrate the current state of the art in this field.
The discussion of operational problems and prospects further amplifies many of the issues raised in preceding chapters, particularly with respect to the problems caused by the dependency on secondary data sources and the need for much more detailed geographic information to overcome some of the problems associated with linking data sets.

Like most of the other contributors to this section, Gatrell and Vincent see decision support systems as a major area for future development in the geographic information management field.
Given that'most GIS are rather dumb systems, requiring intelligent, very computer literate users', managing natural and technological hazards means that this knowledge base must be built into the system so that it can be utilized quickly by untrained users after a disaster has taken place or in an emergency.

The settlement and infrastructure field is also characterized by a wide range of users with a great diversity of interests.
These include not only central and local government but also major utility companies and transport suppliers.
According to Shepherd these users share a common need for up-to-date information on the amount, capacity and condition of urban land, transport networks, utilities, hospitals, schools and other major communal facilities.
In addition to these data requirements, such users are also interested in developing their capabilities for modelling the changing relationships between the supply and demand for infrastructure in the context of both public and private sector decision-making.

Shepherd, more than any other contributor to this section, draws attention to the extent to which current efforts in the geographic information management field are constrained by the highly fragmented nature of both data suppliers and users both in sectoral and spatial terms, the great diversity of data sets in varying formats and the difficulties presented by institutional factors such as copyright provision, data ownership and the control of access to data.
Digital data occupy a central position in this applications field and a number of examples are given to illustrate the extent to which their development has been hampered or facilitated in various countries by the policies of the organizations with responsibility for digital data provision.

In Chapter 12 Brown reviews the development of geodemographics from its origins in the computer-based social area analysis of US census tract data from 1950 onwards.
He describes the features of the four main systems that are currently in use in the UK and illustrates their application with reference to examples drawn from retail analysis and store location, market research, credit rating and target marketing.
Brown demonstrates the extent to which the growth of research activities in this field has led to the emergence of improved cluster analytic methods for the multidimensional classification of people according to the type of area in which they live.

In the last part of this contribution, Brown identifies a number of priorities for future research.
Like Gatrell and Vincent and Shepherd before him, he is concerned with the lack of detailed geographical information particularly in this case with reference to the years between censuses.
Spatial linkages also feature prominently in Brown's discussion which amplifies many of the points made in the earlier contribution from Openshaw in Chapter 3.
The analysis points to the need for the development of a fuzzy geodemographics methodology which takes account of the effects of different types of spatial errors.
Other major research priorities for the future in this applications field are the development of response-modelling techniques to explore the factors affecting consumer choice.
This is particularly important in a field where many of the demands made by users are highly specialized in nature.

In summary, then, as fig. 8.1 shows, many of the issues raised by this review of geographic information handling in the four potential application fields are essentially complementary to those discussed in the part on methodological developments.
Spatial analysis features particularly prominent on the research agenda relating to natural and technological hazards and geodemographics.
Questions relating to data integration emerge as being particularly critical in terms of environmental monitoring and settlement and infrastructure applications.
Spatial linkages and questions relating to spatial representation feature prominently in the settlements and infrastructure and geodemographics fields.
The evaluation of error propagation is a matter of considerable significance in the environmental monitoring and settlements and infrastructure fields.
Finally, in all applications fields, the findings of the reviews above suggest that there is a need for improvements in user interfaces of all kinds.
This is particularly evident in the demand for the development of knowledge-based decision support systems and modelling capabilities.
Such demands highlight the extent to which geographic information management must be regarded as a means to an end rather than an end in itself when viewed from the standpoints of the needs of planners and decision-makers.

The final chapter in this section rounds off the discussion of applications-related research with an examination of organizational issues that need to be taken account of in handling geographic information.
Campbell presents a conceptual framework for the analysis of the organizational issues involved in the development and implementation of GIS.
This contribution cuts across many of the questions relating to particular applications that were raised in preceding chapters and draws attention to the dangers of neglecting institutional and personal considerations in practice.
All too often, as the experience of many mature applications indicates, technical and data-related matters dominate the system development phase and technically elegant solutions are devised which fail to take enough account of user needs and capabilities.

Campbell discusses the role of geographic information in organizations and the process of GIS diffusion drawing upon research from a variety of social science disciplines.
The findings of the analysis are summarized in two sets of research questions for all applications fields.
In this way she sets out a research agenda for applications-related research which serves a similar function to the spatial analysis research agenda set out by Openshaw at the beginning of Part Two.

### Environmental monitoring and prediction

#### Introduction

Monitoring of the state of and the changes in the environment is now universally recognized as being of profound importance to mankind (Tickell 1986, 1989).
This awareness is most obviously manifested by the frequent appearance of press reports on ozone depletion, on the greenhouse effect and possible global warming, on nitrate pollution, on deforestation in the Tropics, on decreasing biological diversity and on many other environmentally related topics.
Usually these reports concentrate on prophecies of a forthcoming Armageddon but many also describe a dire contemporary situation.
Thus the algal bloom off the Italian Adriatic shore in 1989 is reckoned to have caused the holiday trade and local fisherman losses running into tens if not hundreds of millions of pounds.
More globally, the Brundtland Report (WCED 1987) noted that, in the 900 days during which the World Commission was at work,

- 1. The African drought put the lives of 35 million people at risk and may have killed 1 million of them;

- 2. The Bhopal accident killed 2000 and injured 200 000 more;

- 3. The Chernobyl disaster caused environmental damage across Europe;

- 4. A chemical fire in Switzerland caused toxic materials to be transported by the Rhine at least as far as the Netherlands;

- 5. At least 60 million people died of diarrhoeal diseases caused by malnutrition and dirty water.

As a consequence of these and other disasters, of rapid and world-wide broadcasting of them and of the concerned action of many individuals, the environment is now 'moving fast up the political agenda' (Patten 1989).
The then Prime Minister also emphasized the political awakening to the environment in statements such as: 'it is possible that with all these enormous changes (population, agricultural, use of fossil fuels) concentrated into such a short period of time, we have unwittingly begun a massive experiment with the system of this planet itself' (Thatcher 1988).

The political concern is not altruistic.
Mrs Thatcher, a recent convert to environmental conservation, clearly held the opinion that environmental problems are not only soluble but that solving them can be shown to be cost-effective:

> In the past when we identified forms of pollution, we have shown our capacity to act effectively.
The great London smogs are now only a nightmare of the past.
We have cut airborne lead by 50 per cent.
We are spending £4 billion on cleansing the Mersey Basin alone, and the Thames now has the cleanest metropolitan estuary in the world.
Even though this kind of action may cost a lot, I believe it to be money well and necessarily spent because the health of our economy and the health of our environment are totally dependent upon each other....
The Government espouses the concept of sustainable economic development.
Stable prosperity can be achieved throughout the world provided the environment is nurtured and safeguarded (Thatcher 1988).

The primary official manifestation of this UK commitment to the environment has been the government's White Paper (HMSO 1990).
While criticized by many on the grounds that it had few 'teeth' and represented a compromise between the DoE and all other departments (notably those of Agriculture and of Transport), it was none the less a major achievement.
Its main sections dealt with the government's approach to the environment (nationally, at the European level and globally), the nature and effects of the greenhouse effect, environmental problems in both rural and urban areas (especially in relation to land-use matters), pollution control and enhancing awareness of environmental matters.
Central to this approach is said to be an emphasis upon guidance from the best available scientific evidence.
There is also a clear recognition of the need for monitoring and modelling of the state of the natural and man-influenced environment.
Though there has been a change of Prime Minister and of the Secretary of State for the Environment since the publication of the White Paper, the environmental cause seems as strong as ever.
Thus, The Times of 17 December 1990 reported that a group of 40 of the most senior Civil Servants had met the previous weekend to discuss 'ways in which the government machine could respond better to national and international problems such as the threat of global climate change'.

Pearce et al. (1989) have argued that the effects of government, commercial and other actions on the environment can and should be assessed on a cost/benefit basis and this seems likely to be the basis on which at least the UK government will proceed.
Given such a lead, it is scarcely surprising that British scientists have sought to demonstrate the practical and financial consequences of environmental events and processes; Table 9.1, for example illustrates their perception of the importance of global environmental research to the UK domestic economy.

If it now seems self-evident that monitoring of the global environment is necessary, indeed is even vital, the prediction of what is likely to happen is almost as important: the 170 000 people in the Maldives are understandably worried about the prospect of global sea-level change since no part of the islands is more than 2 m above present sea-level!
Yet, as we shall see below, the prediction of the activities of natural and man-influenced environmental systems requires an understanding of the interaction of processes that, in many cases, we simply do not yet have.
Even monitoring of the present is very imperfect, as witness the order of magnitude variations in estimates now current for deforestation rates.
This chapter, then, attempts to review some of the problems in environmental monitoring and prediction, describes some of the relevant scientific and organizational activities and looks ahead to what is likely to happen next.

#### The nature of environmental processes

Notwithstanding Mrs Thatcher's confidence that we can 'fix' environmental problems, the difficulties associated with a task even as apparently simple as monitoring a state variable are considerable.
Some of the reasons for this - the difficulty of deciding on appropriate proxy variables and on economical yet non-biasing temporal and spatial sampling frameworks, taking account of the relative importance of aperiodic and rare events as compared to near-continuous processes, processing the vast volumes of data usually involved and organizing the multidisciplinary and (often) multinational researchers involved - are discussed briefly later.
Even at this stage, however, it is important to stress that we have a very incomplete understanding of many processes in the natural environment.
The next section therefore attempts to summarize what we do know; it is derived chiefly from the Earth System Sciences Committee (ESSC) (1988).

##### Temporal and spatial scales of operation

Even ignoring the effects of man, earth system processes operate at a variety of spatial and temporal scales (see Fig. 9.1; see also Rosswall et al.1988).
Thus microclimate effects can have major short-term implications for local populations (such as those brought about by the photochemical smogs of Los Angeles), are often applicable only over areas of a few hectares or less and may operate on a diurnal cycle.
In contrast, soil creation (cf. soil degradation) may require hundreds or thousands of years.
In between are variations in phenomena such as El Nino.
The sampling theorem indicates that we must sample these phenomena at a frequency of no less than half their wavelength if we are to avoid bias in measurement.
In this chapter, the primary concern is with changes occurring over time spans from minutes to centuries and from spatial wavelengths from about 1 m to about 100 km.
It is, however, impossible to separate out processes acting at different scales and over different periods: a single volcanic eruption lasting hours or days sometimes leads to dust and gas being ejected into the atmosphere over a period of months and this in turn may lead to global climatic fluctuations over years or decades.
Conversely, a large-scale and long-period phenomenon [UNK] such as the movement of tectonic plates can lead to local stress accumulation and to its release by an earthquake in a few seconds and with highly local effects.
This therefore has the following consequences:

- 1. We should know something about the periodicity of the variables we are monitoring if we are not to risk either unnecessarily detailed data collection or aliasing of trends;

- 2. Since we know that the periodicity of some variables is longer than the monitoring already carried out by human beings, we must make use of surrogate or proxy variables to extend our range of knowledge (such as via tree rings, palynology, oxygen isotope ratios from ice cores and geomorphological evidence of environmental change);

- 3. Since we are not yet able to predict all the interactions which may be important in a study of environmental problems, collecting potentially useful data as well as those believed central to the problem under study is often wise;

- 4. We must accept that most data collection exercises will inevitably be a compromise on the grounds of cost and hence less than perfect data sets will be produced;

- 5. Irrespective of the use of surrogates, monitoring environmental processes only makes sense over time-scales which are extended by human standards (hence the IGBP (see below) is designed to run for two or three decades);

- 6. Changes in political priorities may simply result in the need for informed guesswork if suitable data are not available.

Much attention will be given throughout this chapter to monitoring the environment on a global basis.
This is not merely because of its topical nature.
The main reason is that - though some problems are local and are best studied that way - many others (even involving a limited geographical extent) are best understood within a global framework.
Thus no meteorologist would attempt to forecast the weather 2 or 3 days ahead without using a mathematical model based on observations from all around the world.
Moreover, recent work has shown that much of the heat energy in the seas of the North Atlantic (every square kilometre of which gives off as much energy as a nuclear power station and hence influences our weather) is absorbed from sunlight in the tropical Pacific and is carried by ocean currents through the Drake Passage and up into the Atlantic.
Thus, to understand some local and many regional, national and continental and all global environmental events, we need to have a global perspective and hold global databases (Rhind and Mounsey 1989; Mounsey and Tomlinson 1988).
In no way, however, does this invalidate the need for microscale studies - for instance, while global data sets may indicate the extent of algal blooms and may suggest causes of them, only detailed study of the algae themselves can provide understanding of why the bloom is occurring.

##### The processes themselves

A major complication, however, is that the environment can rarely be treated as in a laboratory experiment.
Given this, determining the nature of the interactions between the variables becomes a matter of major difficulty.
Figure 9.2 is taken from ESSC (1988) and is an attempt to show the interactions between environmental processes, as well as the indicators and implications of change in the state of the environment.
In essence, the figure can be summarized as showing processes within the physical climate system and within the biogeochemical one, these systems being interwoven by the global role of water and increasingly affected by human activities.

The main components of the first system are well known: the atmosphere is its engine and atmospheric circulation is driven by differences in solar heating between the equatorial and polar regions.
We are, however, becoming ever more aware of the massive influence of oceans on our climate; research into ocean/atmosphere interactions is now a priority.
In ocean dynamics studies, important topics are heat storage, circulation and the role of sea ice.
Atmospheric circulation (and, in turn, precipitation and temperature) is also greatly affected by the balance of thermal energy at the land surface, itself affected by the vegetation and terrain characteristics.
The biogeochemical system embraces the totality of the movements of the key elements essential to life - carbon, nitrogen, oxygen, phosphorus and others - through what has been described as the total earth system.
The oceans and their biota play a central role in the carbon and nutrient cycles; global ocean circulation is also critical to the global carbon budget.
Trace gases in the atmosphere are key components of the cycles of such elements as carbon, nitrogen, oxygen, sulphur and the halogens; as is now well known, their concentrations are much influenced by biogenic and anthropogenic activities and the concentrations of such gases as carbon dioxide, ozone, methane, nitrous oxide and the chlorofluoromethanes (CFMs) strongly affect radiative transfer and provide a link with the physical climate system.
A particular cause for concern is that the concentrations of the two main CFMs is increasing by about 5 per cent per annum while the equivalent figures for methane, nitrous oxide and carbon dioxide are 1, 0.4 and 0.3 per cent.
Finally, the chemistry of the stratosphere is dominated by the photochemical production and catalytic destruction of ozone.

There are several important ways in which biogeochemical processes can influence climate and hence habitability (except where the latter is maintained at enormous cost).
If, for instance, the concentrations of certain trace gases (see above) continue to increase, it has been predicted that the earth's surface temperature will increase by an amount comparable to that since the last major phase of the most recent glaciation (about 18 000 years BP) - though there is some dispute about the magnitude of the likely change.
The converse case - the effect of physical climate changes on biogeochemical processes - is also of obvious importance: changes in annual averages and cycles of temperature and precipitation, together with the probabilities of [UNK] extreme events such as prolonged droughts or frosts, are major determinants of terrestrial ecosystem type, at least in areas largely unaffected by human activity.

Human-induced changes to the environment have increased rapidly as a consequence of growing population numbers and of numerous developments in technology.
fossil fuel combustion, for instance, has led to increased concentrations of sulphate in precipitation (' acid rain') and many rivers, lakes and estuaries have been greatly affected by phosphates from agricultural, urban or industrial sources.
It should be stressed, however, that - while the outlines of human activities are clear - there are still many uncertainties: for instance, we know that the atmospheric concentration of carbon dioxide has risen about 9 per cent since 1959.
But calculations of the total carbon released by fossil fuel combustion imply that, if all such carbon remained in the atmosphere, the concentration would have increased by twice as much.
The absolute difference between the two figures seems to be due to two different factors: absorption by the oceans and other reductions in carbon stocks in living biota, the latter being strongly affected by human activities since the Industrial Revolution.

##### Does God play dice?

Much environmental prediction is predicated upon a logical positivist or Newtonian deterministic basis.
The environmental systems are effectively regarded as machines whose workings can all be discovered, described in differential equation form and whose future activities can thus be predicted in detail if their initial states are known.
An argument by many atmospheric physicists, for example, is that shortcomings in the accuracy of weather prediction over periods of more than a few days largely results from the unsophisticated nature of existing models, the lack of suitable data and inadequate computer power (see Fig. 9.3, derived from Tyler 1989).
In [UNK] contrast, the advocates of chaos theory (e.g. Stewart 1989) argue that some natural systems are so sensitive to tiny stimuli that even 'the faint beat of a butterfly's wing could be the ultimate trigger for a hurricane'.
In essence, they argue that tiny differences in the initial conditions of many systems can lead to widely different outcomes since the systems exhibit stochastic behaviour within a deterministic framework.
If so, there is little chance of making accurate long-term forecasts of these systems.
This has been recognized by, among others, ESSC (1988).
The authors of that report accepted that there is a theoretical limit of 2-3 weeks in explicit prediction of day-to-day fluctuations in weather because of the influence of small-scale turbulence within the large-scale dynamics; such limits imply that medium and long-term prediction must inevitably be stochastic.
To complicate matters still further, however, it seems at least possible that the components of the earth system may best be predicted deterministically at some spatial and temporal scales but stochastically at others and that the basis of prediction will differ for different components.
As an example, atmospheric temperature shows marked day-to-day variability, a strong seasonal cycle with some year-to-year variations, a weak minimum variability for 10-20 year averages and then increased variation again at longer time-scales (ESSC 1988).
It need hardly be pointed out that coping with such multiple databases on which modelling is to be carried out is not a trivial exercise.

Finally, it is perhaps worth concluding this section by emphasizing that there is still much controversy among the scientific community about the magnitude of many of the effects being discussed.
In general, the research work of the international groups of scientists, including those involved in the Inter-Governmental Committee and in the UK's Inter-Agency Committee on Global Environmental Change, has progressively reduced the magnitude of the predicted effects of, for example, global warming.
In giving the 1990 Robens Coal Science Lecture at the Royal Institution, Sir John Mason (a former Director of the Meteorological Office) urged caution in interpreting the results of the massive atmospheric and oceanic modelling exercises; as the equilibrium models are refined to take account of the thermal lag in oceans, etc., lower values of predicted changes are likely.
Thus, while almost all scientists are - at the time of writing - convinced from the evidence that change in climate is under way and that regional effects may be much greater than the global average, the magnitude of the latter is now thought likely to be about half of what was predicted only 5 years ago.

#### Who is involved and what is going on?

If we consider the environment in the broadest sense, much monitoring of it has been in progress for many years and by an enormous diversity of organizations in the UK; these include the DoE, the Forestry Commission, the Nature Conservancy, the Health and Safety Executive, local authorities, the component members of the Natural Environment Research Council (such as the Institute of Terrestrial Ecology and the British Antarctic Survey), individuals or research groups in academia, the CEGB, the Friends of the Earth, and UK Centre for Economic and Environmental Development (CEED) (1989).
The diversity of monitoring organizations seems just as great in other countries; numerous multinational organizations, both quasi-governmental (e.g. the UN Environment Programme (UNEP)) and non-governmental (e.g. the International Union for the Conservation of Nature (IUCN) and the International Institute for Environment and Development (IIED)) are also active in the field.
Moreover, commercial monitoring of the environment is now also routine, notably to predict crop yields in the main grain-growing areas and hence facilitate the buying of futures.

##### The international scientific involvement

Scientists have both promoted and responded to the increasing interest in the environment.
Thus, at the global scale, the International Council of Scientific Unions (ICSU) has endorsed the setting up of the International Geosphere Biosphere Project (IGBP) to 'describe and understand the interactive physical, chemical and biological processes that regulate the total Earth system, the unique environment it provides for life, the changes that are occurring in that system and the manner by which these changes are influenced by human actions' (Report of ad hoc Planning Group for IGBP 1986, quoted in IGBP 1988).

Priority in the IGBP is intended to be given to those areas which deal with key interactions and significant changes on the time-scales of decades to centuries, that most affect the biosphere, that are most susceptible to human perturbations and those that will most likely lead to a practical, predictive capability for global change.
This is to be put into operation by concentrating on four themes:

- 1. Documenting and predicting global change;

- 2. Observing and improving our understanding of dominant forcing functions;

- 3. Improving our understanding of interactive phenomena in the total Earth system;

- 4. Assessing those effects of global change which will be large scale and cause major modifications to both renewable and non-renewable resources.

By 1990, IGBP had progressed as far as defining a set of seven core projects (IGBP 1990) addressing these four themes.
In addition, plans for regional research centres and for the data and information systems for IGBP (known as IGBP-DIS) had been announced.
The latter are particularly relevant to this chapter.
Based in Paris and working under Professor I. Rasool, it is intended to concentrate on managerial and policy aspects of the task in the first 2 years (1990-92) but then to expand considerably thereafter.
Tasks agreed for the IGBP-DIS include making available a 'directory of data directories' modelled on NASA's Master Directory, providing data sets for education and training and undertaking a land cover pilot study.

Until 1990, remarkably little interaction had taken place between the 'hard science' and the social science communities on global monitoring and prediction.
It is noteworthy, however, that the Royal Society made a plea for just this type of multidisciplinary work in its submission on greenhouse gases to the House of Lords' Select Committee on Science and Technology (Royal Society 1989: 40).
Fortunately, in addition to the actions of the world 'hard science' community, a parallel effort is now being initiated by social scientists (Fuchs 1989; Jacobson and Price 1990).
Currently this is organized and sponsored by the International Social Science Council (ISSC), the UN University and the International Federation of Institutes of Advanced Studies.
Its objectives are to:

- 1. Improve scientific understanding and increase awareness of the complex dynamics governing human interaction with the total Earth system;

- 2. Study, explore and anticipate social change affecting the global environment;

- 3. Identify broad social strategies to prevent or mitigate undesirable impacts of global change or to adapt to changes which are unavoidable;

- 4. Analyse policy options for dealing with global environmental change and promoting the goal of sustainable development.

Jacobson and Price (1990) provide a useful summary of the ways in which human factors contribute to, and are affected by, likely global changes; in particular, they stress the importance of the data-handling issues and the role of GIS in coping with some of the problems of data integration and manipulation.
The ISSC proposed its own work programme in the Human Dimensions of Global Change in late 1990.

While these organizations intrinsically have a world-wide membership and are concerned with research into global environmental change, others share the same interest but from a more restricted geographical base.
A leading example of this is the European Science Foundation which has sponsored research programmes in both the physical and social science aspects of environmental change (ESF 1990).

##### Governmental and political involvement

The spread of environmental awareness is readily demonstrated: in 1972, 26 countries had environmental and natural resource management agencies whereas, a decade later the number was 144 (WEC 1985).
In most countries, the governmental and political concern with the environment has come somewhat later than that of scientists or concerned lay people: the early development of the Green Party in the Federal Republic of Germany is something of an exception.
Such a commitment to the environment is, none the less, both welcome and necessary if resources are to be made available to tackle existing, let alone forthcoming, environmental problems.
The 'conversion' of the UK government has been briefly described earlier; it is manifested in their July 1989 commitment to spend £10m. on climate change research in 1989/90 and the confident request to them from the Advisory Board for the Research Councils (ABRC) for an extra £11m. in 1990 and £13m. in the two succeeding years for additional environmental research.

Perhaps the most significant development of all, however, is the increasing role of the European Commission.
Their role in bringing environmental impact assessment (EIA) on to the statute book is well known, but the Commission has now made a proposal (CEC 1989) for the 'establishment of the European Environment Agency and the European Environment Monitoring and Information Network'.
The Commission argues that there is at present no monitoring of environmental quality and trends on a European scale, nor any guarantee that the results of environmental monitoring will be comparable on a Community-wide basis (a realization brought about through the CORINE programme described later).
The objectives of the new agency would be to assist the Community and the Member States to achieve the goals set out in the Treaty of Rome and in successive environmental action programmes; it must also, however, be seen in the context of the European Council's adoption on 2 December 1988 of the Rhodes Declaration on the Environment and the environment chapter in the Single European Act which comes into effect in 1992.

The detailed specific roles of 'the System' (comprising both agency and network) are envisaged as:

- 1. To provide the Community, the Member States and participating third countries with the objective (sic) information requested for the formulation and implementation of sound and effective environmental policies;

- 2. In particular, to provide technical, scientific and economic information requested by the Commission in its tasks of identification, preparation and assessment of the implementation and results of environmental action and legislation;

- 3. To stimulate the development and the application within the agency of techniques of environmental modelling and forecasting in order that adequate preventative action can be taken at the appropriate time;

- 4. To help ensure the harmonization and comparability of environmental data in the Community as well as the integration of European environmental data into international environmental monitoring programmes, such as those established within the framework of the United Nations and its system of agencies.

Considerable stress is laid by the Commission on collaboration with national data-gathering agencies and with states adjacent to the Community's borders.
It is envisaged that the totality of activities will extend the existing State of the European Environment report (CEC 1988) through addressing the issues of the quality and sensitivity of the environment and also the pressures upon it.
Priorities for the new agency include study of atmospheric emissions and quality, water resources and quality (including the marine environment), soil erosion and pollution and important land resources, and biotopes and nature conservation.

At the time of writing, the proposal has been approved and discussions are in progress on the location of the agency's headquarters.
It seems certain to have major and growing effects upon environmental monitoring and prediction in Europe and on the policies of component governments.
Yet this is by no means the only plan which the Community has in relation to the environment: Directorate-General XII (that for Science, Research and Development) has published details of an extensive R&D programme (CEC 1990a) and the Commission as a whole (CEC 1990b) has made public its plans to develop regular official statistics of the environment.

##### The private sector

Certain aspects of environmental monitoring have long been carried out by the private sector, notably that of crop states on a world-wide basis.
Derived from satellite imagery at comparatively low resolution, predicted yields for different crops in different nation states become of commercial value.
However, significant resources are also being made available by the private sector where there is no immediate commercial gain: thus IBM UK Ltd has donated £3.5m. of computing equipment to UNEP and IBM in general is actively supporting other R&D which can be expected to facilitate 'sustainable development': IBM Europe, for instance, has invested $16m. in its Bergen scientific centre to make it the focal point for the company's environmental modelling and a centre for information on the environment and sustainable development.
On a more modest basis, IBM UK have agreed to fund a pilot global population database being built in Birkbeck College to permit assessment of the impact of environmental change on the world s population.
Many other companies, of course, are supporting environmental work but IBM seems almost to be unique in its corporate commitment to use of high technology for facilitating 'sustainable development'.

#### Some examples of environmental monitoring projects

##### The local scale

At the local scale, it is usually impossible to neglect the effects of multiple processes operating.
An example of environmental modelling and prediction where the interactions between different processes and dynamic feedback is taken into account is given by Haber and Schaller (1988).
Their work formed part of one UNESCO Man and Biosphere (MAB) project, carried out in the Berchtesgaden National Park in Bavaria.
Following Holling (1978) and Grossman (1983), they conceptualized the man/environment relationship at a series of hierarchical levels:

- 1. The lowest, or process, level, is directly and (usually) obviously connected to perceived reality.
Thus processes and interrelationships are mostly obvious, simple and linear; data are usually readily available and may be voluminous.
This level is readily handled in commercial GIS;,

- 2. The intermediate, or dynamic, level is concerned with less frequent and often irregular events, e.g. a temporary lack of water because of fire, frost or excessive demand from an increasing populace.
Characteristically, the data used may be more difficult to obtain and are usually more spatially aggregated; modelling software which permits feedback loops is essential;

- 3. The top, or strategic, level is the most difficult to explore; the external influences are often unpredictable by formal means.
Relevant data are therefore difficult to identify and scenario building is one of the few approaches available.

The Haber and Schaller approach is to 'soft-couple' these different levels and their accompanying approaches using an ecological balance model.
Results of running this with different scenarios include 'time slice' maps of possible outcomes and of the exchange of material and energy within the study area.
While ultimately qualitative, it seems to offer a method for coping with different types of process and incorporating stochastic and truly random events.

##### The national and continental scale: the CORINE project

The CORINE programme represents the product of much activity by the European Commission's Directorate-General (XI) for the Environment.
It originates from an Italian request to the Council of Ministers in 1973 to identify environmentally 'balanced' and 'unbalanced' areas in the Community; the first attempts to do this were unsuccessful and, though by 1981 it was clear that a new approach based on an environmental information system was the most promising one, funding for this was not secured until 1985.
A 4-year experimental programme to 'collect, co-ordinate and ensure the consistency of information on the state of the environment and natural resources in the European Communities' was set up and labelled CORINE.
The objectives of CORINE were to be achieved through bringing together existing data holdings in the member states, developing methods for holding, analysing and presenting the data, and encouraging the exchange of data.
A number of priority areas were identified, including biotopes of importance for nature conservation, acid deposition and its effects on soils and biotopes and the protection of the environment of the Mediterranean region (Briggs and Martin 1988).

Many achievements can be claimed by the CORINE project team.
As a result of some 40 sub-projects involving all the Member States (and often several groups within each one), databases of topography, soils, water resources and quality, biotopes, atmospheric emissions, climate, soil erosion and administrative boundaries have been built up for the whole Community and can be interrelated; other data sets (such as land cover, derived from satellite imagery) have already been compiled for some of the Member States.
Various aspects of the CORINE project have been described in papers by Rhind et al. (1986), Wiggins et al. (1987), Briggs and Martin (1988), Briggs and Mounsey (1989) and CEC (1990c).
For the present purposes, however, the key findings are:

- 1. Many necessary data sets were unavailable for reasons of administrative inadequacies, confidentiality constraints, cost or non-collection in certain countries;

- 2. The unavoidable reliance upon existing data sets led to many problems due to non-harmonization even of commonly used variables, e.g. eight different definitions of potential evapo-transpiration were in use in the Member States and 'maximum temperature' at each weather station was defined in at least four different ways;

- 3. The compilation of a spatially coherent database from mapped information compiled by different organizations at different scales and on different topographic bases (see Rhind and Clark 1988) is often difficult;

- 4. User expectations are often unreasonably high; use of administrative computing systems encourages bureaucrats to believe that environmental data can just as readily be analysed and used to support decisions.
The 'fuzzy' nature of much geographically distributed data, the inherent errors in it, the effects of the processing algorithms used and the assumption of known interactions between variables ensures that completely routine use by unskilled users is unlikely to be possible in the foreseeable future;

- 5. More detailed data are required for particular tasks as the role of CORINE grows.

The European Commission's proposal for an environment agency (see above) will subsume the CORINE team and databases.

##### The global scale: NASA and GEMS/GRID

Without question, the largest 'player' in the global environment arena is NASA.
The organization has initiated many of the schemes which now are under discussion - the IGBP, for instance, has been strongly influenced by NASA proposals.
A summary of current activities and future plans is given in NASA (1988b).
By way of example, current programmes are collecting global data on stratospheric ozone, on sea-surface and sea-ice variables and on the earth's radiation budget.
Approved future programmes include the Upper Atmosphere Research Satellite, the NASA Scatterometer and the joint NASA/CNES Ocean Topography Experiment.
In addition, however, funding has recently been approved for a much more ambitious scheme - the Earth Observing System (EOS).
This is conceived not as a set of hardware but as a comprehensive information system focused on the needs identified by the ESSC (see above) and anticipating somewhat those of IGBP.
It will collate data from the two proposed space station polar platforms, one European Space Agency platform, a Japanese one and also from the manned space station.
On this basis, a data flow of no less than 1 terabyte (i.e. 10&sup12; bytes) /day is anticipated by the mid-1990s.

A major user of NASA data and skills has been the UN Environment Programme.
formed in the wake of the 1972 Stockholm conference, UNEP soon spawned the Global Environment Monitoring System (GEMS) as well as an international register of potentially toxic chemicals and a global network of sources to locate and provide technical, scientific and management information on the environment.
The need for a mechanism to handle the global environmental data was defined in the early 1980s and the Global Resources Information Database (GRID) resulted.
Mooneyhan (1988) has described the progress of the pilot stage of GRID which culminated in approval for a full operational phase; GRID is now involved in integrating, storing and exploiting a variety of global environmental databases, mostly acquired from NASA.
In addition to the work being carried out in the UNEP HQ at Nairobi and in the GEMS/GRID site in Geneva, a series of GRID regional nodes are now being set up world-wide, each equipped with the same hardware and software and local subsets of the data.
The first of these is in Bangkok and another is to be opened in Latin America.
Moreover, national nodes are also being set up; the recent IBM gift to GRID (see above) has ensured that powerful microcomputers have been installed in many African countries, together with national and continental data sets.
Training of unskilled staff to operate this equipment and to exploit the scientific data is now a major role for GRID staff.

#### Technical aspects and problems

It follows from much of the above that there are major challenges in use of environmental data.
These are best considered by itemizing characteristics of contemporary environmental monitoring and prediction:

- 1. The use of secondary data, rather than primary data collected by the data analyst;

- 2. The need, at least with data on the terrestrial environment, for an inference process to extract useful information from the secondary (and often proxy) data;

- 3. The data volumes collected are often voluminous even by the standards of contemporary computing facilities;

- 4. The analyses carried out are often arcane in detail to all but a small group of 'high priests';

- 5. We have only a limited capacity for checking the accuracy of many environmental monitoring results, let alone of predictions.

Some of these characteristics are now addressed in slightly more detail; it will be obvious that such problems merit a paper in themselves.

##### Remote sensing as a data collection process

As the need for more extensive, high-resolution yet consistent and up-to-date data becomes more pressing, increased use of remote sensing seems inevitable.
No other data collection methodology obviates the short distance variation in data sets induced by variations in data collection and aggregation methodology typically encountered between adjacent nation states.
The problem is now recognized, especially in Europe, and strenuous efforts are being made to harmonise the data sets (e.g. through the use of standard classifications, such as that for land use produced by the Conference of European Statisticians in 1989).
At present, however, ground-collected environmental data are far less than ideal.
Recognizing this, NASA (1988a) concluded that forthcoming global science projects would need land surface altitude data at three resolutions: 1 km resolution in XY and 10-100 m resolution in Z on a global basis, 100 m XY resolution and 1-10 m resolution in Z for regional databases and 10 m XY resolution and 0.1-1 m in Z for local studies.
They argued that existing maps and digitized files from them are unable to meet these needs at global or regional scale and only remote sensing could help in the short term: the availability of stereometric data from the French SPOT satellite has already led to proposals for automated creation of global digital elevation models with a spatial (XY) resolution of about 30 m (Muller 1989).

For many terrestrial purposes, however, a substantial inference process must take place to convert the radiometric measurements into useful information (in contrast, more direct measurements of sea state, etc. are possible).
The value of this information is inherently dependent upon the quality of the inference process and that in turn depends upon the complexity of the scene, the spatial, temporal and spectral resolution of the sensors and the particular algorithms used.
Thus far, for instance, accuracies of land cover (let alone what is often needed, i.e. land use) determined from Landsat and SPOT imagery for the UK have rarely been higher than 70 per cent unless trivial classifications (e.g. built/unbuilt land) have been used.
One solution to this is to 'densify' the ground control and another is to use contextually based classifiers rather than the traditional, spectrally based ones.
But the ground conditions in some parts of Europe make good results extremely difficult to obtain: some areas of Portugal, for instance, have field sizes of only a few metres and exhibit multi-level and multi-seasonal cropping.

A further difficulty is the cost of the data in relation to its anticipated benefits.
Relatively few cost/benefit studies have yet been carried out except in such areas as crop prediction and ocean navigation (where they are generally shown to be highly advantageous in saving someone else's money).
It may be that a study commissioned from contractors by the British National Space Centre will provide useful evidence on the cash value of remote sensing; it is particularly timely in view of the appointment of Professor Pearce (see above) as the adviser to the UK Secretary of State for the Environment.
Other work on assessment of costs and benefits of such data have been carried out for the French government by Professor Didier (1990).
Finally, since data are often costly to acquire, it follows that summaries of them e.g. The State of the European Environment report (CEC 1988) and the Environmental Data Report of the UN EP (GEMS MARC 1989) are of considerable value.
Equally, the 'signposting' role now being adopted by UNEP's GRID project - which is expected to offer on-line access to a catalogue of environmental data sets and details of the responsible agencies in 1991 - is to be welcomed.

##### The data problem and partial solutions

The lack of harmonization of definitions and methods of collection of environmental data have already been outlined above.
In the European Community of 12 nation states, for instance, no less than eight procedures for calculating potential evapo-transpiration have been in use!
The need for harmonization is obvious and, in this respect, must follow from the successful pioneering achievements of EUROSTAT in harmonizing the definitions in trade, demographic and other 'social science' statistics (see CEC 1990b).

An additional and severe problem is that the volumes of data which are already collected are huge by the standards of only a decade ago.
By 1995/96, they will be very much greater, notably from the EOS programme.
NASA has announced plans to collect up to 1 terabyte (10&sup12; bytes) /day.
Since remote sensing data sets (especially those pertaining to terrestrial areas of the globe) typically need much pre-processing to calibrate, transform and then perform an inference process and hence convert measurements of the radiation reflected or emitted by small areas of ground into useful (e.g. land cover) data, the processing power required is going to be formidable.
Other, non-remote-sensing data sets are smaller in volume but more complex in structure and in their characteristics.
To hold all of the 1/50 000 scale topographic map coverage alone for the European Community would probably require about 3 terabytes of storage.
Parenthetically, the form in which the data may be held can affect dramatically the scale of the problem faced.
It would be technically possible, for instance, to hold in less than 1 terabyte detailed information for every individual in the world, akin to that collected about everyone in the UK through the Census of Population.
In practice, legislation generally forbids such data being held thus and distributed in anything other than area aggregate form; the cross-tabulations commonly employed (e.g. to give tables of population numbers broken down by age and sex) often result in a great multiplication of the data volumes.

This all presents major problems of data storage, handling (especially for global data sets), display and dissemination.
Fortunately, technical developments have ensured that the increase in computing power per unit cost has been growing at about an order of magnitude every 6 years over the last three decades.
Indeed, this may grossly under-represent the present situation: the rapid spread of UNIX-based systems seems to facilitate competition and, at the time of writing, performance of workstations per unit cost seems to be increasing at about 50 per cent per annum.
Moreover, the advent of low-cost, high-density-storage devices like CD-ROMs may well make substantial data sets available even to those with modest computing power: a CD-ROM, for instance, can hold about 600 megabytes (i.e. 10&sup6; bytes), can be reproduced currently for about £1 and read on a device costing about £400.
Yet, despite such revolutionary changes in technology, novel solutions will still be required to make effective use of the new data sets.
One such solution is Goodchild and Yang's (1989) scheme for a hierarchical spatial data structure to handle data for the spherical earth.

A particular problem is that little or no quantitative regard has been paid until recently to the effects of quality variation in environmental data.
The literature of the last few years is thronged with papers proposing that these must be taken into account - but with few realistic proposals on how this is to be achieved.
Goodchild (1988) has made perhaps the best summary of the problem and possible solutions to date.

Finally, relatively little emphasis has been given to the management of data as a corporate resource, available to a wide community: many environmental data are collected on a project-by-project basis and 'lost' once the urgency of the initial research is over.
However, the 1990 report of the Data and Facilities Working Group of the UK Inter-Agency Committee on Global Environmental Change argued strongly that planning for the dissemination and maintenance of such data was a vital role.
It also noted that ownership of and access to environmental data was a policy matter of the greatest importance; this may be more difficult in 'within country' data than with global data since the latter are often already the subject of international exchange agreements at zero cost.

#### Global environmental research and the social sciences

Thus far, the emphasis has been very much on the natural science aspects of environmental monitoring and prediction.
That is unremarkable since the anticipation of such problems and assessments of some of their causes and magnitudes can only be made by environmental scientists.
Yet the consequences of any significant changes are a matter of the utmost concern to planners and to politicians at all levels, the quantification of the costs and benefits of alternative policy strategies is very much a matter for economists, and the adaptation of societies to massive change is a particular interest to sociologists and others.
For geographers - who span the conventional (and now archaic) dichotomy between the natural and the environmental sciences - all of these aspects need to be woven together to anticipate the likely spatial patterns of the effects of massive change, the redistributions in trade, health and wealth which they will bring about and the 'knock on' effects these consequences themselves will have on society and the environment.
For social scientists, then, environmental monitoring and prediction are a matter of considerable significance, especially as 'globalization' of markets and economies proceeds.

The Economic and Social Research Council (ESRC) commissioned two reports on global environmental change to guide or at least inform the allocation of research funding.
These reports (Pearce 1990; Turner 1990) may be taken as informed views from at least the economists in the UK social science community on the social science aspects of global environmental change.
Pearce (1990), for instance, presented an economist's views of the high-priority topics for research as follows:

- 1. The theory and practice of international agreements, viewed in a game theory context;

- 2. The theory of optimal behaviour under scientific uncertainty;,

- 3. Cost-benefit frameworks, especially for dealing with man-induced climatic effects;

- 4. Definition of the impacts of climate change on eastern Europe and the developing countries;

- 5. Appropriate policies on non-carbon dioxide greenhouse gases;

- 6. Assessment of the ecological values of tropical forest;

- 7. Economic instruments for reducing greenhouse gases;

- 8. The international politics of climate change;

- 9. National and global energy options given the greenhouse effect;

- 10. Trade and global change.

Turner (1990) argued that the priorities are as follows:

- 1. The socio-economic consequences of sea-level rise;

- 2. Techniques for the valuation of environmental resources and effects;

- 3. An assessment of management tools, institutional adaptation and policy integration in regard to global environmental change;

- 4. Studies of agriculture in relation to climate change;

- 5. Understanding of how environmental issues and technical change interact;

- 6. The interrelationship between environmental ethics and economics.

There is, then, no shortage of social science research which is claimed to be necessary if we are to cope with environmental change.
Some of it is being carried out: in March 1991 ESRC announced a £6m programme of research on Global Environmental Change.
However, perhaps most critical of all in the early stages is social science practice rather than research.
In the USA at least, there needs to be an improvement in scientists' understandings of how to influence the allocation of funding for remedial measures or for further research (see Kitsos and Ashe 1989).
All too often, it seems that the coupling of an as yet imperfect scientific understanding to policy-making is tenuous (see Table 9.2).
Fortunately, considerable high-quality work has already begun on the legal, political and institutional aspects of global environmental change (see, for instance, Nitze 1990).

#### What next?

The contents of this chapter have scarcely touched upon such important environmental research as the World Ocean Climate Experiment or the World Climate Research Programme.
Nor has there been any discussion of the growing requirement in the UK (as elsewhere) to carry out an environmental impact assessment for all major developments.
The consequences for some nations or subgroups in a population of being without access to environmental data or the tools for analysing them while others have such access are potentially profound - as the European Commission has recognized in issuing a directive on public access to environmental data (CEC 1990d) - yet space limitations have also precluded their discussion.
Despite these shortcomings dictated by the space available, what has been said should be sufficient to illustrate the enormous and diverse scope of environmental monitoring and prediction.
Such is its diversity that measuring the total expenditure on it seems quite impossible and the number of 'actors' already involved is vast.
What is clear, however, is that monitoring is rarely a simple exercise, that the time-scales of the sponsors of monitoring and environmental research are rarely long term though most science is inevitably of this nature and that the increasingly multinational nature of such work necessitates a degree of management not always present in local or nationally based schemes.
In these circumstances, it is scarcely surprising that there is evidence of international and interdisciplinary dispute, as Terney (1989) has chronicled in regard to IGBP.
Moreover, as Newby (1990) has pointed out, the complexities of environmental research have created a new kind of relationship between research and policy: 'in the past,... the relationship was predicated on the belief that science provided decision-makers with objective 'hard' facts on which to base their soft, value-ridden policies....
But now we find scientists delivering only 'soft', uncertain 'facts' to decision-makers facing 'hard' decisions.'

Yet, even if all of this causes great uncertainty among scientists, it is still a reasonable prediction that a decade ahead will see both environmental monitoring and prediction treated as an everyday need and activity in major organizations.
We shall also see the existence of binding requirements upon national governments - certainly in the European Community - to collect at least basic environmental indicators in a harmonized form (CEC 1990b).
More than that, it seems highly likely that the social science aspects of environmental problems will underpin the actions of governments and international agencies.

Perhaps the single most important conclusion to be drawn from this review is that the monitoring, modelling and management of the global environment are tasks which uniquely require the integration of skills and techniques from many disciplines.
Building such research teams is essential.
Underlying it all, however, is one obvious fact: that the gathering and analysis of geographically distributed environmental data form the necessary starting-point for ensuring the success of our future on earth.

#### Acknowledgements

Thanks are due to Tina Buckle and Jonathan Raper for remastering the diagrams.
The UK ESRC supported the work of the South East Regional Research Laboratory in Birkbeck College, University of London, from which this review has grown.

### Managing natural and technological hazards

#### Introduction

Few areas of the application of GIS technology can be as socially significant, or environmentally relevant, as the management of emergencies and disasters due to natural and technological hazards.
Whether attempting to construct a database of resources for use in planning responses to nuclear emergencies, developing optimal routes for scheduling the safe transport of hazardous substances, or monitoring the health implications of a disaster, GIS can assist in identifying possibilities and formulating solutions.
The 1990s have been declared the International Decade for Natural Disaster Reduction.
Let us hope that G1S can, in some small way, help mitigate the suffering and hardship felt by all those afflicted by the effects of hazards which, as we have learnt with bitter recent experience in the UK, can occur in an untimely fashion in the most improbable of places.

Research on hazards is multidisciplinary and straddles the social, environmental and mathematical sciences.
If, for instance, we wish to model the dispersal of a plume of toxic gas resulting from a chemical explosion, assess its possible impact on human health and evaluate likely evacuation scenarios of the population at risk we would require, for example, a knowledge of atmospheric dispersion models, epidemiology and population distribution.
Some researchers suggest that hazards (and emergencies that might result) can be regarded as either natural or technological.
We shall elaborate on this simple division below but suggest here that the wealth of literature on the former (see, for instance, Burton et al.1978 and Perry 1981) has yet to be matched by a similar volume of work on the latter.
There are signs that this imbalance is being rectified (Zeigler et al.1983).

Hazard research, like few other GIS application areas, is not only stretching the present technology to its limits but is a quite remarkable focus of international effort into several important research-related areas such as expert systems and simulation studies.
In this sense the scene is clearly one of hazard problems looking for improved GIS rather than for GIS looking for good problems, as is all too often the case.

#### Hazard research

##### What are hazards?

Formally, a hazard can be defined as: 'a physical situation with a potential for human injury, damage to property, damage to the environment, or some combination of these' (Health and Safety Executive 1989: 30).
A hazard is a threat which, given a set of circumstances, may become translated into a realized event.
What we choose to call this event depends upon factors such as its magnitude: we speak for instance of accidents, emergencies, disasters and catastrophes, each of which carries connotations concerning the scale of the event and each of which will have a set of human and/or environmental consequences.

On 30 March 1956 one of the most powerful volcanic disturbances this century, the Bezymianny eruption, occurred.
Few people noticed the event as it took place in an uninhabited part of Kamchatcka and caused no known casualties.
In contrast, the extrusion of a small volume of lava from a secondary cone on the slopes of Tristan da Cunha became the focus of global interest when, during October 1961, the island's lobster processing plant was smothered and the 300 people of the island's only settlement were evacuated to the UK.
These two contrasting events emphasize the central fact that even natural hazards are not defined solely by the characteristics of the event but by the interaction of those events with the human occupation of the threatened area.

As noted above, the simple division of hazards is between those which are natural and those which are technological or human-induced.
Each of these may be further subdivided and the typology shown in Fig. 10.1 draws upon the classic work of Burton and Kates (1964) in separating geophysical from biological hazards and Zeigler et al. (1983) in distinguishing public (or what we might call societal) hazards from private (individual) ones.
The further subdivision of natural hazards is self-explanatory as is that of individual technological hazards.
Zeigler divides the public hazards into those which result from the production of raw materials and manufactured goods, those which originate in transport and transmission and those which threaten the public in their role as consumers.

The United Nations Disaster Relief Organization (UNDRO) has produced a classification of disasters, derived on the basis of case data (Table 10.1).
UNDRO recognizes three basic types of disaster: accidents, natural events, and other disasters.
The differentiation of accidents from other types is useful in the context of emergency planning and is not so clearly conveyed by other [UNK] [UNK] hazard typologies.
However, the temptation in all classification exercises is to produce partitional schemes and this should really be resisted here.
It is more useful (Johnson 1983) to adopt a non-partitional scheme (fig. 10.1) that recognizes, for instance, food poisoning as both a personal and consumer hazard, or lead pollution (e.g. from car exhausts) as both a meteorological event and technological hazard (both public and private).
An air crash (as at Lockerbie) affects an entire community directly, as well as being an occupational hazard and risk to the individual traveller.
Hillslope failure (as [UNK] at Aberfan in South Wales in 1966) is a geomorphic hazard but may arise because of raw material extraction.
Dutch elm disease is a floral hazard but is exacerbated by the transport of infected logs.

Hohensemer et al. (1983) make the important point that hazards are multidimensional in nature and suggest 12 dimensions along which any hazard may be scored (see Table 10.2).
These factors will, of course, be important in deciding on the role that GIS can play in hazard monitoring and emergency planning.
For instance, some events will persist briefly, have immediate consequences, minor transgenerational effects and have little or no potential for non-human mortality (an air crash is an example).
Others, such as a chemical explosion involving the release of a toxic gas, may persist for a week or more, have delayed consequences, may affect a future generation if the toxic chemical is mutagenic and may have a significant impact on plant and animal populations.
There may be more scope for a GIS approach in the latter than in the former situations.
The Hohensemer scheme is not, however, beyond criticism.
for example, can hazards really be thought of as having any intentionality?

##### Industrial hazards and risk assessment

Once hazards have been identified there may follow efforts to assess the hazard risk.
By 'risk' we understand 'the likelihood of a specified undesired event occurring within a specified period or in specified circumstances' (Health and Safety Executive 1989: 30).
It may, of course, be easier to quantify risk for natural hazards because of historical records and statistical estimation of recurrence intervals.
Technological hazards are more unpredictable and may be extremely rare, so that it becomes difficult to use probability concepts to quantify risk, especially those which rely on notions of relative frequency.

The identification of chemical hazards requires that the locations of sites be known, together with the dangerous substances stored or processed there.
In the UK (see Petts 1988 for a splendid overview) the Health and Safety Executive must be notified of sites where hazardous substances in excess of threshold limits are handled.
Such substances and thresholds include, for instance, 25 tonnes of flammable liquid petroleum gas and the explosive sodium chlorate, and 10 tonnes of toxic chlorine gas.
Some 1600 installations are notifiable, along with thousands of kilometres of pipelines (mostly high-pressure natural gas transmission lines).

Following a number of major accidents involving industrial activities (including those at Flixborough, Humberside in 1974; Beek, the Netherlands in 1975; and Seveso and Manfredonia in Italy in 1976), the EC issued a Directive on Major Accident Hazards.
The Directive, which is commonly referred to as the 'Seveso' Directive, was issued in June 1982 and in the UK its requirements were embodied in the Control of Major Accident Hazard (CIMAH) Regulations (1984).
Among other things, these regulations require operators of hazardous installations to draw up on-site and off-site emergency plans and to give information to members of the public who live or work near such installations (Houston 1987).
There are presently about 300 CIMAH sites.
However, many potentially hazardous chemical installations are not covered by such regulations.
Clearly, a plant which stores 1 tonne less than is required for notification slips through the net, while large numbers of handling sites (warehouses, for instance) are not covered.
The regulations have obvious implications for G1S work, as illustrated below.
In Halton Borough, Cheshire, for instance, there are 13 notifiable installations, with over 20 000 people living within the defined 'consultation zones' (Petts 1988).

It is also relevant to point out here the work of the Health and Safety Executive in developing techniques for quantitative risk assessment (Health and Safety Executive 1989).
Such techniques include the use of a 'risk assessment tool' (RISKAT), inputs to which include data on wind direction and speed; the output of which is a map of calculated risk contours.
In societal risk assessment 'it is also necessary to input data on the distribution of population around the installation.
This can be a difficult and time-consuming process, and inevitably some simplifying assumptions are needed' (Health and Safety Executive 1989: 17).
Again, the G1S implications are clear and are discussed below.

##### Hazardous waste disposal

The disposal of both nuclear and non-nuclear wastes has proved to be of major public concern in recent years.
The rather clumsy handling by NIREX of the search for sites to store low- and intermediate-level wastes, together with very recent worries about the import of toxic wastes such as polychlorinated biphenyls (PCBs), are but two examples of such concern in the UK.
However, while the former has been given considerable attention by geographers (summarized by Openshaw et al.1989) there has been relatively little such work in the UK on the disposal of non-nuclear wastes.
This contrasts with the situation in the USA (Greenberg and Anderson 1984), where the clean-up of abandoned sites is a priority.
Certainly, in terms of the volume of waste generated in the UK non-nuclear hazardous industrial wastes should be high on the environmental agenda; while less than 1 million tonnes of all nuclear wastes were generated in 1985-86, 10 times that amount were generated of hazardous wastes (Openshaw et al.1989: 13).

Attention should be drawn to the three Annual Reports of the Hazardous Waste Inspectorate (now merged with other branches of the DoE to form Her Majesty's Inspectorate of Pollution).
These contain some valuable material on disposal practices, and volumes of waste generated and disposed of by each waste regulation authority (WRA) - counties in England, districts in Wales, Scotland and Northern Ireland.
Each WRA is required to produce a waste disposal plan and these are starting to appear.
They too contain useful material on, for instance, the locations of sites, though individual site licences must be consulted for details of what each is permitted to take in the way of hazardous wastes.
What is not known is information on the locations of former sites, at which quite toxic materials may have been dumped, though recent work by Egger (1989) in Austria has mapped a vast number of such sites.
It is these, rather than existing, licensed sites which should be a focus of research activity, particularly when examining possible links to ill health.
We simply do not have enough evidence yet to back up the claim that 'people are almost certainly ill, dead, or dying because of these sloppy waste disposal activities' (Openshaw et al.1989: 12).
Research is in progress, however, to assess possible health effects of poor incineration (Diggle et al.1990).
Particular attention should be focused on hospital incinerators, since these have been subject to Crown immunity for many years and most are technically ill-equipped to burn at sufficiently high temperatures for adequate disposal of wastes (Gatrell and Lovett 1991).
We need to produce an inventory of all such sites, together with a publicly available, comprehensive database on all sites accepting hazardous industrial wastes.

##### Emergency planning

It is convenient to retain the nuclear/non-nuclear distinction when discussing the background to emergency planning.
Nuclear emergency planning in the UK has been reviewed by Matthews and Pepper (1981).
Nuclear power stations must prepare a plan and submit this to the Nuclear Installations Inspectorate and Health and Safety Executive for approval.
Evacuation plans are required to cover an area within a distance of 2.4 km; these detail the roles to be played by the emergency services.
The very narrow emergency planning zones contrast with those in the USA (Collins 1981), where planning is required up to 16 km from the site to cover exposure to radiation plumes.
Local authorities in the UK that have declared themselves 'nuclear-free' have been highly critical of British planning, calling for an extension of emergency zones to at least 24 km.
Zeigler et al. (1983) should be consulted for material relating to evacuation behaviour in the wake of the incident at Three Mile Island.

In the UK little work of any description seems to have been done on human behaviour in the aftermath of releases of hazardous substances, nor is much available on public attitudes to emergency planning.
Indeed, no major studies of evacuation due to hazards have been undertaken in recent times and this is a widely recognized deficiency which no research funding body seems willing to rectify.
In the USA on the other hand, a good deal of useful research in these areas has been undertaken.
This research is brought together in very useful reports produced by the Oak Ridge National Laboratory, Tennessee (Sorenson et al.1987; Vogt and Sorenson 1987) and the Disaster Research Centre, University of Delaware.

Perry (1985) has written an interesting book on emergency planning and evacuation, covering both natural and technological hazards.
For him, comprehensive emergency planning and management involve: prevention, protection, response and restoration.
By prevention we understand the elimination or reduction in risk, perhaps by adequate zoning or safe routeing of shipments, for instance.
Included in protection are methods for detecting likely hazard events and in warning those likely to be affected.
Response includes search and rescue (including the need to cope with secondary threats such as contamination of water supplies after an explosion, or fire following an earthquake).
As Perry and others have noted, relatively few resources are devoted to the first two aspects, the bulk going to response and restoration (rebuilding).

It should be clear from this brief description that these issues are inherently geographical.
In one of the few studies of evacuation behaviour after a non-nuclear hazard event Liverman and Wilson (1981) give weight to this argument.
In 1979 a train carrying chlorine, liquid petroleum, toluene and propane was derailed in Mississauga, Ontario, causing a series of explosions.
This led to the evacuation of 250 000 people which, although staggered over several days, led to great pressure on transport arteries.
An important finding was that many relied on their own transport and went to stay with friends and relatives some distance away, rather than relying on the 19 official evacuation reception centres.
Despite this, the evacuation was successful, partly because the accident occurred at a weekend and the immediately affected area was sparsely populated.
In addition, the police were well prepared, stimulated largely by implementing a plan designed more to cope with an emergency at the nearby Toronto International Airport than for the event in question.

It is not without interest to note that in the USA there is a Federal Emergency Management Agency (FEMA), established in 1978, charged with dealing with all types of emergency planning and management.
In the UK there is no equivalent, though the spate of disasters in the past 4 years (involving over 1000 lives lost) has led to several calls for such a national body to be established.

##### Natural hazards

In this short space it is not possible to go into any depth on the nature of particular natural hazards but only to highlight those aspects relevant to GIS.
Needless to say, the study of natural hazards is important, a statement brought into sharp focus by the fact that natural hazards account for up to 4 per cent of total deaths in the world each year (Mitchell, 1974).
In 1970, for example, more than 200 000 people died in the cyclone and flooding of Bangladesh and in 1979 the hurricanes David and Frederick caused more than $3bn damage in the USA.
Shah (1983) made a comprehensive investigation of natural disaster reports for the period 1974-80 and concluded that both disaster frequency and magnitude (measured in terms of lives lost) are increasing.
High death tolls are still a characteristic of less developed, low-income countries.
Surprisingly, fog is the third most important hazard in Europe after floods and volcanoes.

Research on natural hazards has a long tradition in geography going back more than half a century.
Much of the impetus for such research arose in the USA from observations on river basin management and the need to reduce flood damage.
The vast majority of natural hazards studies have ignored the physical nature of the events per se and have concentrated on behavioural issues such as the perception and estimation of hazards.
This emphasis is partly due to the background of the researchers involved (many are human geographers and sociologists) and partly because it is only really since the Second World War that major hazards have been monitored systematically, culminating, of course, in the last decade or so in the use of satellite technology.

Brief reference to two examples of natural hazards may illustrate the potential relevance of a GIS approach, applications of which are considered below.
Jones et al. (1989) have examined the distribution of some 8500 landslides in the UK.
Their maps show clearly an increased propensity for landsliding in the north and west of the UK.
More to the point, however, is the fact that this distribution can be modelled in terms of slopes, rainfall, rock types and so on.
In other words the actual hazard distribution can be understood and areas at risk identified.
The potential benefits to insurance companies, engineers and planners are clear.
Second, a well-known winter hazard in the UK, with marked spatial localization, is fog.
Predictive models of its distribution have clear implications for road and air safety.
Perry (1981) describes a fog potential index that is a function of local topography, environmental features affecting fog formation and distance from standing water bodies.
Reliance is currently placed on a network of monitoring stations, often sparsely located and frequently outside fog-prone areas; GIS could implement a predictive model based on digitized map features and indeed the model could also be used in site allocation studies for airports and the like.

The majority of natural hazard research has focused on single hazards but of course any area may be prone to more than one hazard type.
This idea led Hewitt and Burton (1971) to develop the concept of 'all-hazards-at-a-place'.
To achieve this they concentrated on the whole spectrum of damaging events in an area and explored their aggregate impact.
The implications for GIS in the development of 'hazardousness' indices are obvious and if time-series data are available there is the potential to produce a variety of probability maps.

The collection of historical data on natural hazards is important since it is clear that their spatial pattern varies through time.
Many areas that appear to be hazard-free on current maps may merely by passing through a temporary period of quiescence.
This is perhaps best illustrated with reference to earthquakes.
For example, in 1692, the whole of southern England was affected by an earthquake whose epicentre was located in what is now Belgium; a good deal of minor structural damage was inflicted (Morse 1983).
Presumably the builders of the Channel Tunnel are aware of this?

##### Environmental epidemiology

This is, of course, a vast subject area, embracing the impact of the natural and technological environments on human health.
It covers, for instance, the associations between water and air pollution and ill health, links between geological and pedological environments and ill health, as well as associations between specific technological hazards (e.g. high-voltage power lines) and possible health effects.
We can only consider a small fraction of this work here; little consideration is given to occupational environments, for instance.

In the UK such research is widespread though there are specialist environmental epidemiology research institutes at Southampton and Cardiff (funded by the Medical Research Council), and others at the University of Surrey (Robens Institute) and at the London School for Hygiene and Tropical Medicine.
The latter houses the Small Area Health Statistics Research Unit (SAHSRU), which has a specific remit to conduct research into morbidity and mortality at local scales (Elliot 1988).
The SAHSRU liaises closely with OPCS.
The kinds of databases used by these groups are discussed below.

Greenberg (1983) and a collection of papers in Greenberg (1987) review some of the literature on environmental epidemiology.
It seems worth stating at the outset that there are two ways geographical research in this general area can proceed.
One is to collect morbidity and mortality data (usually the latter is more widely available, though the former more useful) and to examine spatial distributions for clustering.
This has itself generated a substantial literature (see the papers in Elliot 1988 for an overview) and is nowhere better exemplified than in Openshaw's geographical analysis machine (see Ch. 2).
We then search retrospectively for evidence of possible environmental associations.
An alternative approach is to begin by hypothesizing an environmental determinant of ill health and to collect data to test an explicit hypothesis.
If an association is suggested then we would want to collect data in other areas to assess the hypothesis further.
Of course, these two approaches are not clear-cut in practice; in many cases the hypotheses of interest will have themselves been generated by inductive mapping.

One example of an hypothesis which has been given serious attention in recent years is the possible link between electromagnetic fields generated by high-voltage power lines or supply cables and ill health.
Some work (Perry et al.1981) suggested associations with mental illness and suicide, while others (e.g. Wertheimer and Leeper 1982) have examined links to various cancers, including leukaemias.
A good bibliography is provided in Perry and Pearl (1988).
The Central Electricity Generating Board (now privatized and split into two companies) is funding a large-scale, 2-year project to assess links to childhood cancer, while another recently announced study aims to look at links to sudden infant death.
One obvious problem, with implications for any GIS input, is that the effects are highly localized, with little measurable field effect more than a few dozen metres away from the route centre-lines.
Accuracy of digital data collection (either of the power lines or residential locations) is paramount.

There seems to be a growing interest in examining associations between ill health and the geological environment.
GIS work in this field (e.g. Matthews 1989) is reviewed later, but we note here the work of the applied geochemistry group at Imperial College (responsible for a series of atlases on regional geochemistry) and the existence of a Society for Environmental Geochemistry and Health.
One area of recent debate concerns radon gas and its links to lung cancer.
This is taken very seriously in the USA, where the Environmental Protection Agency estimates that 10 000-20 000 deaths from lung cancer each year are due to radon gas exposure.
Estimates from Scandinavia suggest that 10-30 per cent of such deaths are caused by exposure to radon (Richardson 1988: 270-81).
The gas is trapped in well-insulated houses and is produced by the decay of uranium in rocks and soil; thus it has been measured at high concentrations in parts of Cornwall and Devon.
There are great difficulties in assessing health effects, however, since exposure varies greatly from house to house within small neighbourhoods.
Carefully designed case-control studies are therefore required to measure the separate effect of radon exposure after controlling for smoking behaviour and other risk factors.

Other health concerns which might merit attention by those involved in the Regional Research Laboratory (RRL) initiative include air and water pollution.
The debate about lead pollution from vehicle exhaust emissions is well known; less publicity has been given to PAHs (polychlorinated aromatic hydrocarbons), a ubiquitous product of combustion processes and known to be carcinogenic (Lioy and Daisey 1987).
Research at the North West Regional Research Laboratory (NWRRL) aims to create buffers around busy roads and junctions and to use data from the Cancer Registry to examine possible links between proximity to such sources of pollution and prevalence of lung cancer.
Those with an interest in health and air pollution should note the availability of a very detailed database from the Warren Springs Laboratory, containing details of smoke and sulphur dioxide emissions at a large number of sites in the UK.
The possible link between nitrates in water and stomach cancer is the subject of much debate (Beresford 1985), as is the association between aluminium content and Alzheimer's disease.
The problems of assessing such links are, of course, huge, but there is scope for a contribution.

#### The role of GIS in hazard management scenarios - examples

As we have already implied, GIS has a role to play in all aspects of hazard research, from hazard monitoring, risk assessment and emergency planning to coping with an event and evaluating its consequences.
The examples described below illustrate all these, though as yet there do not appear to be many instances of disasters in the management of which GIS has played a significant part.

##### Technological hazards, emergency planning and GIS

A considerable amount of research has been undertaken to apply GIS methods to evacuation scenarios around hazardous sites.
Much of this research has concentrated on network analysis of the road system.

Reference was made above to so-called CIMAH sites, major hazardous installations for which on-site and off-site emergency plans must be prepared.
Early research at the NWRRL focused on developing a GIS for use by the police and county emergency planning officers in Cumbria that would aid in the management of a possible explosion at a chemical factory in Whitehaven, west Cumbria (Vincent et al.1988; Dunn 1989).
The police required a portable system that could be implemented on an IBM-compatible microcomputer.
This was written at the NWRRL using FORTRAN 77 and the Graphical Kernel System.
The GIS is menu-based and is exceptionally user-friendly (Pl. 10.1).
It opens with an outline map and the superimposition of the rather rigid zones used by the emergency planners.
Full zoom facilities are available at any stage.
In any emergency it is of course vital to have high-quality data on the distribution of population and resources.
The system incorporates digitized data on the distribution of all domestic and non-domestic properties in the town together with digitized road centre-line data.
Both sets of data were provided by Pinpoint Analysis Ltd, who are undertaking this digitizing task for the entire country.
Other spatially referenced data incorporated into the system include those on the distribution of schools, medical and transport services which can be displayed and supplementary information about them obtained.
The GIS permits population estimates to be made for any arbitrary rectangular region on the map.
Most significantly, it incorporates a shortest path algorithm which uses the road network to find optimal routes between user-defined start and end nodes.

Although predating the RRL initiative by several years - and, indeed the emergence of GIS as a major research area - we should remind ourselves of Openshaw's work on appraising nuclear reactor sites.
Using what would now be called GIS skills, Openshaw (1980) examined over 13 000 1 km grid squares in the UK which intersect the coastline and related these to data from the 1971 Census (which were made available for such grid squares).
He demonstrated that there is an abundance of 'remote' sites, in contrast to the official view that such sites were increasingly hard to find.
He suggested that in early spatial searches for sites 'only a small number were ever identified in the first place because rigorous searches could not be performed by manual means with poor quality data' (Openshaw 1980: 289).

Heywood and Cornelius (1989) have shown how GIS can be used for monitoring possible radiation releases and thus the relevance of GIS in nuclear emergency planning and monitoring.
They propose a national radiological spatial information system and, in a pilot project in Cumbria, have integrated several layers of data within ARC/INFO to show what this might involve (Fig. 10.2).
Such data include those from the Population and Agricultural Censuses as well as point data from rain gauge sites and radiation monitoring stations.
As an example, the system is used to determine restriction zones for the movement of sheep after the explosion at Chernobyl in 1986.
This is done by finding areas of high rainfall and parishes with high sheep populations.
The map overlay of point and area information shows generally good agreement with the restriction zones imposed by the Ministry of Agriculture, Fisheries and Food, with the exception of a small area to the south-east of Cumbria, bordering on Lancashire.

The British government carried out a review of its arrangements for handling nuclear accidents overseas following the Chernobyl accident.
The DoE, through Her Majesty's Inspectorate of Pollution (HMIP), was given the task of co-ordinating a national response plan, installing the radiation monitoring network and acting as lead government department in an emergency (HMSO 1988).
The monitoring network has become known as the radioactive incident monitoring network (RIMNET) and has, as its prime responsibility, the detection of abnormal increases in radiation levels within the UK of the kind that might arise from an overseas nuclear accident.

The full implementation of the RIMNET system will take some time.
By the end of 1988 gamma radiation dose monitors had been installed at 46 meteorological stations as part of phase 1 of the development programme.
Radiation readings are taken every hour at each station and are transmitted to a central computer which analyses the data.
The current criterion for alert is two readings of more than three times normal background, either successively at the same site or simultaneously at two adjacent sites.
The dissemination of information in the event of an incident is dealt with at three levels: the first is the normal system of press notices; the second is the use of teletext and viewdata (Ceefax and Prestel) to get direct to members of the public at their homes or places of work; the third is the use of Telecom Gold electronic mail to get more technical details to various official bodies, such as water authorities (Jackson 1989).

Phase 2 of the RIMNET scheme will be completed by the end of 1991 when between 80 and 90 monitoring sites will have been established.
Given very wide regional and local variations in deposition, questions must be raised about the effectiveness of such a small network; local authorities will need to supplement it with their own networks.
There are important analytical problems to be addressed concerning the siting of such monitoring equipment and these are elaborated on later.

Abroad, Kaspar (1981) has discussed a computer-based exercise, with GIS overtones, involving the simulated evacuation of the population living in the vicinity of the Neckarwestheim nuclear power plant in Baden Württemberg.
In the scenario he outlines, an area affected by radioactive releases is determined, the population within that area is allocated to reception areas (with capacity constraints), evacuation routes are identified and traffic restrictions implemented.
Little detail is provided, however, and it is thus difficult to evaluate his work fully.

Dangermond (1985) describes the use of the ARC/INFO NETWORK module for use in emergency planning situations.
He describes how a road network is digitized and subsequently analysed using allocation, districting and routeing algorithms.
Allocation determines which arcs in the network will be allocated to a particular node or centre; districting makes it possible to outline rapidly sets of polygons in order to define specific areas of interest (districts) and to summarize their characteristics; routeing provides a minimum path algorithm through the network, the arcs of which can be assigned weights according to road conditions, road capacity and so on.
Dangermond gives several examples in his paper including the use of NETWORK for the allocation of emergency vehicles, optimum routeing of fire engines from garages to the accident scene and the movement of spills through sewers and river networks.
When combined with the other facilities in ARC/INFO, quite complex disaster management scenarios can be handled.
For example, earthquake fault zones can be combined with data on housing density and structural details to predict earthquake damage levels and these data then related to the network model.

Vincent (1989) illustrates the use of ARC/INFO and its NETWORK module for finding safe routes for chlorine transhipment on the road and rail systems of north-west England (Pl. 10.2).
In this case, population density data for a 1 km buffer on either side of network arcs were overlaid on the network itself so as to act as weights for the minimum path algorithm.
Chosen routes were those which minimized population rather than distance.

##### Hazardous waste disposal

There can be little doubt that a GIS approach has wide applicability in all sorts of location problems where the goal is to minimize (rather than, as conventionally, maximize) accessibility to a population.
A particularly good application is to the search for potential sites for the disposal of nuclear and non-nuclear (but none the less hazardous) wastes.
We discuss here some relevant work on the siting of facilities for the disposal of nuclear wastes before examining those for non-nuclear wastes.

The major contribution to informed debate about the search for sites for the disposal of nuclear wastes has come from a group of geographers (Openshaw et al.1989) and a GIS approach to this problem can pay high dividends.
The work of Carver (see Openshaw et al.1989: Ch. 7) is an interesting example.
One advantage is the ability to model a range of alternatives by allowing particular criteria to enter or be omitted from the polygon overlay operation.
Conceptually, what is offered is little more than an automated 'sieve mapping' that land-use planners have used for many years, but the whole procedure is speeded up by many orders of magnitude using GIS software.
The authors examine both near-surface sites and deep repositories (which use more restricted population criteria and allow offshore locations to enter).
Data layers include geological maps, conservation areas, transport routes, petrochemical facilities and demographic data.
As different layers are added sequentially we see how the proportion of available land shrinks (Pl. 10.3); for instance, when geological criteria are set in the search for a deep repository, 25 per cent of land area remains and the addition of the population density layer reduces this to 24 per cent.
However, adding a proximity to transport constraint lowers this to 12 per cent; and so on.
We cannot pretend GIS is a solution to the political problems of negotiation and justification but at the very least the openness of the procedures goes some way towards satisfying a worried public.

GIS research into site selection for non-nuclear hazardous waste has been almost exclusively conducted in North America and has yet to be matched in the UK.
Jensen and Christiansen (1986), working in the south-eastern USA, use a raster approach (with a pixel resolution of 20 m²) and Boolean overlay to 'weed out' particular sites, such as those which are poorly drained, environmentally sensitive or inaccessible (see also Stewart 1987).

Environmental monitoring of sites for the disposal of toxic waste is of particular concern in the USA.
The Comprehensive Environmental Response, Compensation and Liability Act (CERCLA) legislation of 1980 ('Superfund') requires the cleaning up of the worst landfill sites, of which some 800 had been identified by the Environmental Protection Agency by 1986 (Foresman 1986).
A major worry has been the threat posed by groundwater pollution and some research has been conducted on using GIS to monitor this (Merchant et al.1987; Barringer et al.1987; von Braun 1988).
This is an important topic since 95 per cent of rural households in the USA consume only groundwater, while half the US population consumes at least some groundwater (Merchant et al.1987).
Clearly, the research demands access to exceptionally good environmental data, usually in three dimensions.
As Foresman (1986) suggests, we might expect remote sensing technology to play a major role.
Merchant et al. (1987) for example, use the image processing system ERDAS to construct an index of vulnerability to groundwater pollution; this uses variables such as depth to water table, soil type, slope and so on (see Estes et al.1987 for a similar approach).
Barringer et al. (1987) overlay data on soil type and geology with that of groundwater quality (hardness and corrosivity measures) and build a linear model which shows that the background environmental variables are good predictors of the water quality indices.
Again, a raster-based approach is used.

A further example is work by von Braun (1988) who uses pMAP to look at exposure of organic and metallic compounds in groundwater in the vicinity of Tucson airport, Arizona.
Using plume models that predict the movement of contaminants she is able to intersect the results with data on current well locations and to assess which water supply areas are worst contaminated.
Overlaying the results with residential location data provides 'maps delineating location-specific exposures for each residence in each time-period' (von Braun 1988; 1160).
In principle, it is then possible to compare such 'doses' with epidemiological data, once again indicating a link from a hazard event to assessment of health outcomes.

Attention should be drawn to Foresman's comment that the US Geological Survey (USGS) (at the EROS Data Centre) have successfully linked ARC/INFO to a model of groundwater flow (Foresman 1986: 260).
This kind of link between GIS and other modelling programs is to be warmly welcomed and parallels work at the NWRRL in linking GIS and air pollution plume models.

##### Natural hazards and disaster management

Several studies in recent papers have shown the effectiveness of GIS in mitigating the effects of major natural hazards.
Berke and Ruch (1985), for example, describe a GIS for assessing the impacts of hurricanes on the Texas Gulf coast.
Hurricane damage through high winds and tidal surges causes an immense amount of destruction and poses a major threat to many coastal communities in the USA.
It has been estimated, for example, that during the mid 1970s some 50 million US citizens were subject to hurricane winds of over 160 km/h and 6 million were subject to hurricane surge (Brinkman 1975).
The system described by Berke and Ruch (1985) is raster-based and has an interesting modelling component called SLOSH (Sea, Lake and Overland Surges from Hurricanes).
SLOSH is able to estimate still water surge by grid cell for various hurricane intensities, angles of approach to the shoreline, forward movement speeds and landfall locations.
Additional algorithms are used to model total building damage costs for each grid cell based on water-depth and speed-depth rating curves.

Hobeika and Jamei (1985) describe the MASSeVACuation (MASSVAC) simulation software designed to analyse and evaluate traffic evacuation plans given a natural disaster in an urban area.
The system comprises three interrelated modules: community and disaster type characteristics module; population distribution module; network evacuation module.
The type of natural disaster determines the time period within which the road network has to be evacuated.
The control and management strategies are directly correlated to each specific disaster scenario.
MASSVAC is quite flexible and various user-defined road network options are available such as: traffic signal timings on the road network; one-way traffic; reserved lanes for special vehicles such as those of the emergency services.
Hobeika and Jamei have tested MASSVAC on various evacuation scenarios for Virginia Beach City in order to determine evacuation times for flood and hurricane conditions.
In general, they suggest that the model provided reasonable and reliable evacuation times.
Southworth et al. (1989) have enhanced the MASSVAC model with the addition of a colour graphics module which they call MVOPL.
This module has been developed using IBM's Graphics Kernel System and provides a number of display screens.
The most interesting are those which portray population flows as scaled ribbons on the network diagram, and evacuation shelter capacities as bar diagrams.
The diagrams are updated periodically during the course of the simulation.

In dry parts of the world, such as Australia, forest and bush fires are an important natural hazard and some attention has been given to the ways in which GIS might help examine their potential impacts.
Kessell (1988) describes a PC-based GIS called PREPLAN (PRistine Environment Planning LANguage) which is a natural area management, land-use planning and fire modelling system developed for the Australian National Parks and Wildlife Service, PREPLAN comprises four modules: a simple raster-based GIS; a grid cell resource database; a wide range of vegetation, fuel, fire behaviour, erosion and land-use models; tabular, statistical and colour graphics output system.
With this system real-time fire growth can be modelled, taking into account changes in terrain, fuel and temporal changes in the weather.
Kessell points out that uncontrollable fires are recurrent phenomena in many parts of Australia, causing damage in the hundreds of millions of dollars and significant loss of life.
Systems such as PREPLAN can provide the user with sound models of the behaviour patterns of fire and are therefore of enormous value in land-use planning.

One of the most widespread natural hazards is flooding, and the potential for loss of property, risk to life and general social disruption is large.
One interesting example of a GIS approach to flood damage estimation is the ANUFLOOD package which was developed in the early 1980s following detailed flood damage studies for flood-prone coastal towns in northern New South Wales, Australia (Smith and Greenaway, 1988).
The ANUFLOOD system requires locational and building type data on individual properties, stage-damage curves relating the average damage that would result from overfloor flooding to differing depths for each property type, and lastly, flood frequency in terms of flood height expressed as a probability.
Output from the system is both tabular and graphical.
Of particular interest is the construction of maps showing the expected annual amounts of damage for gridded flood-prone areas.
ANUFLOOD also contains modules which permit the investigation of various flood damage mitigation options, such as property height raising, levee construction and flood proofing.

##### Environmental epidemiology

The possibilities sketched above relate to emergency planning, the search for hazardous sites, and risk assessment.
To what extent can GIS help if an event occurs?
What, for instance, of the health consequences?
There is a rich tradition of epidemiological work in geography and with the increasing availability of spatially referenced medical data the scope for GIS applications is wide (Gatrell 1987).
For instance, Diggle et al. (1990) assess the hypothesis that cancer of the larynx is associated with proximity to a now-closed incinerator and develop a statistical model from the theory of spatial point processes to test this.
This would have been impossible without the link provided from postcoded data (increasingly available from sources such as cancer registries) to Ordnance Survey (OS) grid references.
Such a link is provided by the Central Postcode Directory, which matches all 1.5 million unit postcodes in the UK to grid references.
When the cases of laryngeal cancer are compared with a null distribution (provided by the distribution of much more common lung cancer) the hypothesis is given strong support.
Although the proposed method is novel, it is but one of an increasingly large number of methods designed to detect and model 'clusters' of disease (see, for example, Cuzick and Edwards 1990).

The work of Diggle et al. (1990) examined only a single point source, though it generalizes to multiple sources and to linear hazards as well.
As a second example of health work linked to hazard studies we may cite the research being conducted by Cross (1989) on childhood leukaemia.
There are numerous hypotheses concerning the aetiology of this disease (from ionizing radiation to viral transmission) and Cross's approach is to collect digital data designed to test some of these hypotheses and to use ARC/INFO to display and analyse results.
For instance, one hypothesis concerns the role of electromagnetic radiation, a source of which is overhead high-voltage transmission lines as noted earlier.
If these are digitized and buffer zones constructed around them (Fig. 10.3) we can quite easily test hypotheses about prevalence in such buffer zones as compared with prevalence outside.
However, we should bear in mind the earlier point about the resolution of the data, since such electromagnetic effects have a very weak effect beyond perhaps 50 m (Wertheimer and Leeper 1982).

There has been a suspicion for many years that high rates of stomach cancer in parts of Wales may be linked to soil chemistry, specifically such factors as zinc/copper ratios, and to lead content in water supplies.
Matthews (1989) has used data from the Regional Cancer Registry (morbidity rather than mortality data) and data on trace elements to examine this link.
Since the latter are available for a 5 km raster the registration data are assigned to these grid squares using the OS grid reference.
As with any such study there are the usual problems of ecological analysis and influences of migration, together with issues of separating out the risk factors under investigation from possible confounding factors.

In the USA, Morrill's report on the beginnings of a $15m. study into the possible radiation doses received as result of radiation releases by the Hanford (Washington State) nuclear complex would seem to cry out for GIS skills to be applied (Morrill 1989).
The research project will employ plume dispersion models in order to model dispersal by wind and will need to integrate this and other environmental data with detailed demographic records.
To some extent this line of approach was anticipated by Johnson (1981) in his study of exposure to plutonium fall-out from the Rocky Flats nuclear weapons plant near Denver (see Zeigler et al.1983: 47-8).
Using soil samples he constructed a contoured risk surface and then mapped excess cancers in various distance bands, detecting a marked distance decay effect.

#### Research problems and prospects

The work reviewed above suggests that the application of GIS techniques to hazard assessment, emergency planning and environmental monitoring is both actually and potentially an important research area with many challenging problems.
Undoubtedly, the GISs of the 1990s will look very different from their rather primitive ancestors.
Computer power is becoming cheaper, digital data more readily available, and GISs are becoming hybrid systems involving other technologies.
In this last section we highlight some important research areas as we see them.
Doubtless there are many others, such is the surge of interest in GIS technology.

##### Data availability

We should first consider the availability and quality of data concerning the populations who may be at risk from the storage and transport of hazardous substances, from toxic air pollution, from flooding and so on.
Such data are crucial, either for assisting the emergency services to make assessments about resources they need to deploy in such events, or for high-quality estimates to be made of risk.

Within the public domain in the UK we must rely in general on data from the most recent Population Census, the lowest level being that for enumeration districts (EDs).
As is well known (Rhind 1983) these contain on average perhaps 150-200 households and 400-500 people.
The boundaries of EDs have not been widely digitized, unlike the higher-level electoral wards.
However, the centroids of EDs are available as 100 m grid references and artificial ED 'polygons' can be created if necessary.
In some instances such data will suffice; in many cases they will have to suffice as nothing better is available.
But in some areas EDs are very extensive physical units and the shapes will be quite distorted.
Furthermore, the scales at which population estimates are often required means that even EDs are too coarse for risk assessments.
For instance, in performing its quantitative risk assessments the Health and Safety Executive will rarely deal with distances from hazardous sites in excess of 1 km (Petts 1988) and census data will not offer sufficient resolution for accurate population estimates to be made.
It should be pointed out, however, that the National Radiological Protection Board currently uses 1 km grid square resolution population data from the 1971 Census in its radiological protection studies (Hallam et al.1981).

It would seem that, despite the costs involved, they should consider investing in the very detailed digital data (Pinpoint Address Code (PAC)) provided by Pinpoint Analysis Ltd.
This area of application would appear to be an obvious market for such a product.
A useful research exercise would be to compare the use of census and PAC data in deriving quantitative risk assessments and this is an interesting research problem.
Even with PAC data some assumptions would need to be made about numbers of persons per household if good population estimates were to be made.

More generally, we need to consider the availability of large databases for hazard studies and emergency planning and this is an area ripe for major initiatives.
In the UK we seem to be lagging well behind the USA in the construction of databases on hazardous sites and especially hazard events such as those involving toxic releases.
For instance, Lioy and Daisey (1987), in their work on the monitoring of toxic air pollution in New Jersey, construct what they term a 'microinventory' for each of three towns, comprising the locations of chemical plants, metal processing plants, paint spray manufacturers and so on.
Some attribute information is available for these.
More closely linked to GIS is work by McMaster and Johnson (1986) who perform a very detailed inventory of hazardous materials (both stored and transported) in Santa Monica, California.
Although the raster displays are very crude it is simple to answer spatial queries concerning the locations of people (for instance, particular age groups) within certain distances of toxic hazard sites.
We have data on some hazardous sites (e.g. those regulated by CIMAH) in the UK but a much more comprehensive approach should be adopted, especially if we are serious in the search for environmental associations with chronic diseases.

The same is true for toxic releases.
In the USA the Environmental Protection Agency produces an Acute Hazards Events Database while the Department of Transportation has a database recording details of 25 000 releases of toxic materials; such details include locational information, type and amount of material released, mode of release and resulting injuries or deaths (Cutter and Solecki 1989).
Can we not use GIS technology to construct 'risk mosaics' (Zeigler et al.1983), at a variety of spatial scales, akin to Hewitt and Burton's 'hazardousness' of a place?

In the UK only a handful of county emergency planning departments (Cumbria, for instance) have built up resource databases in digital form and this needs to be promoted.
Further afield, we need to recognize that some disasters (most obviously Chernobyl) will have implications for more than one country so that environmental monitoring should take place with some kind of international co-ordination.
There will also be movements of hazardous cargoes across frontiers and there are clearly problems of risk assessment and planning for emergencies at or near international boundaries, or at sea and airports.
As noted above, the work of Fedra (1989) is a major step in this direction, and links need to be forged between initiatives in the UK and the rest of Europe.

In terms of databases on hazardous wastes, attention has already been drawn to the waste disposal plans prepared by WRAs.
These give details of present site locations and some indication of permitted wastes, though little or no information on closed and abandoned sites.
However, for details of disposal the individual site licences must be consulted.
The former Hazardous Waste Inspectorate operated a large database on all sites, with details of permitted wastes, including allowable quantities.
The database was created by a commercial company, Aspinwalls Ltd.

There are numerous potentially usable databases for environmental epidemiological work.
OPCS, of course, is a major data repository for medical statistics and their various Monitor Series are of use, though only at the scale of district health authority and above (see Gatrell and Lovett 1988 for an example).
Regional health authorities will from time to time produce mortality data at ward level.
However, if cancers are of interest it is more appropriate to obtain data from regional cancer registries; these data are morbidity rather than mortality data and are therefore more valuable.
The data are postcoded and may have some occupational details.
For example, we have received data from the Regional Cancer Registry in Manchester comprising all cancers of the larynx and lung notified between 1974 and 1984.
This large data set, to which grid references have now been added, comprises information about nearly 40 000 individuals.
It has now been copied into INGRES, a relational database management system, permitting queries to be made about subsets of the data; for instance, all males between the ages of 25 and 64 suffering from laryngeal cancer.

Other data sources on cancers are independent registries of malignancies.
An example is that on leukaemias, managed by the Leukaemia Research Fund Centre in Leeds (Alexander et al.1989).
It should be noted that there are frequently major discrepancies between the regional registries and the specialist registries, partly because the latter receive notifications directly from consultants.
Indeed, working directly with consultants proves invaluable in gaining access to high-quality morbidity data.

Two other potential sources of data are worth mentioning.
First, attention should be drawn to the new directive from the Department of Health to regional and district health authorities to review the health of the population.
This means in practice that district medical officers are charged with preparing an annual report, presenting and interpreting epidemiological data, identifying local health problems and evaluating service outcomes.
Lancaster University is already heavily involved in the work of Preston District Health Authority in this area.

Second, family health service authorities (FHSAs), are also required to take on these roles, but from the viewpoint of primary health care services.
FHSAs (which correspond to non-metropolitan counties and to metropolitan boroughs) hold large databases on services provided by general practitioners; for instance, uptake of immunization and screening for breast and cervical cancers.

Is it, we wonder, possible to contemplate bringing together some of these data sources to form a National Online Health Information System (NOHIS), to parallel that for employment and unemployment (Townsend et al.1987)?
This might include data on morbidity and mortality, uptake of preventative medicine, service use and availability, at both primary and hospital level.
It would be a useful management tool, particularly in view of the reorganization taking place in the National Health Service.

It should not be forgotten that hazards themselves have geographical distributions yet there has been little effort in the UK to develop public domain databases.
Are there hazard-prone areas?
Is there a regional differentiation in hazard type?
These are, of course, commercially important questions and a good deal of money is going into the collection of such data by insurance companies.
One well known database is Major Hazard Incident Data Service (MHIDAS) global industrial hazards database which is currently being developed by the Safety and Reliability Directorate on behalf of the Major Hazards Assessment Unit of the UK Health and Safety Directorate.
This system currently runs in dBASE II and contains in excess of 3000 items of professionally assessed information on major hazards coded into some 24 separate fields.
Unfortunately, the spatial referencing is poor and with some effort this could easily be remedied.
It is, for example, little use when recording a chemical spill into an Egyptian river to have entered into the appropriate field 'the Nile' - after all, this river is some 6480 km long!
Here, in our view, is a classic case of the absence of a geographical input rendering the data of limited value.

In some cases, good hazard data exist but have simply not yet found their way into a GIS.
A case in point is inland and coastal flooding.
Most river authorities have detailed maps showing the geographical limits of floods in relation to their return periods.
Within the next decade, as the privatized water companies develop their GIS, we shall see a massive amount of data conversion in this area.
This development, together with the availability of digital terrain models, will allow quite sophisticated flood forecasting models to be developed within a GIS framework.
As sea-levels rise in the next 20-30 years due to the 'greenhouse' effect, this very practical use of GIS technology is likely to become commonplace and of considerable practical importance.

##### Spatial statistics

Another way in which there needs to be a rapprochement between statistical methods and GIS is in the area of spatial sampling and estimation from spatial samples.
This is clearly an important issue in radiation monitoring as the discussion of RIMNET above implies.
As an example, Peirson (1988) has reviewed the evidence on artificial radioactivity in Cumbria and shows maps of the distribution of certain radionuclides as contoured surfaces.
The point worth making here is that there are many alternative schemes for interpolating from irregular point data (Lam 1983).
One method in particular, kriging (now available as part of the UNIRAS software), offers not only a contoured surface but also an estimate of the standard error at any point on the map.
Where this is high it suggests that an additional sampling station might be set up.
Such techniques are now standard in environmental science (see Streit 1981 for an application to rainfall monitoring) and need to be promoted vigorously in hazard studies (Estes et al.1987).

Related to this problem is that of making population estimates for new zones that result from overlay operations.
We may want to count numbers living within plumes, circles of fixed radius, buffer zones and so on.
Existing GIS techniques usually base the estimates on area-weighted shares, so that a new polygon created by 'slicing' an existing area in half is assigned half the population of that source unit.
This may be quite absurd in some cases, notably where population is spatially clustered within a physically large ED.
At the NWRRL work is under way (Flowerdew and Green 1989) to solve such problems using the EM algorithm and the statistical modelling package GLIM, which has been interfaced with ARC/INFO.

##### Operations research methods and simulation

While there is some research activity in linking statistical models to GIS there would seem to be scope for further applications of operations research techniques to GIS problems.
Within some sophisticated GIS such as ARC/INFO there are some useful algorithms (such as shortest path calculations), but GIS developers have in general failed to realize the natural links between GIS functions and many operations research techniques.

Over the last 20 years or so a large theoretical literature has been developed to provide tools for the solution of many problems associated with emergency planning (Kolesar 1981).
One important class of problems is the selection of locations for the emergency service units.
The choice of locations need not be for permanent bases, but can also include dynamic repositioning of units as circumstances dictate (Kolesar and Walker 1974).

In any major emergency a typical problem is the assignment of resources to demands.
If resources are held at one set of locations and the demands are at another and the costs of transportation are known, how do we allocate the resources most efficiently?
In a major emergency, for example, there might be a need to supply blood products held at regional blood banks to hospitals.
This, of course, is the classic transportation problem and its solution is well known.
As far as we know the microcomputer-based emergency response system devised by Belardo et al. (1983), is the only GIS-like software to incorporate this algorithm.
In this system, the solution to the transportation problem is shown graphically on the road network, which is displayed on the computer screen.

As a last example of the potential role of operations research in GIS and disaster management we are reminded of the logistic problems that faced the Peel Regional Police Force during the Mississauga evacuation mentioned previously (Scanlon and Padgham 1980).
During the early states of the phased evacuation the logistical problem facing the police was the street-by-street warning of the population to make ready for evacuation.
Speed was of the essence and manpower was limited.
Here, then, is a familiar operations research network problem: all roads have to be traversed such that the journey length/time is a minimum.
This is the so-called Chinese postman problem, which provides a Hamiltonian circuit through the arcs (as compared with the travelling salesman problem which is a minimum route through the network nodes).
In fact, the police force lacked access to any digital information and although the evacuation went off without a hitch there is little doubt that a GIS containing the Chinese postman algorithm could have provided efficient routes and also have guaranteed that no road was missed from the warning sweep.

Simulating the likely consequences of real events is an important, but almost untouched, GIS research area.
As an educational tool, simulation is not only an invaluable training aid for personnel who may one day be confronted with a real situation but is sometimes the only method for dealing with improbable but possible events.
In the UK the Institution of Chemical Engineers has produced a computer simulation program specifically for training personnel at large chemical plants who may one day have to manage major fires and toxic releases (Institution of Chemical Engineers, no date).
Although not a thoroughbred GIS, this package, based on an IBM PC, does make use of map data and site plans can be displayed.

##### Decision support systems and GIS

A decision support system (DSS) can be considered as an integration of computer hardware and software specifically designed to complement the human thought process in problem-solving, decision-making and information processing (Benbasat 1977).
According to Berke and Stubbs (1989) a DSS can often be conceptualized as a tool to be used as part of an interactive learning process allowing the user to undertake 'what if' analyses and view the consequences of such alternatives.

The basic components of a DSS comprise: data storage files; data analysis models; display and interactive use technology.
These three components are managed by: a data management subsystem; a model management subsystem; and an interactive dialogue subsystem.
Berke and Stubbs indicate that the interactive dialogue subsystem and the display and interactive use component are particularly critical for the effective use of a DSS because they provide the interaction between the user and the machine.
These features isolate the user from the technicalities of the computer and encourage a dialogue based on the user's judgements rather than imposing the hardware engineer's or computer programmer's discipline on the user.
In this sense ARC/INFO macros, do, to a certain extent, shield the novice from a bewildering number of options, though such a system is most certainly not conversational and in several respects is very simple as compared with a comprehensive DSS.

The integration of GIS and DSS for hazard mitigation is an active research area in the USA, Japan and Europe.
Dong et al. (1988), for example, have developed microcomputer-based DSS for earthquake hazard mitigation.
This system provides a map display of the threatened region and access to spatially referenced data to facilitate hazard zoning for a given earthquake magnitude.
In addition, the software calculates damage estimates and building repair costs for any geographical area.

Fedra and Reitsma (1989) describe a DSS-GIS developed by the Advanced Computer Applications group at the International Institute for Applied Systems Analysis (IIASA), Austria, which provides an interactive, graphics-oriented framework and post-processor for the risk assessment package SAFETI (Technica 1984).
Raw data such as plant locations, weather data and population distribution can be displayed as overlays on a basic land-use map.
The graphical interface provides a link to SAFETI's databases and consequence modelling and risk estimates and risk contours can be produced.

Expert systems are likely to have a significant impact on DSS and GIS in hazard management (Fedra and Reitsma 1989).
Important characteristics of expert systems are that they provide advice in problem-solving based on the knowledge of experts, facilitate learning through experience and allow the use of natural language processing.
One of the most advanced applications of expert systems to DSS and GIS is a hazardous substances and industrial risk management system (IRIMS - Ispra Risk Management Support System) developed at IIASA in conjunction with the Joint Research Centre of the Commission of the European Communities at Ispra, Italy (Fedra et al.1987; Fedra 1986).
This large system, designed for a SUN workstation has the following main elements: an intelligent user interface; an information system including knowledge bases, databases, inference machine and database management system; a simulation system; a DSS.
The large geographical database held in the system covers Europe as far east as the Urals.
Roads, railways, lakes, rivers, major settlements, chemical storage facilities and political boundaries can be displayed and used as overlays for the various modules that examine the impacts of chemical spills into the atmosphere and river systems.

IRIMS uses a number of expert systems techniques including: a language input parser based on sideways chaining and rule values which allow Bayesian probabilistic reasoning to identify possible user intentions/hypotheses; fuzzy set methods to translate uncertainty and ambiguity in the databases or user specifications into linguistic or graphical descriptions; and various rule-based pre- and post-processors to define appropriate context-dependent default input values.

Even in this brief description of DSS it can be see that, as presently configured, most GIS are rather dumb systems requiring intelligent, very computer-literate users.
But in an emergency or disaster situation, the knowledge base must be in the computer system and there should be no skill barrier to access the system.
In this respect we believe that the next generation of GIS will be more akin to DSS than to sophisticated mapping packages, as is presently the case.
The development of such GIS will surely be at the forefront of any research agenda.

##### Real-time GIS

The ultimate test of the role of GIS in emergency/hazard situations is their response time as external information is fed into the system.
Two approaches can be adopted to minimize the response time: a simple approach is to devise portable GIS which can be taken to the hazard; a more complex solution is to couple the GIS to real-time monitoring systems.

Probably the outstanding example of the portability approach is the USA's National Oceanic and Atmospheric Administration's (NOAA) award-winning emergency response package called CAMEO (NOAA 1988).
The best implementation of CAMEO runs on an Apple Macintosh and makes full use of the Hypercard environment.
The system comes with three components: CODEBREAKER which uses intelligent software to identify hazardous chemical labels, summarize the chemical properties and indicate health risks; MAP which can display digital and scanned maps of the incident site; AIR MODEL which is an atmospheric modelling program linked to CODEBREAKER and MAP.
AIR MODEL also has the facility to link on-line to weather data sources and can estimate the scope of potential downwind hazard zones.
CAMEO is designed to be carried on emergency vehicles and has undergone successful on-scene field trials with the Seattle Fire Department.

An alternative approach to real-time monitoring is to develop software capable of receiving data from external monitoring systems.
Southworth et al. (1989) describe an operational, prototype Real-time Traffic Monitoring and Analysis System (RTMAS) whose purpose is to record and warn of the build-up of significant urban population evacuation in times of threat.
RTMAS integrates three software components: GURU, an expert system; AUTOBOX, a time-series module; CROSSTALK proprietary software for transferring traffic count data from roadside counters to the IBM PS2.
In tracking an evacuation build-up, RTMAS collects and cumulates net traffic movements, building up a quantitative picture of the timing and directions of evacuation.
RTMAS has been developed for an IBM PS2/Model 80 connected via modem to software initiated by direct dial up to a sequence of traffic counters.
Currently, the system monitors traffic movements in Florida and Georgia but ultimately national coverage could be achieved.

Systems such as RTMAS have great practical potential in those emergency situations where there is likely to be self-evacuation by the public.
For example, there were major traffic congestion problems, as a result of self-evacuation, during Hurricane Hugo which threatened large parts of the south-west of the USA in October 1989.

In a similar vein, Martin (1989) describes work by Marconi Defence Systems which integrates an automatic vehicle location system with Marconi's GIS (called Tactic Plus).
Emergency vehicles can be supplied with computers that track their spatial location.
This information can be continuously monitored by a receiving station and then delivered to the map component of the GIS.
What seems to be a very advanced GIS with real-time monitoring capacity for use in emergency planning has been recently developed by Plessey Defence Systems.
The software, called GENERICS, is from the same stable as Plessey's defence and military research.
Quite obviously, there is a good deal of, as yet, classified technology which might one day be available for all sorts of hazard mitigation purposes.

#### Conclusions

It is useful to return to the earlier typology of hazards (Fig. 10.1) and to stress the links that might be made between those working on natural hazards and those working in the socio-economic domains.
There are several examples of natural hazards whose impact might benefit from a GIS perspective that cuts across the science-social science divide.
These include snow and ice hazards, where impacts on transport and the need to plan road salting or gritting strategies are obvious (see Perry et al.1986 for the beginnings of a GIS approach).

It would be foolish to imagine that GIS can assist in all hazard studies, emergencies and disasters.
It is hard to imagine what role it could have played in the prevention or aftermath of events such as the Piper Alpha oil platform explosion in the North Sea, the Zeebrugge ferry disaster or the sinking of the Marchioness pleasure boat on the Thames, for instance.
But it might have assisted in suggesting search areas for victims of the Lockerbie air crash and, at a very different scale, in helping firemen navigate their way around King's Cross underground rail station.
Why, for instance, could there not be a library of scanned plans of all underground stations, showing the detailed topography and assisting fire personnel unfamiliar with the site to direct their efforts in the search for casualties?

In general, however, GIS surely has a function to perform in simulation and role-playing exercises.
The Cumbria emergency planning system outlined above can, for instance, be used as an experimental tool, permitting police and emergency planners to simulate a hazard event and to call up information on resources, to identify possible areas for evacuation, to plan routes through the transport network, and so on.
There must be many opportunities for user-friendly GIS to be employed in these kinds of scenarios, either as special-purpose systems or by employing proprietary GIS packages with easy-to-use macros.

Anyone working in the GIS research field is conscious of the links that need to be made to groups of researchers in other disciplines.
Nowhere, it seems, is this more apparent than in the area under consideration here.
We need the skills of environmental scientists, statisticians, epidemiologists and chemical engineers, not to mention those of the geographer and planner.

Given the spate of recent disasters, notably in the UK the time is ripe for a major initiative in the field of emergency planning and hazard studies.

#### Acknowledgements

The Economic and Social Research Council is thanked for its promotion of GIS research and for funding the NWRRL at Lancaster University.

