CREATE TABLE Parts(
partNumber       INTEGER, /* a UPC code */
partPrice        INTEGER, /* in the range [1,100] */
needsPart        INTEGER, /* a UPC code */
madeIn           CHAR(2), /* a countries 2 letter identifier */
PRIMARY KEY(partNumber));