# EMODnet traits and text mining

In this repo we store some notes, resources and code as we study the feasibility
of an text mining tool for marine species traits. 

The basic componets for this study are

* corpus containing relavant literature
* curation/annotation system to help train models
* dictionary/vocabulary containing traits, their synonyms and definitions
* tagger, to retrieve the terms from the corpus

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


