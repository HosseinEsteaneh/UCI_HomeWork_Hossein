CREATE TABLE "fatal-police-shootings" (
    "date" date NOT NULL,
    "state" varchar(50) NOT NULL,
    "manner_of_death" varchar(50) NOT NULL
);

CREATE TABLE "gun-Owners" (
    "state" varchar(50) NOT NULL,
    "gunOwnership" FLOAT NOT NULL,
	"totalGuns" int NOT NULL
);

SELECT * FROM "fatal-police-shootings";

SELECT * FROM "gun-Owners";

CREATE TABLE fatal-police-shootings (
    "date" date NOT NULL,
    "state" varchar(50) NOT NULL,
    "manner_of_death" varchar(50) NOT NULL
);

CREATE TABLE "gun-Owners" (
    "state" varchar(50) NOT NULL,
    "gunOwnership" FLOAT NOT NULL,
	"totalGuns" int NOT NULL
);

SELECT * FROM "fatal-police-shootings";

SELECT * FROM "gun-Owners";

SELECT f.state, f.date, f.manner_of_death, o.state, o."gunOwnership", o."totalGuns"
FROM "fatal-police-shootings" AS f
LEFT JOIN "gun-Owners" AS o
ON f.state=o.state
ORDER BY f.state;


