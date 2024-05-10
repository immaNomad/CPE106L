-- Create database 'chinook'
USE [master]
GO

CREATE DATABASE [chinook]
  CONTAINMENT = NONE
  ON PRIMARY
  (
    NAME = N'chinook',
    FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\chinook.mdf',
    SIZE = 8192KB,
    MAXSIZE = UNLIMITED,
    FILEGROWTH = 65536KB
  )
  LOG ON
  (
    NAME = N'chinook_log',
    FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\chinook_log.ldf',
    SIZE = 8192KB,
    MAXSIZE = 2048GB,
    FILEGROWTH = 65536KB
  )
  WITH CATALOG_COLLATION = DATABASE_DEFAULT,
  LEDGER = OFF;
GO

-- Enable full-text search if installed (optional comment)
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
BEGIN
  EXEC [chinook].[dbo].[sp_fulltext_database] @action = 'enable';
END;
GO

USE [chinook]
GO

-- Create table 'albums'
CREATE TABLE [dbo].[ALBUMS] (  -- Use uppercase for table names (optional)
  [AlbumId] INT NOT NULL,
  [Title] NVARCHAR(160) NULL,
  [ArtistId] INT NULL,
  CONSTRAINT [PK_albums] PRIMARY KEY CLUSTERED (
    [AlbumId] ASC
  )
  WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY];

-- Create table 'artists'
CREATE TABLE [dbo].[ARTISTS] (  -- Use uppercase for table names (optional)
  [ArtistID] INT NOT NULL,
  [Name] NVARCHAR(120) NOT NULL,
  CONSTRAINT [PK_artists] PRIMARY KEY CLUSTERED (
    [ArtistID] ASC
  )
  WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY];

-- Create table 'tracks'
CREATE TABLE [dbo].[TRACKS] (  -- Use uppercase for table names (optional)
  [TrackId] INT NOT NULL,
  [Name] NVARCHAR(200) NULL,
  [AlbumId] INT NULL,
  [MediaTypeId] INT NULL,
  [GenreId] INT NULL,
  [Composer] NVARCHAR(220) NULL,
  [Milliseconds] INT NULL,
  [Bytes] INT NULL,
  [UnitPrice] NUMERIC(18, 0) NULL,
  CONSTRAINT [PK_tracks] PRIMARY KEY CLUSTERED (
    [TrackId] ASC
  )
  WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY];

-- Create foreign key between 'albums' and 'artists' tables
ALTER TABLE [dbo].[albums]
  WITH CHECK ADD CONSTRAINT [FK_albums_artists] FOREIGN KEY ([ArtistId])
  REFERENCES [dbo].[artists] ([ArtistID]);
GO

ALTER TABLE [dbo].[albums] CHECK CONSTRAINT [FK_albums_artists];
GO

-- Create foreign key between 'tracks' and 'albums' tables
ALTER TABLE [dbo].[tracks]
  WITH CHECK ADD CONSTRAINT [FK_tracks_albums] FOREIGN KEY ([AlbumId])
  REFERENCES [dbo].[albums] ([AlbumId]);
GO

ALTER TABLE [dbo].[tracks] CHECK CONSTRAINT [FK_tracks_albums];
GO

USE [master]
GO

ALTER DATABASE [chinook] SET READ_WRITE;
GO

-- Create table 'artists'
CREATE TABLE [dbo].[ARTISTS] (  -- Use uppercase for table names (optional)
  [ArtistID] INT NOT NULL PRIMARY KEY,  -- Combine primary key definition
  [Name] NVARCHAR(120) NOT NULL
);

-- Create table 'albums'
CREATE TABLE [dbo].[ALBUMS] (  -- Use uppercase for table names (optional)
  [AlbumId] INT NOT NULL PRIMARY KEY,  -- Combine primary key definition
  [Title] NVARCHAR(160) NULL,
  [ArtistId] INT NOT NULL,
  FOREIGN KEY (ArtistId) REFERENCES [dbo].[artists] ([ArtistID])  -- Use full table names
);

-- Create table 'tracks'
CREATE TABLE [dbo].[TRACKS] (  -- Use uppercase for table names (optional)
  [TrackId] INT NOT NULL PRIMARY KEY,  -- Combine primary key definition
  [Name] NVARCHAR(200) NULL,
  [AlbumId] INT NOT NULL,
  [MediaTypeId] INT NULL,
  [GenreId] INT NULL,
  [Composer] NVARCHAR(220) NULL,
  [Milliseconds] INT NULL,
  [Bytes] INT NULL,
  [UnitPrice] NUMERIC(18, 0) NULL,
  FOREIGN KEY (AlbumId) REFERENCES [dbo].[albums] ([AlbumId])  -- Use full table names
);
