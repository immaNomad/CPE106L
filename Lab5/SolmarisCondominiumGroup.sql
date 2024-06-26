
CREATE TABLE PROPERTY(
    PROPERTY_NUM INT PRIMARY KEY,
    lOCATION_NUMBER CHAR(20),
    LOCATION_NAME CHAR(50),
    ADDRESS CHAR(100),
    CITY CHAR(30),
    STATE CHAR(30),
    POSTAL_CODE CHAR(10),
    UNIT_NUMBER CHAR(10),
    SQUARE_FOOTAGE CHAR(20),
    BEDROOM INT,
    BATHROOM INT,
    MAX_PERSON INT,
    BASE_WEEKLY_RATE MONEY
);

CREATE TABLE RENTER(
    RENTER_NUM INT PRIMARY KEY,
    FIRST_NAME CHAR(50),
    MIDDLE_INITIAL CHAR(2),
    LAST_NAME CHAR(50),
    ADDRESS CHAR(100),
    CITY CHAR(30),
    STATE CHAR (30),
    POSTAL_CODE CHAR(10),
    TELEPHONE_NUMBER CHAR(15),
    EMAIL_ADDRESS CHAR(100)
);

CREATE TABLE RENTAL_AGREEMENT(
    RENTER_NUM INT PRIMARY KEY,
    FIRST_NAME CHAR(50),
    MIDDLE_INITIAL CHAR(2),
    LAST_NAME CHAR(50),
    ADDRESS CHAR(100),
    CITY CHAR(30),
    STATE CHAR(30),
    POSTAL_CODE CHAR(10),
    TELEPHONE_NUMBER CHAR(15),
    START_DATE DATE,
    END_DATE DATE,
    WEEKLY_AMOUNT MONEY

);
