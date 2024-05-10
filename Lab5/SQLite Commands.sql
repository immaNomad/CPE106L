CREATE TABLE ADVENTURE_TRIP(
    TRIP_ID DECIMAL(3,0) NOT NULL PRIMARY KEY,
    TRIP_NAME CHAR(75),
    START_LOCATION VARCHAR(50),
    STATE VARCHAR(2),
    DISTANCE NUMBER(4, 0),
    MAX_GRP_SIZE NUMBER(4, 0),
    TYPE VARCHAR(20),
    SEASON VARCHAR(20)
    
);


INSERT INTO ADVENTURE_TRIP VALUES(45, 'Jay Peak', 'Jay', 'VT', 8, 8, 'Hiking', 'Summer');

DELETE TABLE ADVENTURE_TRIP;
