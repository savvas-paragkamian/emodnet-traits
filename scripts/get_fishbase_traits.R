#!/usr/bin/env Rscript
#
###############################################################################
# script name: get_fishbase_traits.R
# developed by: Savvas Paragkamian
# framework: EMODnet Biology Phase IV
###############################################################################
# GOAL:
# Aim of this script is to retrieve all available attributes from 
# fishbase.ca assigned to taxa.
###############################################################################
# usage:./get_fishbase_traits.R
###############################################################################

library(rfishbase)
library(tidyverse)

### Download data from fishbase
### data are stored in the directory 
### Library/Application Support/org.R-project.R/R/rfishbase

### do not run
#ecosystem <- fb_tbl("ecosystem")
#reproduc <- fb_tbl("reproduc")
#diet <- fb_tbl("diet")
#diet_items <- fb_tbl("diet_items")
#ecology <- fb_tbl("ecology")
#taxamatch <- fb_tbl("taxamatch")
#
#
#write_delim(ecosystem, "../fishbase/2022-11-25-fishbase_ecosystem.tsv", delim="\t")
#write_delim(reproduc, "../fishbase/2022-11-25-fishbase_reproduc.tsv", delim="\t")
#write_delim(diet, "../fishbase/2022-11-25-diet.tsv", delim="\t")
#write_delim(diet_items, "../fishbase/2022-11-25-diet_items.tsv", delim="\t")
#write_delim(ecology, "../fishbase/2022-11-25-ecology.tsv", delim="\t")
#write_delim(taxamatch, "../fishbase/2022-11-25-taxamatch.tsv", delim="\t")



