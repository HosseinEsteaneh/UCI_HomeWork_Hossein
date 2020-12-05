-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/WNtAAR
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "fatal_police_shootings" (
    "Date" date   NOT NULL,
    "State" varchar   NOT NULL,
    "manner_of_death" varchar   NOT NULL,
    CONSTRAINT "pk_fatal_police_shootings" PRIMARY KEY (
        "State"
     )
);

CREATE TABLE "Order" (
    "State" varchar   NOT NULL,
    "gunOwnership" float   NOT NULL,
    "totalGuns" int   NOT NULL
);

ALTER TABLE "Order" ADD CONSTRAINT "fk_Order_State" FOREIGN KEY("State")
REFERENCES "fatal_police_shootings" ("State");

