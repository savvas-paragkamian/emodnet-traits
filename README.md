# EMODnet traits and text mining

In this repo we store some notes, resources and code as we study the feasibility
of an text mining tool for marine species traits. 

The basic componets for this study are

* corpus containing relavant literature
* curation/annotation system to help train models
* dictionary/vocabulary containing traits, their synonyms and definitions
* tagger, to retrieve the terms from the corpus

This is a companion and investigating repo of the main work done 
in [EMODnet Phase IV traits feasibility study](https://github.com/EMODnet/EMODnet-Biology-feasibility-ecological-traits)

## Marine Species Traits

The center of WoRMS (marine species) is the Aphia Database. 
The Aphia ID refers to a taxon. Associated with Aphia Ids are 
taxonomic information, distribution and attributes among others.

Attributes are basically the traits. An Attribute ID is a 
measurementtypeID which is associated with a measurement type
and measurement values. So the attributes of an aphia ID are

```
Attribute{
AphiaID	integer
example: 127160
Unique and persistent identifier within WoRMS

measurementTypeID	integer
example: 15
The corresponding AttributeKey its measurementTypeID

measurementType	string
example: Body size
The corresponding AttributeKey its measurementType

measurementValue	string
example: 70
The value of the measurement, fact, characteristic, or assertion

source_id	integer
example: 232308
The identifier for the AphiaSource for this attribute

reference	string
example:
The AphiaSource reference for this attribute

qualitystatus	string
example: checked
Quality status of the record. Possible values: 'checked', 'trusted' or 'unreviewed'. See https://www.marinespecies.org/aphia.php?p=manual#topic22

CategoryID	integer
example:
The category identifier to list possible attribute values for this attribute definition

AphiaID_Inherited	integer
example: 126132
The AphiaID from where this attribute is inherited

children	[...]
}
```

The categoryID is an entry that contains the possible measurementvalues of 
a measurementtypeID.

To download all the worms data one has to ask explicitly the WoRMs database. 
It is not recommended to iteratively download all the database. For scientific
purposes this is standard procudure for WoRMS.

### Bulk data summary

In total, WoRMS, as of 2022-04-01, has 543915 aphia IDS. The taxonomic summary is below.

```
gawk -F"\t" '(NR>1){split($27,a,"="); print $6 "\t" a[3] "\t" $20}' WoRMS_2022-04-01/taxon.txt | gawk -F"\t" '{a[$3]++}END{for (i in a) {print i "\t" a[i]}}'
```

```
Gigaclass       2
Subgenus        6162
Genus   51639
Subvariety      28
Infrakingdom    6
Superorder      72
Subkingdom      15
Supertribe      5
Superfamily     835
Superclass      15
Subforma        23
Variety 10550
Kingdom 9
Forma   1434
Subfamily       2707
Parvorder       28
Subterclass     12
Phylum (Division)       21
Mutatio 1
Natio   23
Parvphylum      2
Family  7174
Subspecies      13047
Infraclass      29
Species 446970
Infraorder      133
Superphylum     1
Subclass        230
Tribe   327
Class   360
Subphylum (Subdivision) 17
Suborder        449
Subphylum       51
Order   1368
Epifamily       4
Megaclass       1
Subtribe        14
Subsection      8
Section 22
Phylum  108
Infraphylum     12
```

### Download from the worms API

Using the `get-worms_traits.py` we got the json files with the attributes of aphia ids. Then with the `parse_worms_traits.py` 
we transformed all json to a single tsv file.

## Fishbase

[Fishbase](https://www.fishbase.ca/search.php) is the most comprehensive database
for fish and marine animals. It has mostly curated content that can be 
consindered as gold standard. There is package in R that allows users to 
download data from the database. 

The species have an internal identifier called SpecCode. In the directory 
`fishbase` there are some tables extracted from fishbase that contain species 
traits. 

WoRMS is connected to fishbase.

## How to use the repo

This repo has submodules so in order to clone all of them use the following 
command:

```
git clone --recurse-submodules <url>
```
